# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.71.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ynab_openapi.models.account import Account
from ynab_openapi.models.currency_format import CurrencyFormat
from ynab_openapi.models.date_format import DateFormat
from typing import Optional, Set
from typing_extensions import Self

class BudgetSummary(BaseModel):
    """
    BudgetSummary
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    last_modified_on: Optional[datetime] = Field(default=None, description="The last time any changes were made to the budget from either a web or mobile client")
    first_month: Optional[date] = Field(default=None, description="The earliest budget month")
    last_month: Optional[date] = Field(default=None, description="The latest budget month")
    date_format: Optional[DateFormat] = None
    currency_format: Optional[CurrencyFormat] = None
    accounts: Optional[List[Account]] = Field(default=None, description="The budget accounts (only included if `include_accounts=true` specified as query parameter)")
    __properties: ClassVar[List[str]] = ["id", "name", "last_modified_on", "first_month", "last_month", "date_format", "currency_format", "accounts"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BudgetSummary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of date_format
        if self.date_format:
            _dict['date_format'] = self.date_format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency_format
        if self.currency_format:
            _dict['currency_format'] = self.currency_format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in accounts (list)
        _items = []
        if self.accounts:
            for _item in self.accounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accounts'] = _items
        # set to None if date_format (nullable) is None
        # and model_fields_set contains the field
        if self.date_format is None and "date_format" in self.model_fields_set:
            _dict['date_format'] = None

        # set to None if currency_format (nullable) is None
        # and model_fields_set contains the field
        if self.currency_format is None and "currency_format" in self.model_fields_set:
            _dict['currency_format'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BudgetSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "last_modified_on": obj.get("last_modified_on"),
            "first_month": obj.get("first_month"),
            "last_month": obj.get("last_month"),
            "date_format": DateFormat.from_dict(obj["date_format"]) if obj.get("date_format") is not None else None,
            "currency_format": CurrencyFormat.from_dict(obj["currency_format"]) if obj.get("currency_format") is not None else None,
            "accounts": [Account.from_dict(_item) for _item in obj["accounts"]] if obj.get("accounts") is not None else None
        })
        return _obj


