import json
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from merlin.models import Devices, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnConfig, LearnInterface, LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual, LearnVLAN, LearnVRF, ShowInventory, ShowIPIntBrief, ShowVersion

class SearchView(TemplateView):
    template_name = 'Search/search.html'

class SearchResultAllView(ListView):
    template_name = 'Search/Results/search_results_all.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = (Devices.objects.filter(
            Q(hostname__icontains=query) | Q(alias__icontains=query) | Q(device_type__icontains=query) | Q(os__icontains=query) | Q(username__icontains=query) | Q(password__icontains=query) | Q(protocol__icontains=query) | Q(ip_address__icontains=query) | Q(port__icontains=query) | Q(connection_timeout__icontains=query)
        ),LearnACL.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(acl__icontains=query) | Q(ace__icontains=query) | Q(permission__icontains=query) | Q(logging__icontains=query) | Q(source_network__icontains=query) | Q(destination_network__icontains=query) | Q(l3_protocol__icontains=query) | Q(l4_protocol__icontains=query) | Q(operator__icontains=query) | Q(port__icontains=query)
        ),LearnARP.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(interface__icontains=query) | Q(neighbor_ip__icontains=query) | Q(neighbor_mac__icontains=query) | Q(origin__icontains=query) | Q(local_proxy__icontains=query) | Q(proxy__icontains=query)
        ),LearnARPStatistics.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(entries_total__icontains=query) | Q(in_drops__icontains=query) | Q(in_replies_pkts__icontains=query) | Q(in_requests_pkts__icontains=query) | Q(incomplete_total__icontains=query) | Q(out_replies_pkts__icontains=query) | Q(out_requests_pkts__icontains=query)
        ),LearnBGPInstances.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(instance__icontains=query) | Q(bgp_id__icontains=query) | Q(protocol_state__icontains=query) | Q(nexthop_trigger_delay_critical__icontains=query) | Q(nexthop_trigger_delay_noncritical__icontains=query) | Q(nexthop_trigger_enabled__icontains=query) | Q(vrf__icontains=query) | Q(router_id__icontains=query) | Q(cluster_id__icontains=query) | Q(confederation_id__icontains=query) | Q(neighbor__icontains=query) | Q(version__icontains=query) | Q(hold_time__icontains=query) | Q(keep_alive_interval__icontains=query) | Q(local_as__icontains=query) | Q(remote_as__icontains=query) | Q(neighbor_counters_received_bytes_in_queue__icontains=query) | Q(neighbor_counters_received_capability__icontains=query) | Q(neighbor_counters_received_keepalives__icontains=query) | Q(neighbor_counters_received_notifications__icontains=query) | Q(neighbor_counters_received_opens__icontains=query) | Q(neighbor_counters_received_route_refresh__icontains=query) | Q(neighbor_counters_received_total__icontains=query) | Q(neighbor_counters_received_total_bytes__icontains=query) | Q(neighbor_counters_received_updates__icontains=query) | Q(neighbor_counters_sent_bytes_in_queue__icontains=query) | Q(neighbor_counters_sent_capability__icontains=query) | Q(neighbor_counters_sent_keepalives__icontains=query) | Q(neighbor_counters_sent_notifications__icontains=query) | Q(neighbor_counters_sent_opens__icontains=query) | Q(neighbor_counters_sent_route_refresh__icontains=query) | Q(neighbor_counters_sent_total__icontains=query) | Q(neighbor_counters_sent_total_bytes__icontains=query) | Q(neighbor_counters_sent_updates__icontains=query) | Q(last_reset__icontains=query) | Q(reset_reason__icontains=query)
        ),LearnBGPRoutesPerPeer.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(instance__icontains=query) | Q(vrf__icontains=query) | Q(neighbor__icontains=query) | Q(advertised__icontains=query) | Q(routes__icontains=query) | Q(remote_as__icontains=query)
        ),LearnBGPTables.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(instance__icontains=query) | Q(vrf__icontains=query) | Q(table_version__icontains=query) | Q(prefix__icontains=query) | Q(index__icontains=query) | Q(localpref__icontains=query) | Q(next_hop__icontains=query) | Q(origin_code__icontains=query) | Q(status_code__icontains=query) | Q(weight__icontains=query) 
        ),LearnConfig.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(config__icontains=query) 
        ),LearnInterface.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(interface__icontains=query) | Q(description__icontains=query) | Q(access_vlan__icontains=query) | Q(native_vlan__icontains=query) | Q(switchport_mode__icontains=query) | Q(interface_type__icontains=query) | Q(bandwidth__icontains=query) | Q(speed__icontains=query) | Q(duplex__icontains=query) | Q(mtu__icontains=query) | Q(mac_address__icontains=query) | Q(physical_address__icontains=query) | Q(ip_address__icontains=query) | Q(encapsulation__icontains=query)
        ),LearnPlatform.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(chassis__icontains=query) | Q(chassis_sn__icontains=query) | Q(image__icontains=query) | Q(installed_packages__icontains=query) | Q(rtr_type__icontains=query) | Q(version__icontains=query) 
        ),LearnPlatformSlots.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(slot__icontains=query) | Q(slot_name__icontains=query) | Q(slot_sn__icontains=query) | Q(slot_state__icontains=query) | Q(slot_redundancy_state__icontains=query) | Q(rp_boot_image__icontains=query)
        ),LearnPlatformVirtual.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(virtual_device_name__icontains=query) | Q(virtual_device_status__icontains=query) | Q(virtual_device_member__icontains=query) | Q(virtual_device_member_status__icontains=query) | Q(virtual_device_member_type__icontains=query)
        ),LearnVLAN.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(vlan__icontains=query) | Q(interfaces__icontains=query) | Q(mode__icontains=query) | Q(name__icontains=query) | Q(shutdown__icontains=query) | Q(state__icontains=query)
        ),LearnVRF.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(vrf__icontains=query) | Q(address_family_ipv4__icontains=query) | Q(address_family_ipv6__icontains=query) | Q(route_distinguisher__icontains=query)
        ),ShowInventory.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(part__icontains=query) | Q(description__icontains=query) | Q(pid__icontains=query) | Q(serial_number__icontains=query) 
        ),ShowIPIntBrief.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(interface__icontains=query) | Q(interface_status__icontains=query) | Q(ip_address__icontains=query)
        ),ShowVersion.objects.filter(
            Q(pyats_alias__icontains=query) | Q(bootflash__icontains=query) | Q(chassis__icontains=query) | Q(cpu__icontains=query) | Q(device_name__icontains=query) | Q(memory__icontains=query) | Q(model__icontains=query) | Q(processor_board_id__icontains=query) | Q(rp__icontains=query) | Q(slots__icontains=query) | Q(days__icontains=query) | Q(hours__icontains=query) | Q(minutes__icontains=query) | Q(seconds__icontains=query) | Q(name__icontains=query) | Q(os__icontains=query) | Q(reason__icontains=query) | Q(system_compile_time__icontains=query) | Q(system_image_file__icontains=query) | Q(system_version__icontains=query) | Q(chassis_sn__icontains=query) | Q(compiled_by__icontains=query) | Q(curr_config_register__icontains=query) | Q(image_id__icontains=query) | Q(image_type__icontains=query) | Q(label__icontains=query) | Q(license_level__icontains=query) | Q(license_type__icontains=query) | Q(non_volatile__icontains=query) | Q(physical__icontains=query) | Q(next_reload_license_level__icontains=query) | Q(platform__icontains=query) | Q(processor_type__icontains=query) | Q(returned_to_rom_by__icontains=query) | Q(rom__icontains=query) | Q(rtr_type__icontains=query) | Q(uptime__icontains=query) | Q(uptime_this_cp__icontains=query) | Q(version_short__icontains=query) | Q(xe_version__icontains=query) 
        )
        )

        return object_list

