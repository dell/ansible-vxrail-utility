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

class DiscoveredNodeInfo(object):
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
        'psnt': 'str',
        'slot': 'int',
        'model': 'str',
        'serial_number': 'str',
        'appliance_id': 'str',
        'is_primary_node': 'bool',
        'cluster_affinity': 'bool',
        'discovered_date': 'int',
        'bios_uuid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'psnt': 'psnt',
        'slot': 'slot',
        'model': 'model',
        'serial_number': 'serial_number',
        'appliance_id': 'appliance_id',
        'is_primary_node': 'is_primary_node',
        'cluster_affinity': 'cluster_affinity',
        'discovered_date': 'discovered_date',
        'bios_uuid': 'bios_uuid'
    }

    def __init__(self, id=None, psnt=None, slot=None, model=None, serial_number=None, appliance_id=None, is_primary_node=None, cluster_affinity=None, discovered_date=None, bios_uuid=None):  # noqa: E501
        """DiscoveredNodeInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._psnt = None
        self._slot = None
        self._model = None
        self._serial_number = None
        self._appliance_id = None
        self._is_primary_node = None
        self._cluster_affinity = None
        self._discovered_date = None
        self._bios_uuid = None
        self.discriminator = None
        self.id = id
        self.psnt = psnt
        self.slot = slot
        self.model = model
        self.serial_number = serial_number
        self.appliance_id = appliance_id
        self.is_primary_node = is_primary_node
        self.cluster_affinity = cluster_affinity
        self.discovered_date = discovered_date
        self.bios_uuid = bios_uuid

    @property
    def id(self):
        """Gets the id of this DiscoveredNodeInfo.  # noqa: E501

        ID of the node. ID=appliance_id + number of total supported nodes in a chassis + node position  # noqa: E501

        :return: The id of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DiscoveredNodeInfo.

        ID of the node. ID=appliance_id + number of total supported nodes in a chassis + node position  # noqa: E501

        :param id: The id of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def psnt(self):
        """Gets the psnt of this DiscoveredNodeInfo.  # noqa: E501

        Product serial number tag (PSNT) of the node  # noqa: E501

        :return: The psnt of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._psnt

    @psnt.setter
    def psnt(self, psnt):
        """Sets the psnt of this DiscoveredNodeInfo.

        Product serial number tag (PSNT) of the node  # noqa: E501

        :param psnt: The psnt of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        if psnt is None:
            raise ValueError("Invalid value for `psnt`, must not be `None`")  # noqa: E501

        self._psnt = psnt

    @property
    def slot(self):
        """Gets the slot of this DiscoveredNodeInfo.  # noqa: E501

        Position of the rack slot where the VxRail host appliance is installed  # noqa: E501

        :return: The slot of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this DiscoveredNodeInfo.

        Position of the rack slot where the VxRail host appliance is installed  # noqa: E501

        :param slot: The slot of this DiscoveredNodeInfo.  # noqa: E501
        :type: int
        """
        if slot is None:
            raise ValueError("Invalid value for `slot`, must not be `None`")  # noqa: E501

        self._slot = slot

    @property
    def model(self):
        """Gets the model of this DiscoveredNodeInfo.  # noqa: E501

        Platform model of the node  # noqa: E501

        :return: The model of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DiscoveredNodeInfo.

        Platform model of the node  # noqa: E501

        :param model: The model of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def serial_number(self):
        """Gets the serial_number of this DiscoveredNodeInfo.  # noqa: E501

        The serial number of the node  # noqa: E501

        :return: The serial_number of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this DiscoveredNodeInfo.

        The serial number of the node  # noqa: E501

        :param serial_number: The serial_number of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def appliance_id(self):
        """Gets the appliance_id of this DiscoveredNodeInfo.  # noqa: E501

        Product serial number tag (PSNT) or application ID of the node  # noqa: E501

        :return: The appliance_id of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this DiscoveredNodeInfo.

        Product serial number tag (PSNT) or application ID of the node  # noqa: E501

        :param appliance_id: The appliance_id of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        if appliance_id is None:
            raise ValueError("Invalid value for `appliance_id`, must not be `None`")  # noqa: E501

        self._appliance_id = appliance_id

    @property
    def is_primary_node(self):
        """Gets the is_primary_node of this DiscoveredNodeInfo.  # noqa: E501

        Whether the node is the primary node  # noqa: E501

        :return: The is_primary_node of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary_node

    @is_primary_node.setter
    def is_primary_node(self, is_primary_node):
        """Sets the is_primary_node of this DiscoveredNodeInfo.

        Whether the node is the primary node  # noqa: E501

        :param is_primary_node: The is_primary_node of this DiscoveredNodeInfo.  # noqa: E501
        :type: bool
        """
        if is_primary_node is None:
            raise ValueError("Invalid value for `is_primary_node`, must not be `None`")  # noqa: E501

        self._is_primary_node = is_primary_node

    @property
    def cluster_affinity(self):
        """Gets the cluster_affinity of this DiscoveredNodeInfo.  # noqa: E501

        Whether the node is installed in the current cluster  # noqa: E501

        :return: The cluster_affinity of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._cluster_affinity

    @cluster_affinity.setter
    def cluster_affinity(self, cluster_affinity):
        """Sets the cluster_affinity of this DiscoveredNodeInfo.

        Whether the node is installed in the current cluster  # noqa: E501

        :param cluster_affinity: The cluster_affinity of this DiscoveredNodeInfo.  # noqa: E501
        :type: bool
        """
        if cluster_affinity is None:
            raise ValueError("Invalid value for `cluster_affinity`, must not be `None`")  # noqa: E501

        self._cluster_affinity = cluster_affinity

    @property
    def discovered_date(self):
        """Gets the discovered_date of this DiscoveredNodeInfo.  # noqa: E501

        Discovered date of the node  # noqa: E501

        :return: The discovered_date of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._discovered_date

    @discovered_date.setter
    def discovered_date(self, discovered_date):
        """Sets the discovered_date of this DiscoveredNodeInfo.

        Discovered date of the node  # noqa: E501

        :param discovered_date: The discovered_date of this DiscoveredNodeInfo.  # noqa: E501
        :type: int
        """
        if discovered_date is None:
            raise ValueError("Invalid value for `discovered_date`, must not be `None`")  # noqa: E501

        self._discovered_date = discovered_date

    @property
    def bios_uuid(self):
        """Gets the bios_uuid of this DiscoveredNodeInfo.  # noqa: E501

        Bios UUID of the node  # noqa: E501

        :return: The bios_uuid of this DiscoveredNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._bios_uuid

    @bios_uuid.setter
    def bios_uuid(self, bios_uuid):
        """Sets the bios_uuid of this DiscoveredNodeInfo.

        Bios UUID of the node  # noqa: E501

        :param bios_uuid: The bios_uuid of this DiscoveredNodeInfo.  # noqa: E501
        :type: str
        """
        if bios_uuid is None:
            raise ValueError("Invalid value for `bios_uuid`, must not be `None`")  # noqa: E501

        self._bios_uuid = bios_uuid

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
        if issubclass(DiscoveredNodeInfo, dict):
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
        if not isinstance(other, DiscoveredNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
