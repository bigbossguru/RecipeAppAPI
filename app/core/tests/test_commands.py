from unittest.mock import patch, Mock

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("core.management.commands.waitdb.Command.check")
class CommandTests(SimpleTestCase):
    def test_wait_for_db_ready(self, patched_check: Mock):
        patched_check.return_value = True
        call_command("waitdb")

        patched_check.assert_called_once_with(databases=["default"])

    @patch("time.sleep")
    def test_wait_for_db_delay(self, patched_sleep: Mock, patched_check: Mock):
        patched_check.side_effect = [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]
        call_command("waitdb")

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=["default"])
