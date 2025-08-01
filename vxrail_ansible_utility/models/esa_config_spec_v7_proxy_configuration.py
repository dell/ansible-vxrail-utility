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

class ESAConfigSpecV7ProxyConfiguration(object):
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
        'proxy_address': 'str',
        'proxy_port': 'int'
    }

    attribute_map = {
        'proxy_address': 'proxy_address',
        'proxy_port': 'proxy_port'
    }

    def __init__(self, proxy_address=None, proxy_port=None):  # noqa: E501
        """ESAConfigSpecV7ProxyConfiguration - a model defined in Swagger"""  # noqa: E501
        self._proxy_address = None
        self._proxy_port = None
        self.discriminator = None
        if proxy_address is not None:
            self.proxy_address = proxy_address
        if proxy_port is not None:
            self.proxy_port = proxy_port

    @property
    def proxy_address(self):
        """Gets the proxy_address of this ESAConfigSpecV7ProxyConfiguration.  # noqa: E501

        The KMS server proxy IP or FQDN  # noqa: E501

        :return: The proxy_address of this ESAConfigSpecV7ProxyConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._proxy_address

    @proxy_address.setter
    def proxy_address(self, proxy_address):
        """Sets the proxy_address of this ESAConfigSpecV7ProxyConfiguration.

        The KMS server proxy IP or FQDN  # noqa: E501

        :param proxy_address: The proxy_address of this ESAConfigSpecV7ProxyConfiguration.  # noqa: E501
        :type: str
        """

        self._proxy_address = proxy_address

    @property
    def proxy_port(self):
        """Gets the proxy_port of this ESAConfigSpecV7ProxyConfiguration.  # noqa: E501

        The KMS server proxy port number  # noqa: E501

        :return: The proxy_port of this ESAConfigSpecV7ProxyConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._proxy_port

    @proxy_port.setter
    def proxy_port(self, proxy_port):
        """Sets the proxy_port of this ESAConfigSpecV7ProxyConfiguration.

        The KMS server proxy port number  # noqa: E501

        :param proxy_port: The proxy_port of this ESAConfigSpecV7ProxyConfiguration.  # noqa: E501
        :type: int
        """

        self._proxy_port = proxy_port

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
        if issubclass(ESAConfigSpecV7ProxyConfiguration, dict):
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
        if not isinstance(other, ESAConfigSpecV7ProxyConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
