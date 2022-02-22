# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.350
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ChassisInfoV3(object):
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
        'description': 'str',
        'service_tag': 'str',
        'psnt': 'str',
        'model': 'str',
        'render_category': 'str',
        'generation': 'int',
        'health': 'str',
        'missing': 'bool',
        'hosts': 'list[HostBasicInfoV3]',
        'power_supplies': 'list[PowerSupplyInfo]'
    }

    attribute_map = {
        'id': 'id',
        'sn': 'sn',
        'part_number': 'part_number',
        'description': 'description',
        'service_tag': 'service_tag',
        'psnt': 'psnt',
        'model': 'model',
        'render_category': 'render_category',
        'generation': 'generation',
        'health': 'health',
        'missing': 'missing',
        'hosts': 'hosts',
        'power_supplies': 'power_supplies'
    }

    def __init__(self, id=None, sn=None, part_number=None, description=None, service_tag=None, psnt=None, model=None, render_category=None, generation=None, health=None, missing=None, hosts=None, power_supplies=None):  # noqa: E501
        """ChassisInfoV3 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._sn = None
        self._part_number = None
        self._description = None
        self._service_tag = None
        self._psnt = None
        self._model = None
        self._render_category = None
        self._generation = None
        self._health = None
        self._missing = None
        self._hosts = None
        self._power_supplies = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if sn is not None:
            self.sn = sn
        if part_number is not None:
            self.part_number = part_number
        if description is not None:
            self.description = description
        if service_tag is not None:
            self.service_tag = service_tag
        if psnt is not None:
            self.psnt = psnt
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
        if power_supplies is not None:
            self.power_supplies = power_supplies

    @property
    def id(self):
        """Gets the id of this ChassisInfoV3.  # noqa: E501

        ID of the chassis  # noqa: E501

        :return: The id of this ChassisInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChassisInfoV3.

        ID of the chassis  # noqa: E501

        :param id: The id of this ChassisInfoV3.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sn(self):
        """Gets the sn of this ChassisInfoV3.  # noqa: E501

        Serial number of the chassis  # noqa: E501

        :return: The sn of this ChassisInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this ChassisInfoV3.

        Serial number of the chassis  # noqa: E501

        :param sn: The sn of this ChassisInfoV3.  # noqa: E501
        :type: str
        """

        self._sn = sn

    @property
    def part_number(self):
        """Gets the part_number of this ChassisInfoV3.  # noqa: E501

        Part number of the chassis  # noqa: E501

        :return: The part_number of this ChassisInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this ChassisInfoV3.

        Part number of the chassis  # noqa: E501

        :param part_number: The part_number of this ChassisInfoV3.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def description(self):
        """Gets the description of this ChassisInfoV3.  # noqa: E501

        Chassis description  # noqa: E501

        :return: The description of this ChassisInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChassisInfoV3.

        Chassis description  # noqa: E501

        :param description: The description of this ChassisInfoV3.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def service_tag(self):
        """Gets the service_tag of this ChassisInfoV3.  # noqa: E501

        Service tag of the chassis  # noqa: E501

        :return: The service_tag of this ChassisInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._service_tag

    @service_tag.setter
    def service_tag(self, service_tag):
        """Sets the service_tag of this ChassisInfoV3.

        Service tag of the chassis  # noqa: E501

        :param service_tag: The service_tag of this ChassisInfoV3.  # noqa: E501
        :type: str
        """

        self._service_tag = service_tag

    @property
    def psnt(self):
        """Gets the psnt of this ChassisInfoV3.  # noqa: E501

        PSNT of the chassis  # noqa: E501

        :return: The psnt of this ChassisInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._psnt

    @psnt.setter
    def psnt(self, psnt):
        """Sets the psnt of this ChassisInfoV3.

        PSNT of the chassis  # noqa: E501

        :param psnt: The psnt of this ChassisInfoV3.  # noqa: E501
        :type: str
        """

        self._psnt = psnt

    @property
    def model(self):
        """Gets the model of this ChassisInfoV3.  # noqa: E501

        Model of the chassis  # noqa: E501

        :return: The model of this ChassisInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ChassisInfoV3.

        Model of the chassis  # noqa: E501

        :param model: The model of this ChassisInfoV3.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def render_category(self):
        """Gets the render_category of this ChassisInfoV3.  # noqa: E501

        Dell render category of the chassis  # noqa: E501

        :return: The render_category of this ChassisInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._render_category

    @render_category.setter
    def render_category(self, render_category):
        """Sets the render_category of this ChassisInfoV3.

        Dell render category of the chassis  # noqa: E501

        :param render_category: The render_category of this ChassisInfoV3.  # noqa: E501
        :type: str
        """

        self._render_category = render_category

    @property
    def generation(self):
        """Gets the generation of this ChassisInfoV3.  # noqa: E501

        VxRail generation of the chassis  # noqa: E501

        :return: The generation of this ChassisInfoV3.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this ChassisInfoV3.

        VxRail generation of the chassis  # noqa: E501

        :param generation: The generation of this ChassisInfoV3.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def health(self):
        """Gets the health of this ChassisInfoV3.  # noqa: E501

        Health status of the chassis  # noqa: E501

        :return: The health of this ChassisInfoV3.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this ChassisInfoV3.

        Health status of the chassis  # noqa: E501

        :param health: The health of this ChassisInfoV3.  # noqa: E501
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
        """Gets the missing of this ChassisInfoV3.  # noqa: E501

        Whether the chassis health status is critical. Supported values are false (not critical) and true (critical)  # noqa: E501

        :return: The missing of this ChassisInfoV3.  # noqa: E501
        :rtype: bool
        """
        return self._missing

    @missing.setter
    def missing(self, missing):
        """Sets the missing of this ChassisInfoV3.

        Whether the chassis health status is critical. Supported values are false (not critical) and true (critical)  # noqa: E501

        :param missing: The missing of this ChassisInfoV3.  # noqa: E501
        :type: bool
        """

        self._missing = missing

    @property
    def hosts(self):
        """Gets the hosts of this ChassisInfoV3.  # noqa: E501


        :return: The hosts of this ChassisInfoV3.  # noqa: E501
        :rtype: list[HostBasicInfoV3]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ChassisInfoV3.


        :param hosts: The hosts of this ChassisInfoV3.  # noqa: E501
        :type: list[HostBasicInfoV3]
        """

        self._hosts = hosts

    @property
    def power_supplies(self):
        """Gets the power_supplies of this ChassisInfoV3.  # noqa: E501


        :return: The power_supplies of this ChassisInfoV3.  # noqa: E501
        :rtype: list[PowerSupplyInfo]
        """
        return self._power_supplies

    @power_supplies.setter
    def power_supplies(self, power_supplies):
        """Sets the power_supplies of this ChassisInfoV3.


        :param power_supplies: The power_supplies of this ChassisInfoV3.  # noqa: E501
        :type: list[PowerSupplyInfo]
        """

        self._power_supplies = power_supplies

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
        if issubclass(ChassisInfoV3, dict):
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
        if not isinstance(other, ChassisInfoV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other