# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.400
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class HostV7(object):
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
        'type': 'str',
        'slot': 'int',
        'hostname': 'str',
        'name': 'str',
        'manufacturer': 'str',
        'psnt': 'str',
        'led_status': 'str',
        'health': 'str',
        'missing': 'bool',
        'tpm_present': 'bool',
        'operational_status': 'str',
        'power_status': 'str',
        'boot_devices': 'list[BootDeviceV2]',
        'nics': 'list[NicV2]',
        'disks': 'list[DiskInfoV3]',
        'firmware_info': 'FirmwareInfoV3',
        'geo_location': 'GeoLocation',
        'drive_configuration': 'DriveConfigurationInfo',
        'encryption_status': 'EncryptionStatus'
    }

    attribute_map = {
        'id': 'id',
        'sn': 'sn',
        'type': 'type',
        'slot': 'slot',
        'hostname': 'hostname',
        'name': 'name',
        'manufacturer': 'manufacturer',
        'psnt': 'psnt',
        'led_status': 'led_status',
        'health': 'health',
        'missing': 'missing',
        'tpm_present': 'tpm_present',
        'operational_status': 'operational_status',
        'power_status': 'power_status',
        'boot_devices': 'boot_devices',
        'nics': 'nics',
        'disks': 'disks',
        'firmware_info': 'firmwareInfo',
        'geo_location': 'geo_location',
        'drive_configuration': 'drive_configuration',
        'encryption_status': 'encryption_status'
    }

    def __init__(self, id=None, sn=None, type=None, slot=None, hostname=None, name=None, manufacturer=None, psnt=None, led_status=None, health=None, missing=None, tpm_present=None, operational_status=None, power_status=None, boot_devices=None, nics=None, disks=None, firmware_info=None, geo_location=None, drive_configuration=None, encryption_status=None):  # noqa: E501
        """HostV7 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._sn = None
        self._type = None
        self._slot = None
        self._hostname = None
        self._name = None
        self._manufacturer = None
        self._psnt = None
        self._led_status = None
        self._health = None
        self._missing = None
        self._tpm_present = None
        self._operational_status = None
        self._power_status = None
        self._boot_devices = None
        self._nics = None
        self._disks = None
        self._firmware_info = None
        self._geo_location = None
        self._drive_configuration = None
        self._encryption_status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if sn is not None:
            self.sn = sn
        if type is not None:
            self.type = type
        if slot is not None:
            self.slot = slot
        if hostname is not None:
            self.hostname = hostname
        if name is not None:
            self.name = name
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
        if tpm_present is not None:
            self.tpm_present = tpm_present
        if operational_status is not None:
            self.operational_status = operational_status
        if power_status is not None:
            self.power_status = power_status
        if boot_devices is not None:
            self.boot_devices = boot_devices
        if nics is not None:
            self.nics = nics
        if disks is not None:
            self.disks = disks
        if firmware_info is not None:
            self.firmware_info = firmware_info
        if geo_location is not None:
            self.geo_location = geo_location
        if drive_configuration is not None:
            self.drive_configuration = drive_configuration
        if encryption_status is not None:
            self.encryption_status = encryption_status

    @property
    def id(self):
        """Gets the id of this HostV7.  # noqa: E501

        ID number of the host  # noqa: E501

        :return: The id of this HostV7.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostV7.

        ID number of the host  # noqa: E501

        :param id: The id of this HostV7.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sn(self):
        """Gets the sn of this HostV7.  # noqa: E501

        Serial number of the host  # noqa: E501

        :return: The sn of this HostV7.  # noqa: E501
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this HostV7.

        Serial number of the host  # noqa: E501

        :param sn: The sn of this HostV7.  # noqa: E501
        :type: str
        """

        self._sn = sn

    @property
    def type(self):
        """Gets the type of this HostV7.  # noqa: E501

        Node type  # noqa: E501

        :return: The type of this HostV7.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HostV7.

        Node type  # noqa: E501

        :param type: The type of this HostV7.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLUSTER", "SATELLITE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def slot(self):
        """Gets the slot of this HostV7.  # noqa: E501

        Rack slot position where the VxRail host appliance is installed  # noqa: E501

        :return: The slot of this HostV7.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this HostV7.

        Rack slot position where the VxRail host appliance is installed  # noqa: E501

        :param slot: The slot of this HostV7.  # noqa: E501
        :type: int
        """

        self._slot = slot

    @property
    def hostname(self):
        """Gets the hostname of this HostV7.  # noqa: E501

        Hostname of the host  # noqa: E501

        :return: The hostname of this HostV7.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this HostV7.

        Hostname of the host  # noqa: E501

        :param hostname: The hostname of this HostV7.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def name(self):
        """Gets the name of this HostV7.  # noqa: E501

        Name of the host  # noqa: E501

        :return: The name of this HostV7.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostV7.

        Name of the host  # noqa: E501

        :param name: The name of this HostV7.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def manufacturer(self):
        """Gets the manufacturer of this HostV7.  # noqa: E501

        Manufacturer of the host  # noqa: E501

        :return: The manufacturer of this HostV7.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this HostV7.

        Manufacturer of the host  # noqa: E501

        :param manufacturer: The manufacturer of this HostV7.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def psnt(self):
        """Gets the psnt of this HostV7.  # noqa: E501

        Product serial number tag (PSNT) of the host  # noqa: E501

        :return: The psnt of this HostV7.  # noqa: E501
        :rtype: str
        """
        return self._psnt

    @psnt.setter
    def psnt(self, psnt):
        """Sets the psnt of this HostV7.

        Product serial number tag (PSNT) of the host  # noqa: E501

        :param psnt: The psnt of this HostV7.  # noqa: E501
        :type: str
        """

        self._psnt = psnt

    @property
    def led_status(self):
        """Gets the led_status of this HostV7.  # noqa: E501

        State of the chassis LED indicator for the host  # noqa: E501

        :return: The led_status of this HostV7.  # noqa: E501
        :rtype: str
        """
        return self._led_status

    @led_status.setter
    def led_status(self, led_status):
        """Sets the led_status of this HostV7.

        State of the chassis LED indicator for the host  # noqa: E501

        :param led_status: The led_status of this HostV7.  # noqa: E501
        :type: str
        """

        self._led_status = led_status

    @property
    def health(self):
        """Gets the health of this HostV7.  # noqa: E501

        Health status of the VxRail system. Supported values are Critica, Error, Warning, and Healthy  # noqa: E501

        :return: The health of this HostV7.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this HostV7.

        Health status of the VxRail system. Supported values are Critica, Error, Warning, and Healthy  # noqa: E501

        :param health: The health of this HostV7.  # noqa: E501
        :type: str
        """

        self._health = health

    @property
    def missing(self):
        """Gets the missing of this HostV7.  # noqa: E501

        Whether the chassis health status is critical. Supported values are false (not critical) and true (critical)  # noqa: E501

        :return: The missing of this HostV7.  # noqa: E501
        :rtype: bool
        """
        return self._missing

    @missing.setter
    def missing(self, missing):
        """Sets the missing of this HostV7.

        Whether the chassis health status is critical. Supported values are false (not critical) and true (critical)  # noqa: E501

        :param missing: The missing of this HostV7.  # noqa: E501
        :type: bool
        """

        self._missing = missing

    @property
    def tpm_present(self):
        """Gets the tpm_present of this HostV7.  # noqa: E501

        Whether a TPM security device is installed on the VxRail host  # noqa: E501

        :return: The tpm_present of this HostV7.  # noqa: E501
        :rtype: bool
        """
        return self._tpm_present

    @tpm_present.setter
    def tpm_present(self, tpm_present):
        """Sets the tpm_present of this HostV7.

        Whether a TPM security device is installed on the VxRail host  # noqa: E501

        :param tpm_present: The tpm_present of this HostV7.  # noqa: E501
        :type: bool
        """

        self._tpm_present = tpm_present

    @property
    def operational_status(self):
        """Gets the operational_status of this HostV7.  # noqa: E501

        Operational status of the host  # noqa: E501

        :return: The operational_status of this HostV7.  # noqa: E501
        :rtype: str
        """
        return self._operational_status

    @operational_status.setter
    def operational_status(self, operational_status):
        """Sets the operational_status of this HostV7.

        Operational status of the host  # noqa: E501

        :param operational_status: The operational_status of this HostV7.  # noqa: E501
        :type: str
        """

        self._operational_status = operational_status

    @property
    def power_status(self):
        """Gets the power_status of this HostV7.  # noqa: E501

        Power supply status of the host  # noqa: E501

        :return: The power_status of this HostV7.  # noqa: E501
        :rtype: str
        """
        return self._power_status

    @power_status.setter
    def power_status(self, power_status):
        """Sets the power_status of this HostV7.

        Power supply status of the host  # noqa: E501

        :param power_status: The power_status of this HostV7.  # noqa: E501
        :type: str
        """

        self._power_status = power_status

    @property
    def boot_devices(self):
        """Gets the boot_devices of this HostV7.  # noqa: E501


        :return: The boot_devices of this HostV7.  # noqa: E501
        :rtype: list[BootDeviceV2]
        """
        return self._boot_devices

    @boot_devices.setter
    def boot_devices(self, boot_devices):
        """Sets the boot_devices of this HostV7.


        :param boot_devices: The boot_devices of this HostV7.  # noqa: E501
        :type: list[BootDeviceV2]
        """

        self._boot_devices = boot_devices

    @property
    def nics(self):
        """Gets the nics of this HostV7.  # noqa: E501


        :return: The nics of this HostV7.  # noqa: E501
        :rtype: list[NicV2]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this HostV7.


        :param nics: The nics of this HostV7.  # noqa: E501
        :type: list[NicV2]
        """

        self._nics = nics

    @property
    def disks(self):
        """Gets the disks of this HostV7.  # noqa: E501


        :return: The disks of this HostV7.  # noqa: E501
        :rtype: list[DiskInfoV3]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this HostV7.


        :param disks: The disks of this HostV7.  # noqa: E501
        :type: list[DiskInfoV3]
        """

        self._disks = disks

    @property
    def firmware_info(self):
        """Gets the firmware_info of this HostV7.  # noqa: E501


        :return: The firmware_info of this HostV7.  # noqa: E501
        :rtype: FirmwareInfoV3
        """
        return self._firmware_info

    @firmware_info.setter
    def firmware_info(self, firmware_info):
        """Sets the firmware_info of this HostV7.


        :param firmware_info: The firmware_info of this HostV7.  # noqa: E501
        :type: FirmwareInfoV3
        """

        self._firmware_info = firmware_info

    @property
    def geo_location(self):
        """Gets the geo_location of this HostV7.  # noqa: E501


        :return: The geo_location of this HostV7.  # noqa: E501
        :rtype: GeoLocation
        """
        return self._geo_location

    @geo_location.setter
    def geo_location(self, geo_location):
        """Sets the geo_location of this HostV7.


        :param geo_location: The geo_location of this HostV7.  # noqa: E501
        :type: GeoLocation
        """

        self._geo_location = geo_location

    @property
    def drive_configuration(self):
        """Gets the drive_configuration of this HostV7.  # noqa: E501


        :return: The drive_configuration of this HostV7.  # noqa: E501
        :rtype: DriveConfigurationInfo
        """
        return self._drive_configuration

    @drive_configuration.setter
    def drive_configuration(self, drive_configuration):
        """Sets the drive_configuration of this HostV7.


        :param drive_configuration: The drive_configuration of this HostV7.  # noqa: E501
        :type: DriveConfigurationInfo
        """

        self._drive_configuration = drive_configuration

    @property
    def encryption_status(self):
        """Gets the encryption_status of this HostV7.  # noqa: E501


        :return: The encryption_status of this HostV7.  # noqa: E501
        :rtype: EncryptionStatus
        """
        return self._encryption_status

    @encryption_status.setter
    def encryption_status(self, encryption_status):
        """Sets the encryption_status of this HostV7.


        :param encryption_status: The encryption_status of this HostV7.  # noqa: E501
        :type: EncryptionStatus
        """

        self._encryption_status = encryption_status

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
        if issubclass(HostV7, dict):
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
        if not isinstance(other, HostV7):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
