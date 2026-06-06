"""Terminal chat management command for conversing with the ChatterBot."""

from django.core.management.base import BaseCommand

from terminal_chat.bot import create_chatbot

EXIT_COMMANDS = frozenset({'exit', 'quit'})


class Command(BaseCommand):
    """Run an interactive terminal session with the ChatterBot."""

    help = 'Start a terminal chat session with the ChatterBot.'

    def handle(self, *args, **options):
        bot = create_chatbot()

        self.stdout.write('Type a message to begin. Enter "exit" or "quit" to leave.')
        self.stdout.write('')

        while True:
            try:
                user_input = input('user: ').strip()
            except (KeyboardInterrupt, EOFError):
                self.stdout.write('')
                break

            if not user_input:
                continue

            if user_input.lower() in EXIT_COMMANDS:
                break

            bot_response = bot.get_response(user_input)
            self.stdout.write(f'bot: {bot_response}')
            self.stdout.write('')
