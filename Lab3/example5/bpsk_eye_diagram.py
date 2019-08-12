#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BSPK eye diagram
# Author: Alexandros-Apostolos A. Boulogeorgos
# Generated: Mon Aug 12 16:13:05 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class bpsk_eye_diagram(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="BSPK eye diagram")

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.samp_rate = samp_rate = 100000
        
        self.pam = pam = digital.constellation_calcdist(([-1, 1]), ([0, 1]), 4, 1).base()
        
        self.noise_voltage = noise_voltage = 0

        ##################################################
        # Blocks
        ##################################################
        _noise_voltage_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noise_voltage_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_noise_voltage_sizer,
        	value=self.noise_voltage,
        	callback=self.set_noise_voltage,
        	label='Noise voltage',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noise_voltage_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_noise_voltage_sizer,
        	value=self.noise_voltage,
        	callback=self.set_noise_voltage,
        	minimum=0,
        	maximum=100,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_noise_voltage_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, sps, 1.0, 0.35, 88))
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=pam,
          differential=False,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise_voltage,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0 , ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.digital_constellation_modulator_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.root_raised_cosine_filter_0, 0))    
        self.connect((self.digital_constellation_modulator_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_complex_to_real_0, 0))    

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.sps, 1.0, 0.35, 88))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_pam(self):
        return self.pam

    def set_pam(self, pam):
        self.pam = pam

    def get_noise_voltage(self):
        return self.noise_voltage

    def set_noise_voltage(self, noise_voltage):
        self.noise_voltage = noise_voltage
        self._noise_voltage_slider.set_value(self.noise_voltage)
        self._noise_voltage_text_box.set_value(self.noise_voltage)
        self.channels_channel_model_0.set_noise_voltage(self.noise_voltage)


def main(top_block_cls=bpsk_eye_diagram, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
