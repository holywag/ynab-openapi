# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.71.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab_openapi.models.save_transaction_with_optional_fields import SaveTransactionWithOptionalFields

class TestSaveTransactionWithOptionalFields(unittest.TestCase):
    """SaveTransactionWithOptionalFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SaveTransactionWithOptionalFields:
        """Test SaveTransactionWithOptionalFields
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SaveTransactionWithOptionalFields`
        """
        model = SaveTransactionWithOptionalFields()
        if include_optional:
            return SaveTransactionWithOptionalFields(
                account_id = '',
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                amount = 56,
                payee_id = '',
                payee_name = '',
                category_id = '',
                memo = '',
                cleared = 'cleared',
                approved = True,
                flag_color = 'red',
                subtransactions = [
                    ynab_openapi.models.save_sub_transaction.SaveSubTransaction(
                        amount = 56, 
                        payee_id = '', 
                        payee_name = '', 
                        category_id = '', 
                        memo = '', )
                    ]
            )
        else:
            return SaveTransactionWithOptionalFields(
        )
        """

    def testSaveTransactionWithOptionalFields(self):
        """Test SaveTransactionWithOptionalFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
