from typing import Any, Optional
from time import sleep
from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(self.style.WARNING("Database unavailable, waiting 1 second..."))
                sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
