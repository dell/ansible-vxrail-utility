# coding: utf-8

"""
    Day1 Bring Up Configuration

    The set of Day 1 Bring Up Configuration API(s) are used to deploy VxRail cluster.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class SystemInitSpecVcenterSsoDomain(object):
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
        'server': 'str',
        'port': 'int',
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'server': 'server',
        'port': 'port',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, server=None, port=None, username=None, password=None):  # noqa: E501
        """SystemInitSpecVcenterSsoDomain - a model defined in Swagger"""  # noqa: E501
        self._server = None
        self._port = None
        self._username = None
        self._password = None
        self.discriminator = None
        if server is not None:
            self.server = server
        if port is not None:
            self.port = port
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

    @property
    def server(self):
        """Gets the server of this SystemInitSpecVcenterSsoDomain.  # noqa: E501


        :return: The server of this SystemInitSpecVcenterSsoDomain.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this SystemInitSpecVcenterSsoDomain.


        :param server: The server of this SystemInitSpecVcenterSsoDomain.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def port(self):
        """Gets the port of this SystemInitSpecVcenterSsoDomain.  # noqa: E501


        :return: The port of this SystemInitSpecVcenterSsoDomain.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SystemInitSpecVcenterSsoDomain.


        :param port: The port of this SystemInitSpecVcenterSsoDomain.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def username(self):
        """Gets the username of this SystemInitSpecVcenterSsoDomain.  # noqa: E501


        :return: The username of this SystemInitSpecVcenterSsoDomain.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SystemInitSpecVcenterSsoDomain.


        :param username: The username of this SystemInitSpecVcenterSsoDomain.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this SystemInitSpecVcenterSsoDomain.  # noqa: E501


        :return: The password of this SystemInitSpecVcenterSsoDomain.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SystemInitSpecVcenterSsoDomain.


        :param password: The password of this SystemInitSpecVcenterSsoDomain.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(SystemInitSpecVcenterSsoDomain, dict):
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
        if not isinstance(other, SystemInitSpecVcenterSsoDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
