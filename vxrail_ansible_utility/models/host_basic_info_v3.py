# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class HostBasicInfoV3(object):
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
        'firmware_information': 'FirmwareInfo',
        'geo_location': 'GeoLocation'
    }

    attribute_map = {
        'id': 'id',
        'sn': 'sn',
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
        'firmware_information': 'firmwareInfo',
        'geo_location': 'geo_location'
    }

    def __init__(self, id=None, sn=None, slot=None, hostname=None, name=None, manufacturer=None, psnt=None, led_status=None, health=None, missing=None, tpm_present=None, operational_status=None, power_status=None, firmware_information=None, geo_location=None):  # noqa: E501
        """HostBasicInfoV3 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._sn = None
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
        self._firmware_information = None
        self._geo_location = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if sn is not None:
            self.sn = sn
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
        if firmware_information is not None:
            self.firmware_information = firmware_information
        if geo_location is not None:
            self.geo_location = geo_location

    @property
    def id(self):
        """Gets the id of this HostBasicInfoV3.  # noqa: E501

        host id  # noqa: E501

        :return: The id of this HostBasicInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostBasicInfoV3.

        host id  # noqa: E501

        :param id: The id of this HostBasicInfoV3.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sn(self):
        """Gets the sn of this HostBasicInfoV3.  # noqa: E501

        host sn  # noqa: E501

        :return: The sn of this HostBasicInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this HostBasicInfoV3.

        host sn  # noqa: E501

        :param sn: The sn of this HostBasicInfoV3.  # noqa: E501
        :type: str
        """

        self._sn = sn

    @property
    def slot(self):
        """Gets the slot of this HostBasicInfoV3.  # noqa: E501

        host slot  # noqa: E501

        :return: The slot of this HostBasicInfoV3.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this HostBasicInfoV3.

        host slot  # noqa: E501

        :param slot: The slot of this HostBasicInfoV3.  # noqa: E501
        :type: int
        """

        self._slot = slot

    @property
    def hostname(self):
        """Gets the hostname of this HostBasicInfoV3.  # noqa: E501

        host hostname  # noqa: E501

        :return: The hostname of this HostBasicInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this HostBasicInfoV3.

        host hostname  # noqa: E501

        :param hostname: The hostname of this HostBasicInfoV3.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def name(self):
        """Gets the name of this HostBasicInfoV3.  # noqa: E501

        host name  # noqa: E501

        :return: The name of this HostBasicInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostBasicInfoV3.

        host name  # noqa: E501

        :param name: The name of this HostBasicInfoV3.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def manufacturer(self):
        """Gets the manufacturer of this HostBasicInfoV3.  # noqa: E501

        host manufacturer  # noqa: E501

        :return: The manufacturer of this HostBasicInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this HostBasicInfoV3.

        host manufacturer  # noqa: E501

        :param manufacturer: The manufacturer of this HostBasicInfoV3.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def psnt(self):
        """Gets the psnt of this HostBasicInfoV3.  # noqa: E501

        host psnt  # noqa: E501

        :return: The psnt of this HostBasicInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._psnt

    @psnt.setter
    def psnt(self, psnt):
        """Sets the psnt of this HostBasicInfoV3.

        host psnt  # noqa: E501

        :param psnt: The psnt of this HostBasicInfoV3.  # noqa: E501
        :type: str
        """

        self._psnt = psnt

    @property
    def led_status(self):
        """Gets the led_status of this HostBasicInfoV3.  # noqa: E501

        host led status  # noqa: E501

        :return: The led_status of this HostBasicInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._led_status

    @led_status.setter
    def led_status(self, led_status):
        """Sets the led_status of this HostBasicInfoV3.

        host led status  # noqa: E501

        :param led_status: The led_status of this HostBasicInfoV3.  # noqa: E501
        :type: str
        """

        self._led_status = led_status

    @property
    def health(self):
        """Gets the health of this HostBasicInfoV3.  # noqa: E501

        host health status  # noqa: E501

        :return: The health of this HostBasicInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this HostBasicInfoV3.

        host health status  # noqa: E501

        :param health: The health of this HostBasicInfoV3.  # noqa: E501
        :type: str
        """

        self._health = health

    @property
    def missing(self):
        """Gets the missing of this HostBasicInfoV3.  # noqa: E501

        host is missing or not  # noqa: E501

        :return: The missing of this HostBasicInfoV3.  # noqa: E501
        :rtype: bool
        """
        return self._missing

    @missing.setter
    def missing(self, missing):
        """Sets the missing of this HostBasicInfoV3.

        host is missing or not  # noqa: E501

        :param missing: The missing of this HostBasicInfoV3.  # noqa: E501
        :type: bool
        """

        self._missing = missing

    @property
    def tpm_present(self):
        """Gets the tpm_present of this HostBasicInfoV3.  # noqa: E501

        host support tpm or not  # noqa: E501

        :return: The tpm_present of this HostBasicInfoV3.  # noqa: E501
        :rtype: bool
        """
        return self._tpm_present

    @tpm_present.setter
    def tpm_present(self, tpm_present):
        """Sets the tpm_present of this HostBasicInfoV3.

        host support tpm or not  # noqa: E501

        :param tpm_present: The tpm_present of this HostBasicInfoV3.  # noqa: E501
        :type: bool
        """

        self._tpm_present = tpm_present

    @property
    def operational_status(self):
        """Gets the operational_status of this HostBasicInfoV3.  # noqa: E501

        host operational status  # noqa: E501

        :return: The operational_status of this HostBasicInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._operational_status

    @operational_status.setter
    def operational_status(self, operational_status):
        """Sets the operational_status of this HostBasicInfoV3.

        host operational status  # noqa: E501

        :param operational_status: The operational_status of this HostBasicInfoV3.  # noqa: E501
        :type: str
        """

        self._operational_status = operational_status

    @property
    def power_status(self):
        """Gets the power_status of this HostBasicInfoV3.  # noqa: E501

        host power status  # noqa: E501

        :return: The power_status of this HostBasicInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._power_status

    @power_status.setter
    def power_status(self, power_status):
        """Sets the power_status of this HostBasicInfoV3.

        host power status  # noqa: E501

        :param power_status: The power_status of this HostBasicInfoV3.  # noqa: E501
        :type: str
        """

        self._power_status = power_status

    @property
    def firmware_information(self):
        """Gets the firmware_information of this HostBasicInfoV3.  # noqa: E501


        :return: The firmware_information of this HostBasicInfoV3.  # noqa: E501
        :rtype: FirmwareInfo
        """
        return self._firmware_information

    @firmware_information.setter
    def firmware_information(self, firmware_information):
        """Sets the firmware_information of this HostBasicInfoV3.


        :param firmware_information: The firmware_information of this HostBasicInfoV3.  # noqa: E501
        :type: FirmwareInfo
        """

        self._firmware_information = firmware_information

    @property
    def geo_location(self):
        """Gets the geo_location of this HostBasicInfoV3.  # noqa: E501


        :return: The geo_location of this HostBasicInfoV3.  # noqa: E501
        :rtype: GeoLocation
        """
        return self._geo_location

    @geo_location.setter
    def geo_location(self, geo_location):
        """Sets the geo_location of this HostBasicInfoV3.


        :param geo_location: The geo_location of this HostBasicInfoV3.  # noqa: E501
        :type: GeoLocation
        """

        self._geo_location = geo_location

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
        if issubclass(HostBasicInfoV3, dict):
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
        if not isinstance(other, HostBasicInfoV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
