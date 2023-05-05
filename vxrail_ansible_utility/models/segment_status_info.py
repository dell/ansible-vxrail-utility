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

class SegmentStatusInfo(object):
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
        'type': 'str',
        'status': 'str',
        'errors': 'list[SegmentErrorSpec]'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'errors': 'errors'
    }

    def __init__(self, type=None, status=None, errors=None):  # noqa: E501
        """SegmentStatusInfo - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._status = None
        self._errors = None
        self.discriminator = None
        self.type = type
        self.status = status
        if errors is not None:
            self.errors = errors

    @property
    def type(self):
        """Gets the type of this SegmentStatusInfo.  # noqa: E501

        The type of health check performed  # noqa: E501

        :return: The type of this SegmentStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SegmentStatusInfo.

        The type of health check performed  # noqa: E501

        :param type: The type of this SegmentStatusInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this SegmentStatusInfo.  # noqa: E501

        The status of the health check  # noqa: E501

        :return: The status of this SegmentStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SegmentStatusInfo.

        The status of the health check  # noqa: E501

        :param status: The status of this SegmentStatusInfo.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["HEALTHY", "UNHEALTHY", "SKIP"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def errors(self):
        """Gets the errors of this SegmentStatusInfo.  # noqa: E501

        Details about health check issues  # noqa: E501

        :return: The errors of this SegmentStatusInfo.  # noqa: E501
        :rtype: list[SegmentErrorSpec]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this SegmentStatusInfo.

        Details about health check issues  # noqa: E501

        :param errors: The errors of this SegmentStatusInfo.  # noqa: E501
        :type: list[SegmentErrorSpec]
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
        if issubclass(SegmentStatusInfo, dict):
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
        if not isinstance(other, SegmentStatusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
