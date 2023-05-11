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

class TemporaryIpSettingSpec(object):
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
        'temporary_ip': 'str',
        'gateway': 'str',
        'netmask': 'str'
    }

    attribute_map = {
        'temporary_ip': 'temporary_ip',
        'gateway': 'gateway',
        'netmask': 'netmask'
    }

    def __init__(self, temporary_ip=None, gateway=None, netmask=None):  # noqa: E501
        """TemporaryIpSettingSpec - a model defined in Swagger"""  # noqa: E501
        self._temporary_ip = None
        self._gateway = None
        self._netmask = None
        self.discriminator = None
        self.temporary_ip = temporary_ip
        self.gateway = gateway
        self.netmask = netmask

    @property
    def temporary_ip(self):
        """Gets the temporary_ip of this TemporaryIpSettingSpec.  # noqa: E501

        Temporary IP address to be used during the VMware vCenter Server upgrade.  # noqa: E501

        :return: The temporary_ip of this TemporaryIpSettingSpec.  # noqa: E501
        :rtype: str
        """
        return self._temporary_ip

    @temporary_ip.setter
    def temporary_ip(self, temporary_ip):
        """Sets the temporary_ip of this TemporaryIpSettingSpec.

        Temporary IP address to be used during the VMware vCenter Server upgrade.  # noqa: E501

        :param temporary_ip: The temporary_ip of this TemporaryIpSettingSpec.  # noqa: E501
        :type: str
        """
        if temporary_ip is None:
            raise ValueError("Invalid value for `temporary_ip`, must not be `None`")  # noqa: E501

        self._temporary_ip = temporary_ip

    @property
    def gateway(self):
        """Gets the gateway of this TemporaryIpSettingSpec.  # noqa: E501

        Gateway to be used during the VMware vCenter Server upgrade.  # noqa: E501

        :return: The gateway of this TemporaryIpSettingSpec.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this TemporaryIpSettingSpec.

        Gateway to be used during the VMware vCenter Server upgrade.  # noqa: E501

        :param gateway: The gateway of this TemporaryIpSettingSpec.  # noqa: E501
        :type: str
        """
        if gateway is None:
            raise ValueError("Invalid value for `gateway`, must not be `None`")  # noqa: E501

        self._gateway = gateway

    @property
    def netmask(self):
        """Gets the netmask of this TemporaryIpSettingSpec.  # noqa: E501

        Netmask to be used during the VMware vCenter Server upgrade.  # noqa: E501

        :return: The netmask of this TemporaryIpSettingSpec.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this TemporaryIpSettingSpec.

        Netmask to be used during the VMware vCenter Server upgrade.  # noqa: E501

        :param netmask: The netmask of this TemporaryIpSettingSpec.  # noqa: E501
        :type: str
        """
        if netmask is None:
            raise ValueError("Invalid value for `netmask`, must not be `None`")  # noqa: E501

        self._netmask = netmask

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
        if issubclass(TemporaryIpSettingSpec, dict):
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
        if not isinstance(other, TemporaryIpSettingSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
