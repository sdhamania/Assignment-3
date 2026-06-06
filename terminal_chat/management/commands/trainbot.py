"""Management command to train the ChatterBot from the English corpus."""

from django.core.management.base import BaseCommand
from chatterbot.trainers import ChatterBotCorpusTrainer

from terminal_chat.bot import create_chatbot

# Default training data bundled with chatterbot-corpus
ENGLISH_CORPUS = 'chatterbot.corpus.english'


class Command(BaseCommand):
    """Train the ChatterBot using the built-in English conversation corpus."""

    help = 'Train the ChatterBot from the English corpus (run once before chatting).'

    def handle(self, *args, **options):
        bot = create_chatbot()
        trainer = ChatterBotCorpusTrainer(bot)

        self.stdout.write('Training bot from English corpus. This may take a minute...')
        trainer.train(ENGLISH_CORPUS)
        self.stdout.write(self.style.SUCCESS('Training complete. Run "python manage.py chat" to start.'))
