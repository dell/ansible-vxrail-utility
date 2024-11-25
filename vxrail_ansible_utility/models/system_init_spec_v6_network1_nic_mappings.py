# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SystemInitSpecV6Network1NicMappings(object):
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
        'uplinks': 'list[SystemInitSpecV6Network1Uplinks]',
        'lags': 'list[SystemInitSpecV6Network1Lags]'
    }

    attribute_map = {
        'uplinks': 'uplinks',
        'lags': 'lags'
    }

    def __init__(self, uplinks=None, lags=None):  # noqa: E501
        """SystemInitSpecV6Network1NicMappings - a model defined in Swagger"""  # noqa: E501
        self._uplinks = None
        self._lags = None
        self.discriminator = None
        if uplinks is not None:
            self.uplinks = uplinks
        if lags is not None:
            self.lags = lags

    @property
    def uplinks(self):
        """Gets the uplinks of this SystemInitSpecV6Network1NicMappings.  # noqa: E501

        A list of uplinks.  # noqa: E501

        :return: The uplinks of this SystemInitSpecV6Network1NicMappings.  # noqa: E501
        :rtype: list[SystemInitSpecV6Network1Uplinks]
        """
        return self._uplinks

    @uplinks.setter
    def uplinks(self, uplinks):
        """Sets the uplinks of this SystemInitSpecV6Network1NicMappings.

        A list of uplinks.  # noqa: E501

        :param uplinks: The uplinks of this SystemInitSpecV6Network1NicMappings.  # noqa: E501
        :type: list[SystemInitSpecV6Network1Uplinks]
        """

        self._uplinks = uplinks

    @property
    def lags(self):
        """Gets the lags of this SystemInitSpecV6Network1NicMappings.  # noqa: E501

        A list of link aggregation groups (LAG).  # noqa: E501

        :return: The lags of this SystemInitSpecV6Network1NicMappings.  # noqa: E501
        :rtype: list[SystemInitSpecV6Network1Lags]
        """
        return self._lags

    @lags.setter
    def lags(self, lags):
        """Sets the lags of this SystemInitSpecV6Network1NicMappings.

        A list of link aggregation groups (LAG).  # noqa: E501

        :param lags: The lags of this SystemInitSpecV6Network1NicMappings.  # noqa: E501
        :type: list[SystemInitSpecV6Network1Lags]
        """

        self._lags = lags

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
        if issubclass(SystemInitSpecV6Network1NicMappings, dict):
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
        if not isinstance(other, SystemInitSpecV6Network1NicMappings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
