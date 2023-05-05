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

class CertificateContentInfo(object):
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
        'cert': 'str'
    }

    attribute_map = {
        'cert': 'cert'
    }

    def __init__(self, cert=None):  # noqa: E501
        """CertificateContentInfo - a model defined in Swagger"""  # noqa: E501
        self._cert = None
        self.discriminator = None
        if cert is not None:
            self.cert = cert

    @property
    def cert(self):
        """Gets the cert of this CertificateContentInfo.  # noqa: E501

        Content of the target certificate according to the fingerprint parameter.  # noqa: E501

        :return: The cert of this CertificateContentInfo.  # noqa: E501
        :rtype: str
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this CertificateContentInfo.

        Content of the target certificate according to the fingerprint parameter.  # noqa: E501

        :param cert: The cert of this CertificateContentInfo.  # noqa: E501
        :type: str
        """

        self._cert = cert

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
        if issubclass(CertificateContentInfo, dict):
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
        if not isinstance(other, CertificateContentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
