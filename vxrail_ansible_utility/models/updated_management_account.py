# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.400
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdatedManagementAccount(object):
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
        'component': 'str',
        'hostname': 'str',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'component': 'component',
        'hostname': 'hostname',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, component=None, hostname=None, status=None, message=None):  # noqa: E501
        """UpdatedManagementAccount - a model defined in Swagger"""  # noqa: E501
        self._component = None
        self._hostname = None
        self._status = None
        self._message = None
        self.discriminator = None
        self.component = component
        self.hostname = hostname
        self.status = status
        if message is not None:
            self.message = message

    @property
    def component(self):
        """Gets the component of this UpdatedManagementAccount.  # noqa: E501

        The component type  # noqa: E501

        :return: The component of this UpdatedManagementAccount.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this UpdatedManagementAccount.

        The component type  # noqa: E501

        :param component: The component of this UpdatedManagementAccount.  # noqa: E501
        :type: str
        """
        if component is None:
            raise ValueError("Invalid value for `component`, must not be `None`")  # noqa: E501

        self._component = component

    @property
    def hostname(self):
        """Gets the hostname of this UpdatedManagementAccount.  # noqa: E501

        The hostname of the vCenter or ESXi host  # noqa: E501

        :return: The hostname of this UpdatedManagementAccount.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this UpdatedManagementAccount.

        The hostname of the vCenter or ESXi host  # noqa: E501

        :param hostname: The hostname of this UpdatedManagementAccount.  # noqa: E501
        :type: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def status(self):
        """Gets the status of this UpdatedManagementAccount.  # noqa: E501

        Information about whether the password update is successful or failed  # noqa: E501

        :return: The status of this UpdatedManagementAccount.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdatedManagementAccount.

        Information about whether the password update is successful or failed  # noqa: E501

        :param status: The status of this UpdatedManagementAccount.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def message(self):
        """Gets the message of this UpdatedManagementAccount.  # noqa: E501

        Informational message about the update  # noqa: E501

        :return: The message of this UpdatedManagementAccount.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UpdatedManagementAccount.

        Informational message about the update  # noqa: E501

        :param message: The message of this UpdatedManagementAccount.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(UpdatedManagementAccount, dict):
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
        if not isinstance(other, UpdatedManagementAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
