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

class VlcmParametersV3ParallelRemediationAction(object):
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
        'max_hosts': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'max_hosts': 'max_hosts'
    }

    def __init__(self, enabled=None, max_hosts=None):  # noqa: E501
        """VlcmParametersV3ParallelRemediationAction - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._max_hosts = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if max_hosts is not None:
            self.max_hosts = max_hosts

    @property
    def enabled(self):
        """Gets the enabled of this VlcmParametersV3ParallelRemediationAction.  # noqa: E501


        :return: The enabled of this VlcmParametersV3ParallelRemediationAction.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this VlcmParametersV3ParallelRemediationAction.


        :param enabled: The enabled of this VlcmParametersV3ParallelRemediationAction.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def max_hosts(self):
        """Gets the max_hosts of this VlcmParametersV3ParallelRemediationAction.  # noqa: E501

        Assign the maximum number of hosts to enter maintenance mode at a time and perform remediation.  This number should be at least 2 if parallel remediation is enabled.   Set it as null or leave it blank to indicate that it will be decided automatically based on the total number of hosts.  # noqa: E501

        :return: The max_hosts of this VlcmParametersV3ParallelRemediationAction.  # noqa: E501
        :rtype: int
        """
        return self._max_hosts

    @max_hosts.setter
    def max_hosts(self, max_hosts):
        """Sets the max_hosts of this VlcmParametersV3ParallelRemediationAction.

        Assign the maximum number of hosts to enter maintenance mode at a time and perform remediation.  This number should be at least 2 if parallel remediation is enabled.   Set it as null or leave it blank to indicate that it will be decided automatically based on the total number of hosts.  # noqa: E501

        :param max_hosts: The max_hosts of this VlcmParametersV3ParallelRemediationAction.  # noqa: E501
        :type: int
        """

        self._max_hosts = max_hosts

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
        if issubclass(VlcmParametersV3ParallelRemediationAction, dict):
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
        if not isinstance(other, VlcmParametersV3ParallelRemediationAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
