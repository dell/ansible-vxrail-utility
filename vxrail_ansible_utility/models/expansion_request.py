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

class ExpansionRequest(object):
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
        'version': 'str',
        'hosts': 'list[ExpansionNodeSpecV2]',
        'vcenter': 'Account',
        'segment_label': 'str'
    }

    attribute_map = {
        'version': 'version',
        'hosts': 'hosts',
        'vcenter': 'vcenter',
        'segment_label': 'segment_label'
    }

    def __init__(self, version=None, hosts=None, vcenter=None, segment_label=None):  # noqa: E501
        """ExpansionRequest - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self._hosts = None
        self._vcenter = None
        self._segment_label = None
        self.discriminator = None
        self.version = version
        self.hosts = hosts
        self.vcenter = vcenter
        if segment_label is not None:
            self.segment_label = segment_label

    @property
    def version(self):
        """Gets the version of this ExpansionRequest.  # noqa: E501

        The software version of the VxRail cluster. For example, 7.0.240  # noqa: E501

        :return: The version of this ExpansionRequest.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ExpansionRequest.

        The software version of the VxRail cluster. For example, 7.0.240  # noqa: E501

        :param version: The version of this ExpansionRequest.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def hosts(self):
        """Gets the hosts of this ExpansionRequest.  # noqa: E501

        Information about the hosts  # noqa: E501

        :return: The hosts of this ExpansionRequest.  # noqa: E501
        :rtype: list[ExpansionNodeSpecV2]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ExpansionRequest.

        Information about the hosts  # noqa: E501

        :param hosts: The hosts of this ExpansionRequest.  # noqa: E501
        :type: list[ExpansionNodeSpecV2]
        """
        if hosts is None:
            raise ValueError("Invalid value for `hosts`, must not be `None`")  # noqa: E501

        self._hosts = hosts

    @property
    def vcenter(self):
        """Gets the vcenter of this ExpansionRequest.  # noqa: E501


        :return: The vcenter of this ExpansionRequest.  # noqa: E501
        :rtype: Account
        """
        return self._vcenter

    @vcenter.setter
    def vcenter(self, vcenter):
        """Sets the vcenter of this ExpansionRequest.


        :param vcenter: The vcenter of this ExpansionRequest.  # noqa: E501
        :type: Account
        """
        if vcenter is None:
            raise ValueError("Invalid value for `vcenter`, must not be `None`")  # noqa: E501

        self._vcenter = vcenter

    @property
    def segment_label(self):
        """Gets the segment_label of this ExpansionRequest.  # noqa: E501

        Label name of the segment  # noqa: E501

        :return: The segment_label of this ExpansionRequest.  # noqa: E501
        :rtype: str
        """
        return self._segment_label

    @segment_label.setter
    def segment_label(self, segment_label):
        """Sets the segment_label of this ExpansionRequest.

        Label name of the segment  # noqa: E501

        :param segment_label: The segment_label of this ExpansionRequest.  # noqa: E501
        :type: str
        """

        self._segment_label = segment_label

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
        if issubclass(ExpansionRequest, dict):
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
        if not isinstance(other, ExpansionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
