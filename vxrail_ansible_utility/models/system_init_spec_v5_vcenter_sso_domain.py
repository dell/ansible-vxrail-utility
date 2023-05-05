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

class SystemInitSpecV5VcenterSsoDomain(object):
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
        'password': 'str',
        'auto_accept_sso_vc_cert': 'bool'
    }

    attribute_map = {
        'server': 'server',
        'port': 'port',
        'username': 'username',
        'password': 'password',
        'auto_accept_sso_vc_cert': 'auto_accept_sso_vc_cert'
    }

    def __init__(self, server=None, port=None, username=None, password=None, auto_accept_sso_vc_cert=None):  # noqa: E501
        """SystemInitSpecV5VcenterSsoDomain - a model defined in Swagger"""  # noqa: E501
        self._server = None
        self._port = None
        self._username = None
        self._password = None
        self._auto_accept_sso_vc_cert = None
        self.discriminator = None
        if server is not None:
            self.server = server
        if port is not None:
            self.port = port
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if auto_accept_sso_vc_cert is not None:
            self.auto_accept_sso_vc_cert = auto_accept_sso_vc_cert

    @property
    def server(self):
        """Gets the server of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501

        The IP address of the SSO domain  # noqa: E501

        :return: The server of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this SystemInitSpecV5VcenterSsoDomain.

        The IP address of the SSO domain  # noqa: E501

        :param server: The server of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def port(self):
        """Gets the port of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501

        The port of the SSO domain  # noqa: E501

        :return: The port of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SystemInitSpecV5VcenterSsoDomain.

        The port of the SSO domain  # noqa: E501

        :param port: The port of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def username(self):
        """Gets the username of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501

        Username of the SSO domain  # noqa: E501

        :return: The username of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SystemInitSpecV5VcenterSsoDomain.

        Username of the SSO domain  # noqa: E501

        :param username: The username of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501

        Password of the SSO domain  # noqa: E501

        :return: The password of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SystemInitSpecV5VcenterSsoDomain.

        Password of the SSO domain  # noqa: E501

        :param password: The password of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def auto_accept_sso_vc_cert(self):
        """Gets the auto_accept_sso_vc_cert of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501

        Whether to automatically download the SSO vCenter root certificate. True means VxRail Manager will download the target SSO vCenter root certificate automatically. False means users should provide the target SSO vCenter root certificate manually.  # noqa: E501

        :return: The auto_accept_sso_vc_cert of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501
        :rtype: bool
        """
        return self._auto_accept_sso_vc_cert

    @auto_accept_sso_vc_cert.setter
    def auto_accept_sso_vc_cert(self, auto_accept_sso_vc_cert):
        """Sets the auto_accept_sso_vc_cert of this SystemInitSpecV5VcenterSsoDomain.

        Whether to automatically download the SSO vCenter root certificate. True means VxRail Manager will download the target SSO vCenter root certificate automatically. False means users should provide the target SSO vCenter root certificate manually.  # noqa: E501

        :param auto_accept_sso_vc_cert: The auto_accept_sso_vc_cert of this SystemInitSpecV5VcenterSsoDomain.  # noqa: E501
        :type: bool
        """

        self._auto_accept_sso_vc_cert = auto_accept_sso_vc_cert

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
        if issubclass(SystemInitSpecV5VcenterSsoDomain, dict):
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
        if not isinstance(other, SystemInitSpecV5VcenterSsoDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
