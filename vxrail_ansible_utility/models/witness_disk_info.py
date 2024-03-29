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

class WitnessDiskInfo(object):
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
        'id': 'str',
        'sn': 'str',
        'disk_type': 'str',
        'capacity': 'str'
    }

    attribute_map = {
        'id': 'id',
        'sn': 'sn',
        'disk_type': 'disk_type',
        'capacity': 'capacity'
    }

    def __init__(self, id=None, sn=None, disk_type=None, capacity=None):  # noqa: E501
        """WitnessDiskInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._sn = None
        self._disk_type = None
        self._capacity = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if sn is not None:
            self.sn = sn
        if disk_type is not None:
            self.disk_type = disk_type
        if capacity is not None:
            self.capacity = capacity

    @property
    def id(self):
        """Gets the id of this WitnessDiskInfo.  # noqa: E501

        ID of the disk  # noqa: E501

        :return: The id of this WitnessDiskInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WitnessDiskInfo.

        ID of the disk  # noqa: E501

        :param id: The id of this WitnessDiskInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sn(self):
        """Gets the sn of this WitnessDiskInfo.  # noqa: E501

        Serial number of the disk  # noqa: E501

        :return: The sn of this WitnessDiskInfo.  # noqa: E501
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this WitnessDiskInfo.

        Serial number of the disk  # noqa: E501

        :param sn: The sn of this WitnessDiskInfo.  # noqa: E501
        :type: str
        """

        self._sn = sn

    @property
    def disk_type(self):
        """Gets the disk_type of this WitnessDiskInfo.  # noqa: E501

        Type of disk drive  # noqa: E501

        :return: The disk_type of this WitnessDiskInfo.  # noqa: E501
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        """Sets the disk_type of this WitnessDiskInfo.

        Type of disk drive  # noqa: E501

        :param disk_type: The disk_type of this WitnessDiskInfo.  # noqa: E501
        :type: str
        """

        self._disk_type = disk_type

    @property
    def capacity(self):
        """Gets the capacity of this WitnessDiskInfo.  # noqa: E501

        Capacity of the disk  # noqa: E501

        :return: The capacity of this WitnessDiskInfo.  # noqa: E501
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this WitnessDiskInfo.

        Capacity of the disk  # noqa: E501

        :param capacity: The capacity of this WitnessDiskInfo.  # noqa: E501
        :type: str
        """

        self._capacity = capacity

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
        if issubclass(WitnessDiskInfo, dict):
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
        if not isinstance(other, WitnessDiskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
