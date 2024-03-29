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

class EnableCallhomeSpec(object):
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
        'serial_number': 'str',
        'pin': 'str',
        'access_key': 'str',
        'proxy_type': 'str',
        'proxy': 'CallhomeProxy',
        'gateways': 'list[CallhomeGateway]',
        'customer_contact_infos': 'list[CustomerContactInfo]',
        'connection_type': 'str'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'pin': 'pin',
        'access_key': 'access_key',
        'proxy_type': 'proxy_type',
        'proxy': 'proxy',
        'gateways': 'gateways',
        'customer_contact_infos': 'customer_contact_infos',
        'connection_type': 'connection_type'
    }

    def __init__(self, serial_number=None, pin=None, access_key=None, proxy_type=None, proxy=None, gateways=None, customer_contact_infos=None, connection_type=None):  # noqa: E501
        """EnableCallhomeSpec - a model defined in Swagger"""  # noqa: E501
        self._serial_number = None
        self._pin = None
        self._access_key = None
        self._proxy_type = None
        self._proxy = None
        self._gateways = None
        self._customer_contact_infos = None
        self._connection_type = None
        self.discriminator = None
        self.serial_number = serial_number
        if pin is not None:
            self.pin = pin
        if access_key is not None:
            self.access_key = access_key
        if proxy_type is not None:
            self.proxy_type = proxy_type
        if proxy is not None:
            self.proxy = proxy
        if gateways is not None:
            self.gateways = gateways
        if customer_contact_infos is not None:
            self.customer_contact_infos = customer_contact_infos
        self.connection_type = connection_type

    @property
    def serial_number(self):
        """Gets the serial_number of this EnableCallhomeSpec.  # noqa: E501

        node serial number for ESE enalement  # noqa: E501

        :return: The serial_number of this EnableCallhomeSpec.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this EnableCallhomeSpec.

        node serial number for ESE enalement  # noqa: E501

        :param serial_number: The serial_number of this EnableCallhomeSpec.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def pin(self):
        """Gets the pin of this EnableCallhomeSpec.  # noqa: E501

        the PIN code  # noqa: E501

        :return: The pin of this EnableCallhomeSpec.  # noqa: E501
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this EnableCallhomeSpec.

        the PIN code  # noqa: E501

        :param pin: The pin of this EnableCallhomeSpec.  # noqa: E501
        :type: str
        """

        self._pin = pin

    @property
    def access_key(self):
        """Gets the access_key of this EnableCallhomeSpec.  # noqa: E501

        access key  # noqa: E501

        :return: The access_key of this EnableCallhomeSpec.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this EnableCallhomeSpec.

        access key  # noqa: E501

        :param access_key: The access_key of this EnableCallhomeSpec.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def proxy_type(self):
        """Gets the proxy_type of this EnableCallhomeSpec.  # noqa: E501


        :return: The proxy_type of this EnableCallhomeSpec.  # noqa: E501
        :rtype: str
        """
        return self._proxy_type

    @proxy_type.setter
    def proxy_type(self, proxy_type):
        """Sets the proxy_type of this EnableCallhomeSpec.


        :param proxy_type: The proxy_type of this EnableCallhomeSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["USER", "SYSTEM", "NA"]  # noqa: E501
        if proxy_type not in allowed_values:
            raise ValueError(
                "Invalid value for `proxy_type` ({0}), must be one of {1}"  # noqa: E501
                .format(proxy_type, allowed_values)
            )

        self._proxy_type = proxy_type

    @property
    def proxy(self):
        """Gets the proxy of this EnableCallhomeSpec.  # noqa: E501


        :return: The proxy of this EnableCallhomeSpec.  # noqa: E501
        :rtype: CallhomeProxy
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this EnableCallhomeSpec.


        :param proxy: The proxy of this EnableCallhomeSpec.  # noqa: E501
        :type: CallhomeProxy
        """

        self._proxy = proxy

    @property
    def gateways(self):
        """Gets the gateways of this EnableCallhomeSpec.  # noqa: E501


        :return: The gateways of this EnableCallhomeSpec.  # noqa: E501
        :rtype: list[CallhomeGateway]
        """
        return self._gateways

    @gateways.setter
    def gateways(self, gateways):
        """Sets the gateways of this EnableCallhomeSpec.


        :param gateways: The gateways of this EnableCallhomeSpec.  # noqa: E501
        :type: list[CallhomeGateway]
        """

        self._gateways = gateways

    @property
    def customer_contact_infos(self):
        """Gets the customer_contact_infos of this EnableCallhomeSpec.  # noqa: E501


        :return: The customer_contact_infos of this EnableCallhomeSpec.  # noqa: E501
        :rtype: list[CustomerContactInfo]
        """
        return self._customer_contact_infos

    @customer_contact_infos.setter
    def customer_contact_infos(self, customer_contact_infos):
        """Sets the customer_contact_infos of this EnableCallhomeSpec.


        :param customer_contact_infos: The customer_contact_infos of this EnableCallhomeSpec.  # noqa: E501
        :type: list[CustomerContactInfo]
        """

        self._customer_contact_infos = customer_contact_infos

    @property
    def connection_type(self):
        """Gets the connection_type of this EnableCallhomeSpec.  # noqa: E501


        :return: The connection_type of this EnableCallhomeSpec.  # noqa: E501
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this EnableCallhomeSpec.


        :param connection_type: The connection_type of this EnableCallhomeSpec.  # noqa: E501
        :type: str
        """
        if connection_type is None:
            raise ValueError("Invalid value for `connection_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DIRECT", "GATEWAY"]  # noqa: E501
        if connection_type not in allowed_values:
            raise ValueError(
                "Invalid value for `connection_type` ({0}), must be one of {1}"  # noqa: E501
                .format(connection_type, allowed_values)
            )

        self._connection_type = connection_type

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
        if issubclass(EnableCallhomeSpec, dict):
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
        if not isinstance(other, EnableCallhomeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
