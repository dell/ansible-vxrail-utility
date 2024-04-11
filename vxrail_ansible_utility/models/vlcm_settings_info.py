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

class VlcmSettingsInfo(object):
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
        'enabled': 'bool',
        'cluster_name': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'cluster_name': 'cluster_name'
    }

    def __init__(self, enabled=None, cluster_name=None):  # noqa: E501
        """VlcmSettingsInfo - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._cluster_name = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if cluster_name is not None:
            self.cluster_name = cluster_name

    @property
    def enabled(self):
        """Gets the enabled of this VlcmSettingsInfo.  # noqa: E501

        Indicates whether vLCM settings are enabled.  # noqa: E501

        :return: The enabled of this VlcmSettingsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this VlcmSettingsInfo.

        Indicates whether vLCM settings are enabled.  # noqa: E501

        :param enabled: The enabled of this VlcmSettingsInfo.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def cluster_name(self):
        """Gets the cluster_name of this VlcmSettingsInfo.  # noqa: E501


        :return: The cluster_name of this VlcmSettingsInfo.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this VlcmSettingsInfo.


        :param cluster_name: The cluster_name of this VlcmSettingsInfo.  # noqa: E501
        :type: str
        """

        self._cluster_name = cluster_name

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
        if issubclass(VlcmSettingsInfo, dict):
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
        if not isinstance(other, VlcmSettingsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other