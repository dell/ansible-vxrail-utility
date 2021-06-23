# VxmSystemInfoV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the VxRail system | 
**version** | **str** | Software version of the VxRail appliance | 
**installed_time** | **int** | Time that the VxRail appliance software was installed | [optional] 
**health** | **str** | Health status of the VxRail system | 
**network_connected** | **bool** | Whether the host is connected to the internet | 
**vc_connected** | **bool** | Whether the vCenter is connected | 
**upgrade_status** | **str** | The upgrade status of the VxRail appliance software | [optional] 
**installed_components** | [**list[InstalledComponent]**](InstalledComponent.md) | Software components installed in the VxRail system | [optional] 
**deployment_type** | **list[str]** | Information about the type of cluster deployed | 
**number_of_host** | **int** | Number of hosts in the cluster | 
**is_external_vc** | **bool** | Whether the vCenter is an external vCenter | 
**logical_view_status** | **bool** | Whether the VxRail Manager logical view is enabled | 
**shared_storage** | [**list[SharedStorage]**](SharedStorage.md) | Information about shared storage in the VxRail cluster | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

