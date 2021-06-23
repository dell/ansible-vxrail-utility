# InstalledComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | Type of software component installed | [optional] 
**name** | **str** | Installed component name | 
**description** | **str** | Installed component description | 
**current_version** | **str** | Installed component version | 
**upgrade_status** | **str** | Description of the upgrade status of the installed software component | [optional] 
**baseline** | **str** | Software version of component at the time the component was initially installed | [optional] 
**installed_time** | **int** | The time that the software component was initially installed (in milliseconds) | [optional] 
**incompatibilities** | **list[str]** | A list of other software components that the installed component is incompatible with | [optional] 
**multiple_version** | **bool** | Whether the software component has different versions installed in other nodes in the cluster | [optional] 
**baseline_drifted** | **bool** | Whether the current configuration of the installed software component is different than the initial configuration | [optional] 
**supported** | **bool** | Whether the current version of the installed software component is supported | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

