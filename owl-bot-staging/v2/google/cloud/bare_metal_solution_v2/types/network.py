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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.protobuf import field_mask_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.baremetalsolution.v2',
    manifest={
        'Network',
        'NetworkAddressReservation',
        'VRF',
        'LogicalInterface',
        'GetNetworkRequest',
        'ListNetworksRequest',
        'ListNetworksResponse',
        'UpdateNetworkRequest',
        'NetworkUsage',
        'ListNetworkUsageRequest',
        'ListNetworkUsageResponse',
    },
)


class Network(proto.Message):
    r"""A Network.

    Attributes:
        name (str):
            Output only. The resource name of this ``Network``. Resource
            names are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. Format:
            ``projects/{project}/locations/{location}/networks/{network}``
        id (str):
            An identifier for the ``Network``, generated by the backend.
        type_ (google.cloud.bare_metal_solution_v2.types.Network.Type):
            The type of this network.
        ip_address (str):
            IP address configured.
        mac_address (MutableSequence[str]):
            List of physical interfaces.
        state (google.cloud.bare_metal_solution_v2.types.Network.State):
            The Network state.
        vlan_id (str):
            The vlan id of the Network.
        cidr (str):
            The cidr of the Network.
        vrf (google.cloud.bare_metal_solution_v2.types.VRF):
            The vrf for the Network.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        services_cidr (str):
            IP range for reserved for services (e.g.
            NFS).
        reservations (MutableSequence[google.cloud.bare_metal_solution_v2.types.NetworkAddressReservation]):
            List of IP address reservations in this
            network. When updating this field, an error will
            be generated if a reservation conflicts with an
            IP address already allocated to a physical
            server.
    """
    class Type(proto.Enum):
        r"""Network type.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified value.
            CLIENT (1):
                Client network, a network peered to a Google
                Cloud VPC.
            PRIVATE (2):
                Private network, a network local to the Bare
                Metal Solution environment.
        """
        TYPE_UNSPECIFIED = 0
        CLIENT = 1
        PRIVATE = 2

    class State(proto.Enum):
        r"""The possible states for this Network.

        Values:
            STATE_UNSPECIFIED (0):
                The Network is in an unknown state.
            PROVISIONING (1):
                The Network is provisioning.
            PROVISIONED (2):
                The Network has been provisioned.
        """
        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        PROVISIONED = 2

    name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    id: str = proto.Field(
        proto.STRING,
        number=10,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=3,
    )
    mac_address: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    vlan_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    cidr: str = proto.Field(
        proto.STRING,
        number=8,
    )
    vrf: 'VRF' = proto.Field(
        proto.MESSAGE,
        number=9,
        message='VRF',
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )
    services_cidr: str = proto.Field(
        proto.STRING,
        number=12,
    )
    reservations: MutableSequence['NetworkAddressReservation'] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message='NetworkAddressReservation',
    )


class NetworkAddressReservation(proto.Message):
    r"""A reservation of one or more addresses in a network.

    Attributes:
        start_address (str):
            The first address of this reservation block.
            Must be specified as a single IPv4 address, e.g.
            10.1.2.2.
        end_address (str):
            The last address of this reservation block, inclusive. I.e.,
            for cases when reservations are only single addresses,
            end_address and start_address will be the same. Must be
            specified as a single IPv4 address, e.g. 10.1.2.2.
        note (str):
            A note about this reservation, intended for
            human consumption.
    """

    start_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    end_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    note: str = proto.Field(
        proto.STRING,
        number=3,
    )


class VRF(proto.Message):
    r"""A network VRF.

    Attributes:
        name (str):
            The name of the VRF.
        state (google.cloud.bare_metal_solution_v2.types.VRF.State):
            The possible state of VRF.
        qos_policy (google.cloud.bare_metal_solution_v2.types.VRF.QosPolicy):
            The QOS policy applied to this VRF.
        vlan_attachments (MutableSequence[google.cloud.bare_metal_solution_v2.types.VRF.VlanAttachment]):
            The list of VLAN attachments for the VRF.
    """
    class State(proto.Enum):
        r"""The possible states for this VRF.

        Values:
            STATE_UNSPECIFIED (0):
                The unspecified state.
            PROVISIONING (1):
                The vrf is provisioning.
            PROVISIONED (2):
                The vrf is provisioned.
        """
        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        PROVISIONED = 2

    class QosPolicy(proto.Message):
        r"""QOS policy parameters.

        Attributes:
            bandwidth_gbps (float):
                The bandwidth permitted by the QOS policy, in
                gbps.
        """

        bandwidth_gbps: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )

    class VlanAttachment(proto.Message):
        r"""VLAN attachment details.

        Attributes:
            peer_vlan_id (int):
                The peer vlan ID of the attachment.
            peer_ip (str):
                The peer IP of the attachment.
            router_ip (str):
                The router IP of the attachment.
        """

        peer_vlan_id: int = proto.Field(
            proto.INT64,
            number=1,
        )
        peer_ip: str = proto.Field(
            proto.STRING,
            number=2,
        )
        router_ip: str = proto.Field(
            proto.STRING,
            number=3,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    qos_policy: QosPolicy = proto.Field(
        proto.MESSAGE,
        number=6,
        message=QosPolicy,
    )
    vlan_attachments: MutableSequence[VlanAttachment] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=VlanAttachment,
    )


