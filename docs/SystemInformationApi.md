# vxrail_ansible_utility.SystemInformationApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_vx_rail_manager_system_information_v2**](SystemInformationApi.md#query_vx_rail_manager_system_information_v2) | **GET** /v2/system | Retrieves VxRail system information (v2).
[**query_vx_rail_manager_system_information_v3**](SystemInformationApi.md#query_vx_rail_manager_system_information_v3) | **GET** /v3/system | Retrieves VxRail system information (v3).

# **query_vx_rail_manager_system_information_v2**
> VxmSystemInfoV2 query_vx_rail_manager_system_information_v2()

Retrieves VxRail system information (v2).

Retrieves VxRail system information (v2).

### Example
```python
from __future__ import print_function
import time
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = vxrail_ansible_utility.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = vxrail_ansible_utility.SystemInformationApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Retrieves VxRail system information (v2).
    api_response = api_instance.query_vx_rail_manager_system_information_v2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInformationApi->query_vx_rail_manager_system_information_v2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VxmSystemInfoV2**](VxmSystemInfoV2.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_vx_rail_manager_system_information_v3**
> VxmSystemInfoV3 query_vx_rail_manager_system_information_v3()

Retrieves VxRail system information (v3).

Retrieves VxRail system information (v3).

### Example
```python
from __future__ import print_function
import time
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = vxrail_ansible_utility.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = vxrail_ansible_utility.SystemInformationApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Retrieves VxRail system information (v3).
    api_response = api_instance.query_vx_rail_manager_system_information_v3()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInformationApi->query_vx_rail_manager_system_information_v3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VxmSystemInfoV3**](VxmSystemInfoV3.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

