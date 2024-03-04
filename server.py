import streamlit as st
from repository.main import RunRag
from llama_index.core.chat_engine.types import ChatMode
from llama_index.core.indices.postprocessor import SentenceEmbeddingOptimizer
from repository.postprocessing import DuplicateRemoverNodePostprocessor
# from llama_index.core.callbacks import LlamaDebugHandler, CallbackManager
# from llama_index.core import ServiceContext
import time

rag = RunRag()
@st.cache_resource(show_spinner=False)
def get_index():
    indexing, service_ctx = rag.run()
    return indexing, service_ctx


index, service_context = get_index()
if "chat_engine" not in st.session_state.keys():
    postprocessor = SentenceEmbeddingOptimizer(
        embed_model=service_context.embed_model,
        percentile_cutoff=0.5,
        # threshold_cutoff=0.6
    )

    st.session_state.chat_engine = index.as_chat_engine(
        chat_mode=ChatMode.CONTEXT,
        verbose=True,
        node_postprocessors=[
            postprocessor,
            DuplicateRemoverNodePostprocessor()
        ]
    )

st.set_page_config(
    page_title="Chat with Spotify Review Dataset",
    page_icon="🟢⏯",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)
st.title("Chat with Spotify Review Dataset 💬🎶")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Ask me a question about Spotify mobile application review?",
        }
    ]
if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def stream_data():
    for w in response.response.split():
        yield w + " "
        time.sleep(0.02)

if st.session_state.messages[-1]["role"] == "user":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(message=prompt)
            st.write_stream(stream_data)
            nodes = [node for node in response.source_nodes]
            for col, node, i in zip(st.columns(len(nodes)), nodes, range(len(nodes))):
                with col:
                    st.text(f"Source Node {i+1}: score= {node.score}")
                    st.write(node.text)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)
