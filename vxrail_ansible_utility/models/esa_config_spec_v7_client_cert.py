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

class ESAConfigSpecV7ClientCert(object):
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
        'certificate': 'str',
        'private_key': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'private_key': 'private_key'
    }

    def __init__(self, certificate=None, private_key=None):  # noqa: E501
        """ESAConfigSpecV7ClientCert - a model defined in Swagger"""  # noqa: E501
        self._certificate = None
        self._private_key = None
        self.discriminator = None
        if certificate is not None:
            self.certificate = certificate
        if private_key is not None:
            self.private_key = private_key

    @property
    def certificate(self):
        """Gets the certificate of this ESAConfigSpecV7ClientCert.  # noqa: E501

        The KMS server client certificate  # noqa: E501

        :return: The certificate of this ESAConfigSpecV7ClientCert.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this ESAConfigSpecV7ClientCert.

        The KMS server client certificate  # noqa: E501

        :param certificate: The certificate of this ESAConfigSpecV7ClientCert.  # noqa: E501
        :type: str
        """

        self._certificate = certificate

    @property
    def private_key(self):
        """Gets the private_key of this ESAConfigSpecV7ClientCert.  # noqa: E501

        The KMS server client private key  # noqa: E501

        :return: The private_key of this ESAConfigSpecV7ClientCert.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this ESAConfigSpecV7ClientCert.

        The KMS server client private key  # noqa: E501

        :param private_key: The private_key of this ESAConfigSpecV7ClientCert.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

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
        if issubclass(ESAConfigSpecV7ClientCert, dict):
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
        if not isinstance(other, ESAConfigSpecV7ClientCert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
