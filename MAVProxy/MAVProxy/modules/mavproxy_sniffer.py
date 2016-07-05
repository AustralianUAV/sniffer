#!/usr/bin/env python
'''
AUAV gas sensor module
Andrew Chapman
March 2016
'''

import sys, os, time
#from cuav.lib import cuav_util
from MAVProxy.modules.lib import mp_module

class SnifferModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(SnifferModule, self).__init__(mpstate, "sniffer", "gas sensing and control module")
        #self.gcs_location = None
        #self.last_bearing = 0
        #self.last_announce = 0
        self.add_command('sniffer', self.cmd_sniffer, "gas sensing control")

    def cmd_sniffer(self, args):
        '''xxx'''
        # if len(args) != 2:
        #     if self.gcs_location is None:
        #         print("GCS location not set")
        #     else:
        #         print("GCS location %s" % str(self.gcs_location))
        #     return
        #self.gcs_location = (float(args[0]), float(args[1]))

    def mavlink_packet(self, m):
        '''handle an incoming mavlink packet'''
        if m.get_type() == 'GLOBAL_POSITION_INT':
            #(gcs_lat, gcs_lon) = self.gcs_location
            #bearing = cuav_util.gps_bearing(gcs_lat, gcs_lon, m.lat, m.lon)
            #print("GPS packet: %f,%f", m.lat, m.lon)
            #print("sniffer: %.2f %.2f %.2f\n" % (m.roll, m.pitch, m.yaw))
            alt = m.relative_alt * 1.0e-3
            print("sniffer: altitude is %f" % alt)
            if alt > 60:
                self.master.set_mode("RTL")


def init(mpstate):
    '''initialise module'''
    return SnifferModule(mpstate)
