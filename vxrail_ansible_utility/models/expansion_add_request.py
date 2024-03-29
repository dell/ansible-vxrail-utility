# coding: utf-8

"""
    VxRail Cluster and System Management

    APIs for cluster management and system management  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExpansionAddRequest(object):
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
        'host': 'PrivateExpansionNodeSpec',
        'vcenter': 'Account'
    }

    attribute_map = {
        'host': 'host',
        'vcenter': 'vcenter'
    }

    def __init__(self, host=None, vcenter=None):  # noqa: E501
        """ExpansionAddRequest - a model defined in Swagger"""  # noqa: E501
        self._host = None
        self._vcenter = None
        self.discriminator = None
        self.host = host
        self.vcenter = vcenter

    @property
    def host(self):
        """Gets the host of this ExpansionAddRequest.  # noqa: E501


        :return: The host of this ExpansionAddRequest.  # noqa: E501
        :rtype: PrivateExpansionNodeSpec
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ExpansionAddRequest.


        :param host: The host of this ExpansionAddRequest.  # noqa: E501
        :type: PrivateExpansionNodeSpec
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def vcenter(self):
        """Gets the vcenter of this ExpansionAddRequest.  # noqa: E501


        :return: The vcenter of this ExpansionAddRequest.  # noqa: E501
        :rtype: Account
        """
        return self._vcenter

    @vcenter.setter
    def vcenter(self, vcenter):
        """Sets the vcenter of this ExpansionAddRequest.


        :param vcenter: The vcenter of this ExpansionAddRequest.  # noqa: E501
        :type: Account
        """
        if vcenter is None:
            raise ValueError("Invalid value for `vcenter`, must not be `None`")  # noqa: E501

        self._vcenter = vcenter

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
        if issubclass(ExpansionAddRequest, dict):
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
        if not isinstance(other, ExpansionAddRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
