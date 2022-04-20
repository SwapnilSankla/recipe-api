import time
from django.db import connections
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for db connection")
        database_connection = None

        while not database_connection:
            self.stdout.write("Trying out db connection")
            try:
                database_connection = connections['default']
            except OperationalError:
                self.stdout.write("Db connection not available, waiting for 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database connection is available!"))

