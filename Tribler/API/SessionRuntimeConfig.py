# Written by Arno Bakker 
# see LICENSE.txt for license information

import triblerAPI

class SessionRuntimeConfig(triblerAPI.SessionConfigInterface):
    
    # triblerAPI.SessionConfigInterface
    #
    # Use these to change the session config at runtime.
    #
    def set_state_dir(self,statedir):
        raise OperationNotPossibleAtRuntimeExeption()
    
    def get_state_dir(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_state_dir(self)
        finally:
            self.sesslock.release()
    
    def set_permid(self,keypair):
        raise OperationNotPossibleAtRuntimeExeption()
        
    def set_listen_port(self,port):
        raise OperationNotPossibleAtRuntimeExeption()

    def get_listen_port(self):
        # To protect self.sessconfig
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_listen_port(self)
        finally:
            self.sesslock.release()
        
    def get_video_analyser_path(self):
        # To protect self.sessconfig
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_video_analyser_path(self)
        finally:
            self.sesslock.release()

    def set_tracker_ip(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_ip(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_ip(self)
        finally:
            self.sesslock.release()

    def set_bind_to_address(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_bind_to_address(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_bind(self)
        finally:
            self.sesslock.release()

    def set_upnp_mode(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_upnp_mode(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_upnp_nat_access(self)
        finally:
            self.sesslock.release()

    def set_autoclose_timeout(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_autoclose_timeout(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_timeout(self)
        finally:
            self.sesslock.release()

    def set_autoclose_check_interval(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_autoclose_check_interval(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_timeout_check_interval(self)
        finally:
            self.sesslock.release()

    def set_megacache(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_megacache(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_cache(self)
        finally:
            self.sesslock.release()

    def set_overlay(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_overlay(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_overlay(self)
        finally:
            self.sesslock.release()

    def set_buddycast(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_buddycast(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_buddycast(self)
        finally:
            self.sesslock.release()

    def set_start_recommender(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_start_recommender(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_start_recommender(self)
        finally:
            self.sesslock.release()

    def set_download_help(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_download_help(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_download_help(self)
        finally:
            self.sesslock.release()

    def set_torrent_collecting(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_torrent_collecting(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_torrent_collecting(self)
        finally:
            self.sesslock.release()

    def set_superpeer(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_superpeer(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_superpeer(self)
        finally:
            self.sesslock.release()

    def set_overlay_log(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_overlay_log(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_overlay_log(self)
        finally:
            self.sesslock.release()

    def set_buddycast_interval(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_buddycast_interval(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_buddycast_interval(self)
        finally:
            self.sesslock.release()

    def set_max_torrents(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_max_torrents(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_max_torrents(self)
        finally:
            self.sesslock.release()

    def set_max_peers(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_max_peers(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_max_peers(self)
        finally:
            self.sesslock.release()

    def set_torrent_collecting_rate(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_torrent_collecting_rate(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_torrent_collecting_rate(self)
        finally:
            self.sesslock.release()

    def set_torrent_checking(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_torrent_checking(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_torrent_checking(self)
        finally:
            self.sesslock.release()

    def set_torrent_checking_period(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_torrent_checking_period(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_torrent_checking_period(self)
        finally:
            self.sesslock.release()

    def set_dialback(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_dialback(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_dialback(self)
        finally:
            self.sesslock.release()

    def set_dialback_active(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_dialback_active(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_dialback_active(self)
        finally:
            self.sesslock.release()

    def set_dialback_trust_superpeers(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_dialback_trust_superpeers(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_dialback_trust_superpeers(self)
        finally:
            self.sesslock.release()

    def set_dialback_interval(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_dialback_interval(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_dialback_interval(self)
        finally:
            self.sesslock.release()

    def set_socnet(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_socnet(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_socnet(self)
        finally:
            self.sesslock.release()

    def set_rquery(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_rquery(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_rquery(self)
        finally:
            self.sesslock.release()

    def set_stop_collecting_threshold(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_stop_collecting_threshold(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_stop_collecting_threshold(self)
        finally:
            self.sesslock.release()

    def set_internaltracker(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_internaltracker(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_internaltracker(self)
        finally:
            self.sesslock.release()

    def set_nickname(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_nickname(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_nickname(self)
        finally:
            self.sesslock.release()

    def set_videoplayerpath(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_videoplayerpath(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_videoplayerpath(self)
        finally:
            self.sesslock.release()

    def set_tracker_dfile(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_dfile(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_dfile(self)
        finally:
            self.sesslock.release()

    def set_tracker_dfile_format(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_dfile_format(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_dfile_format(self)
        finally:
            self.sesslock.release()

    def set_tracker_socket_timeout(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_socket_timeout(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_socket_timeout(self)
        finally:
            self.sesslock.release()

    def set_tracker_save_dfile_interval(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_save_dfile_interval(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_save_dfile_interval(self)
        finally:
            self.sesslock.release()

    def set_tracker_timeout_downloaders_interval(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_timeout_downloaders_interval(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_timeout_downloaders_interval(self)
        finally:
            self.sesslock.release()

    def set_tracker_reannounce_interval(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_reannounce_interval(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_reannounce_interval(self)
        finally:
            self.sesslock.release()

    def set_tracker_response_size(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_response_size(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_response_size(self)
        finally:
            self.sesslock.release()

    def set_tracker_timeout_check_interval(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_timeout_check_interval(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_timeout_check_interval(self)
        finally:
            self.sesslock.release()

    def set_tracker_nat_check(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_nat_check(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_nat_check(self)
        finally:
            self.sesslock.release()

    def set_tracker_log_nat_checks(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_log_nat_checks(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_log_nat_checks(self)
        finally:
            self.sesslock.release()

    def set_tracker_min_time_between_log_flushes(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_min_time_between_log_flushes(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_min_time_between_log_flushes(self)
        finally:
            self.sesslock.release()

    def set_tracker_min_time_between_cache_refreshes(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_min_time_between_cache_refreshes(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_min_time_between_cache_refreshes(self)
        finally:
            self.sesslock.release()

    def set_tracker_allowed_dir(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_allowed_dir(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_allowed_dir(self)
        finally:
            self.sesslock.release()

    def set_tracker_allowed_list(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_allowed_list(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_allowed_list(self)
        finally:
            self.sesslock.release()

    def set_tracker_allowed_controls(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_allowed_controls(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_allowed_controls(self)
        finally:
            self.sesslock.release()

    def set_tracker_multitracker_enabled(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_multitracker_enabled(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_multitracker_enabled(self)
        finally:
            self.sesslock.release()

    def set_tracker_multitracker_allowed(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_multitracker_allowed(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_multitracker_allowed(self)
        finally:
            self.sesslock.release()

    def set_tracker_multitracker_reannounce_interval(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_multitracker_reannounce_interval(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_multitracker_reannounce_interval(self)
        finally:
            self.sesslock.release()

    def set_tracker_multitracker_maxpeers(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_multitracker_maxpeers(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_multitracker_maxpeers(self)
        finally:
            self.sesslock.release()

    def set_tracker_aggregate_forward(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_aggregate_forward(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_aggregate_forward(self)
        finally:
            self.sesslock.release()

    def set_tracker_aggregator(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_aggregator(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_aggregator(self)
        finally:
            self.sesslock.release()

    def set_tracker_hupmonitor(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_hupmonitor(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_hupmonitor(self)
        finally:
            self.sesslock.release()

    def set_tracker_http_timeout(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_http_timeout(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_http_timeout(self)
        finally:
            self.sesslock.release()

    def set_tracker_parse_dir_interval(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_parse_dir_interval(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_parse_dir_interval(self)
        finally:
            self.sesslock.release()

    def set_tracker_show_infopage(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_show_infopage(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_show_infopage(self)
        finally:
            self.sesslock.release()

    def set_tracker_infopage_redirect(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_infopage_redirect(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_infopage_redirect(self)
        finally:
            self.sesslock.release()

    def set_tracker_show_names(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_show_names(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_show_names(self)
        finally:
            self.sesslock.release()

    def set_tracker_favicon(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_favicon(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_favicon(self)
        finally:
            self.sesslock.release()

    def set_tracker_allowed_ips(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_allowed_ips(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_allowed_ips(self)
        finally:
            self.sesslock.release()

    def set_tracker_banned_ips(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_banned_ips(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_banned_ips(self)
        finally:
            self.sesslock.release()

    def set_tracker_only_local_override_ip(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_only_local_override_ip(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_only_local_override_ip(self)
        finally:
            self.sesslock.release()

    def set_tracker_logfile(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_logfile(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_logfile(self)
        finally:
            self.sesslock.release()

    def set_tracker_allow_get(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_allow_get(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_allow_get(self)
        finally:
            self.sesslock.release()

    def set_tracker_keep_dead(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_keep_dead(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_keep_dead(self)
        finally:
            self.sesslock.release()

    def set_tracker_scrape_allowed(self,value):
        raise triblerAPI.OperationNotPossibleAtRuntimeException()

    def get_tracker_scrape_allowed(self):
        self.sesslock.acquire()
        try:
            return triblerAPI.SessionConfigInterface.get_tracker_scrape_allowed(self)
        finally:
            self.sesslock.release()

