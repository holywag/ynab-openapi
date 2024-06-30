# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.71.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab_openapi.models.categories_response import CategoriesResponse

class TestCategoriesResponse(unittest.TestCase):
    """CategoriesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoriesResponse:
        """Test CategoriesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoriesResponse`
        """
        model = CategoriesResponse()
        if include_optional:
            return CategoriesResponse(
                data = ynab_openapi.models.categories_response_data.CategoriesResponse_data(
                    category_groups = [
                        null
                        ], 
                    server_knowledge = 56, )
            )
        else:
            return CategoriesResponse(
                data = ynab_openapi.models.categories_response_data.CategoriesResponse_data(
                    category_groups = [
                        null
                        ], 
                    server_knowledge = 56, ),
        )
        """

    def testCategoriesResponse(self):
        """Test CategoriesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
