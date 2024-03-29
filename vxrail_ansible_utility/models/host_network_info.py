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

class HostNetworkInfo(object):
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
        'management_ip': 'str',
        'vmotion_ip': 'str',
        'vsan_ip': 'str',
        'witness_ip': 'str'
    }

    attribute_map = {
        'management_ip': 'management_ip',
        'vmotion_ip': 'vmotion_ip',
        'vsan_ip': 'vsan_ip',
        'witness_ip': 'witness_ip'
    }

    def __init__(self, management_ip=None, vmotion_ip=None, vsan_ip=None, witness_ip=None):  # noqa: E501
        """HostNetworkInfo - a model defined in Swagger"""  # noqa: E501
        self._management_ip = None
        self._vmotion_ip = None
        self._vsan_ip = None
        self._witness_ip = None
        self.discriminator = None
        self.management_ip = management_ip
        self.vmotion_ip = vmotion_ip
        self.vsan_ip = vsan_ip
        if witness_ip is not None:
            self.witness_ip = witness_ip

    @property
    def management_ip(self):
        """Gets the management_ip of this HostNetworkInfo.  # noqa: E501


        :return: The management_ip of this HostNetworkInfo.  # noqa: E501
        :rtype: str
        """
        return self._management_ip

    @management_ip.setter
    def management_ip(self, management_ip):
        """Sets the management_ip of this HostNetworkInfo.


        :param management_ip: The management_ip of this HostNetworkInfo.  # noqa: E501
        :type: str
        """
        if management_ip is None:
            raise ValueError("Invalid value for `management_ip`, must not be `None`")  # noqa: E501

        self._management_ip = management_ip

    @property
    def vmotion_ip(self):
        """Gets the vmotion_ip of this HostNetworkInfo.  # noqa: E501


        :return: The vmotion_ip of this HostNetworkInfo.  # noqa: E501
        :rtype: str
        """
        return self._vmotion_ip

    @vmotion_ip.setter
    def vmotion_ip(self, vmotion_ip):
        """Sets the vmotion_ip of this HostNetworkInfo.


        :param vmotion_ip: The vmotion_ip of this HostNetworkInfo.  # noqa: E501
        :type: str
        """
        if vmotion_ip is None:
            raise ValueError("Invalid value for `vmotion_ip`, must not be `None`")  # noqa: E501

        self._vmotion_ip = vmotion_ip

    @property
    def vsan_ip(self):
        """Gets the vsan_ip of this HostNetworkInfo.  # noqa: E501


        :return: The vsan_ip of this HostNetworkInfo.  # noqa: E501
        :rtype: str
        """
        return self._vsan_ip

    @vsan_ip.setter
    def vsan_ip(self, vsan_ip):
        """Sets the vsan_ip of this HostNetworkInfo.


        :param vsan_ip: The vsan_ip of this HostNetworkInfo.  # noqa: E501
        :type: str
        """
        if vsan_ip is None:
            raise ValueError("Invalid value for `vsan_ip`, must not be `None`")  # noqa: E501

        self._vsan_ip = vsan_ip

    @property
    def witness_ip(self):
        """Gets the witness_ip of this HostNetworkInfo.  # noqa: E501


        :return: The witness_ip of this HostNetworkInfo.  # noqa: E501
        :rtype: str
        """
        return self._witness_ip

    @witness_ip.setter
    def witness_ip(self, witness_ip):
        """Sets the witness_ip of this HostNetworkInfo.


        :param witness_ip: The witness_ip of this HostNetworkInfo.  # noqa: E501
        :type: str
        """

        self._witness_ip = witness_ip

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
        if issubclass(HostNetworkInfo, dict):
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
        if not isinstance(other, HostNetworkInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
