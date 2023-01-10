# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.410
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LcmEcosystemCheckSpec(object):
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
        'continue_with_incompatible': 'bool',
        'components': 'list[EcosystemComponentsSpec]'
    }

    attribute_map = {
        'continue_with_incompatible': 'continue_with_incompatible',
        'components': 'components'
    }

    def __init__(self, continue_with_incompatible=None, components=None):  # noqa: E501
        """LcmEcosystemCheckSpec - a model defined in Swagger"""  # noqa: E501
        self._continue_with_incompatible = None
        self._components = None
        self.discriminator = None
        if continue_with_incompatible is not None:
            self.continue_with_incompatible = continue_with_incompatible
        if components is not None:
            self.components = components

    @property
    def continue_with_incompatible(self):
        """Gets the continue_with_incompatible of this LcmEcosystemCheckSpec.  # noqa: E501


        :return: The continue_with_incompatible of this LcmEcosystemCheckSpec.  # noqa: E501
        :rtype: bool
        """
        return self._continue_with_incompatible

    @continue_with_incompatible.setter
    def continue_with_incompatible(self, continue_with_incompatible):
        """Sets the continue_with_incompatible of this LcmEcosystemCheckSpec.


        :param continue_with_incompatible: The continue_with_incompatible of this LcmEcosystemCheckSpec.  # noqa: E501
        :type: bool
        """

        self._continue_with_incompatible = continue_with_incompatible

    @property
    def components(self):
        """Gets the components of this LcmEcosystemCheckSpec.  # noqa: E501


        :return: The components of this LcmEcosystemCheckSpec.  # noqa: E501
        :rtype: list[EcosystemComponentsSpec]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this LcmEcosystemCheckSpec.


        :param components: The components of this LcmEcosystemCheckSpec.  # noqa: E501
        :type: list[EcosystemComponentsSpec]
        """

        self._components = components

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
        if issubclass(LcmEcosystemCheckSpec, dict):
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
        if not isinstance(other, LcmEcosystemCheckSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
