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


class CertificateInfoDataPublicKey(object):
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
        'algorithm': 'str',
        'length': 'str',
        'modulus': 'str'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'length': 'length',
        'modulus': 'modulus'
    }

    def __init__(self, algorithm=None, length=None, modulus=None):  # noqa: E501
        """CertificateInfoDataPublicKey - a model defined in Swagger"""  # noqa: E501
        self._algorithm = None
        self._length = None
        self._modulus = None
        self.discriminator = None
        if algorithm is not None:
            self.algorithm = algorithm
        if length is not None:
            self.length = length
        if modulus is not None:
            self.modulus = modulus

    @property
    def algorithm(self):
        """Gets the algorithm of this CertificateInfoDataPublicKey.  # noqa: E501

        publik key alogorithm  # noqa: E501

        :return: The algorithm of this CertificateInfoDataPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this CertificateInfoDataPublicKey.

        publik key alogorithm  # noqa: E501

        :param algorithm: The algorithm of this CertificateInfoDataPublicKey.  # noqa: E501
        :type: str
        """

        self._algorithm = algorithm

    @property
    def length(self):
        """Gets the length of this CertificateInfoDataPublicKey.  # noqa: E501

        publik key length  # noqa: E501

        :return: The length of this CertificateInfoDataPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this CertificateInfoDataPublicKey.

        publik key length  # noqa: E501

        :param length: The length of this CertificateInfoDataPublicKey.  # noqa: E501
        :type: str
        """

        self._length = length

    @property
    def modulus(self):
        """Gets the modulus of this CertificateInfoDataPublicKey.  # noqa: E501

        vmodulus  # noqa: E501

        :return: The modulus of this CertificateInfoDataPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._modulus

    @modulus.setter
    def modulus(self, modulus):
        """Sets the modulus of this CertificateInfoDataPublicKey.

        vmodulus  # noqa: E501

        :param modulus: The modulus of this CertificateInfoDataPublicKey.  # noqa: E501
        :type: str
        """

        self._modulus = modulus

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
        if issubclass(CertificateInfoDataPublicKey, dict):
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
        if not isinstance(other, CertificateInfoDataPublicKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
