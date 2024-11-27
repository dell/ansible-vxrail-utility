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

class WitnessSpec(object):
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
        'witness_user': 'UserSpec',
        'auto_witness_upgrade': 'bool'
    }

    attribute_map = {
        'witness_user': 'witness_user',
        'auto_witness_upgrade': 'auto_witness_upgrade'
    }

    def __init__(self, witness_user=None, auto_witness_upgrade=None):  # noqa: E501
        """WitnessSpec - a model defined in Swagger"""  # noqa: E501
        self._witness_user = None
        self._auto_witness_upgrade = None
        self.discriminator = None
        if witness_user is not None:
            self.witness_user = witness_user
        self.auto_witness_upgrade = auto_witness_upgrade

    @property
    def witness_user(self):
        """Gets the witness_user of this WitnessSpec.  # noqa: E501


        :return: The witness_user of this WitnessSpec.  # noqa: E501
        :rtype: UserSpec
        """
        return self._witness_user

    @witness_user.setter
    def witness_user(self, witness_user):
        """Sets the witness_user of this WitnessSpec.


        :param witness_user: The witness_user of this WitnessSpec.  # noqa: E501
        :type: UserSpec
        """

        self._witness_user = witness_user

    @property
    def auto_witness_upgrade(self):
        """Gets the auto_witness_upgrade of this WitnessSpec.  # noqa: E501

        Whether VxRail will automatically upgrade the witness node.  # noqa: E501

        :return: The auto_witness_upgrade of this WitnessSpec.  # noqa: E501
        :rtype: bool
        """
        return self._auto_witness_upgrade

    @auto_witness_upgrade.setter
    def auto_witness_upgrade(self, auto_witness_upgrade):
        """Sets the auto_witness_upgrade of this WitnessSpec.

        Whether VxRail will automatically upgrade the witness node.  # noqa: E501

        :param auto_witness_upgrade: The auto_witness_upgrade of this WitnessSpec.  # noqa: E501
        :type: bool
        """
        if auto_witness_upgrade is None:
            raise ValueError("Invalid value for `auto_witness_upgrade`, must not be `None`")  # noqa: E501

        self._auto_witness_upgrade = auto_witness_upgrade

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
        if issubclass(WitnessSpec, dict):
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
        if not isinstance(other, WitnessSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
