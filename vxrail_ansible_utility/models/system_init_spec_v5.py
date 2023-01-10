# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.410
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SystemInitSpecV5(object):
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
        '_global': 'SystemInitSpecV5Global',
        'hosts': 'list[SystemInitSpecV5Hosts]',
        'vcenter': 'SystemInitSpecV5Vcenter',
        'witness_node': 'SystemInitSpecV5WitnessNode',
        'vxrail_managed_witness_node': 'SystemInitSpecV5VxrailManagedWitnessNode',
        'vxrail_manager': 'SystemInitSpecV5VxrailManager',
        'network': 'SystemInitSpecV5Network1',
        'storage': 'SystemInitSpecV5Storage'
    }

    attribute_map = {
        'version': 'version',
        '_global': 'global',
        'hosts': 'hosts',
        'vcenter': 'vcenter',
        'witness_node': 'witness_node',
        'vxrail_managed_witness_node': 'vxrail_managed_witness_node',
        'vxrail_manager': 'vxrail_manager',
        'network': 'network',
        'storage': 'storage'
    }

    def __init__(self, version=None, _global=None, hosts=None, vcenter=None, witness_node=None, vxrail_managed_witness_node=None, vxrail_manager=None, network=None, storage=None):  # noqa: E501
        """SystemInitSpecV5 - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self.__global = None
        self._hosts = None
        self._vcenter = None
        self._witness_node = None
        self._vxrail_managed_witness_node = None
        self._vxrail_manager = None
        self._network = None
        self._storage = None
        self.discriminator = None
        self.version = version
        self._global = _global
        self.hosts = hosts
        self.vcenter = vcenter
        if witness_node is not None:
            self.witness_node = witness_node
        if vxrail_managed_witness_node is not None:
            self.vxrail_managed_witness_node = vxrail_managed_witness_node
        self.vxrail_manager = vxrail_manager
        self.network = network
        if storage is not None:
            self.storage = storage

    @property
    def version(self):
        """Gets the version of this SystemInitSpecV5.  # noqa: E501

        The VxRail Manager version to be deployed  # noqa: E501

        :return: The version of this SystemInitSpecV5.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SystemInitSpecV5.

        The VxRail Manager version to be deployed  # noqa: E501

        :param version: The version of this SystemInitSpecV5.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def _global(self):
        """Gets the _global of this SystemInitSpecV5.  # noqa: E501


        :return: The _global of this SystemInitSpecV5.  # noqa: E501
        :rtype: SystemInitSpecV5Global
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this SystemInitSpecV5.


        :param _global: The _global of this SystemInitSpecV5.  # noqa: E501
        :type: SystemInitSpecV5Global
        """
        if _global is None:
            raise ValueError("Invalid value for `_global`, must not be `None`")  # noqa: E501

        self.__global = _global

    @property
    def hosts(self):
        """Gets the hosts of this SystemInitSpecV5.  # noqa: E501

        Configuration settings for each of the VxRail hosts  # noqa: E501

        :return: The hosts of this SystemInitSpecV5.  # noqa: E501
        :rtype: list[SystemInitSpecV5Hosts]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this SystemInitSpecV5.

        Configuration settings for each of the VxRail hosts  # noqa: E501

        :param hosts: The hosts of this SystemInitSpecV5.  # noqa: E501
        :type: list[SystemInitSpecV5Hosts]
        """
        if hosts is None:
            raise ValueError("Invalid value for `hosts`, must not be `None`")  # noqa: E501

        self._hosts = hosts

    @property
    def vcenter(self):
        """Gets the vcenter of this SystemInitSpecV5.  # noqa: E501


        :return: The vcenter of this SystemInitSpecV5.  # noqa: E501
        :rtype: SystemInitSpecV5Vcenter
        """
        return self._vcenter

    @vcenter.setter
    def vcenter(self, vcenter):
        """Sets the vcenter of this SystemInitSpecV5.


        :param vcenter: The vcenter of this SystemInitSpecV5.  # noqa: E501
        :type: SystemInitSpecV5Vcenter
        """
        if vcenter is None:
            raise ValueError("Invalid value for `vcenter`, must not be `None`")  # noqa: E501

        self._vcenter = vcenter

    @property
    def witness_node(self):
        """Gets the witness_node of this SystemInitSpecV5.  # noqa: E501


        :return: The witness_node of this SystemInitSpecV5.  # noqa: E501
        :rtype: SystemInitSpecV5WitnessNode
        """
        return self._witness_node

    @witness_node.setter
    def witness_node(self, witness_node):
        """Sets the witness_node of this SystemInitSpecV5.


        :param witness_node: The witness_node of this SystemInitSpecV5.  # noqa: E501
        :type: SystemInitSpecV5WitnessNode
        """

        self._witness_node = witness_node

    @property
    def vxrail_managed_witness_node(self):
        """Gets the vxrail_managed_witness_node of this SystemInitSpecV5.  # noqa: E501


        :return: The vxrail_managed_witness_node of this SystemInitSpecV5.  # noqa: E501
        :rtype: SystemInitSpecV5VxrailManagedWitnessNode
        """
        return self._vxrail_managed_witness_node

    @vxrail_managed_witness_node.setter
    def vxrail_managed_witness_node(self, vxrail_managed_witness_node):
        """Sets the vxrail_managed_witness_node of this SystemInitSpecV5.


        :param vxrail_managed_witness_node: The vxrail_managed_witness_node of this SystemInitSpecV5.  # noqa: E501
        :type: SystemInitSpecV5VxrailManagedWitnessNode
        """

        self._vxrail_managed_witness_node = vxrail_managed_witness_node

    @property
    def vxrail_manager(self):
        """Gets the vxrail_manager of this SystemInitSpecV5.  # noqa: E501


        :return: The vxrail_manager of this SystemInitSpecV5.  # noqa: E501
        :rtype: SystemInitSpecV5VxrailManager
        """
        return self._vxrail_manager

    @vxrail_manager.setter
    def vxrail_manager(self, vxrail_manager):
        """Sets the vxrail_manager of this SystemInitSpecV5.


        :param vxrail_manager: The vxrail_manager of this SystemInitSpecV5.  # noqa: E501
        :type: SystemInitSpecV5VxrailManager
        """
        if vxrail_manager is None:
            raise ValueError("Invalid value for `vxrail_manager`, must not be `None`")  # noqa: E501

        self._vxrail_manager = vxrail_manager

    @property
    def network(self):
        """Gets the network of this SystemInitSpecV5.  # noqa: E501


        :return: The network of this SystemInitSpecV5.  # noqa: E501
        :rtype: SystemInitSpecV5Network1
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this SystemInitSpecV5.


        :param network: The network of this SystemInitSpecV5.  # noqa: E501
        :type: SystemInitSpecV5Network1
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def storage(self):
        """Gets the storage of this SystemInitSpecV5.  # noqa: E501


        :return: The storage of this SystemInitSpecV5.  # noqa: E501
        :rtype: SystemInitSpecV5Storage
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this SystemInitSpecV5.


        :param storage: The storage of this SystemInitSpecV5.  # noqa: E501
        :type: SystemInitSpecV5Storage
        """

        self._storage = storage

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
        if issubclass(SystemInitSpecV5, dict):
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
        if not isinstance(other, SystemInitSpecV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
