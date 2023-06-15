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

class DpuInfoV1(object):
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
        'sn': 'str',
        'model': 'str',
        'slot': 'int',
        'os_name': 'str',
        'health': 'str'
    }

    attribute_map = {
        'sn': 'sn',
        'model': 'model',
        'slot': 'slot',
        'os_name': 'os_name',
        'health': 'health'
    }

    def __init__(self, sn=None, model=None, slot=None, os_name=None, health=None):  # noqa: E501
        """DpuInfoV1 - a model defined in Swagger"""  # noqa: E501
        self._sn = None
        self._model = None
        self._slot = None
        self._os_name = None
        self._health = None
        self.discriminator = None
        if sn is not None:
            self.sn = sn
        if model is not None:
            self.model = model
        if slot is not None:
            self.slot = slot
        if os_name is not None:
            self.os_name = os_name
        if health is not None:
            self.health = health

    @property
    def sn(self):
        """Gets the sn of this DpuInfoV1.  # noqa: E501

        The serial number of the DPU card.  # noqa: E501

        :return: The sn of this DpuInfoV1.  # noqa: E501
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this DpuInfoV1.

        The serial number of the DPU card.  # noqa: E501

        :param sn: The sn of this DpuInfoV1.  # noqa: E501
        :type: str
        """

        self._sn = sn

    @property
    def model(self):
        """Gets the model of this DpuInfoV1.  # noqa: E501

        The model type of the DPU card.  # noqa: E501

        :return: The model of this DpuInfoV1.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DpuInfoV1.

        The model type of the DPU card.  # noqa: E501

        :param model: The model of this DpuInfoV1.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def slot(self):
        """Gets the slot of this DpuInfoV1.  # noqa: E501

        The slot position of the DPU card.  # noqa: E501

        :return: The slot of this DpuInfoV1.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this DpuInfoV1.

        The slot position of the DPU card.  # noqa: E501

        :param slot: The slot of this DpuInfoV1.  # noqa: E501
        :type: int
        """

        self._slot = slot

    @property
    def os_name(self):
        """Gets the os_name of this DpuInfoV1.  # noqa: E501

        The OS name.  # noqa: E501

        :return: The os_name of this DpuInfoV1.  # noqa: E501
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this DpuInfoV1.

        The OS name.  # noqa: E501

        :param os_name: The os_name of this DpuInfoV1.  # noqa: E501
        :type: str
        """

        self._os_name = os_name

    @property
    def health(self):
        """Gets the health of this DpuInfoV1.  # noqa: E501

        Health status of the DPU system.  # noqa: E501

        :return: The health of this DpuInfoV1.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this DpuInfoV1.

        Health status of the DPU system.  # noqa: E501

        :param health: The health of this DpuInfoV1.  # noqa: E501
        :type: str
        """
        allowed_values = ["Critical", "Error", "Warning", "Healthy"]  # noqa: E501
        if health not in allowed_values:
            raise ValueError(
                "Invalid value for `health` ({0}), must be one of {1}"  # noqa: E501
                .format(health, allowed_values)
            )

        self._health = health

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
        if issubclass(DpuInfoV1, dict):
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
        if not isinstance(other, DpuInfoV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
