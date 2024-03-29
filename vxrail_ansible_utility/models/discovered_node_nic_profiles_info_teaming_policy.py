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

class DiscoveredNodeNICProfilesInfoTeamingPolicy(object):
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
        'management': 'DiscoveredNodeTeamingPolicyInfo',
        'vxraildiscovery': 'DiscoveredNodeTeamingPolicyInfo',
        'vsan': 'DiscoveredNodeTeamingPolicyInfo',
        'vmotion': 'DiscoveredNodeTeamingPolicyInfo',
        'witness': 'DiscoveredNodeTeamingPolicyInfo',
        'vxrailsystemvm': 'DiscoveredNodeTeamingPolicyInfo',
        'customervm': 'DiscoveredNodeTeamingPolicyInfo'
    }

    attribute_map = {
        'management': 'management',
        'vxraildiscovery': 'vxraildiscovery',
        'vsan': 'vsan',
        'vmotion': 'vmotion',
        'witness': 'witness',
        'vxrailsystemvm': 'vxrailsystemvm',
        'customervm': 'customervm'
    }

    def __init__(self, management=None, vxraildiscovery=None, vsan=None, vmotion=None, witness=None, vxrailsystemvm=None, customervm=None):  # noqa: E501
        """DiscoveredNodeNICProfilesInfoTeamingPolicy - a model defined in Swagger"""  # noqa: E501
        self._management = None
        self._vxraildiscovery = None
        self._vsan = None
        self._vmotion = None
        self._witness = None
        self._vxrailsystemvm = None
        self._customervm = None
        self.discriminator = None
        if management is not None:
            self.management = management
        if vxraildiscovery is not None:
            self.vxraildiscovery = vxraildiscovery
        if vsan is not None:
            self.vsan = vsan
        if vmotion is not None:
            self.vmotion = vmotion
        if witness is not None:
            self.witness = witness
        if vxrailsystemvm is not None:
            self.vxrailsystemvm = vxrailsystemvm
        if customervm is not None:
            self.customervm = customervm

    @property
    def management(self):
        """Gets the management of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501


        :return: The management of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :rtype: DiscoveredNodeTeamingPolicyInfo
        """
        return self._management

    @management.setter
    def management(self, management):
        """Sets the management of this DiscoveredNodeNICProfilesInfoTeamingPolicy.


        :param management: The management of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :type: DiscoveredNodeTeamingPolicyInfo
        """

        self._management = management

    @property
    def vxraildiscovery(self):
        """Gets the vxraildiscovery of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501


        :return: The vxraildiscovery of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :rtype: DiscoveredNodeTeamingPolicyInfo
        """
        return self._vxraildiscovery

    @vxraildiscovery.setter
    def vxraildiscovery(self, vxraildiscovery):
        """Sets the vxraildiscovery of this DiscoveredNodeNICProfilesInfoTeamingPolicy.


        :param vxraildiscovery: The vxraildiscovery of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :type: DiscoveredNodeTeamingPolicyInfo
        """

        self._vxraildiscovery = vxraildiscovery

    @property
    def vsan(self):
        """Gets the vsan of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501


        :return: The vsan of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :rtype: DiscoveredNodeTeamingPolicyInfo
        """
        return self._vsan

    @vsan.setter
    def vsan(self, vsan):
        """Sets the vsan of this DiscoveredNodeNICProfilesInfoTeamingPolicy.


        :param vsan: The vsan of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :type: DiscoveredNodeTeamingPolicyInfo
        """

        self._vsan = vsan

    @property
    def vmotion(self):
        """Gets the vmotion of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501


        :return: The vmotion of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :rtype: DiscoveredNodeTeamingPolicyInfo
        """
        return self._vmotion

    @vmotion.setter
    def vmotion(self, vmotion):
        """Sets the vmotion of this DiscoveredNodeNICProfilesInfoTeamingPolicy.


        :param vmotion: The vmotion of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :type: DiscoveredNodeTeamingPolicyInfo
        """

        self._vmotion = vmotion

    @property
    def witness(self):
        """Gets the witness of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501


        :return: The witness of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :rtype: DiscoveredNodeTeamingPolicyInfo
        """
        return self._witness

    @witness.setter
    def witness(self, witness):
        """Sets the witness of this DiscoveredNodeNICProfilesInfoTeamingPolicy.


        :param witness: The witness of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :type: DiscoveredNodeTeamingPolicyInfo
        """

        self._witness = witness

    @property
    def vxrailsystemvm(self):
        """Gets the vxrailsystemvm of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501


        :return: The vxrailsystemvm of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :rtype: DiscoveredNodeTeamingPolicyInfo
        """
        return self._vxrailsystemvm

    @vxrailsystemvm.setter
    def vxrailsystemvm(self, vxrailsystemvm):
        """Sets the vxrailsystemvm of this DiscoveredNodeNICProfilesInfoTeamingPolicy.


        :param vxrailsystemvm: The vxrailsystemvm of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :type: DiscoveredNodeTeamingPolicyInfo
        """

        self._vxrailsystemvm = vxrailsystemvm

    @property
    def customervm(self):
        """Gets the customervm of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501


        :return: The customervm of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :rtype: DiscoveredNodeTeamingPolicyInfo
        """
        return self._customervm

    @customervm.setter
    def customervm(self, customervm):
        """Sets the customervm of this DiscoveredNodeNICProfilesInfoTeamingPolicy.


        :param customervm: The customervm of this DiscoveredNodeNICProfilesInfoTeamingPolicy.  # noqa: E501
        :type: DiscoveredNodeTeamingPolicyInfo
        """

        self._customervm = customervm

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
        if issubclass(DiscoveredNodeNICProfilesInfoTeamingPolicy, dict):
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
        if not isinstance(other, DiscoveredNodeNICProfilesInfoTeamingPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