class LogicalInterface(proto.Message):
    r"""Each logical interface represents a logical abstraction of
    the underlying physical interface (for eg. bond, nic) of the
    instance. Each logical interface can effectively map to multiple
    network-IP pairs and still be mapped to one underlying physical
    interface.

    Attributes:
        logical_network_interfaces (MutableSequence[google.cloud.bare_metal_solution_v2.types.LogicalInterface.LogicalNetworkInterface]):
            List of logical network interfaces within a
            logical interface.
        name (str):
            Interface name. This is of syntax <bond_mode> or and forms
            part of the network template name.
        interface_index (int):
            The index of the logical interface mapping to
            the index of the hardware bond or nic on the
            chosen network template.
    """

    class LogicalNetworkInterface(proto.Message):
        r"""Each logical network interface is effectively a network and
        IP pair.

        Attributes:
            network (str):
                Name of the network
            ip_address (str):
                IP address in the network
            default_gateway (bool):
                Whether this interface is the default gateway
                for the instance. Only one interface can be the
                default gateway for the instance.
            network_type (google.cloud.bare_metal_solution_v2.types.Network.Type):
                Type of network.
            id (str):
                An identifier for the ``Network``, generated by the backend.
        """

        network: str = proto.Field(
            proto.STRING,
            number=1,
        )
        ip_address: str = proto.Field(
            proto.STRING,
            number=2,
        )
        default_gateway: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        network_type: 'Network.Type' = proto.Field(
            proto.ENUM,
            number=4,
            enum='Network.Type',
        )
        id: str = proto.Field(
            proto.STRING,
            number=5,
        )

    logical_network_interfaces: MutableSequence[LogicalNetworkInterface] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=LogicalNetworkInterface,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    interface_index: int = proto.Field(
        proto.INT32,
        number=3,
    )


class GetNetworkRequest(proto.Message):
    r"""Message for requesting network information.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListNetworksRequest(proto.Message):
    r"""Message for requesting a list of networks.

    Attributes:
        parent (str):
            Required. Parent value for
            ListNetworksRequest.
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


class ListNetworksResponse(proto.Message):
    r"""Response message containing the list of networks.

    Attributes:
        networks (MutableSequence[google.cloud.bare_metal_solution_v2.types.Network]):
            The list of networks.
        next_page_token (str):
            A token identifying a page of results from
            the server.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    networks: MutableSequence['Network'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Network',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdateNetworkRequest(proto.Message):
    r"""Message requesting to updating a network.

    Attributes:
        network (google.cloud.bare_metal_solution_v2.types.Network):
            Required. The network to update.

            The ``name`` field is used to identify the instance to
            update. Format:
            projects/{project}/locations/{location}/networks/{network}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update. The only currently supported
            fields are: ``labels``, ``reservations``
    """

    network: 'Network' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Network',
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class NetworkUsage(proto.Message):
    r"""Network with all used IP addresses.

    Attributes:
        network (google.cloud.bare_metal_solution_v2.types.Network):
            Network.
        used_ips (MutableSequence[str]):
            All used IP addresses in this network.
    """

    network: 'Network' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Network',
    )
    used_ips: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ListNetworkUsageRequest(proto.Message):
    r"""Request to get networks with IPs.

    Attributes:
        location (str):
            Required. Parent value (project and
            location).
    """

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListNetworkUsageResponse(proto.Message):
    r"""Response with Networks with IPs

    Attributes:
        networks (MutableSequence[google.cloud.bare_metal_solution_v2.types.NetworkUsage]):
            Networks with IPs.
    """

    networks: MutableSequence['NetworkUsage'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='NetworkUsage',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
