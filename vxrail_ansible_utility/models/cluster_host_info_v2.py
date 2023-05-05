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

class ClusterHostInfoV2(object):
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
        'serial_number': 'str',
        'slot': 'int',
        'host_name': 'str',
        'appliance_id': 'str',
        'model': 'str',
        'is_primary_node': 'bool',
        'cluster_affinity': 'bool',
        'discovered_date': 'int',
        'bios_uuid': 'str',
        'segment_label': 'str',
        'manufacturer': 'str',
        'psnt': 'str',
        'led_status': 'str',
        'health': 'str',
        'missing': 'bool',
        'ip_set': 'ClusterHostInfoIpSet',
        'ip_set_ipv6': 'ClusterHostInfoV2IpSetIpv6',
        'tpm_present': 'bool',
        'operational_status': 'str',
        'power_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'serial_number': 'serial_number',
        'slot': 'slot',
        'host_name': 'host_name',
        'appliance_id': 'appliance_id',
        'model': 'model',
        'is_primary_node': 'is_primary_node',
        'cluster_affinity': 'cluster_affinity',
        'discovered_date': 'discovered_date',
        'bios_uuid': 'bios_uuid',
        'segment_label': 'segment_label',
        'manufacturer': 'manufacturer',
        'psnt': 'psnt',
        'led_status': 'led_status',
        'health': 'health',
        'missing': 'missing',
        'ip_set': 'ip_set',
        'ip_set_ipv6': 'ip_set_ipv6',
        'tpm_present': 'tpm_present',
        'operational_status': 'operational_status',
        'power_status': 'power_status'
    }

    def __init__(self, id=None, serial_number=None, slot=None, host_name=None, appliance_id=None, model=None, is_primary_node=None, cluster_affinity=None, discovered_date=None, bios_uuid=None, segment_label=None, manufacturer=None, psnt=None, led_status=None, health=None, missing=None, ip_set=None, ip_set_ipv6=None, tpm_present=None, operational_status=None, power_status=None):  # noqa: E501
        """ClusterHostInfoV2 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._serial_number = None
        self._slot = None
        self._host_name = None
        self._appliance_id = None
        self._model = None
        self._is_primary_node = None
        self._cluster_affinity = None
        self._discovered_date = None
        self._bios_uuid = None
        self._segment_label = None
        self._manufacturer = None
        self._psnt = None
        self._led_status = None
        self._health = None
        self._missing = None
        self._ip_set = None
        self._ip_set_ipv6 = None
        self._tpm_present = None
        self._operational_status = None
        self._power_status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if serial_number is not None:
            self.serial_number = serial_number
        if slot is not None:
            self.slot = slot
        if host_name is not None:
            self.host_name = host_name
        if appliance_id is not None:
            self.appliance_id = appliance_id
        if model is not None:
            self.model = model
        if is_primary_node is not None:
            self.is_primary_node = is_primary_node
        if cluster_affinity is not None:
            self.cluster_affinity = cluster_affinity
        if discovered_date is not None:
            self.discovered_date = discovered_date
        if bios_uuid is not None:
            self.bios_uuid = bios_uuid
        if segment_label is not None:
            self.segment_label = segment_label
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if psnt is not None:
            self.psnt = psnt
        if led_status is not None:
            self.led_status = led_status
        if health is not None:
            self.health = health
        if missing is not None:
            self.missing = missing
        if ip_set is not None:
            self.ip_set = ip_set
        if ip_set_ipv6 is not None:
            self.ip_set_ipv6 = ip_set_ipv6
        if tpm_present is not None:
            self.tpm_present = tpm_present
        if operational_status is not None:
            self.operational_status = operational_status
        if power_status is not None:
            self.power_status = power_status

    @property
    def id(self):
        """Gets the id of this ClusterHostInfoV2.  # noqa: E501

        ID number of the host.  # noqa: E501

        :return: The id of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterHostInfoV2.

        ID number of the host.  # noqa: E501

        :param id: The id of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def serial_number(self):
        """Gets the serial_number of this ClusterHostInfoV2.  # noqa: E501

        Serial number of the host.  # noqa: E501

        :return: The serial_number of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this ClusterHostInfoV2.

        Serial number of the host.  # noqa: E501

        :param serial_number: The serial_number of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def slot(self):
        """Gets the slot of this ClusterHostInfoV2.  # noqa: E501

        Rack slot position where the VxRail host appliance is installed.  # noqa: E501

        :return: The slot of this ClusterHostInfoV2.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this ClusterHostInfoV2.

        Rack slot position where the VxRail host appliance is installed.  # noqa: E501

        :param slot: The slot of this ClusterHostInfoV2.  # noqa: E501
        :type: int
        """

        self._slot = slot

    @property
    def host_name(self):
        """Gets the host_name of this ClusterHostInfoV2.  # noqa: E501

        Indicates the hostname.  # noqa: E501

        :return: The host_name of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ClusterHostInfoV2.

        Indicates the hostname.  # noqa: E501

        :param host_name: The host_name of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def appliance_id(self):
        """Gets the appliance_id of this ClusterHostInfoV2.  # noqa: E501

        Host appliance ID.  # noqa: E501

        :return: The appliance_id of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this ClusterHostInfoV2.

        Host appliance ID.  # noqa: E501

        :param appliance_id: The appliance_id of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._appliance_id = appliance_id

    @property
    def model(self):
        """Gets the model of this ClusterHostInfoV2.  # noqa: E501

        Host model.  # noqa: E501

        :return: The model of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ClusterHostInfoV2.

        Host model.  # noqa: E501

        :param model: The model of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def is_primary_node(self):
        """Gets the is_primary_node of this ClusterHostInfoV2.  # noqa: E501

        Whether the node is a primary node.  # noqa: E501

        :return: The is_primary_node of this ClusterHostInfoV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary_node

    @is_primary_node.setter
    def is_primary_node(self, is_primary_node):
        """Sets the is_primary_node of this ClusterHostInfoV2.

        Whether the node is a primary node.  # noqa: E501

        :param is_primary_node: The is_primary_node of this ClusterHostInfoV2.  # noqa: E501
        :type: bool
        """

        self._is_primary_node = is_primary_node

    @property
    def cluster_affinity(self):
        """Gets the cluster_affinity of this ClusterHostInfoV2.  # noqa: E501

        Whether the node is installed in current cluster.  # noqa: E501

        :return: The cluster_affinity of this ClusterHostInfoV2.  # noqa: E501
        :rtype: bool
        """
        return self._cluster_affinity

    @cluster_affinity.setter
    def cluster_affinity(self, cluster_affinity):
        """Sets the cluster_affinity of this ClusterHostInfoV2.

        Whether the node is installed in current cluster.  # noqa: E501

        :param cluster_affinity: The cluster_affinity of this ClusterHostInfoV2.  # noqa: E501
        :type: bool
        """

        self._cluster_affinity = cluster_affinity

    @property
    def discovered_date(self):
        """Gets the discovered_date of this ClusterHostInfoV2.  # noqa: E501

        Discovered date.  # noqa: E501

        :return: The discovered_date of this ClusterHostInfoV2.  # noqa: E501
        :rtype: int
        """
        return self._discovered_date

    @discovered_date.setter
    def discovered_date(self, discovered_date):
        """Sets the discovered_date of this ClusterHostInfoV2.

        Discovered date.  # noqa: E501

        :param discovered_date: The discovered_date of this ClusterHostInfoV2.  # noqa: E501
        :type: int
        """

        self._discovered_date = discovered_date

    @property
    def bios_uuid(self):
        """Gets the bios_uuid of this ClusterHostInfoV2.  # noqa: E501

        BIOS UUID.  # noqa: E501

        :return: The bios_uuid of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._bios_uuid

    @bios_uuid.setter
    def bios_uuid(self, bios_uuid):
        """Sets the bios_uuid of this ClusterHostInfoV2.

        BIOS UUID.  # noqa: E501

        :param bios_uuid: The bios_uuid of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._bios_uuid = bios_uuid

    @property
    def segment_label(self):
        """Gets the segment_label of this ClusterHostInfoV2.  # noqa: E501

        Segment label.  # noqa: E501

        :return: The segment_label of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._segment_label

    @segment_label.setter
    def segment_label(self, segment_label):
        """Sets the segment_label of this ClusterHostInfoV2.

        Segment label.  # noqa: E501

        :param segment_label: The segment_label of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._segment_label = segment_label

    @property
    def manufacturer(self):
        """Gets the manufacturer of this ClusterHostInfoV2.  # noqa: E501

        Manufacturer of the host.  # noqa: E501

        :return: The manufacturer of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this ClusterHostInfoV2.

        Manufacturer of the host.  # noqa: E501

        :param manufacturer: The manufacturer of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def psnt(self):
        """Gets the psnt of this ClusterHostInfoV2.  # noqa: E501

        Product serial number tag (PSNT) of the host.  # noqa: E501

        :return: The psnt of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._psnt

    @psnt.setter
    def psnt(self, psnt):
        """Sets the psnt of this ClusterHostInfoV2.

        Product serial number tag (PSNT) of the host.  # noqa: E501

        :param psnt: The psnt of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._psnt = psnt

    @property
    def led_status(self):
        """Gets the led_status of this ClusterHostInfoV2.  # noqa: E501

        State of the chassis LED indicator for the host.  # noqa: E501

        :return: The led_status of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._led_status

    @led_status.setter
    def led_status(self, led_status):
        """Sets the led_status of this ClusterHostInfoV2.

        State of the chassis LED indicator for the host.  # noqa: E501

        :param led_status: The led_status of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._led_status = led_status

    @property
    def health(self):
        """Gets the health of this ClusterHostInfoV2.  # noqa: E501

        Health status of the VxRail system. Supported values are Critical, Error, Warning, and Healthy.  # noqa: E501

        :return: The health of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this ClusterHostInfoV2.

        Health status of the VxRail system. Supported values are Critical, Error, Warning, and Healthy.  # noqa: E501

        :param health: The health of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._health = health

    @property
    def missing(self):
        """Gets the missing of this ClusterHostInfoV2.  # noqa: E501

        Whether the chassis health status is critical. Supported values are false (not critical) and true (critical).  # noqa: E501

        :return: The missing of this ClusterHostInfoV2.  # noqa: E501
        :rtype: bool
        """
        return self._missing

    @missing.setter
    def missing(self, missing):
        """Sets the missing of this ClusterHostInfoV2.

        Whether the chassis health status is critical. Supported values are false (not critical) and true (critical).  # noqa: E501

        :param missing: The missing of this ClusterHostInfoV2.  # noqa: E501
        :type: bool
        """

        self._missing = missing

    @property
    def ip_set(self):
        """Gets the ip_set of this ClusterHostInfoV2.  # noqa: E501


        :return: The ip_set of this ClusterHostInfoV2.  # noqa: E501
        :rtype: ClusterHostInfoIpSet
        """
        return self._ip_set

    @ip_set.setter
    def ip_set(self, ip_set):
        """Sets the ip_set of this ClusterHostInfoV2.


        :param ip_set: The ip_set of this ClusterHostInfoV2.  # noqa: E501
        :type: ClusterHostInfoIpSet
        """

        self._ip_set = ip_set

    @property
    def ip_set_ipv6(self):
        """Gets the ip_set_ipv6 of this ClusterHostInfoV2.  # noqa: E501


        :return: The ip_set_ipv6 of this ClusterHostInfoV2.  # noqa: E501
        :rtype: ClusterHostInfoV2IpSetIpv6
        """
        return self._ip_set_ipv6

    @ip_set_ipv6.setter
    def ip_set_ipv6(self, ip_set_ipv6):
        """Sets the ip_set_ipv6 of this ClusterHostInfoV2.


        :param ip_set_ipv6: The ip_set_ipv6 of this ClusterHostInfoV2.  # noqa: E501
        :type: ClusterHostInfoV2IpSetIpv6
        """

        self._ip_set_ipv6 = ip_set_ipv6

    @property
    def tpm_present(self):
        """Gets the tpm_present of this ClusterHostInfoV2.  # noqa: E501

        Whether a TPM security device is installed on the VxRail host.  # noqa: E501

        :return: The tpm_present of this ClusterHostInfoV2.  # noqa: E501
        :rtype: bool
        """
        return self._tpm_present

    @tpm_present.setter
    def tpm_present(self, tpm_present):
        """Sets the tpm_present of this ClusterHostInfoV2.

        Whether a TPM security device is installed on the VxRail host.  # noqa: E501

        :param tpm_present: The tpm_present of this ClusterHostInfoV2.  # noqa: E501
        :type: bool
        """

        self._tpm_present = tpm_present

    @property
    def operational_status(self):
        """Gets the operational_status of this ClusterHostInfoV2.  # noqa: E501

        Operational status of the host.  # noqa: E501

        :return: The operational_status of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._operational_status

    @operational_status.setter
    def operational_status(self, operational_status):
        """Sets the operational_status of this ClusterHostInfoV2.

        Operational status of the host.  # noqa: E501

        :param operational_status: The operational_status of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._operational_status = operational_status

    @property
    def power_status(self):
        """Gets the power_status of this ClusterHostInfoV2.  # noqa: E501

        Power supply status of the host.  # noqa: E501

        :return: The power_status of this ClusterHostInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._power_status

    @power_status.setter
    def power_status(self, power_status):
        """Sets the power_status of this ClusterHostInfoV2.

        Power supply status of the host.  # noqa: E501

        :param power_status: The power_status of this ClusterHostInfoV2.  # noqa: E501
        :type: str
        """

        self._power_status = power_status

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
        if issubclass(ClusterHostInfoV2, dict):
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
        if not isinstance(other, ClusterHostInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
