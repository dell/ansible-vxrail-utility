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


class CertificateInfo(object):
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
        'type': 'str',
        'valid': 'bool',
        'thumbprint': 'str',
        'message': 'str',
        'data': 'CertificateInfoData'
    }

    attribute_map = {
        'type': 'type',
        'valid': 'valid',
        'thumbprint': 'thumbprint',
        'message': 'message',
        'data': 'data'
    }

    def __init__(self, type=None, valid=None, thumbprint=None, message=None, data=None):  # noqa: E501
        """CertificateInfo - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._valid = None
        self._thumbprint = None
        self._message = None
        self._data = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if valid is not None:
            self.valid = valid
        if thumbprint is not None:
            self.thumbprint = thumbprint
        if message is not None:
            self.message = message
        if data is not None:
            self.data = data

    @property
    def type(self):
        """Gets the type of this CertificateInfo.  # noqa: E501

        type  # noqa: E501

        :return: The type of this CertificateInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CertificateInfo.

        type  # noqa: E501

        :param type: The type of this CertificateInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def valid(self):
        """Gets the valid of this CertificateInfo.  # noqa: E501

        true if this certificate is a VxM trusted one.  # noqa: E501

        :return: The valid of this CertificateInfo.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this CertificateInfo.

        true if this certificate is a VxM trusted one.  # noqa: E501

        :param valid: The valid of this CertificateInfo.  # noqa: E501
        :type: bool
        """

        self._valid = valid

    @property
    def thumbprint(self):
        """Gets the thumbprint of this CertificateInfo.  # noqa: E501

        SSL thumbprint.  # noqa: E501

        :return: The thumbprint of this CertificateInfo.  # noqa: E501
        :rtype: str
        """
        return self._thumbprint

    @thumbprint.setter
    def thumbprint(self, thumbprint):
        """Sets the thumbprint of this CertificateInfo.

        SSL thumbprint.  # noqa: E501

        :param thumbprint: The thumbprint of this CertificateInfo.  # noqa: E501
        :type: str
        """

        self._thumbprint = thumbprint

    @property
    def message(self):
        """Gets the message of this CertificateInfo.  # noqa: E501

        extra message like vc thumbprint mode warning.  # noqa: E501

        :return: The message of this CertificateInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CertificateInfo.

        extra message like vc thumbprint mode warning.  # noqa: E501

        :param message: The message of this CertificateInfo.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def data(self):
        """Gets the data of this CertificateInfo.  # noqa: E501


        :return: The data of this CertificateInfo.  # noqa: E501
        :rtype: CertificateInfoData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CertificateInfo.


        :param data: The data of this CertificateInfo.  # noqa: E501
        :type: CertificateInfoData
        """

        self._data = data

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
        if issubclass(CertificateInfo, dict):
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
        if not isinstance(other, CertificateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
