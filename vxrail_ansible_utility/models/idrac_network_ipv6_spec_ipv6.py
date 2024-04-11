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

class IdracNetworkIPv6SpecIpv6(object):
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
        'ip_address': 'str',
        'prefix_length': 'int',
        'gateway': 'str',
        'auto_config_enabled': 'bool'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'prefix_length': 'prefix_length',
        'gateway': 'gateway',
        'auto_config_enabled': 'auto_config_enabled'
    }

    def __init__(self, ip_address=None, prefix_length=None, gateway=None, auto_config_enabled=None):  # noqa: E501
        """IdracNetworkIPv6SpecIpv6 - a model defined in Swagger"""  # noqa: E501
        self._ip_address = None
        self._prefix_length = None
        self._gateway = None
        self._auto_config_enabled = None
        self.discriminator = None
        if ip_address is not None:
            self.ip_address = ip_address
        if prefix_length is not None:
            self.prefix_length = prefix_length
        if gateway is not None:
            self.gateway = gateway
        self.auto_config_enabled = auto_config_enabled

    @property
    def ip_address(self):
        """Gets the ip_address of this IdracNetworkIPv6SpecIpv6.  # noqa: E501

        The static IPv6 address of the IDRAC. To configure the IPv6 address, set the property of auto_config_enabled as false. The IPv6 address information is not required to configure the IPv6 address through DHCP.  # noqa: E501

        :return: The ip_address of this IdracNetworkIPv6SpecIpv6.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this IdracNetworkIPv6SpecIpv6.

        The static IPv6 address of the IDRAC. To configure the IPv6 address, set the property of auto_config_enabled as false. The IPv6 address information is not required to configure the IPv6 address through DHCP.  # noqa: E501

        :param ip_address: The ip_address of this IdracNetworkIPv6SpecIpv6.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def prefix_length(self):
        """Gets the prefix_length of this IdracNetworkIPv6SpecIpv6.  # noqa: E501

        The prefix length of the iDRAC  # noqa: E501

        :return: The prefix_length of this IdracNetworkIPv6SpecIpv6.  # noqa: E501
        :rtype: int
        """
        return self._prefix_length

    @prefix_length.setter
    def prefix_length(self, prefix_length):
        """Sets the prefix_length of this IdracNetworkIPv6SpecIpv6.

        The prefix length of the iDRAC  # noqa: E501

        :param prefix_length: The prefix_length of this IdracNetworkIPv6SpecIpv6.  # noqa: E501
        :type: int
        """

        self._prefix_length = prefix_length

    @property
    def gateway(self):
        """Gets the gateway of this IdracNetworkIPv6SpecIpv6.  # noqa: E501

        The IPv6 gateway address of the iDRAC  # noqa: E501

        :return: The gateway of this IdracNetworkIPv6SpecIpv6.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this IdracNetworkIPv6SpecIpv6.

        The IPv6 gateway address of the iDRAC  # noqa: E501

        :param gateway: The gateway of this IdracNetworkIPv6SpecIpv6.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def auto_config_enabled(self):
        """Gets the auto_config_enabled of this IdracNetworkIPv6SpecIpv6.  # noqa: E501

        The flag indicates whether or not DHCP is enabled to obtain an IPv6 address. If this property is set to false, the property of IPv6 is configured. Otherwise, an IPv6 address is configured through DHCP.  # noqa: E501

        :return: The auto_config_enabled of this IdracNetworkIPv6SpecIpv6.  # noqa: E501
        :rtype: bool
        """
        return self._auto_config_enabled

    @auto_config_enabled.setter
    def auto_config_enabled(self, auto_config_enabled):
        """Sets the auto_config_enabled of this IdracNetworkIPv6SpecIpv6.

        The flag indicates whether or not DHCP is enabled to obtain an IPv6 address. If this property is set to false, the property of IPv6 is configured. Otherwise, an IPv6 address is configured through DHCP.  # noqa: E501

        :param auto_config_enabled: The auto_config_enabled of this IdracNetworkIPv6SpecIpv6.  # noqa: E501
        :type: bool
        """
        if auto_config_enabled is None:
            raise ValueError("Invalid value for `auto_config_enabled`, must not be `None`")  # noqa: E501

        self._auto_config_enabled = auto_config_enabled

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
        if issubclass(IdracNetworkIPv6SpecIpv6, dict):
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
        if not isinstance(other, IdracNetworkIPv6SpecIpv6):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
