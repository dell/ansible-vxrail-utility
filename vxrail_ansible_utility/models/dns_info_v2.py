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

class DNSInfoV2(object):
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
        'servers': 'list[str]',
        'upstream_dns': 'list[str]',
        'is_internal': 'bool'
    }

    attribute_map = {
        'servers': 'servers',
        'upstream_dns': 'upstream_dns',
        'is_internal': 'is_internal'
    }

    def __init__(self, servers=None, upstream_dns=None, is_internal=None):  # noqa: E501
        """DNSInfoV2 - a model defined in Swagger"""  # noqa: E501
        self._servers = None
        self._upstream_dns = None
        self._is_internal = None
        self.discriminator = None
        self.servers = servers
        if upstream_dns is not None:
            self.upstream_dns = upstream_dns
        self.is_internal = is_internal

    @property
    def servers(self):
        """Gets the servers of this DNSInfoV2.  # noqa: E501

        A list of IP addresses for the external DNS servers or the internal DNS server (VxRail Manager IP address(es)).  # noqa: E501

        :return: The servers of this DNSInfoV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this DNSInfoV2.

        A list of IP addresses for the external DNS servers or the internal DNS server (VxRail Manager IP address(es)).  # noqa: E501

        :param servers: The servers of this DNSInfoV2.  # noqa: E501
        :type: list[str]
        """
        if servers is None:
            raise ValueError("Invalid value for `servers`, must not be `None`")  # noqa: E501

        self._servers = servers

    @property
    def upstream_dns(self):
        """Gets the upstream_dns of this DNSInfoV2.  # noqa: E501

        A list of IP addresses for the upstream DNS servers when the internal DNS is used.  # noqa: E501

        :return: The upstream_dns of this DNSInfoV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._upstream_dns

    @upstream_dns.setter
    def upstream_dns(self, upstream_dns):
        """Sets the upstream_dns of this DNSInfoV2.

        A list of IP addresses for the upstream DNS servers when the internal DNS is used.  # noqa: E501

        :param upstream_dns: The upstream_dns of this DNSInfoV2.  # noqa: E501
        :type: list[str]
        """

        self._upstream_dns = upstream_dns

    @property
    def is_internal(self):
        """Gets the is_internal of this DNSInfoV2.  # noqa: E501

        Whether the DNS server is integrated (internal) or external. If is_internal is true, only VxRail Manager IP is listed in the servers list and other DNS servers are returned in the upstream_dns list.  # noqa: E501

        :return: The is_internal of this DNSInfoV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_internal

    @is_internal.setter
    def is_internal(self, is_internal):
        """Sets the is_internal of this DNSInfoV2.

        Whether the DNS server is integrated (internal) or external. If is_internal is true, only VxRail Manager IP is listed in the servers list and other DNS servers are returned in the upstream_dns list.  # noqa: E501

        :param is_internal: The is_internal of this DNSInfoV2.  # noqa: E501
        :type: bool
        """
        if is_internal is None:
            raise ValueError("Invalid value for `is_internal`, must not be `None`")  # noqa: E501

        self._is_internal = is_internal

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
        if issubclass(DNSInfoV2, dict):
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
        if not isinstance(other, DNSInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
