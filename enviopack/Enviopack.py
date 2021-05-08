# -*- coding: utf-8 -*-
"""
Base class for enviopack integration, common features for all modules
"""
from enviopack.constants import BASE_API_URL

class Enviopack:
  _name = "Abstract class which contains url and other integration methods"

  base_request_url:str = BASE_API_URL
  base_request_path:str = '/'

  def _optional_params(self, mandatory_params:dict, optional_fields:dict) -> dict:
    """
    Update the params dict copied from mandatory_params by getting the attributes specified in optional_fields from the object.

    @mandatory_params is a dict which contains the field in the api as key, and its value.
    @optional_fields dict with the attribute as key and the param name for the api as value
    """
    params = mandatory_params.copy()
    for field in optional_fields:
      attr = getattr(self, field,False)
      if attr:
        params.update({
          optional_fields.get(field):attr
        })
    return params