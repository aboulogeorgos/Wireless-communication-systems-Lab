#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM_TX
# Author: Alexandros-Apostolos A. Boulogeorgos
# Generated: Tue Aug  6 14:33:36 2019
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


class fm_tx(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="FM_TX")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000
        self.fm = fm = 2000
        self.fc = fc = samp_rate/8
        self.beta = beta = 4

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
        	minimum=0,
        	maximum=samp_rate/2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_fc_sizer)
        _beta_sizer = wx.BoxSizer(wx.VERTICAL)
        self._beta_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_beta_sizer,
        	value=self.beta,
        	callback=self.set_beta,
        	label='beta',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._beta_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_beta_sizer,
        	value=self.beta,
        	callback=self.set_beta,
        	minimum=0,
        	maximum=4,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_beta_sizer)
        self.wxgui_scopesink2_2_0 = scopesink2.scope_sink_f(
        	self.notebook.GetPage(1).GetWin(),
        	title='FM Scop Plot',
        	sample_rate=samp_rate*1,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook.GetPage(1).Add(self.wxgui_scopesink2_2_0.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.notebook.GetPage(0).GetWin(),
        	title='Integrated Message',
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
        self.notebook.GetPage(0).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_f(
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
        	title='FM FFT Plot',
        	peak_hold=False,
        )
        self.notebook.GetPage(2).Add(self.wxgui_fftsink2_1.win)
        self.blocks_transcendental_1 = blocks.transcendental('sin', "float")
        self.blocks_transcendental_0 = blocks.transcendental('cos', "float")
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((beta, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_1_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fc, 1, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, fc, -1, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, fm, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.analog_sig_source_x_0_1, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_transcendental_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_transcendental_1, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_scopesink2_2_0, 0))    
        self.connect((self.blocks_transcendental_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_transcendental_1, 0), (self.blocks_multiply_xx_0_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_fc(self.samp_rate/8)
        self.wxgui_scopesink2_2_0.set_sample_rate(self.samp_rate*1)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self._fm_slider.set_value(self.fm)
        self._fm_text_box.set_value(self.fm)
        self.analog_sig_source_x_0_1.set_frequency(self.fm)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self._fc_slider.set_value(self.fc)
        self._fc_text_box.set_value(self.fc)
        self.analog_sig_source_x_1_0.set_frequency(self.fc)
        self.analog_sig_source_x_1.set_frequency(self.fc)

    def get_beta(self):
        return self.beta

    def set_beta(self, beta):
        self.beta = beta
        self._beta_slider.set_value(self.beta)
        self._beta_text_box.set_value(self.beta)
        self.blocks_multiply_const_vxx_1.set_k((self.beta, ))


def main(top_block_cls=fm_tx, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
