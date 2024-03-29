# coding: utf-8

"""
    standard public schema

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 12.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Crossreferences(object):
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
        'cross_reference_id': 'int',
        'scene_id': 'int',
        'referenced_scene_id': 'int',
        'description': 'str'
    }

    attribute_map = {
        'cross_reference_id': 'cross_reference_id',
        'scene_id': 'scene_id',
        'referenced_scene_id': 'referenced_scene_id',
        'description': 'description'
    }

    def __init__(self, cross_reference_id=None, scene_id=None, referenced_scene_id=None, description=None):  # noqa: E501
        """Crossreferences - a model defined in Swagger"""  # noqa: E501
        self._cross_reference_id = None
        self._scene_id = None
        self._referenced_scene_id = None
        self._description = None
        self.discriminator = None
        self.cross_reference_id = cross_reference_id
        if scene_id is not None:
            self.scene_id = scene_id
        if referenced_scene_id is not None:
            self.referenced_scene_id = referenced_scene_id
        if description is not None:
            self.description = description

    @property
    def cross_reference_id(self):
        """Gets the cross_reference_id of this Crossreferences.  # noqa: E501

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :return: The cross_reference_id of this Crossreferences.  # noqa: E501
        :rtype: int
        """
        return self._cross_reference_id

    @cross_reference_id.setter
    def cross_reference_id(self, cross_reference_id):
        """Sets the cross_reference_id of this Crossreferences.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :param cross_reference_id: The cross_reference_id of this Crossreferences.  # noqa: E501
        :type: int
        """
        if cross_reference_id is None:
            raise ValueError("Invalid value for `cross_reference_id`, must not be `None`")  # noqa: E501

        self._cross_reference_id = cross_reference_id

    @property
    def scene_id(self):
        """Gets the scene_id of this Crossreferences.  # noqa: E501

        Note: This is a Foreign Key to `scene.scene_id`.<fk table='scene' column='scene_id'/>  # noqa: E501

        :return: The scene_id of this Crossreferences.  # noqa: E501
        :rtype: int
        """
        return self._scene_id

    @scene_id.setter
    def scene_id(self, scene_id):
        """Sets the scene_id of this Crossreferences.

        Note: This is a Foreign Key to `scene.scene_id`.<fk table='scene' column='scene_id'/>  # noqa: E501

        :param scene_id: The scene_id of this Crossreferences.  # noqa: E501
        :type: int
        """

        self._scene_id = scene_id

    @property
    def referenced_scene_id(self):
        """Gets the referenced_scene_id of this Crossreferences.  # noqa: E501

        Note: This is a Foreign Key to `scene.scene_id`.<fk table='scene' column='scene_id'/>  # noqa: E501

        :return: The referenced_scene_id of this Crossreferences.  # noqa: E501
        :rtype: int
        """
        return self._referenced_scene_id

    @referenced_scene_id.setter
    def referenced_scene_id(self, referenced_scene_id):
        """Sets the referenced_scene_id of this Crossreferences.

        Note: This is a Foreign Key to `scene.scene_id`.<fk table='scene' column='scene_id'/>  # noqa: E501

        :param referenced_scene_id: The referenced_scene_id of this Crossreferences.  # noqa: E501
        :type: int
        """

        self._referenced_scene_id = referenced_scene_id

    @property
    def description(self):
        """Gets the description of this Crossreferences.  # noqa: E501


        :return: The description of this Crossreferences.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Crossreferences.


        :param description: The description of this Crossreferences.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(Crossreferences, dict):
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
        if not isinstance(other, Crossreferences):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