class SearchResultStateView(ListView):
    template_name = 'Search/Results/search_results_state.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = (Devices.objects.filter(
            Q(hostname__icontains=query) | Q(alias__icontains=query) | Q(device_type__icontains=query) | Q(os__icontains=query) | Q(username__icontains=query) | Q(password__icontains=query) | Q(protocol__icontains=query) | Q(ip_address__icontains=query) | Q(port__icontains=query) | Q(connection_timeout__icontains=query)
        ),LearnACL.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(acl__icontains=query) | Q(ace__icontains=query) | Q(permission__icontains=query) | Q(logging__icontains=query) | Q(source_network__icontains=query) | Q(destination_network__icontains=query) | Q(l3_protocol__icontains=query) | Q(l4_protocol__icontains=query) | Q(operator__icontains=query) | Q(port__icontains=query)
        ),LearnARP.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(interface__icontains=query) | Q(neighbor_ip__icontains=query) | Q(neighbor_mac__icontains=query) | Q(origin__icontains=query) | Q(local_proxy__icontains=query) | Q(proxy__icontains=query)
        ),LearnARPStatistics.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(entries_total__icontains=query) | Q(in_drops__icontains=query) | Q(in_replies_pkts__icontains=query) | Q(in_requests_pkts__icontains=query) | Q(incomplete_total__icontains=query) | Q(out_replies_pkts__icontains=query) | Q(out_requests_pkts__icontains=query)
        ),LearnBGPInstances.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(instance__icontains=query) | Q(bgp_id__icontains=query) | Q(protocol_state__icontains=query) | Q(nexthop_trigger_delay_critical__icontains=query) | Q(nexthop_trigger_delay_noncritical__icontains=query) | Q(nexthop_trigger_enabled__icontains=query) | Q(vrf__icontains=query) | Q(router_id__icontains=query) | Q(cluster_id__icontains=query) | Q(confederation_id__icontains=query) | Q(neighbor__icontains=query) | Q(version__icontains=query) | Q(hold_time__icontains=query) | Q(keep_alive_interval__icontains=query) | Q(local_as__icontains=query) | Q(remote_as__icontains=query) | Q(neighbor_counters_received_bytes_in_queue__icontains=query) | Q(neighbor_counters_received_capability__icontains=query) | Q(neighbor_counters_received_keepalives__icontains=query) | Q(neighbor_counters_received_notifications__icontains=query) | Q(neighbor_counters_received_opens__icontains=query) | Q(neighbor_counters_received_route_refresh__icontains=query) | Q(neighbor_counters_received_total__icontains=query) | Q(neighbor_counters_received_total_bytes__icontains=query) | Q(neighbor_counters_received_updates__icontains=query) | Q(neighbor_counters_sent_bytes_in_queue__icontains=query) | Q(neighbor_counters_sent_capability__icontains=query) | Q(neighbor_counters_sent_keepalives__icontains=query) | Q(neighbor_counters_sent_notifications__icontains=query) | Q(neighbor_counters_sent_opens__icontains=query) | Q(neighbor_counters_sent_route_refresh__icontains=query) | Q(neighbor_counters_sent_total__icontains=query) | Q(neighbor_counters_sent_total_bytes__icontains=query) | Q(neighbor_counters_sent_updates__icontains=query) | Q(last_reset__icontains=query) | Q(reset_reason__icontains=query)
        ),LearnBGPRoutesPerPeer.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(instance__icontains=query) | Q(vrf__icontains=query) | Q(neighbor__icontains=query) | Q(advertised__icontains=query) | Q(routes__icontains=query) | Q(remote_as__icontains=query)
        ),LearnBGPTables.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(instance__icontains=query) | Q(vrf__icontains=query) | Q(table_version__icontains=query) | Q(prefix__icontains=query) | Q(index__icontains=query) | Q(localpref__icontains=query) | Q(next_hop__icontains=query) | Q(origin_code__icontains=query) | Q(status_code__icontains=query) | Q(weight__icontains=query) 
        ),LearnInterface.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(interface__icontains=query) | Q(description__icontains=query) | Q(access_vlan__icontains=query) | Q(native_vlan__icontains=query) | Q(switchport_mode__icontains=query) | Q(interface_type__icontains=query) | Q(bandwidth__icontains=query) | Q(speed__icontains=query) | Q(duplex__icontains=query) | Q(mtu__icontains=query) | Q(mac_address__icontains=query) | Q(physical_address__icontains=query) | Q(ip_address__icontains=query) | Q(encapsulation__icontains=query)
        ),LearnPlatform.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(chassis__icontains=query) | Q(chassis_sn__icontains=query) | Q(image__icontains=query) | Q(installed_packages__icontains=query) | Q(rtr_type__icontains=query) | Q(version__icontains=query) 
        ),LearnPlatformSlots.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(slot__icontains=query) | Q(slot_name__icontains=query) | Q(slot_sn__icontains=query) | Q(slot_state__icontains=query) | Q(slot_redundancy_state__icontains=query) | Q(rp_boot_image__icontains=query)
        ),LearnPlatformVirtual.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(virtual_device_name__icontains=query) | Q(virtual_device_status__icontains=query) | Q(virtual_device_member__icontains=query) | Q(virtual_device_member_status__icontains=query) | Q(virtual_device_member_type__icontains=query)
        ),LearnVLAN.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(vlan__icontains=query) | Q(interfaces__icontains=query) | Q(mode__icontains=query) | Q(name__icontains=query) | Q(shutdown__icontains=query) | Q(state__icontains=query)
        ),LearnVRF.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(vrf__icontains=query) | Q(address_family_ipv4__icontains=query) | Q(address_family_ipv6__icontains=query) | Q(route_distinguisher__icontains=query)
        ),ShowInventory.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(part__icontains=query) | Q(description__icontains=query) | Q(pid__icontains=query) | Q(serial_number__icontains=query) 
        ),ShowIPIntBrief.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(interface__icontains=query) | Q(interface_status__icontains=query) | Q(ip_address__icontains=query)
        ),ShowVersion.objects.filter(
            Q(pyats_alias__icontains=query) | Q(bootflash__icontains=query) | Q(chassis__icontains=query) | Q(cpu__icontains=query) | Q(device_name__icontains=query) | Q(memory__icontains=query) | Q(model__icontains=query) | Q(processor_board_id__icontains=query) | Q(rp__icontains=query) | Q(slots__icontains=query) | Q(days__icontains=query) | Q(hours__icontains=query) | Q(minutes__icontains=query) | Q(seconds__icontains=query) | Q(name__icontains=query) | Q(os__icontains=query) | Q(reason__icontains=query) | Q(system_compile_time__icontains=query) | Q(system_image_file__icontains=query) | Q(system_version__icontains=query) | Q(chassis_sn__icontains=query) | Q(compiled_by__icontains=query) | Q(curr_config_register__icontains=query) | Q(image_id__icontains=query) | Q(image_type__icontains=query) | Q(label__icontains=query) | Q(license_level__icontains=query) | Q(license_type__icontains=query) | Q(non_volatile__icontains=query) | Q(physical__icontains=query) | Q(next_reload_license_level__icontains=query) | Q(platform__icontains=query) | Q(processor_type__icontains=query) | Q(returned_to_rom_by__icontains=query) | Q(rom__icontains=query) | Q(rtr_type__icontains=query) | Q(uptime__icontains=query) | Q(uptime_this_cp__icontains=query) | Q(version_short__icontains=query) | Q(xe_version__icontains=query) 
        )
        )

        return object_list

class SearchResultConfigView(ListView):
    template_name = 'Search/Results/search_results_config.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = (LearnConfig.objects.filter(
            Q(pyats_alias__icontains=query) | Q(os__icontains=query) | Q(config__icontains=query)))
        inner_object_list = []
        for config in object_list:
            for key,value in config.config.items():
                if query in key:
                    inner_object_list.append({'pyats_alias': config.pyats_alias,key: value,'timestamp': config.timestamp})
                for value_item in value:
                    if query in value_item:
                        inner_object_list.append({'pyats_alias': config.pyats_alias,key: value,'timestamp': config.timestamp})
                    
        object_list = inner_object_list
        return object_list 