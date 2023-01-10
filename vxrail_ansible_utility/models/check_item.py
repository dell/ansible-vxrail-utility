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

class CheckItem(object):
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
        'status': 'str',
        'check_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'plugin_name': 'str',
        'plugin_version': 'str',
        'result': 'CheckItemResult'
    }

    attribute_map = {
        'status': 'status',
        'check_id': 'check_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'plugin_name': 'plugin_name',
        'plugin_version': 'plugin_version',
        'result': 'result'
    }

    def __init__(self, status=None, check_id=None, start_time=None, end_time=None, plugin_name=None, plugin_version=None, result=None):  # noqa: E501
        """CheckItem - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._check_id = None
        self._start_time = None
        self._end_time = None
        self._plugin_name = None
        self._plugin_version = None
        self._result = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if check_id is not None:
            self.check_id = check_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_version is not None:
            self.plugin_version = plugin_version
        if result is not None:
            self.result = result

    @property
    def status(self):
        """Gets the status of this CheckItem.  # noqa: E501

        Execution status of the pre-check  # noqa: E501

        :return: The status of this CheckItem.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CheckItem.

        Execution status of the pre-check  # noqa: E501

        :param status: The status of this CheckItem.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def check_id(self):
        """Gets the check_id of this CheckItem.  # noqa: E501

        Check ID  # noqa: E501

        :return: The check_id of this CheckItem.  # noqa: E501
        :rtype: str
        """
        return self._check_id

    @check_id.setter
    def check_id(self, check_id):
        """Sets the check_id of this CheckItem.

        Check ID  # noqa: E501

        :param check_id: The check_id of this CheckItem.  # noqa: E501
        :type: str
        """

        self._check_id = check_id

    @property
    def start_time(self):
        """Gets the start_time of this CheckItem.  # noqa: E501

        Start time of the pre-check  # noqa: E501

        :return: The start_time of this CheckItem.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CheckItem.

        Start time of the pre-check  # noqa: E501

        :param start_time: The start_time of this CheckItem.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CheckItem.  # noqa: E501

        end time of check  # noqa: E501

        :return: The end_time of this CheckItem.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CheckItem.

        end time of check  # noqa: E501

        :param end_time: The end_time of this CheckItem.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def plugin_name(self):
        """Gets the plugin_name of this CheckItem.  # noqa: E501

        Plugin check name  # noqa: E501

        :return: The plugin_name of this CheckItem.  # noqa: E501
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this CheckItem.

        Plugin check name  # noqa: E501

        :param plugin_name: The plugin_name of this CheckItem.  # noqa: E501
        :type: str
        """

        self._plugin_name = plugin_name

    @property
    def plugin_version(self):
        """Gets the plugin_version of this CheckItem.  # noqa: E501

        plugin check version  # noqa: E501

        :return: The plugin_version of this CheckItem.  # noqa: E501
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        """Sets the plugin_version of this CheckItem.

        plugin check version  # noqa: E501

        :param plugin_version: The plugin_version of this CheckItem.  # noqa: E501
        :type: str
        """

        self._plugin_version = plugin_version

    @property
    def result(self):
        """Gets the result of this CheckItem.  # noqa: E501


        :return: The result of this CheckItem.  # noqa: E501
        :rtype: CheckItemResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CheckItem.


        :param result: The result of this CheckItem.  # noqa: E501
        :type: CheckItemResult
        """

        self._result = result

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
        if issubclass(CheckItem, dict):
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
        if not isinstance(other, CheckItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
