"""Factory for creating a ChatterBot instance wired to Django settings."""

from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings as chatterbot_settings


def create_chatbot() -> ChatBot:
    """Return a ChatBot configured from the project's CHATTERBOT settings."""
    return ChatBot(**chatterbot_settings.CHATTERBOT)
