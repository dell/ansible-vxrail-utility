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

class ClusterNodesPnics(object):
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
        'vmnic_name': 'str',
        'vds_name': 'str',
        'uplink_name': 'str',
        'pnic_info': 'str',
        'pnic_current_spped': 'int'
    }

    attribute_map = {
        'vmnic_name': 'vmnic_name',
        'vds_name': 'vds_name',
        'uplink_name': 'uplink_name',
        'pnic_info': 'pnic_info',
        'pnic_current_spped': 'pnic_current_spped'
    }

    def __init__(self, vmnic_name=None, vds_name=None, uplink_name=None, pnic_info=None, pnic_current_spped=None):  # noqa: E501
        """ClusterNodesPnics - a model defined in Swagger"""  # noqa: E501
        self._vmnic_name = None
        self._vds_name = None
        self._uplink_name = None
        self._pnic_info = None
        self._pnic_current_spped = None
        self.discriminator = None
        self.vmnic_name = vmnic_name
        self.vds_name = vds_name
        self.uplink_name = uplink_name
        self.pnic_info = pnic_info
        if pnic_current_spped is not None:
            self.pnic_current_spped = pnic_current_spped

    @property
    def vmnic_name(self):
        """Gets the vmnic_name of this ClusterNodesPnics.  # noqa: E501

        The name of physical adapter on VMWare ESXi host  # noqa: E501

        :return: The vmnic_name of this ClusterNodesPnics.  # noqa: E501
        :rtype: str
        """
        return self._vmnic_name

    @vmnic_name.setter
    def vmnic_name(self, vmnic_name):
        """Sets the vmnic_name of this ClusterNodesPnics.

        The name of physical adapter on VMWare ESXi host  # noqa: E501

        :param vmnic_name: The vmnic_name of this ClusterNodesPnics.  # noqa: E501
        :type: str
        """
        if vmnic_name is None:
            raise ValueError("Invalid value for `vmnic_name`, must not be `None`")  # noqa: E501

        self._vmnic_name = vmnic_name

    @property
    def vds_name(self):
        """Gets the vds_name of this ClusterNodesPnics.  # noqa: E501

        The name of vSphere Distributed Switch  # noqa: E501

        :return: The vds_name of this ClusterNodesPnics.  # noqa: E501
        :rtype: str
        """
        return self._vds_name

    @vds_name.setter
    def vds_name(self, vds_name):
        """Sets the vds_name of this ClusterNodesPnics.

        The name of vSphere Distributed Switch  # noqa: E501

        :param vds_name: The vds_name of this ClusterNodesPnics.  # noqa: E501
        :type: str
        """
        if vds_name is None:
            raise ValueError("Invalid value for `vds_name`, must not be `None`")  # noqa: E501

        self._vds_name = vds_name

    @property
    def uplink_name(self):
        """Gets the uplink_name of this ClusterNodesPnics.  # noqa: E501

        The name of uplink  # noqa: E501

        :return: The uplink_name of this ClusterNodesPnics.  # noqa: E501
        :rtype: str
        """
        return self._uplink_name

    @uplink_name.setter
    def uplink_name(self, uplink_name):
        """Sets the uplink_name of this ClusterNodesPnics.

        The name of uplink  # noqa: E501

        :param uplink_name: The uplink_name of this ClusterNodesPnics.  # noqa: E501
        :type: str
        """
        if uplink_name is None:
            raise ValueError("Invalid value for `uplink_name`, must not be `None`")  # noqa: E501

        self._uplink_name = uplink_name

    @property
    def pnic_info(self):
        """Gets the pnic_info of this ClusterNodesPnics.  # noqa: E501

        The pnic information  # noqa: E501

        :return: The pnic_info of this ClusterNodesPnics.  # noqa: E501
        :rtype: str
        """
        return self._pnic_info

    @pnic_info.setter
    def pnic_info(self, pnic_info):
        """Sets the pnic_info of this ClusterNodesPnics.

        The pnic information  # noqa: E501

        :param pnic_info: The pnic_info of this ClusterNodesPnics.  # noqa: E501
        :type: str
        """
        if pnic_info is None:
            raise ValueError("Invalid value for `pnic_info`, must not be `None`")  # noqa: E501

        self._pnic_info = pnic_info

    @property
    def pnic_current_spped(self):
        """Gets the pnic_current_spped of this ClusterNodesPnics.  # noqa: E501

        pnic current speed  # noqa: E501

        :return: The pnic_current_spped of this ClusterNodesPnics.  # noqa: E501
        :rtype: int
        """
        return self._pnic_current_spped

    @pnic_current_spped.setter
    def pnic_current_spped(self, pnic_current_spped):
        """Sets the pnic_current_spped of this ClusterNodesPnics.

        pnic current speed  # noqa: E501

        :param pnic_current_spped: The pnic_current_spped of this ClusterNodesPnics.  # noqa: E501
        :type: int
        """

        self._pnic_current_spped = pnic_current_spped

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
        if issubclass(ClusterNodesPnics, dict):
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
        if not isinstance(other, ClusterNodesPnics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
