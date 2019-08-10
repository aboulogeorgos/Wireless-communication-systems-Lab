#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: AM TX
# Author: Alexandros-Apostolos A. Boulogeorgos
# Description: A simple AM transmitter
# Generated: Sat Aug 10 06:57:48 2019
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

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class am_tx(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="AM TX")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000
        self.ka = ka = 1
        self.fm = fm = 4000
        self.fc = fc = 32000

        ##################################################
        # Blocks
        ##################################################
        self.notebook = self.notebook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "tab1")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "tab2")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "tab3")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "tab4")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "tab5")
        self.Add(self.notebook)
        _ka_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ka_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ka_sizer,
        	value=self.ka,
        	callback=self.set_ka,
        	label='ka',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._ka_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ka_sizer,
        	value=self.ka,
        	callback=self.set_ka,
        	minimum=0,
        	maximum=2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_ka_sizer)
        _fm_sizer = wx.BoxSizer(wx.VERTICAL)
        self._fm_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_fm_sizer,
        	value=self.fm,
        	callback=self.set_fm,
        	label='fm',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._fm_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_fm_sizer,
        	value=self.fm,
        	callback=self.set_fm,
        	minimum=0,
        	maximum=10000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_fm_sizer)
        _fc_sizer = wx.BoxSizer(wx.VERTICAL)
        self._fc_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_fc_sizer,
        	value=self.fc,
        	callback=self.set_fc,
        	label='fc',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._fc_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_fc_sizer,
        	value=self.fc,
        	callback=self.set_fc,
        	minimum=16000,
        	maximum=samp_rate/2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_fc_sizer)
        self.wxgui_scopesink2_2_1_0 = scopesink2.scope_sink_f(
        	self.notebook.GetPage(2).GetWin(),
        	title='Message Scope Plot',
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
        self.notebook.GetPage(2).Add(self.wxgui_scopesink2_2_1_0.win)
        self.wxgui_scopesink2_2_1 = scopesink2.scope_sink_f(
        	self.notebook.GetPage(0).GetWin(),
        	title='Message Scope Plot',
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
        self.notebook.GetPage(0).Add(self.wxgui_scopesink2_2_1.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.notebook.GetPage(3).GetWin(),
        	title='AM_Bandpass Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook.GetPage(3).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0_0_0 = fftsink2.fft_sink_f(
        	self.notebook.GetPage(2).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Message FFT Plot',
        	peak_hold=False,
        )
        self.notebook.GetPage(2).Add(self.wxgui_fftsink2_0_0_0.win)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_f(
        	self.notebook.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Message FFT Plot',
        	peak_hold=False,
        )
        self.notebook.GetPage(1).Add(self.wxgui_fftsink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.notebook.GetPage(4).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='AM_Bandpass FFT Plot',
        	peak_hold=False,
        )
        self.notebook.GetPage(4).Add(self.wxgui_fftsink2_0.win)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_2 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((ka, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_1_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fc, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fm, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_1, 0))    
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blocks_multiply_xx_2, 1))    
        self.connect((self.analog_sig_source_x_1_1, 0), (self.wxgui_fftsink2_0_0_0, 0))    
        self.connect((self.analog_sig_source_x_1_1, 0), (self.wxgui_scopesink2_2_1_0, 0))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_2, 0))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_xx_2, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.blocks_multiply_xx_2, 0), (self.wxgui_scopesink2_0, 1))    
        self.connect((self.blocks_throttle_1, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_throttle_1, 0), (self.wxgui_fftsink2_0_0, 0))    
        self.connect((self.blocks_throttle_1, 0), (self.wxgui_scopesink2_2_1, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_2_1_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_2_1.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_1_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_ka(self):
        return self.ka

    def set_ka(self, ka):
        self.ka = ka
        self._ka_slider.set_value(self.ka)
        self._ka_text_box.set_value(self.ka)
        self.blocks_multiply_const_vxx_0.set_k((self.ka, ))

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self._fm_slider.set_value(self.fm)
        self._fm_text_box.set_value(self.fm)
        self.analog_sig_source_x_0.set_frequency(self.fm)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self._fc_slider.set_value(self.fc)
        self._fc_text_box.set_value(self.fc)
        self.analog_sig_source_x_1_1.set_frequency(self.fc)


def main(top_block_cls=am_tx, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
