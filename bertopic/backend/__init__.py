from ._base import BaseEmbedder
from ._word_doc import WordDocEmbedder
from ._utils import languages
from bertopic._utils import NotInstalled

# OpenAI Embeddings
try:
    from bertopic.backend._openai import OpenAIBackend
except ModuleNotFoundError:
    msg = "`pip install openai` \n\n"
    OpenAIBackend = NotInstalled("OpenAI", "OpenAI", custom_msg=msg)

__all__ = [
    "BaseEmbedder",
    "WordDocEmbedder",
    "OpenAIBackend",
    "languages"
]
