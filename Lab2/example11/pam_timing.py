#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: PAM Timing
# Author: Alexandros-Apostolos A. Boulogeorgos
# Generated: Sun Mar 15 11:55:00 2020
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

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import sip
import sys


class pam_timing(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "PAM Timing")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("PAM Timing")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "pam_timing")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.time_bw = time_bw = 0
        self.spb = spb = 4.2563
        self.sig_amp = sig_amp = 1
        self.samp_rate = samp_rate = 32000
        self.rolloff = rolloff = .35
        self.noise_amp = noise_amp = 0
        self.nfilts = nfilts = 32
        self.interpratio = interpratio = 1
        self.freq_offset = freq_offset = 0
        self.const = const = digital.qpsk_constellation()

        ##################################################
        # Blocks
        ##################################################
        self._time_bw_range = Range(0, .1, .001, 0, 200)
        self._time_bw_win = RangeWidget(self._time_bw_range, self.set_time_bw, 'Timing Loop BW', "counter_slider", float)
        self.top_grid_layout.addWidget(self._time_bw_win, 1,2,1,1)
        self.notebook = Qt.QTabWidget()
        self.notebook_widget_0 = Qt.QWidget()
        self.notebook_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.notebook_widget_0)
        self.notebook_grid_layout_0 = Qt.QGridLayout()
        self.notebook_layout_0.addLayout(self.notebook_grid_layout_0)
        self.notebook.addTab(self.notebook_widget_0, 'Error')
        self.notebook_widget_1 = Qt.QWidget()
        self.notebook_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.notebook_widget_1)
        self.notebook_grid_layout_1 = Qt.QGridLayout()
        self.notebook_layout_1.addLayout(self.notebook_grid_layout_1)
        self.notebook.addTab(self.notebook_widget_1, 'Phase')
        self.notebook_widget_2 = Qt.QWidget()
        self.notebook_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.notebook_widget_2)
        self.notebook_grid_layout_2 = Qt.QGridLayout()
        self.notebook_layout_2.addLayout(self.notebook_grid_layout_2)
        self.notebook.addTab(self.notebook_widget_2, 'Freq')
        self.notebook_widget_3 = Qt.QWidget()
        self.notebook_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.notebook_widget_3)
        self.notebook_grid_layout_3 = Qt.QGridLayout()
        self.notebook_layout_3.addLayout(self.notebook_grid_layout_3)
        self.notebook.addTab(self.notebook_widget_3, 'Resampled Signal')
        self.top_grid_layout.addWidget(self.notebook, 1,1,5,1)
        self._noise_amp_range = Range(0, 1, .001, 0, 200)
        self._noise_amp_win = RangeWidget(self._noise_amp_range, self.set_noise_amp, 'Channel Noise', "counter_slider", float)
        self.top_grid_layout.addWidget(self._noise_amp_win, 3,2,1,1)
        self._interpratio_range = Range(.99, 1.01, 0.0001, 1, 200)
        self._interpratio_win = RangeWidget(self._interpratio_range, self.set_interpratio, 'Timing Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._interpratio_win, 2,2,1,1)
        self._freq_offset_range = Range(-.5, .5, .01, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, 'Frequency Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_offset_win, 4,2,1,1)
        self.qtgui_time_sink_x_1_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	'Phase', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1_1.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1_1.enable_grid(False)
        self.qtgui_time_sink_x_1_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1_1.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1.pyqwidget(), Qt.QWidget)
        self.notebook_layout_1.addWidget(self._qtgui_time_sink_x_1_1_win)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	'Rate', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.notebook_layout_2.addWidget(self._qtgui_time_sink_x_1_0_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	'Error', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.notebook_layout_0.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	'Scope Plot', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	'Error', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.notebook_layout_3.addWidget(self._qtgui_time_sink_x_0_win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  spb,
                  taps=(firdes.root_raised_cosine(nfilts, nfilts, 1.0, rolloff, 44*nfilts)),
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        	
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(spb, time_bw, (firdes.root_raised_cosine(nfilts, nfilts*spb, 1.0, rolloff, 44*nfilts)), nfilts, 16, 1.5, 1)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((const.points()), 1)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise_amp,
        	frequency_offset=freq_offset,
        	epsilon=interpratio,
        	taps=(1.0, ),
        	noise_seed=42,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((sig_amp, ))
        self.analog_random_source_x = blocks.vector_source_b(map(int, numpy.random.randint(0, const.arity(), 10000000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x, 0), (self.digital_chunks_to_symbols_xx, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.pfb_arb_resampler_xxx_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 1), (self.qtgui_time_sink_x_1, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 2), (self.qtgui_time_sink_x_1_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 3), (self.qtgui_time_sink_x_1_1, 0))    
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "pam_timing")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_time_bw(self):
        return self.time_bw

    def set_time_bw(self, time_bw):
        self.time_bw = time_bw
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.time_bw)

    def get_spb(self):
        return self.spb

    def set_spb(self, spb):
        self.spb = spb
        self.pfb_arb_resampler_xxx_0.set_rate(self.spb)
        self.digital_pfb_clock_sync_xxx_0.update_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts*self.spb, 1.0, self.rolloff, 44*self.nfilts)))

    def get_sig_amp(self):
        return self.sig_amp

    def set_sig_amp(self, sig_amp):
        self.sig_amp = sig_amp
        self.blocks_multiply_const_vxx_0.set_k((self.sig_amp, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.pfb_arb_resampler_xxx_0.set_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.rolloff, 44*self.nfilts)))
        self.digital_pfb_clock_sync_xxx_0.update_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts*self.spb, 1.0, self.rolloff, 44*self.nfilts)))

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.channels_channel_model_0.set_noise_voltage(self.noise_amp)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.pfb_arb_resampler_xxx_0.set_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.rolloff, 44*self.nfilts)))
        self.digital_pfb_clock_sync_xxx_0.update_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts*self.spb, 1.0, self.rolloff, 44*self.nfilts)))

    def get_interpratio(self):
        return self.interpratio

    def set_interpratio(self, interpratio):
        self.interpratio = interpratio
        self.channels_channel_model_0.set_timing_offset(self.interpratio)

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const


def main(top_block_cls=pam_timing, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
