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

class RequestStatusInfo(object):
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
        'owner': 'str',
        'state': 'str',
        'error': 'str',
        'progress': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'target': 'str',
        'step': 'str',
        'detail': 'str',
        'extension': 'str'
    }

    attribute_map = {
        'id': 'id',
        'owner': 'owner',
        'state': 'state',
        'error': 'error',
        'progress': 'progress',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'target': 'target',
        'step': 'step',
        'detail': 'detail',
        'extension': 'extension'
    }

    def __init__(self, id=None, owner=None, state=None, error=None, progress=None, start_time=None, end_time=None, target=None, step=None, detail=None, extension=None):  # noqa: E501
        """RequestStatusInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._owner = None
        self._state = None
        self._error = None
        self._progress = None
        self._start_time = None
        self._end_time = None
        self._target = None
        self._step = None
        self._detail = None
        self._extension = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if owner is not None:
            self.owner = owner
        if state is not None:
            self.state = state
        if error is not None:
            self.error = error
        if progress is not None:
            self.progress = progress
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if target is not None:
            self.target = target
        if step is not None:
            self.step = step
        if detail is not None:
            self.detail = detail
        if extension is not None:
            self.extension = extension

    @property
    def id(self):
        """Gets the id of this RequestStatusInfo.  # noqa: E501

        Each asynchronous (long-running) request needs to return a requestId which can be used to get the status of execution.  # noqa: E501

        :return: The id of this RequestStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RequestStatusInfo.

        Each asynchronous (long-running) request needs to return a requestId which can be used to get the status of execution.  # noqa: E501

        :param id: The id of this RequestStatusInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this RequestStatusInfo.  # noqa: E501

        The owner of the request which is typically the user who issue the original request  # noqa: E501

        :return: The owner of this RequestStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this RequestStatusInfo.

        The owner of the request which is typically the user who issue the original request  # noqa: E501

        :param owner: The owner of this RequestStatusInfo.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def state(self):
        """Gets the state of this RequestStatusInfo.  # noqa: E501

        The current state of the execution  # noqa: E501

        :return: The state of this RequestStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RequestStatusInfo.

        The current state of the execution  # noqa: E501

        :param state: The state of this RequestStatusInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "STARTED", "IN_PROGRESS", "COMPLETED", "FAILED", "ABANDONED", "ABORTED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def error(self):
        """Gets the error of this RequestStatusInfo.  # noqa: E501

        The error message if the execution state is ERROR  # noqa: E501

        :return: The error of this RequestStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this RequestStatusInfo.

        The error message if the execution state is ERROR  # noqa: E501

        :param error: The error of this RequestStatusInfo.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def progress(self):
        """Gets the progress of this RequestStatusInfo.  # noqa: E501

        The progress of the current execution, ranging from 0 to 100  # noqa: E501

        :return: The progress of this RequestStatusInfo.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this RequestStatusInfo.

        The progress of the current execution, ranging from 0 to 100  # noqa: E501

        :param progress: The progress of this RequestStatusInfo.  # noqa: E501
        :type: int
        """

        self._progress = progress

    @property
    def start_time(self):
        """Gets the start_time of this RequestStatusInfo.  # noqa: E501

        The start time of the current execution  # noqa: E501

        :return: The start_time of this RequestStatusInfo.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RequestStatusInfo.

        The start time of the current execution  # noqa: E501

        :param start_time: The start_time of this RequestStatusInfo.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this RequestStatusInfo.  # noqa: E501

        The end time of the current execution  # noqa: E501

        :return: The end_time of this RequestStatusInfo.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this RequestStatusInfo.

        The end time of the current execution  # noqa: E501

        :param end_time: The end_time of this RequestStatusInfo.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def target(self):
        """Gets the target of this RequestStatusInfo.  # noqa: E501

        The target of the current execution  # noqa: E501

        :return: The target of this RequestStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this RequestStatusInfo.

        The target of the current execution  # noqa: E501

        :param target: The target of this RequestStatusInfo.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def step(self):
        """Gets the step of this RequestStatusInfo.  # noqa: E501

        The current step if the original request has been separated into multiple steps  # noqa: E501

        :return: The step of this RequestStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this RequestStatusInfo.

        The current step if the original request has been separated into multiple steps  # noqa: E501

        :param step: The step of this RequestStatusInfo.  # noqa: E501
        :type: str
        """

        self._step = step

    @property
    def detail(self):
        """Gets the detail of this RequestStatusInfo.  # noqa: E501

        The detailed status of a specific application  # noqa: E501

        :return: The detail of this RequestStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this RequestStatusInfo.

        The detailed status of a specific application  # noqa: E501

        :param detail: The detail of this RequestStatusInfo.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def extension(self):
        """Gets the extension of this RequestStatusInfo.  # noqa: E501

        The application specific status information  # noqa: E501

        :return: The extension of this RequestStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this RequestStatusInfo.

        The application specific status information  # noqa: E501

        :param extension: The extension of this RequestStatusInfo.  # noqa: E501
        :type: str
        """

        self._extension = extension

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
        if issubclass(RequestStatusInfo, dict):
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
        if not isinstance(other, RequestStatusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
