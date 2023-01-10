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

class LogSpec(object):
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
        'types': 'list[str]',
        'nodes': 'list[str]',
        'autoclean': 'bool'
    }

    attribute_map = {
        'types': 'types',
        'nodes': 'nodes',
        'autoclean': 'autoclean'
    }

    def __init__(self, types=None, nodes=None, autoclean=None):  # noqa: E501
        """LogSpec - a model defined in Swagger"""  # noqa: E501
        self._types = None
        self._nodes = None
        self._autoclean = None
        self.discriminator = None
        self.types = types
        if nodes is not None:
            self.nodes = nodes
        if autoclean is not None:
            self.autoclean = autoclean

    @property
    def types(self):
        """Gets the types of this LogSpec.  # noqa: E501

        An array of the components included in the log  # noqa: E501

        :return: The types of this LogSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this LogSpec.

        An array of the components included in the log  # noqa: E501

        :param types: The types of this LogSpec.  # noqa: E501
        :type: list[str]
        """
        if types is None:
            raise ValueError("Invalid value for `types`, must not be `None`")  # noqa: E501
        allowed_values = ["vxm", "vcenter", "esxi", "idrac", "ptagent", "witness"]  # noqa: E501
        if not set(types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._types = types

    @property
    def nodes(self):
        """Gets the nodes of this LogSpec.  # noqa: E501

        An array of serial numbers for the nodes included in the log  # noqa: E501

        :return: The nodes of this LogSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this LogSpec.

        An array of serial numbers for the nodes included in the log  # noqa: E501

        :param nodes: The nodes of this LogSpec.  # noqa: E501
        :type: list[str]
        """

        self._nodes = nodes

    @property
    def autoclean(self):
        """Gets the autoclean of this LogSpec.  # noqa: E501

        Whether to auto clean log bundles if VxRail Manager is at capacity  # noqa: E501

        :return: The autoclean of this LogSpec.  # noqa: E501
        :rtype: bool
        """
        return self._autoclean

    @autoclean.setter
    def autoclean(self, autoclean):
        """Sets the autoclean of this LogSpec.

        Whether to auto clean log bundles if VxRail Manager is at capacity  # noqa: E501

        :param autoclean: The autoclean of this LogSpec.  # noqa: E501
        :type: bool
        """

        self._autoclean = autoclean

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
        if issubclass(LogSpec, dict):
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
        if not isinstance(other, LogSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
