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

class Dialogue(object):
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
        'dialogue_id': 'int',
        'scene_id': 'int',
        'character_id': 'int',
        'original_text': 'str',
        'modernized_text': 'str'
    }

    attribute_map = {
        'dialogue_id': 'dialogue_id',
        'scene_id': 'scene_id',
        'character_id': 'character_id',
        'original_text': 'original_text',
        'modernized_text': 'modernized_text'
    }

    def __init__(self, dialogue_id=None, scene_id=None, character_id=None, original_text=None, modernized_text=None):  # noqa: E501
        """Dialogue - a model defined in Swagger"""  # noqa: E501
        self._dialogue_id = None
        self._scene_id = None
        self._character_id = None
        self._original_text = None
        self._modernized_text = None
        self.discriminator = None
        self.dialogue_id = dialogue_id
        if scene_id is not None:
            self.scene_id = scene_id
        if character_id is not None:
            self.character_id = character_id
        if original_text is not None:
            self.original_text = original_text
        if modernized_text is not None:
            self.modernized_text = modernized_text

    @property
    def dialogue_id(self):
        """Gets the dialogue_id of this Dialogue.  # noqa: E501

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :return: The dialogue_id of this Dialogue.  # noqa: E501
        :rtype: int
        """
        return self._dialogue_id

    @dialogue_id.setter
    def dialogue_id(self, dialogue_id):
        """Sets the dialogue_id of this Dialogue.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :param dialogue_id: The dialogue_id of this Dialogue.  # noqa: E501
        :type: int
        """
        if dialogue_id is None:
            raise ValueError("Invalid value for `dialogue_id`, must not be `None`")  # noqa: E501

        self._dialogue_id = dialogue_id

    @property
    def scene_id(self):
        """Gets the scene_id of this Dialogue.  # noqa: E501

        Note: This is a Foreign Key to `scene.scene_id`.<fk table='scene' column='scene_id'/>  # noqa: E501

        :return: The scene_id of this Dialogue.  # noqa: E501
        :rtype: int
        """
        return self._scene_id

    @scene_id.setter
    def scene_id(self, scene_id):
        """Sets the scene_id of this Dialogue.

        Note: This is a Foreign Key to `scene.scene_id`.<fk table='scene' column='scene_id'/>  # noqa: E501

        :param scene_id: The scene_id of this Dialogue.  # noqa: E501
        :type: int
        """

        self._scene_id = scene_id

    @property
    def character_id(self):
        """Gets the character_id of this Dialogue.  # noqa: E501

        Note: This is a Foreign Key to `character.character_id`.<fk table='character' column='character_id'/>  # noqa: E501

        :return: The character_id of this Dialogue.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this Dialogue.

        Note: This is a Foreign Key to `character.character_id`.<fk table='character' column='character_id'/>  # noqa: E501

        :param character_id: The character_id of this Dialogue.  # noqa: E501
        :type: int
        """

        self._character_id = character_id

    @property
    def original_text(self):
        """Gets the original_text of this Dialogue.  # noqa: E501


        :return: The original_text of this Dialogue.  # noqa: E501
        :rtype: str
        """
        return self._original_text

    @original_text.setter
    def original_text(self, original_text):
        """Sets the original_text of this Dialogue.


        :param original_text: The original_text of this Dialogue.  # noqa: E501
        :type: str
        """

        self._original_text = original_text

    @property
    def modernized_text(self):
        """Gets the modernized_text of this Dialogue.  # noqa: E501


        :return: The modernized_text of this Dialogue.  # noqa: E501
        :rtype: str
        """
        return self._modernized_text

    @modernized_text.setter
    def modernized_text(self, modernized_text):
        """Sets the modernized_text of this Dialogue.


        :param modernized_text: The modernized_text of this Dialogue.  # noqa: E501
        :type: str
        """

        self._modernized_text = modernized_text

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
        if issubclass(Dialogue, dict):
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
        if not isinstance(other, Dialogue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
