# coding: utf-8

"""
    Day1 Bring Up Configuration

    The set of Day 1 Bring Up Configuration API(s) are used to deploy VxRail cluster.  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Day1StateInfo(object):
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
        'state': 'str',
        'config_params': 'SystemInitSpecV4'
    }

    attribute_map = {
        'state': 'state',
        'config_params': 'config_params'
    }

    def __init__(self, state=None, config_params=None):  # noqa: E501
        """Day1StateInfo - a model defined in Swagger"""  # noqa: E501
        self._state = None
        self._config_params = None
        self.discriminator = None
        self.state = state
        self.config_params = config_params

    @property
    def state(self):
        """Gets the state of this Day1StateInfo.  # noqa: E501

        state name  # noqa: E501

        :return: The state of this Day1StateInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Day1StateInfo.

        state name  # noqa: E501

        :param state: The state of this Day1StateInfo.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["NOT_CONFIGURED", "PRE_CONFIGURING", "PRE_CONFIGURATION_FAILED", "PRE_CONFIGURATION_DONE", "VALIDATING", "VALIDATION_FAILED", "VALIDATION_DONE", "CONFIGURING", "CONFIGURATION_DONE", "CONFIGURATION_FAILED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def config_params(self):
        """Gets the config_params of this Day1StateInfo.  # noqa: E501


        :return: The config_params of this Day1StateInfo.  # noqa: E501
        :rtype: SystemInitSpecV4
        """
        return self._config_params

    @config_params.setter
    def config_params(self, config_params):
        """Sets the config_params of this Day1StateInfo.


        :param config_params: The config_params of this Day1StateInfo.  # noqa: E501
        :type: SystemInitSpecV4
        """
        if config_params is None:
            raise ValueError("Invalid value for `config_params`, must not be `None`")  # noqa: E501

        self._config_params = config_params

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
        if issubclass(Day1StateInfo, dict):
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
        if not isinstance(other, Day1StateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
