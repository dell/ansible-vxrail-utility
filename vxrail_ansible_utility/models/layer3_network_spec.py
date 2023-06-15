# coding: utf-8

"""
    VxRail Cluster and System Management

    APIs for cluster management and system management  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Layer3NetworkSpec(object):
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
        'ip_list': 'list[str]',
        'gateway': 'str',
        'netmask': 'str',
        'vlan_id': 'str',
        'traffic_type': 'str',
        'configurable': 'bool'
    }

    attribute_map = {
        'ip_list': 'ip_list',
        'gateway': 'gateway',
        'netmask': 'netmask',
        'vlan_id': 'vlan_id',
        'traffic_type': 'traffic_type',
        'configurable': 'configurable'
    }

    def __init__(self, ip_list=None, gateway=None, netmask=None, vlan_id=None, traffic_type=None, configurable=None):  # noqa: E501
        """Layer3NetworkSpec - a model defined in Swagger"""  # noqa: E501
        self._ip_list = None
        self._gateway = None
        self._netmask = None
        self._vlan_id = None
        self._traffic_type = None
        self._configurable = None
        self.discriminator = None
        self.ip_list = ip_list
        self.gateway = gateway
        self.netmask = netmask
        self.vlan_id = vlan_id
        self.traffic_type = traffic_type
        self.configurable = configurable

    @property
    def ip_list(self):
        """Gets the ip_list of this Layer3NetworkSpec.  # noqa: E501


        :return: The ip_list of this Layer3NetworkSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this Layer3NetworkSpec.


        :param ip_list: The ip_list of this Layer3NetworkSpec.  # noqa: E501
        :type: list[str]
        """
        if ip_list is None:
            raise ValueError("Invalid value for `ip_list`, must not be `None`")  # noqa: E501

        self._ip_list = ip_list

    @property
    def gateway(self):
        """Gets the gateway of this Layer3NetworkSpec.  # noqa: E501


        :return: The gateway of this Layer3NetworkSpec.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this Layer3NetworkSpec.


        :param gateway: The gateway of this Layer3NetworkSpec.  # noqa: E501
        :type: str
        """
        if gateway is None:
            raise ValueError("Invalid value for `gateway`, must not be `None`")  # noqa: E501

        self._gateway = gateway

    @property
    def netmask(self):
        """Gets the netmask of this Layer3NetworkSpec.  # noqa: E501


        :return: The netmask of this Layer3NetworkSpec.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this Layer3NetworkSpec.


        :param netmask: The netmask of this Layer3NetworkSpec.  # noqa: E501
        :type: str
        """
        if netmask is None:
            raise ValueError("Invalid value for `netmask`, must not be `None`")  # noqa: E501

        self._netmask = netmask

    @property
    def vlan_id(self):
        """Gets the vlan_id of this Layer3NetworkSpec.  # noqa: E501


        :return: The vlan_id of this Layer3NetworkSpec.  # noqa: E501
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this Layer3NetworkSpec.


        :param vlan_id: The vlan_id of this Layer3NetworkSpec.  # noqa: E501
        :type: str
        """
        if vlan_id is None:
            raise ValueError("Invalid value for `vlan_id`, must not be `None`")  # noqa: E501

        self._vlan_id = vlan_id

    @property
    def traffic_type(self):
        """Gets the traffic_type of this Layer3NetworkSpec.  # noqa: E501


        :return: The traffic_type of this Layer3NetworkSpec.  # noqa: E501
        :rtype: str
        """
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, traffic_type):
        """Sets the traffic_type of this Layer3NetworkSpec.


        :param traffic_type: The traffic_type of this Layer3NetworkSpec.  # noqa: E501
        :type: str
        """
        if traffic_type is None:
            raise ValueError("Invalid value for `traffic_type`, must not be `None`")  # noqa: E501
        allowed_values = ["MANAGEMENT", "VSAN", "VMOTION"]  # noqa: E501
        if traffic_type not in allowed_values:
            raise ValueError(
                "Invalid value for `traffic_type` ({0}), must be one of {1}"  # noqa: E501
                .format(traffic_type, allowed_values)
            )

        self._traffic_type = traffic_type

    @property
    def configurable(self):
        """Gets the configurable of this Layer3NetworkSpec.  # noqa: E501


        :return: The configurable of this Layer3NetworkSpec.  # noqa: E501
        :rtype: bool
        """
        return self._configurable

    @configurable.setter
    def configurable(self, configurable):
        """Sets the configurable of this Layer3NetworkSpec.


        :param configurable: The configurable of this Layer3NetworkSpec.  # noqa: E501
        :type: bool
        """
        if configurable is None:
            raise ValueError("Invalid value for `configurable`, must not be `None`")  # noqa: E501

        self._configurable = configurable

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
        if issubclass(Layer3NetworkSpec, dict):
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
        if not isinstance(other, Layer3NetworkSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
