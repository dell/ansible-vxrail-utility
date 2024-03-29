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

class IdracNetworkInfoWithIPv6(object):
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
        'ipv4': 'IdracNetworkInfoWithIPv6Ipv4',
        'ipv6': 'IdracNetworkInfoWithIPv6Ipv6',
        'vlan': 'IdracNetworkInfoWithIPv6Vlan'
    }

    attribute_map = {
        'ipv4': 'ipv4',
        'ipv6': 'ipv6',
        'vlan': 'vlan'
    }

    def __init__(self, ipv4=None, ipv6=None, vlan=None):  # noqa: E501
        """IdracNetworkInfoWithIPv6 - a model defined in Swagger"""  # noqa: E501
        self._ipv4 = None
        self._ipv6 = None
        self._vlan = None
        self.discriminator = None
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.vlan = vlan

    @property
    def ipv4(self):
        """Gets the ipv4 of this IdracNetworkInfoWithIPv6.  # noqa: E501


        :return: The ipv4 of this IdracNetworkInfoWithIPv6.  # noqa: E501
        :rtype: IdracNetworkInfoWithIPv6Ipv4
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """Sets the ipv4 of this IdracNetworkInfoWithIPv6.


        :param ipv4: The ipv4 of this IdracNetworkInfoWithIPv6.  # noqa: E501
        :type: IdracNetworkInfoWithIPv6Ipv4
        """
        if ipv4 is None:
            raise ValueError("Invalid value for `ipv4`, must not be `None`")  # noqa: E501

        self._ipv4 = ipv4

    @property
    def ipv6(self):
        """Gets the ipv6 of this IdracNetworkInfoWithIPv6.  # noqa: E501


        :return: The ipv6 of this IdracNetworkInfoWithIPv6.  # noqa: E501
        :rtype: IdracNetworkInfoWithIPv6Ipv6
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this IdracNetworkInfoWithIPv6.


        :param ipv6: The ipv6 of this IdracNetworkInfoWithIPv6.  # noqa: E501
        :type: IdracNetworkInfoWithIPv6Ipv6
        """
        if ipv6 is None:
            raise ValueError("Invalid value for `ipv6`, must not be `None`")  # noqa: E501

        self._ipv6 = ipv6

    @property
    def vlan(self):
        """Gets the vlan of this IdracNetworkInfoWithIPv6.  # noqa: E501


        :return: The vlan of this IdracNetworkInfoWithIPv6.  # noqa: E501
        :rtype: IdracNetworkInfoWithIPv6Vlan
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this IdracNetworkInfoWithIPv6.


        :param vlan: The vlan of this IdracNetworkInfoWithIPv6.  # noqa: E501
        :type: IdracNetworkInfoWithIPv6Vlan
        """
        if vlan is None:
            raise ValueError("Invalid value for `vlan`, must not be `None`")  # noqa: E501

        self._vlan = vlan

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
        if issubclass(IdracNetworkInfoWithIPv6, dict):
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
        if not isinstance(other, IdracNetworkInfoWithIPv6):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
