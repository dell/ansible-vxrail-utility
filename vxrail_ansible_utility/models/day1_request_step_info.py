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

class Day1RequestStepInfo(object):
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
        'name': 'str',
        'path': 'str',
        'state': 'str',
        'steps': 'list[Day1RequestStepInfo]',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'path': 'path',
        'state': 'state',
        'steps': 'steps',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, name=None, path=None, state=None, steps=None, start_time=None, end_time=None):  # noqa: E501
        """Day1RequestStepInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._path = None
        self._state = None
        self._steps = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.path = path
        self.state = state
        if steps is not None:
            self.steps = steps
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        """Gets the id of this Day1RequestStepInfo.  # noqa: E501

        The identification string for the step  # noqa: E501

        :return: The id of this Day1RequestStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Day1RequestStepInfo.

        The identification string for the step  # noqa: E501

        :param id: The id of this Day1RequestStepInfo.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Day1RequestStepInfo.  # noqa: E501

        The name of the step  # noqa: E501

        :return: The name of this Day1RequestStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Day1RequestStepInfo.

        The name of the step  # noqa: E501

        :param name: The name of this Day1RequestStepInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this Day1RequestStepInfo.  # noqa: E501

        The full path for the step including parent including parent steps  # noqa: E501

        :return: The path of this Day1RequestStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Day1RequestStepInfo.

        The full path for the step including parent including parent steps  # noqa: E501

        :param path: The path of this Day1RequestStepInfo.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def state(self):
        """Gets the state of this Day1RequestStepInfo.  # noqa: E501

        The status state of the step  # noqa: E501

        :return: The state of this Day1RequestStepInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Day1RequestStepInfo.

        The status state of the step  # noqa: E501

        :param state: The state of this Day1RequestStepInfo.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["STARTED", "FAILED", "COMPLETED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def steps(self):
        """Gets the steps of this Day1RequestStepInfo.  # noqa: E501

        An array of any steps running in parallel  # noqa: E501

        :return: The steps of this Day1RequestStepInfo.  # noqa: E501
        :rtype: list[Day1RequestStepInfo]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this Day1RequestStepInfo.

        An array of any steps running in parallel  # noqa: E501

        :param steps: The steps of this Day1RequestStepInfo.  # noqa: E501
        :type: list[Day1RequestStepInfo]
        """

        self._steps = steps

    @property
    def start_time(self):
        """Gets the start_time of this Day1RequestStepInfo.  # noqa: E501

        The timestamp for the start of the step  # noqa: E501

        :return: The start_time of this Day1RequestStepInfo.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Day1RequestStepInfo.

        The timestamp for the start of the step  # noqa: E501

        :param start_time: The start_time of this Day1RequestStepInfo.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Day1RequestStepInfo.  # noqa: E501

        The timestamp for the end of the step  # noqa: E501

        :return: The end_time of this Day1RequestStepInfo.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Day1RequestStepInfo.

        The timestamp for the end of the step  # noqa: E501

        :param end_time: The end_time of this Day1RequestStepInfo.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

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
        if issubclass(Day1RequestStepInfo, dict):
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
        if not isinstance(other, Day1RequestStepInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
