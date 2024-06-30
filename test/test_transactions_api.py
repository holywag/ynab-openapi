# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.71.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab_openapi.api.transactions_api import TransactionsApi


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TransactionsApi()

    def tearDown(self) -> None:
        pass

    def test_create_transaction(self) -> None:
        """Test case for create_transaction

        Create a single transaction or multiple transactions
        """
        pass

    def test_delete_transaction(self) -> None:
        """Test case for delete_transaction

        Deletes an existing transaction
        """
        pass

    def test_get_transaction_by_id(self) -> None:
        """Test case for get_transaction_by_id

        Single transaction
        """
        pass

    def test_get_transactions(self) -> None:
        """Test case for get_transactions

        List transactions
        """
        pass

    def test_get_transactions_by_account(self) -> None:
        """Test case for get_transactions_by_account

        List account transactions
        """
        pass

    def test_get_transactions_by_category(self) -> None:
        """Test case for get_transactions_by_category

        List category transactions, excluding any pending transactions
        """
        pass

    def test_get_transactions_by_payee(self) -> None:
        """Test case for get_transactions_by_payee

        List payee transactions, excluding any pending transactions
        """
        pass

    def test_import_transactions(self) -> None:
        """Test case for import_transactions

        Import transactions
        """
        pass

    def test_update_transaction(self) -> None:
        """Test case for update_transaction

        Updates an existing transaction
        """
        pass

    def test_update_transactions(self) -> None:
        """Test case for update_transactions

        Update multiple transactions
        """
        pass


if __name__ == '__main__':
    unittest.main()
