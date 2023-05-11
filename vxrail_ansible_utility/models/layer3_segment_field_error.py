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

class Layer3SegmentFieldError(object):
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
        'id': 'str',
        'errors': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'errors': 'errors'
    }

    def __init__(self, id=None, errors=None):  # noqa: E501
        """Layer3SegmentFieldError - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._errors = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if errors is not None:
            self.errors = errors

    @property
    def id(self):
        """Gets the id of this Layer3SegmentFieldError.  # noqa: E501


        :return: The id of this Layer3SegmentFieldError.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Layer3SegmentFieldError.


        :param id: The id of this Layer3SegmentFieldError.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def errors(self):
        """Gets the errors of this Layer3SegmentFieldError.  # noqa: E501


        :return: The errors of this Layer3SegmentFieldError.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Layer3SegmentFieldError.


        :param errors: The errors of this Layer3SegmentFieldError.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

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
        if issubclass(Layer3SegmentFieldError, dict):
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
        if not isinstance(other, Layer3SegmentFieldError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
