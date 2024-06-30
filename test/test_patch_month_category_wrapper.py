# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.71.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab_openapi.models.patch_month_category_wrapper import PatchMonthCategoryWrapper

class TestPatchMonthCategoryWrapper(unittest.TestCase):
    """PatchMonthCategoryWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchMonthCategoryWrapper:
        """Test PatchMonthCategoryWrapper
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchMonthCategoryWrapper`
        """
        model = PatchMonthCategoryWrapper()
        if include_optional:
            return PatchMonthCategoryWrapper(
                category = ynab_openapi.models.save_month_category.SaveMonthCategory(
                    budgeted = 56, )
            )
        else:
            return PatchMonthCategoryWrapper(
                category = ynab_openapi.models.save_month_category.SaveMonthCategory(
                    budgeted = 56, ),
        )
        """

    def testPatchMonthCategoryWrapper(self):
        """Test PatchMonthCategoryWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
