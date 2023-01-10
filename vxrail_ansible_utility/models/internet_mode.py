# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.410
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InternetMode(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_dark_site': 'bool'
    }

    attribute_map = {
        'is_dark_site': 'is_dark_site'
    }

    def __init__(self, is_dark_site=None):  # noqa: E501
        """InternetMode - a model defined in Swagger"""  # noqa: E501
        self._is_dark_site = None
        self.discriminator = None
        self.is_dark_site = is_dark_site

    @property
    def is_dark_site(self):
        """Gets the is_dark_site of this InternetMode.  # noqa: E501

        Whether the system network is a darksite.  # noqa: E501

        :return: The is_dark_site of this InternetMode.  # noqa: E501
        :rtype: bool
        """
        return self._is_dark_site

    @is_dark_site.setter
    def is_dark_site(self, is_dark_site):
        """Sets the is_dark_site of this InternetMode.

        Whether the system network is a darksite.  # noqa: E501

        :param is_dark_site: The is_dark_site of this InternetMode.  # noqa: E501
        :type: bool
        """
        if is_dark_site is None:
            raise ValueError("Invalid value for `is_dark_site`, must not be `None`")  # noqa: E501

        self._is_dark_site = is_dark_site

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InternetMode, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InternetMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
