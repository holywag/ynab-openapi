# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.71.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab_openapi.models.payee_locations_response_data import PayeeLocationsResponseData

class TestPayeeLocationsResponseData(unittest.TestCase):
    """PayeeLocationsResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PayeeLocationsResponseData:
        """Test PayeeLocationsResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PayeeLocationsResponseData`
        """
        model = PayeeLocationsResponseData()
        if include_optional:
            return PayeeLocationsResponseData(
                payee_locations = [
                    ynab_openapi.models.payee_location.PayeeLocation(
                        id = '', 
                        payee_id = '', 
                        latitude = '', 
                        longitude = '', 
                        deleted = True, )
                    ]
            )
        else:
            return PayeeLocationsResponseData(
                payee_locations = [
                    ynab_openapi.models.payee_location.PayeeLocation(
                        id = '', 
                        payee_id = '', 
                        latitude = '', 
                        longitude = '', 
                        deleted = True, )
                    ],
        )
        """

    def testPayeeLocationsResponseData(self):
        """Test PayeeLocationsResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
