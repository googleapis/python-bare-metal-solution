# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.cloud.bare_metal_solution_v2.services.bare_metal_solution.client import BareMetalSolutionClient
from google.cloud.bare_metal_solution_v2.services.bare_metal_solution.async_client import BareMetalSolutionAsyncClient

from google.cloud.bare_metal_solution_v2.types.baremetalsolution import CreateSnapshotSchedulePolicyRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import CreateVolumeSnapshotRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import DeleteSnapshotSchedulePolicyRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import DeleteVolumeSnapshotRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import GetInstanceRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import GetLunRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import GetNetworkRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import GetSnapshotSchedulePolicyRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import GetVolumeRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import GetVolumeSnapshotRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import Instance
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ListInstancesRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ListInstancesResponse
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ListLunsRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ListLunsResponse
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ListNetworksRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ListNetworksResponse
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ListSnapshotSchedulePoliciesRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ListSnapshotSchedulePoliciesResponse
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ListVolumeSnapshotsRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ListVolumeSnapshotsResponse
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ListVolumesRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ListVolumesResponse
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import Lun
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import Network
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import OperationMetadata
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ResetInstanceRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import ResetInstanceResponse
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import RestoreVolumeSnapshotRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import SnapshotSchedulePolicy
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import UpdateSnapshotSchedulePolicyRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import UpdateVolumeRequest
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import Volume
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import VolumeSnapshot
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import VRF

__all__ = ('BareMetalSolutionClient',
    'BareMetalSolutionAsyncClient',
    'CreateSnapshotSchedulePolicyRequest',
    'CreateVolumeSnapshotRequest',
    'DeleteSnapshotSchedulePolicyRequest',
    'DeleteVolumeSnapshotRequest',
    'GetInstanceRequest',
    'GetLunRequest',
    'GetNetworkRequest',
    'GetSnapshotSchedulePolicyRequest',
    'GetVolumeRequest',
    'GetVolumeSnapshotRequest',
    'Instance',
    'ListInstancesRequest',
    'ListInstancesResponse',
    'ListLunsRequest',
    'ListLunsResponse',
    'ListNetworksRequest',
    'ListNetworksResponse',
    'ListSnapshotSchedulePoliciesRequest',
    'ListSnapshotSchedulePoliciesResponse',
    'ListVolumeSnapshotsRequest',
    'ListVolumeSnapshotsResponse',
    'ListVolumesRequest',
    'ListVolumesResponse',
    'Lun',
    'Network',
    'OperationMetadata',
    'ResetInstanceRequest',
    'ResetInstanceResponse',
    'RestoreVolumeSnapshotRequest',
    'SnapshotSchedulePolicy',
    'UpdateSnapshotSchedulePolicyRequest',
    'UpdateVolumeRequest',
    'Volume',
    'VolumeSnapshot',
    'VRF',
)
