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

class VlcmParametersV2(object):
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
        'enforce_quick_patch': 'VlcmParametersV2EnforceQuickPatch',
        'parallel_remediation_action': 'VlcmParametersV2ParallelRemediationAction',
        'enable_quick_boot': 'bool'
    }

    attribute_map = {
        'enforce_quick_patch': 'enforce_quick_patch',
        'parallel_remediation_action': 'parallel_remediation_action',
        'enable_quick_boot': 'enable_quick_boot'
    }

    def __init__(self, enforce_quick_patch=None, parallel_remediation_action=None, enable_quick_boot=None):  # noqa: E501
        """VlcmParametersV2 - a model defined in Swagger"""  # noqa: E501
        self._enforce_quick_patch = None
        self._parallel_remediation_action = None
        self._enable_quick_boot = None
        self.discriminator = None
        if enforce_quick_patch is not None:
            self.enforce_quick_patch = enforce_quick_patch
        if parallel_remediation_action is not None:
            self.parallel_remediation_action = parallel_remediation_action
        if enable_quick_boot is not None:
            self.enable_quick_boot = enable_quick_boot

    @property
    def enforce_quick_patch(self):
        """Gets the enforce_quick_patch of this VlcmParametersV2.  # noqa: E501


        :return: The enforce_quick_patch of this VlcmParametersV2.  # noqa: E501
        :rtype: VlcmParametersV2EnforceQuickPatch
        """
        return self._enforce_quick_patch

    @enforce_quick_patch.setter
    def enforce_quick_patch(self, enforce_quick_patch):
        """Sets the enforce_quick_patch of this VlcmParametersV2.


        :param enforce_quick_patch: The enforce_quick_patch of this VlcmParametersV2.  # noqa: E501
        :type: VlcmParametersV2EnforceQuickPatch
        """

        self._enforce_quick_patch = enforce_quick_patch

    @property
    def parallel_remediation_action(self):
        """Gets the parallel_remediation_action of this VlcmParametersV2.  # noqa: E501


        :return: The parallel_remediation_action of this VlcmParametersV2.  # noqa: E501
        :rtype: VlcmParametersV2ParallelRemediationAction
        """
        return self._parallel_remediation_action

    @parallel_remediation_action.setter
    def parallel_remediation_action(self, parallel_remediation_action):
        """Sets the parallel_remediation_action of this VlcmParametersV2.


        :param parallel_remediation_action: The parallel_remediation_action of this VlcmParametersV2.  # noqa: E501
        :type: VlcmParametersV2ParallelRemediationAction
        """

        self._parallel_remediation_action = parallel_remediation_action

    @property
    def enable_quick_boot(self):
        """Gets the enable_quick_boot of this VlcmParametersV2.  # noqa: E501

        Enable quick boot to reduce reboot time.   # noqa: E501

        :return: The enable_quick_boot of this VlcmParametersV2.  # noqa: E501
        :rtype: bool
        """
        return self._enable_quick_boot

    @enable_quick_boot.setter
    def enable_quick_boot(self, enable_quick_boot):
        """Sets the enable_quick_boot of this VlcmParametersV2.

        Enable quick boot to reduce reboot time.   # noqa: E501

        :param enable_quick_boot: The enable_quick_boot of this VlcmParametersV2.  # noqa: E501
        :type: bool
        """

        self._enable_quick_boot = enable_quick_boot

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
        if issubclass(VlcmParametersV2, dict):
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
        if not isinstance(other, VlcmParametersV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
