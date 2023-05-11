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

class CustomerSuppliedNodeInfo(object):
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
        'management_ip': 'str',
        'current_root_password': 'str',
        'diskgroup_type': 'str'
    }

    attribute_map = {
        'management_ip': 'management_ip',
        'current_root_password': 'current_root_password',
        'diskgroup_type': 'diskgroup_type'
    }

    def __init__(self, management_ip=None, current_root_password=None, diskgroup_type=None):  # noqa: E501
        """CustomerSuppliedNodeInfo - a model defined in Swagger"""  # noqa: E501
        self._management_ip = None
        self._current_root_password = None
        self._diskgroup_type = None
        self.discriminator = None
        if management_ip is not None:
            self.management_ip = management_ip
        self.current_root_password = current_root_password
        if diskgroup_type is not None:
            self.diskgroup_type = diskgroup_type

    @property
    def management_ip(self):
        """Gets the management_ip of this CustomerSuppliedNodeInfo.  # noqa: E501

        Management IP address  # noqa: E501

        :return: The management_ip of this CustomerSuppliedNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._management_ip

    @management_ip.setter
    def management_ip(self, management_ip):
        """Sets the management_ip of this CustomerSuppliedNodeInfo.

        Management IP address  # noqa: E501

        :param management_ip: The management_ip of this CustomerSuppliedNodeInfo.  # noqa: E501
        :type: str
        """

        self._management_ip = management_ip

    @property
    def current_root_password(self):
        """Gets the current_root_password of this CustomerSuppliedNodeInfo.  # noqa: E501

        Root password  # noqa: E501

        :return: The current_root_password of this CustomerSuppliedNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._current_root_password

    @current_root_password.setter
    def current_root_password(self, current_root_password):
        """Sets the current_root_password of this CustomerSuppliedNodeInfo.

        Root password  # noqa: E501

        :param current_root_password: The current_root_password of this CustomerSuppliedNodeInfo.  # noqa: E501
        :type: str
        """
        if current_root_password is None:
            raise ValueError("Invalid value for `current_root_password`, must not be `None`")  # noqa: E501

        self._current_root_password = current_root_password

    @property
    def diskgroup_type(self):
        """Gets the diskgroup_type of this CustomerSuppliedNodeInfo.  # noqa: E501

        Disk Group  # noqa: E501

        :return: The diskgroup_type of this CustomerSuppliedNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._diskgroup_type

    @diskgroup_type.setter
    def diskgroup_type(self, diskgroup_type):
        """Sets the diskgroup_type of this CustomerSuppliedNodeInfo.

        Disk Group  # noqa: E501

        :param diskgroup_type: The diskgroup_type of this CustomerSuppliedNodeInfo.  # noqa: E501
        :type: str
        """

        self._diskgroup_type = diskgroup_type

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
        if issubclass(CustomerSuppliedNodeInfo, dict):
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
        if not isinstance(other, CustomerSuppliedNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
