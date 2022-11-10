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
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.protobuf import field_mask_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.baremetalsolution.v2',
    manifest={
        'Volume',
        'GetVolumeRequest',
        'ListVolumesRequest',
        'ListVolumesResponse',
        'UpdateVolumeRequest',
        'ResizeVolumeRequest',
    },
)


class Volume(proto.Message):
    r"""A storage volume.

    Attributes:
        name (str):
            Output only. The resource name of this ``Volume``. Resource
            names are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. Format:
            ``projects/{project}/locations/{location}/volumes/{volume}``
        id (str):
            An identifier for the ``Volume``, generated by the backend.
        storage_type (google.cloud.bare_metal_solution_v2.types.Volume.StorageType):
            The storage type for this volume.
        state (google.cloud.bare_metal_solution_v2.types.Volume.State):
            The state of this storage volume.
        requested_size_gib (int):
            The requested size of this storage volume, in
            GiB.
        current_size_gib (int):
            The current size of this storage volume, in
            GiB, including space reserved for snapshots.
            This size might be different than the requested
            size if the storage volume has been configured
            with auto grow or auto shrink.
        emergency_size_gib (int):
            Additional emergency size that was requested for this
            Volume, in GiB. current_size_gib includes this value.
        auto_grown_size_gib (int):
            The size, in GiB, that this storage volume
            has expanded as a result of an auto grow policy.
            In the absence of auto-grow, the value is 0.
        remaining_space_gib (int):
            The space remaining in the storage volume for
            new LUNs, in GiB, excluding space reserved for
            snapshots.
        snapshot_reservation_detail (google.cloud.bare_metal_solution_v2.types.Volume.SnapshotReservationDetail):
            Details about snapshot space reservation and
            usage on the storage volume.
        snapshot_auto_delete_behavior (google.cloud.bare_metal_solution_v2.types.Volume.SnapshotAutoDeleteBehavior):
            The behavior to use when snapshot reserved
            space is full.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        snapshot_enabled (bool):
            Whether snapshots are enabled.
        pod (str):
            Immutable. Pod name.
    """
    class StorageType(proto.Enum):
        r"""The storage type for a volume."""
        STORAGE_TYPE_UNSPECIFIED = 0
        SSD = 1
        HDD = 2

    class State(proto.Enum):
        r"""The possible states for a storage volume."""
        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3

    class SnapshotAutoDeleteBehavior(proto.Enum):
        r"""The kinds of auto delete behavior to use when snapshot
        reserved space is full.
        """
        SNAPSHOT_AUTO_DELETE_BEHAVIOR_UNSPECIFIED = 0
        DISABLED = 1
        OLDEST_FIRST = 2
        NEWEST_FIRST = 3

    class SnapshotReservationDetail(proto.Message):
        r"""Details about snapshot space reservation and usage on the
        storage volume.

        Attributes:
            reserved_space_gib (int):
                The space on this storage volume reserved for
                snapshots, shown in GiB.
            reserved_space_used_percent (int):
                The percent of snapshot space on this storage
                volume actually being used by the snapshot
                copies. This value might be higher than 100% if
                the snapshot copies have overflowed into the
                data portion of the storage volume.
            reserved_space_remaining_gib (int):
                The amount, in GiB, of available space in
                this storage volume's reserved snapshot space.
            reserved_space_percent (int):
                Percent of the total Volume size reserved for snapshot
                copies. Enabling snapshots requires reserving 20% or more of
                the storage volume space for snapshots. Maximum reserved
                space for snapshots is 40%. Setting this field will
                effectively set snapshot_enabled to true.
        """

        reserved_space_gib: int = proto.Field(
            proto.INT64,
            number=1,
        )
        reserved_space_used_percent: int = proto.Field(
            proto.INT32,
            number=2,
        )
        reserved_space_remaining_gib: int = proto.Field(
            proto.INT64,
            number=3,
        )
        reserved_space_percent: int = proto.Field(
            proto.INT32,
            number=4,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=11,
    )
    storage_type: StorageType = proto.Field(
        proto.ENUM,
        number=2,
        enum=StorageType,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    requested_size_gib: int = proto.Field(
        proto.INT64,
        number=4,
    )
    current_size_gib: int = proto.Field(
        proto.INT64,
        number=5,
    )
    emergency_size_gib: int = proto.Field(
        proto.INT64,
        number=14,
    )
    auto_grown_size_gib: int = proto.Field(
        proto.INT64,
        number=6,
    )
    remaining_space_gib: int = proto.Field(
        proto.INT64,
        number=7,
    )
    snapshot_reservation_detail: SnapshotReservationDetail = proto.Field(
        proto.MESSAGE,
        number=8,
        message=SnapshotReservationDetail,
    )
    snapshot_auto_delete_behavior: SnapshotAutoDeleteBehavior = proto.Field(
        proto.ENUM,
        number=9,
        enum=SnapshotAutoDeleteBehavior,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )
    snapshot_enabled: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    pod: str = proto.Field(
        proto.STRING,
        number=15,
    )


class GetVolumeRequest(proto.Message):
    r"""Message for requesting storage volume information.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListVolumesRequest(proto.Message):
    r"""Message for requesting a list of storage volumes.

    Attributes:
        parent (str):
            Required. Parent value for
            ListVolumesRequest.
        page_size (int):
            Requested page size. The server might return
            fewer items than requested. If unspecified,
            server will pick an appropriate default.
        page_token (str):
            A token identifying a page of results from
            the server.
        filter (str):
            List filter.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListVolumesResponse(proto.Message):
    r"""Response message containing the list of storage volumes.

    Attributes:
        volumes (MutableSequence[google.cloud.bare_metal_solution_v2.types.Volume]):
            The list of storage volumes.
        next_page_token (str):
            A token identifying a page of results from
            the server.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    volumes: MutableSequence['Volume'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Volume',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdateVolumeRequest(proto.Message):
    r"""Message for updating a volume.

    Attributes:
        volume (google.cloud.bare_metal_solution_v2.types.Volume):
            Required. The volume to update.

            The ``name`` field is used to identify the volume to update.
            Format:
            projects/{project}/locations/{location}/volumes/{volume}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update. The only currently supported
            fields are: ``snapshot_auto_delete_behavior``
            ``snapshot_schedule_policy_name`` 'labels'
            'snapshot_enabled'
            'snapshot_reservation_detail.reserved_space_percent'
    """

    volume: 'Volume' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Volume',
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ResizeVolumeRequest(proto.Message):
    r"""Request for emergency resize Volume.

    Attributes:
        volume (str):
            Required. Volume to resize.
        size_gib (int):
            New Volume size, in GiB.
    """

    volume: str = proto.Field(
        proto.STRING,
        number=1,
    )
    size_gib: int = proto.Field(
        proto.INT64,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))