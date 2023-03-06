# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network nsg rule update",
)
class Update(AAZCommand):
    """Update a network security group rule.

    :example: Update an NSG rule with a new wildcard destination address prefix.
        az network nsg rule update -g MyResourceGroup --nsg-name MyNsg -n MyNsgRule --destination-address-prefix '*'

    :example: Update a network security group rule.
        az network nsg rule update --name MyNsgRule --nsg-name MyNsg --resource-group MyResourceGroup --source-address-prefixes 208.130.28/24
    """

    _aaz_info = {
        "version": "2015-06-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networksecuritygroups/{}/securityrules/{}", "2015-06-15"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.nsg_name = AAZStrArg(
            options=["--nsg-name"],
            help="Name of the network security group.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the network security group rule.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.access = AAZStrArg(
            options=["--access"],
            help="Network traffic is allowed or denied.",
            enum={"Allow": "Allow", "Deny": "Deny"},
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            help="Description for this rule. Restricted to 140 chars.",
            nullable=True,
        )
        _args_schema.direction = AAZStrArg(
            options=["--direction"],
            help="Direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic.",
            enum={"Inbound": "Inbound", "Outbound": "Outbound"},
        )
        _args_schema.priority = AAZIntArg(
            options=["--priority"],
            help="Priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.",
            nullable=True,
        )
        _args_schema.protocol = AAZStrArg(
            options=["--protocol"],
            help="Network protocol this rule applies to.",
            enum={"*": "*", "Tcp": "Tcp", "Udp": "Udp"},
        )

        # define Arg Group "Destination"

        _args_schema = cls._args_schema
        _args_schema.destination_address_prefix = AAZStrArg(
            options=["--destination-address-prefix"],
            arg_group="Destination",
            help="The destination address prefix. CIDR or destination IP range. Asterisk '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used.",
        )
        _args_schema.destination_port_range = AAZStrArg(
            options=["--destination-port-range"],
            arg_group="Destination",
            help="The destination port or range. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports.",
            nullable=True,
        )

        # define Arg Group "Properties"

        # define Arg Group "SecurityRuleParameters"

        # define Arg Group "Source"

        _args_schema = cls._args_schema
        _args_schema.source_address_prefix = AAZStrArg(
            options=["--source-address-prefix"],
            arg_group="Source",
            help="The CIDR or source IP range. Asterisk '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used. If this is an ingress rule, specifies where network traffic originates from.",
        )
        _args_schema.source_port_range = AAZStrArg(
            options=["--source-port-range"],
            arg_group="Source",
            help="The source port or range. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports.",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SecurityRulesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.SecurityRulesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SecurityRulesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{networkSecurityGroupName}/securityRules/{securityRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkSecurityGroupName", self.ctx.args.nsg_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "securityRuleName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2015-06-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_security_rule_read(cls._schema_on_200)

            return cls._schema_on_200

    class SecurityRulesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{networkSecurityGroupName}/securityRules/{securityRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkSecurityGroupName", self.ctx.args.nsg_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "securityRuleName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2015-06-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_security_rule_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("access", AAZStrType, ".access", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("destinationAddressPrefix", AAZStrType, ".destination_address_prefix", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("destinationPortRange", AAZStrType, ".destination_port_range")
                properties.set_prop("direction", AAZStrType, ".direction", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("priority", AAZIntType, ".priority")
                properties.set_prop("protocol", AAZStrType, ".protocol", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("sourceAddressPrefix", AAZStrType, ".source_address_prefix", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("sourcePortRange", AAZStrType, ".source_port_range")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_security_rule_read = None

    @classmethod
    def _build_schema_security_rule_read(cls, _schema):
        if cls._schema_security_rule_read is not None:
            _schema.etag = cls._schema_security_rule_read.etag
            _schema.id = cls._schema_security_rule_read.id
            _schema.name = cls._schema_security_rule_read.name
            _schema.properties = cls._schema_security_rule_read.properties
            return

        cls._schema_security_rule_read = _schema_security_rule_read = AAZObjectType()

        security_rule_read = _schema_security_rule_read
        security_rule_read.etag = AAZStrType()
        security_rule_read.id = AAZStrType()
        security_rule_read.name = AAZStrType()
        security_rule_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_security_rule_read.properties
        properties.access = AAZStrType(
            flags={"required": True},
        )
        properties.description = AAZStrType()
        properties.destination_address_prefix = AAZStrType(
            serialized_name="destinationAddressPrefix",
            flags={"required": True},
        )
        properties.destination_port_range = AAZStrType(
            serialized_name="destinationPortRange",
        )
        properties.direction = AAZStrType(
            flags={"required": True},
        )
        properties.priority = AAZIntType()
        properties.protocol = AAZStrType(
            flags={"required": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.source_address_prefix = AAZStrType(
            serialized_name="sourceAddressPrefix",
            flags={"required": True},
        )
        properties.source_port_range = AAZStrType(
            serialized_name="sourcePortRange",
        )

        _schema.etag = cls._schema_security_rule_read.etag
        _schema.id = cls._schema_security_rule_read.id
        _schema.name = cls._schema_security_rule_read.name
        _schema.properties = cls._schema_security_rule_read.properties


__all__ = ["Update"]
