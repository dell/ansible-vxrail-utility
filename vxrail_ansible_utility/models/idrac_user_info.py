# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 1.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class IdracUserInfo(object):
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
        'id': 'int',
        'name': 'str',
        'privilege': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'privilege': 'privilege'
    }

    def __init__(self, id=None, name=None, privilege=None):  # noqa: E501
        """IdracUserInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._privilege = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.privilege = privilege

    @property
    def id(self):
        """Gets the id of this IdracUserInfo.  # noqa: E501

        The ID of the user in iDRAC, value scope 3-16  # noqa: E501

        :return: The id of this IdracUserInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdracUserInfo.

        The ID of the user in iDRAC, value scope 3-16  # noqa: E501

        :param id: The id of this IdracUserInfo.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this IdracUserInfo.  # noqa: E501

        The iDRAC username  # noqa: E501

        :return: The name of this IdracUserInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdracUserInfo.

        The iDRAC username  # noqa: E501

        :param name: The name of this IdracUserInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def privilege(self):
        """Gets the privilege of this IdracUserInfo.  # noqa: E501

        The iDRAC user privilege  # noqa: E501

        :return: The privilege of this IdracUserInfo.  # noqa: E501
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this IdracUserInfo.

        The iDRAC user privilege  # noqa: E501

        :param privilege: The privilege of this IdracUserInfo.  # noqa: E501
        :type: str
        """
        if privilege is None:
            raise ValueError("Invalid value for `privilege`, must not be `None`")  # noqa: E501
        allowed_values = ["ADMIN", "OPER", "READONLY", "NONE", "UNKNOWN"]  # noqa: E501
        if privilege not in allowed_values:
            raise ValueError(
                "Invalid value for `privilege` ({0}), must be one of {1}"  # noqa: E501
                .format(privilege, allowed_values)
            )

        self._privilege = privilege

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
        if issubclass(IdracUserInfo, dict):
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
        if not isinstance(other, IdracUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
