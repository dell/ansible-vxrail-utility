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

class VlcmUpgradeImageDepotSpec(object):
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
        'bundle_file_locator': 'str',
        'vxrail': 'VxRailManagerSpec'
    }

    attribute_map = {
        'bundle_file_locator': 'bundle_file_locator',
        'vxrail': 'vxrail'
    }

    def __init__(self, bundle_file_locator=None, vxrail=None):  # noqa: E501
        """VlcmUpgradeImageDepotSpec - a model defined in Swagger"""  # noqa: E501
        self._bundle_file_locator = None
        self._vxrail = None
        self.discriminator = None
        self.bundle_file_locator = bundle_file_locator
        self.vxrail = vxrail

    @property
    def bundle_file_locator(self):
        """Gets the bundle_file_locator of this VlcmUpgradeImageDepotSpec.  # noqa: E501

        File path of the upgrade bundle.  # noqa: E501

        :return: The bundle_file_locator of this VlcmUpgradeImageDepotSpec.  # noqa: E501
        :rtype: str
        """
        return self._bundle_file_locator

    @bundle_file_locator.setter
    def bundle_file_locator(self, bundle_file_locator):
        """Sets the bundle_file_locator of this VlcmUpgradeImageDepotSpec.

        File path of the upgrade bundle.  # noqa: E501

        :param bundle_file_locator: The bundle_file_locator of this VlcmUpgradeImageDepotSpec.  # noqa: E501
        :type: str
        """
        if bundle_file_locator is None:
            raise ValueError("Invalid value for `bundle_file_locator`, must not be `None`")  # noqa: E501

        self._bundle_file_locator = bundle_file_locator

    @property
    def vxrail(self):
        """Gets the vxrail of this VlcmUpgradeImageDepotSpec.  # noqa: E501


        :return: The vxrail of this VlcmUpgradeImageDepotSpec.  # noqa: E501
        :rtype: VxRailManagerSpec
        """
        return self._vxrail

    @vxrail.setter
    def vxrail(self, vxrail):
        """Sets the vxrail of this VlcmUpgradeImageDepotSpec.


        :param vxrail: The vxrail of this VlcmUpgradeImageDepotSpec.  # noqa: E501
        :type: VxRailManagerSpec
        """
        if vxrail is None:
            raise ValueError("Invalid value for `vxrail`, must not be `None`")  # noqa: E501

        self._vxrail = vxrail

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
        if issubclass(VlcmUpgradeImageDepotSpec, dict):
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
        if not isinstance(other, VlcmUpgradeImageDepotSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
