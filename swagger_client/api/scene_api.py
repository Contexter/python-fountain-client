# coding: utf-8

"""
    standard public schema

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 12.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SceneApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def scene_delete(self, **kwargs):  # noqa: E501
        """scene_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_delete(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scene_id:
        :param str act_id:
        :param str scene_number:
        :param str synopsis:
        :param str notes:
        :param str prefer: Preference
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scene_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.scene_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def scene_delete_with_http_info(self, **kwargs):  # noqa: E501
        """scene_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scene_id:
        :param str act_id:
        :param str scene_number:
        :param str synopsis:
        :param str notes:
        :param str prefer: Preference
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scene_id', 'act_id', 'scene_number', 'synopsis', 'notes', 'prefer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scene_delete" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scene_id' in params:
            query_params.append(('scene_id', params['scene_id']))  # noqa: E501
        if 'act_id' in params:
            query_params.append(('act_id', params['act_id']))  # noqa: E501
        if 'scene_number' in params:
            query_params.append(('scene_number', params['scene_number']))  # noqa: E501
        if 'synopsis' in params:
            query_params.append(('synopsis', params['synopsis']))  # noqa: E501
        if 'notes' in params:
            query_params.append(('notes', params['notes']))  # noqa: E501

        header_params = {}
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/scene', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scene_get(self, **kwargs):  # noqa: E501
        """scene_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scene_id:
        :param str act_id:
        :param str scene_number:
        :param str synopsis:
        :param str notes:
        :param str select: Filtering Columns
        :param str order: Ordering
        :param str range: Limiting and Pagination
        :param str range_unit: Limiting and Pagination
        :param str offset: Limiting and Pagination
        :param str limit: Limiting and Pagination
        :param str prefer: Preference
        :return: list[Scene]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scene_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.scene_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def scene_get_with_http_info(self, **kwargs):  # noqa: E501
        """scene_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scene_id:
        :param str act_id:
        :param str scene_number:
        :param str synopsis:
        :param str notes:
        :param str select: Filtering Columns
        :param str order: Ordering
        :param str range: Limiting and Pagination
        :param str range_unit: Limiting and Pagination
        :param str offset: Limiting and Pagination
        :param str limit: Limiting and Pagination
        :param str prefer: Preference
        :return: list[Scene]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scene_id', 'act_id', 'scene_number', 'synopsis', 'notes', 'select', 'order', 'range', 'range_unit', 'offset', 'limit', 'prefer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scene_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scene_id' in params:
            query_params.append(('scene_id', params['scene_id']))  # noqa: E501
        if 'act_id' in params:
            query_params.append(('act_id', params['act_id']))  # noqa: E501
        if 'scene_number' in params:
            query_params.append(('scene_number', params['scene_number']))  # noqa: E501
        if 'synopsis' in params:
            query_params.append(('synopsis', params['synopsis']))  # noqa: E501
        if 'notes' in params:
            query_params.append(('notes', params['notes']))  # noqa: E501
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}
        if 'range' in params:
            header_params['Range'] = params['range']  # noqa: E501
        if 'range_unit' in params:
            header_params['Range-Unit'] = params['range_unit']  # noqa: E501
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/vnd.pgrst.object+json;nulls=stripped', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/scene', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Scene]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scene_patch(self, **kwargs):  # noqa: E501
        """scene_patch  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_patch(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Scene body: scene
        :param str prefer: Preference
        :param str scene_id:
        :param str act_id:
        :param str scene_number:
        :param str synopsis:
        :param str notes:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scene_patch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.scene_patch_with_http_info(**kwargs)  # noqa: E501
            return data

    def scene_patch_with_http_info(self, **kwargs):  # noqa: E501
        """scene_patch  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_patch_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Scene body: scene
        :param str prefer: Preference
        :param str scene_id:
        :param str act_id:
        :param str scene_number:
        :param str synopsis:
        :param str notes:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'prefer', 'scene_id', 'act_id', 'scene_number', 'synopsis', 'notes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scene_patch" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scene_id' in params:
            query_params.append(('scene_id', params['scene_id']))  # noqa: E501
        if 'act_id' in params:
            query_params.append(('act_id', params['act_id']))  # noqa: E501
        if 'scene_number' in params:
            query_params.append(('scene_number', params['scene_number']))  # noqa: E501
        if 'synopsis' in params:
            query_params.append(('synopsis', params['synopsis']))  # noqa: E501
        if 'notes' in params:
            query_params.append(('notes', params['notes']))  # noqa: E501

        header_params = {}
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/vnd.pgrst.object+json;nulls=stripped', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/scene', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scene_post(self, **kwargs):  # noqa: E501
        """scene_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Scene body: scene
        :param str prefer: Preference
        :param str select: Filtering Columns
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scene_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.scene_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def scene_post_with_http_info(self, **kwargs):  # noqa: E501
        """scene_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scene_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Scene body: scene
        :param str prefer: Preference
        :param str select: Filtering Columns
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'prefer', 'select']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scene_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501

        header_params = {}
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/vnd.pgrst.object+json;nulls=stripped', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/scene', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)