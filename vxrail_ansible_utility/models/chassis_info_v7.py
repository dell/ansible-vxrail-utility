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

class ChassisInfoV7(object):
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
        'part_number': 'str',
        'slot': 'int',
        'hostname': 'object',
        'description': 'str',
        'service_tag': 'str',
        'firmware_version': 'str',
        'psnt': 'str',
        'moid': 'str',
        'model': 'str',
        'render_category': 'str',
        'generation': 'int',
        'health': 'str',
        'missing': 'bool',
        'hosts': 'list[HostBasicInfoV7]',
        'witness': 'WitnessBasicInfoV2',
        'power_supplies': 'list[PowerSupplyInfo]',
        'chassis_manager_fw_version': 'str',
        'bay': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'sn': 'sn',
        'part_number': 'part_number',
        'slot': 'slot',
        'hostname': 'hostname',
        'description': 'description',
        'service_tag': 'service_tag',
        'firmware_version': 'firmware_version',
        'psnt': 'psnt',
        'moid': 'moid',
        'model': 'model',
        'render_category': 'render_category',
        'generation': 'generation',
        'health': 'health',
        'missing': 'missing',
        'hosts': 'hosts',
        'witness': 'witness',
        'power_supplies': 'power_supplies',
        'chassis_manager_fw_version': 'chassis_manager_fw_version',
        'bay': 'bay'
    }

    def __init__(self, id=None, sn=None, part_number=None, slot=None, hostname=None, description=None, service_tag=None, firmware_version=None, psnt=None, moid=None, model=None, render_category=None, generation=None, health=None, missing=None, hosts=None, witness=None, power_supplies=None, chassis_manager_fw_version=None, bay=None):  # noqa: E501
        """ChassisInfoV7 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._sn = None
        self._part_number = None
        self._slot = None
        self._hostname = None
        self._description = None
        self._service_tag = None
        self._firmware_version = None
        self._psnt = None
        self._moid = None
        self._model = None
        self._render_category = None
        self._generation = None
        self._health = None
        self._missing = None
        self._hosts = None
        self._witness = None
        self._power_supplies = None
        self._chassis_manager_fw_version = None
        self._bay = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if sn is not None:
            self.sn = sn
        if part_number is not None:
            self.part_number = part_number
        if slot is not None:
            self.slot = slot
        if hostname is not None:
            self.hostname = hostname
        if description is not None:
            self.description = description
        if service_tag is not None:
            self.service_tag = service_tag
        if firmware_version is not None:
            self.firmware_version = firmware_version
        if psnt is not None:
            self.psnt = psnt
        if moid is not None:
            self.moid = moid
        if model is not None:
            self.model = model
        if render_category is not None:
            self.render_category = render_category
        if generation is not None:
            self.generation = generation
        if health is not None:
            self.health = health
        if missing is not None:
            self.missing = missing
        if hosts is not None:
            self.hosts = hosts
        if witness is not None:
            self.witness = witness
        if power_supplies is not None:
            self.power_supplies = power_supplies
        if chassis_manager_fw_version is not None:
            self.chassis_manager_fw_version = chassis_manager_fw_version
        if bay is not None:
            self.bay = bay

    @property
    def id(self):
        """Gets the id of this ChassisInfoV7.  # noqa: E501

        ID of the chassis  # noqa: E501

        :return: The id of this ChassisInfoV7.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChassisInfoV7.

        ID of the chassis  # noqa: E501

        :param id: The id of this ChassisInfoV7.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sn(self):
        """Gets the sn of this ChassisInfoV7.  # noqa: E501

        Serial number of the chassis  # noqa: E501

        :return: The sn of this ChassisInfoV7.  # noqa: E501
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this ChassisInfoV7.

        Serial number of the chassis  # noqa: E501

        :param sn: The sn of this ChassisInfoV7.  # noqa: E501
        :type: str
        """

        self._sn = sn

    @property
    def part_number(self):
        """Gets the part_number of this ChassisInfoV7.  # noqa: E501

        Part number of the chassis  # noqa: E501

        :return: The part_number of this ChassisInfoV7.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this ChassisInfoV7.

        Part number of the chassis  # noqa: E501

        :param part_number: The part_number of this ChassisInfoV7.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLUSTER", "SATELLITE"]  # noqa: E501
        if part_number not in allowed_values:
            raise ValueError(
                "Invalid value for `part_number` ({0}), must be one of {1}"  # noqa: E501
                .format(part_number, allowed_values)
            )

        self._part_number = part_number

    @property
    def slot(self):
        """Gets the slot of this ChassisInfoV7.  # noqa: E501

        Rack slot position where the VxRail host appliance is installed  # noqa: E501

        :return: The slot of this ChassisInfoV7.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this ChassisInfoV7.

        Rack slot position where the VxRail host appliance is installed  # noqa: E501

        :param slot: The slot of this ChassisInfoV7.  # noqa: E501
        :type: int
        """

        self._slot = slot

    @property
    def hostname(self):
        """Gets the hostname of this ChassisInfoV7.  # noqa: E501

        Indicates the hostname  # noqa: E501

        :return: The hostname of this ChassisInfoV7.  # noqa: E501
        :rtype: object
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ChassisInfoV7.

        Indicates the hostname  # noqa: E501

        :param hostname: The hostname of this ChassisInfoV7.  # noqa: E501
        :type: object
        """

        self._hostname = hostname

    @property
    def description(self):
        """Gets the description of this ChassisInfoV7.  # noqa: E501

        Chassis description  # noqa: E501

        :return: The description of this ChassisInfoV7.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChassisInfoV7.

        Chassis description  # noqa: E501

        :param description: The description of this ChassisInfoV7.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def service_tag(self):
        """Gets the service_tag of this ChassisInfoV7.  # noqa: E501

        Service tag of the chassis  # noqa: E501

        :return: The service_tag of this ChassisInfoV7.  # noqa: E501
        :rtype: str
        """
        return self._service_tag

    @service_tag.setter
    def service_tag(self, service_tag):
        """Sets the service_tag of this ChassisInfoV7.

        Service tag of the chassis  # noqa: E501

        :param service_tag: The service_tag of this ChassisInfoV7.  # noqa: E501
        :type: str
        """

        self._service_tag = service_tag

    @property
    def firmware_version(self):
        """Gets the firmware_version of this ChassisInfoV7.  # noqa: E501

        Firmware version of the chassis  # noqa: E501

        :return: The firmware_version of this ChassisInfoV7.  # noqa: E501
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        """Sets the firmware_version of this ChassisInfoV7.

        Firmware version of the chassis  # noqa: E501

        :param firmware_version: The firmware_version of this ChassisInfoV7.  # noqa: E501
        :type: str
        """

        self._firmware_version = firmware_version

    @property
    def psnt(self):
        """Gets the psnt of this ChassisInfoV7.  # noqa: E501

        PSNT of the chassis  # noqa: E501

        :return: The psnt of this ChassisInfoV7.  # noqa: E501
        :rtype: str
        """
        return self._psnt

    @psnt.setter
    def psnt(self, psnt):
        """Sets the psnt of this ChassisInfoV7.

        PSNT of the chassis  # noqa: E501

        :param psnt: The psnt of this ChassisInfoV7.  # noqa: E501
        :type: str
        """

        self._psnt = psnt

    @property
    def moid(self):
        """Gets the moid of this ChassisInfoV7.  # noqa: E501

        MOID of the chassis  # noqa: E501

        :return: The moid of this ChassisInfoV7.  # noqa: E501
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """Sets the moid of this ChassisInfoV7.

        MOID of the chassis  # noqa: E501

        :param moid: The moid of this ChassisInfoV7.  # noqa: E501
        :type: str
        """

        self._moid = moid

    @property
    def model(self):
        """Gets the model of this ChassisInfoV7.  # noqa: E501

        Model of the chassis  # noqa: E501

        :return: The model of this ChassisInfoV7.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ChassisInfoV7.

        Model of the chassis  # noqa: E501

        :param model: The model of this ChassisInfoV7.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def render_category(self):
        """Gets the render_category of this ChassisInfoV7.  # noqa: E501

        Dell render category of the chassis  # noqa: E501

        :return: The render_category of this ChassisInfoV7.  # noqa: E501
        :rtype: str
        """
        return self._render_category

    @render_category.setter
    def render_category(self, render_category):
        """Sets the render_category of this ChassisInfoV7.

        Dell render category of the chassis  # noqa: E501

        :param render_category: The render_category of this ChassisInfoV7.  # noqa: E501
        :type: str
        """

        self._render_category = render_category

    @property
    def generation(self):
        """Gets the generation of this ChassisInfoV7.  # noqa: E501

        VxRail generation of the chassis  # noqa: E501

        :return: The generation of this ChassisInfoV7.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this ChassisInfoV7.

        VxRail generation of the chassis  # noqa: E501

        :param generation: The generation of this ChassisInfoV7.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def health(self):
        """Gets the health of this ChassisInfoV7.  # noqa: E501

        Health status of the chassis  # noqa: E501

        :return: The health of this ChassisInfoV7.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this ChassisInfoV7.

        Health status of the chassis  # noqa: E501

        :param health: The health of this ChassisInfoV7.  # noqa: E501
        :type: str
        """
        allowed_values = ["Critical", "Error", "Warning", "Healthy"]  # noqa: E501
        if health not in allowed_values:
            raise ValueError(
                "Invalid value for `health` ({0}), must be one of {1}"  # noqa: E501
                .format(health, allowed_values)
            )

        self._health = health

    @property
    def missing(self):
        """Gets the missing of this ChassisInfoV7.  # noqa: E501

        Whether the chassis health status is critical. Supported values are false (not critical) and true (critical)  # noqa: E501

        :return: The missing of this ChassisInfoV7.  # noqa: E501
        :rtype: bool
        """
        return self._missing

    @missing.setter
    def missing(self, missing):
        """Sets the missing of this ChassisInfoV7.

        Whether the chassis health status is critical. Supported values are false (not critical) and true (critical)  # noqa: E501

        :param missing: The missing of this ChassisInfoV7.  # noqa: E501
        :type: bool
        """

        self._missing = missing

    @property
    def hosts(self):
        """Gets the hosts of this ChassisInfoV7.  # noqa: E501


        :return: The hosts of this ChassisInfoV7.  # noqa: E501
        :rtype: list[HostBasicInfoV7]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ChassisInfoV7.


        :param hosts: The hosts of this ChassisInfoV7.  # noqa: E501
        :type: list[HostBasicInfoV7]
        """

        self._hosts = hosts

    @property
    def witness(self):
        """Gets the witness of this ChassisInfoV7.  # noqa: E501


        :return: The witness of this ChassisInfoV7.  # noqa: E501
        :rtype: WitnessBasicInfoV2
        """
        return self._witness

    @witness.setter
    def witness(self, witness):
        """Sets the witness of this ChassisInfoV7.


        :param witness: The witness of this ChassisInfoV7.  # noqa: E501
        :type: WitnessBasicInfoV2
        """

        self._witness = witness

    @property
    def power_supplies(self):
        """Gets the power_supplies of this ChassisInfoV7.  # noqa: E501


        :return: The power_supplies of this ChassisInfoV7.  # noqa: E501
        :rtype: list[PowerSupplyInfo]
        """
        return self._power_supplies

    @power_supplies.setter
    def power_supplies(self, power_supplies):
        """Sets the power_supplies of this ChassisInfoV7.


        :param power_supplies: The power_supplies of this ChassisInfoV7.  # noqa: E501
        :type: list[PowerSupplyInfo]
        """

        self._power_supplies = power_supplies

    @property
    def chassis_manager_fw_version(self):
        """Gets the chassis_manager_fw_version of this ChassisInfoV7.  # noqa: E501

        Firmware version of the chassis manager.  # noqa: E501

        :return: The chassis_manager_fw_version of this ChassisInfoV7.  # noqa: E501
        :rtype: str
        """
        return self._chassis_manager_fw_version

    @chassis_manager_fw_version.setter
    def chassis_manager_fw_version(self, chassis_manager_fw_version):
        """Sets the chassis_manager_fw_version of this ChassisInfoV7.

        Firmware version of the chassis manager.  # noqa: E501

        :param chassis_manager_fw_version: The chassis_manager_fw_version of this ChassisInfoV7.  # noqa: E501
        :type: str
        """

        self._chassis_manager_fw_version = chassis_manager_fw_version

    @property
    def bay(self):
        """Gets the bay of this ChassisInfoV7.  # noqa: E501

        Whether the chassis has a bay or not  # noqa: E501

        :return: The bay of this ChassisInfoV7.  # noqa: E501
        :rtype: bool
        """
        return self._bay

    @bay.setter
    def bay(self, bay):
        """Sets the bay of this ChassisInfoV7.

        Whether the chassis has a bay or not  # noqa: E501

        :param bay: The bay of this ChassisInfoV7.  # noqa: E501
        :type: bool
        """

        self._bay = bay

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
        if issubclass(ChassisInfoV7, dict):
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
        if not isinstance(other, ChassisInfoV7):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
