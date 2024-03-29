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

class Layer3ManagementNetworkConfigSpec(object):
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
        'hosts': 'list[Layer3ManagementNetworkHostSpec]',
        'management_network': 'Layer3NetworkSpec'
    }

    attribute_map = {
        'hosts': 'hosts',
        'management_network': 'managementNetwork'
    }

    def __init__(self, hosts=None, management_network=None):  # noqa: E501
        """Layer3ManagementNetworkConfigSpec - a model defined in Swagger"""  # noqa: E501
        self._hosts = None
        self._management_network = None
        self.discriminator = None
        self.hosts = hosts
        self.management_network = management_network

    @property
    def hosts(self):
        """Gets the hosts of this Layer3ManagementNetworkConfigSpec.  # noqa: E501


        :return: The hosts of this Layer3ManagementNetworkConfigSpec.  # noqa: E501
        :rtype: list[Layer3ManagementNetworkHostSpec]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this Layer3ManagementNetworkConfigSpec.


        :param hosts: The hosts of this Layer3ManagementNetworkConfigSpec.  # noqa: E501
        :type: list[Layer3ManagementNetworkHostSpec]
        """
        if hosts is None:
            raise ValueError("Invalid value for `hosts`, must not be `None`")  # noqa: E501

        self._hosts = hosts

    @property
    def management_network(self):
        """Gets the management_network of this Layer3ManagementNetworkConfigSpec.  # noqa: E501


        :return: The management_network of this Layer3ManagementNetworkConfigSpec.  # noqa: E501
        :rtype: Layer3NetworkSpec
        """
        return self._management_network

    @management_network.setter
    def management_network(self, management_network):
        """Sets the management_network of this Layer3ManagementNetworkConfigSpec.


        :param management_network: The management_network of this Layer3ManagementNetworkConfigSpec.  # noqa: E501
        :type: Layer3NetworkSpec
        """
        if management_network is None:
            raise ValueError("Invalid value for `management_network`, must not be `None`")  # noqa: E501

        self._management_network = management_network

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
        if issubclass(Layer3ManagementNetworkConfigSpec, dict):
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
        if not isinstance(other, Layer3ManagementNetworkConfigSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
