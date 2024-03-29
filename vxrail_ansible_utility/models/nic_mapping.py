# coding: utf-8

"""
    VxRail Cluster and System Management

    APIs for cluster management and system management  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NicMapping(object):
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
        'host_serial_numbers': 'list[str]',
        'uplinks': 'list[NicUplink]'
    }

    attribute_map = {
        'host_serial_numbers': 'host_serial_numbers',
        'uplinks': 'uplinks'
    }

    def __init__(self, host_serial_numbers=None, uplinks=None):  # noqa: E501
        """NicMapping - a model defined in Swagger"""  # noqa: E501
        self._host_serial_numbers = None
        self._uplinks = None
        self.discriminator = None
        if host_serial_numbers is not None:
            self.host_serial_numbers = host_serial_numbers
        self.uplinks = uplinks

    @property
    def host_serial_numbers(self):
        """Gets the host_serial_numbers of this NicMapping.  # noqa: E501


        :return: The host_serial_numbers of this NicMapping.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_serial_numbers

    @host_serial_numbers.setter
    def host_serial_numbers(self, host_serial_numbers):
        """Sets the host_serial_numbers of this NicMapping.


        :param host_serial_numbers: The host_serial_numbers of this NicMapping.  # noqa: E501
        :type: list[str]
        """

        self._host_serial_numbers = host_serial_numbers

    @property
    def uplinks(self):
        """Gets the uplinks of this NicMapping.  # noqa: E501


        :return: The uplinks of this NicMapping.  # noqa: E501
        :rtype: list[NicUplink]
        """
        return self._uplinks

    @uplinks.setter
    def uplinks(self, uplinks):
        """Sets the uplinks of this NicMapping.


        :param uplinks: The uplinks of this NicMapping.  # noqa: E501
        :type: list[NicUplink]
        """
        if uplinks is None:
            raise ValueError("Invalid value for `uplinks`, must not be `None`")  # noqa: E501

        self._uplinks = uplinks

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
        if issubclass(NicMapping, dict):
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
        if not isinstance(other, NicMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
