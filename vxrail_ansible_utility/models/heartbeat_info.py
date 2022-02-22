# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.350
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class HeartbeatInfo(object):
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
        'status': 'str',
        'begin_time': 'datetime',
        'end_time': 'datetime',
        'message': 'str',
        'data': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'begin_time': 'beginTime',
        'end_time': 'endTime',
        'message': 'message',
        'data': 'data'
    }

    def __init__(self, id=None, status=None, begin_time=None, end_time=None, message=None, data=None):  # noqa: E501
        """HeartbeatInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._message = None
        self._data = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if message is not None:
            self.message = message
        if data is not None:
            self.data = data

    @property
    def id(self):
        """Gets the id of this HeartbeatInfo.  # noqa: E501

        ID of the heartbeat  # noqa: E501

        :return: The id of this HeartbeatInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HeartbeatInfo.

        ID of the heartbeat  # noqa: E501

        :param id: The id of this HeartbeatInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this HeartbeatInfo.  # noqa: E501

        Status of the heartbeat  # noqa: E501

        :return: The status of this HeartbeatInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HeartbeatInfo.

        Status of the heartbeat  # noqa: E501

        :param status: The status of this HeartbeatInfo.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["SUCCESS", "FAIL", "ESRS_INACTIVE", "INACTIVE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def begin_time(self):
        """Gets the begin_time of this HeartbeatInfo.  # noqa: E501

        The timestamp that status data started to be collected  # noqa: E501

        :return: The begin_time of this HeartbeatInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this HeartbeatInfo.

        The timestamp that status data started to be collected  # noqa: E501

        :param begin_time: The begin_time of this HeartbeatInfo.  # noqa: E501
        :type: datetime
        """

        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this HeartbeatInfo.  # noqa: E501

        The timestamp that status data stopped being collected  # noqa: E501

        :return: The end_time of this HeartbeatInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this HeartbeatInfo.

        The timestamp that status data stopped being collected  # noqa: E501

        :param end_time: The end_time of this HeartbeatInfo.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def message(self):
        """Gets the message of this HeartbeatInfo.  # noqa: E501

        Status message for the heartbeat  # noqa: E501

        :return: The message of this HeartbeatInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this HeartbeatInfo.

        Status message for the heartbeat  # noqa: E501

        :param message: The message of this HeartbeatInfo.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def data(self):
        """Gets the data of this HeartbeatInfo.  # noqa: E501

        The system configuration data of the heartbeat  # noqa: E501

        :return: The data of this HeartbeatInfo.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this HeartbeatInfo.

        The system configuration data of the heartbeat  # noqa: E501

        :param data: The data of this HeartbeatInfo.  # noqa: E501
        :type: str
        """

        self._data = data

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
        if issubclass(HeartbeatInfo, dict):
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
        if not isinstance(other, HeartbeatInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other