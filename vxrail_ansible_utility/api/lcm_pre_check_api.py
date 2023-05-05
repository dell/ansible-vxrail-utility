# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 1.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vxrail_ansible_utility.api_client import ApiClient


class LCMPreCheckApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def precheck_v1(self, body, **kwargs):  # noqa: E501
        """Perform a health pre-check  # noqa: E501

        Perform a separate health pre-check for the VxRail system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.precheck_v1(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HealthPrecheckSpecV1 body: Input parameters needed for health pre-check (required)
        :return: AsyncLcmRequestSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.precheck_v1_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.precheck_v1_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def precheck_v1_with_http_info(self, body, **kwargs):  # noqa: E501
        """Perform a health pre-check  # noqa: E501

        Perform a separate health pre-check for the VxRail system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.precheck_v1_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HealthPrecheckSpecV1 body: Input parameters needed for health pre-check (required)
        :return: AsyncLcmRequestSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method precheck_v1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `precheck_v1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/lcm/precheck', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncLcmRequestSuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_upload_bundle_customized_component(self, customized_component, checksum, type, **kwargs):  # noqa: E501
        """Upload the content of the file to destination  # noqa: E501

        Upload the content of the file to any designated location. Limitation: 1. Only one file can be uploaded at a time.  2. The file size should not exceed 10 GB.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_upload_bundle_customized_component(customized_component, checksum, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customized_component: Indicates if the uploading file is a customized component. If the value is false, the system treats this file as a common file, such as an LCM bundle. (required)
        :param str checksum: Indicates that the checksum of the uploaded file is SHA512. Enter the correct checksum value, which is verified after uploading the file. (required)
        :param str type: Supports driver, firmware, or bundle type only. (required)
        :param str component_bundle:
        :return: UploadCustomizedComponentv1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_upload_bundle_customized_component_with_http_info(customized_component, checksum, type, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_upload_bundle_customized_component_with_http_info(customized_component, checksum, type, **kwargs)  # noqa: E501
            return data

    def v1_upload_bundle_customized_component_with_http_info(self, customized_component, checksum, type, **kwargs):  # noqa: E501
        """Upload the content of the file to destination  # noqa: E501

        Upload the content of the file to any designated location. Limitation: 1. Only one file can be uploaded at a time.  2. The file size should not exceed 10 GB.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_upload_bundle_customized_component_with_http_info(customized_component, checksum, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customized_component: Indicates if the uploading file is a customized component. If the value is false, the system treats this file as a common file, such as an LCM bundle. (required)
        :param str checksum: Indicates that the checksum of the uploaded file is SHA512. Enter the correct checksum value, which is verified after uploading the file. (required)
        :param str type: Supports driver, firmware, or bundle type only. (required)
        :param str component_bundle:
        :return: UploadCustomizedComponentv1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customized_component', 'checksum', 'type', 'component_bundle']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_upload_bundle_customized_component" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customized_component' is set
        if ('customized_component' not in params or
                params['customized_component'] is None):
            raise ValueError("Missing the required parameter `customized_component` when calling `v1_upload_bundle_customized_component`")  # noqa: E501
        # verify the required parameter 'checksum' is set
        if ('checksum' not in params or
                params['checksum'] is None):
            raise ValueError("Missing the required parameter `checksum` when calling `v1_upload_bundle_customized_component`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `v1_upload_bundle_customized_component`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'customized_component' in params:
            query_params.append(('customized_component', params['customized_component']))  # noqa: E501
        if 'checksum' in params:
            query_params.append(('checksum', params['checksum']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'component_bundle' in params:
            local_var_files['component_bundle'] = params['component_bundle']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/lcm/upgrade/upload-bundle', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UploadCustomizedComponentv1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
