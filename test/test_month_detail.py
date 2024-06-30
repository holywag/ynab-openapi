# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.71.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab_openapi.models.month_detail import MonthDetail

class TestMonthDetail(unittest.TestCase):
    """MonthDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MonthDetail:
        """Test MonthDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MonthDetail`
        """
        model = MonthDetail()
        if include_optional:
            return MonthDetail(
                month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                note = '',
                income = 56,
                budgeted = 56,
                activity = 56,
                to_be_budgeted = 56,
                age_of_money = 56,
                deleted = True,
                categories = [
                    ynab_openapi.models.category.Category(
                        id = '', 
                        category_group_id = '', 
                        category_group_name = '', 
                        name = '', 
                        hidden = True, 
                        original_category_group_id = '', 
                        note = '', 
                        budgeted = 56, 
                        activity = 56, 
                        balance = 56, 
                        goal_type = 'TB', 
                        goal_needs_whole_amount = True, 
                        goal_day = 56, 
                        goal_cadence = 56, 
                        goal_cadence_frequency = 56, 
                        goal_creation_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        goal_target = 56, 
                        goal_target_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        goal_percentage_complete = 56, 
                        goal_months_to_budget = 56, 
                        goal_under_funded = 56, 
                        goal_overall_funded = 56, 
                        goal_overall_left = 56, 
                        deleted = True, )
                    ]
            )
        else:
            return MonthDetail(
                month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                income = 56,
                budgeted = 56,
                activity = 56,
                to_be_budgeted = 56,
                deleted = True,
                categories = [
                    ynab_openapi.models.category.Category(
                        id = '', 
                        category_group_id = '', 
                        category_group_name = '', 
                        name = '', 
                        hidden = True, 
                        original_category_group_id = '', 
                        note = '', 
                        budgeted = 56, 
                        activity = 56, 
                        balance = 56, 
                        goal_type = 'TB', 
                        goal_needs_whole_amount = True, 
                        goal_day = 56, 
                        goal_cadence = 56, 
                        goal_cadence_frequency = 56, 
                        goal_creation_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        goal_target = 56, 
                        goal_target_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        goal_percentage_complete = 56, 
                        goal_months_to_budget = 56, 
                        goal_under_funded = 56, 
                        goal_overall_funded = 56, 
                        goal_overall_left = 56, 
                        deleted = True, )
                    ],
        )
        """

    def testMonthDetail(self):
        """Test MonthDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()