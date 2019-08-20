#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: OFDM in the presence of fast fading, channel and hardware impairments
# Author: Alexandros-Apostolos A. Boulogeorgos
# Generated: Mon Aug 19 15:39:38 2019
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
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import sip
import sys


class ofdm_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "OFDM in the presence of fast fading, channel and hardware impairments")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("OFDM in the presence of fast fading, channel and hardware impairments")
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

        self.settings = Qt.QSettings("GNU Radio", "ofdm_simulation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.timing = timing = 1.0001
        self.samp_rate = samp_rate = 7.68e6
        self.q_offset = q_offset = 0
        self.phase_noise = phase_noise = 0
        self.packet_len = packet_len = 50
        self.noise = noise = 1.2
        self.len_tag_key = len_tag_key = "packet_len"
        self.iq_ph = iq_ph = 0
        self.iq_mag = iq_mag = 0
        self.i_offset = i_offset = 0
        self.freq = freq = 0.01
        self.fft_len = fft_len = 128
        self.dist3 = dist3 = 0
        self.dist2 = dist2 = 0

        ##################################################
        # Blocks
        ##################################################
        self._timing_range = Range(0.999, 1.001, 0.0001, 1.0001, 200)
        self._timing_win = RangeWidget(self._timing_range, self.set_timing, 'Timing Offset', "slider", float)
        self.top_grid_layout.addWidget(self._timing_win, 0,2,1,1)
        self._q_offset_range = Range(-1, 1, 0.01, 0, 200)
        self._q_offset_win = RangeWidget(self._q_offset_range, self.set_q_offset, 'Quadrature Offset', "slider", float)
        self.top_grid_layout.addWidget(self._q_offset_win, 1,3,1,1)
        self._phase_noise_range = Range(0, 40, 0.5, 0, 200)
        self._phase_noise_win = RangeWidget(self._phase_noise_range, self.set_phase_noise, 'Phase Noise', "slider", float)
        self.top_grid_layout.addWidget(self._phase_noise_win, 0,3,1,1)
        self._noise_range = Range(0, 2, 0.01, 1.2, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, 'Noise Voltage', "slider", float)
        self.top_grid_layout.addWidget(self._noise_win, 0,0,1,1)
        self._iq_ph_range = Range(-3.14, 3.14, 0.01, 0, 200)
        self._iq_ph_win = RangeWidget(self._iq_ph_range, self.set_iq_ph, 'IQ Phase Imbalance', "slider", float)
        self.top_grid_layout.addWidget(self._iq_ph_win, 1,1,1,1)
        self._iq_mag_range = Range(0, 1, 0.01, 0, 200)
        self._iq_mag_win = RangeWidget(self._iq_mag_range, self.set_iq_mag, 'IQ Mag. Imbalance', "slider", float)
        self.top_grid_layout.addWidget(self._iq_mag_win, 1,0,1,1)
        self._i_offset_range = Range(-1, 1, 0.01, 0, 200)
        self._i_offset_win = RangeWidget(self._i_offset_range, self.set_i_offset, 'Inphase Offset', "slider", float)
        self.top_grid_layout.addWidget(self._i_offset_win, 1,2,1,1)
        self._freq_range = Range(-1, 1, 0.01, 0.01, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Frequency Offset', "slider", float)
        self.top_grid_layout.addWidget(self._freq_win, 0,1,1,1)
        self._dist3_range = Range(0, 0.1, 0.0001, 0, 200)
        self._dist3_win = RangeWidget(self._dist3_range, self.set_dist3, 'Third Order Dist', "slider", float)
        self.top_grid_layout.addWidget(self._dist3_win, 2,1,1,1)
        self._dist2_range = Range(0, 0.1, 0.0001, 0, 200)
        self._dist2_win = RangeWidget(self._dist2_range, self.set_dist2, '2nd Order Dist.', "slider", float)
        self.top_grid_layout.addWidget(self._dist2_win, 2,0,1,1)
        self.qtgui_waterfall_sink_x_1_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"GT GUI Waterfall Sink- TX Output", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_1_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_1_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_1_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_waterfall_sink_x_1_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_1_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_1_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_1_0.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_1_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_1_0_win, 4,2,1,1)
        self.qtgui_waterfall_sink_x_1 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"GT GUI Waterfall Sink- TX Output", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_1.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_1.enable_grid(False)
        self.qtgui_waterfall_sink_x_1.enable_axis_labels(True)
        
        if not True:
          self.qtgui_waterfall_sink_x_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_1.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_1.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_1.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_1_win, 3,2,1,1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'QT GUI Waterfall Sink - RX RF front-end output', #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['Rx', '', '', '', '',
                  '', '', '', '', '']
        colors = [3, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 5,2,1,1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"QT GUI Time Sink - RX RF front-end output", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()
        
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
                    self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win, 5,0,1,1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"QT GUI Time Sink - Channel output", #name
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 4,0,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"QT GUI Time Sink - TX output", #name
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 3,0,1,1)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"QT GUI Frequency Sink - TX Output", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_win, 4,1,1,1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"QT GUI Frequency Sink - TX Output", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 3,1,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'QT GUI Frequenx=cy Sink - RX RF front-end output', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-80, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['Rx', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 5,1,1,1)
        self.digital_ofdm_tx_0 = digital.ofdm_tx(
        	  fft_len=fft_len, cp_len=fft_len/4,
        	  packet_length_tag_key=len_tag_key,
        	  bps_header=1,
        	  bps_payload=2,
        	  rolloff=0,
        	  debug_log=False,
        	  scramble_bits=False
        	 )
        self.digital_ofdm_rx_0 = digital.ofdm_rx(
        	  fft_len=fft_len, cp_len=fft_len/4,
        	  frame_length_tag_key='frame_'+"rx_len",
        	  packet_length_tag_key="rx_len",
        	  bps_header=1,
        	  bps_payload=2,
        	  debug_log=False,
        	  scramble_bits=False
        	 )
        self.channels_impairments_0 = channels.impairments(phase_noise, iq_mag, iq_ph, q_offset, i_offset, 0, dist2, dist3)
        self.channels_dynamic_channel_model_0 = channels.dynamic_channel_model( samp_rate, 0.01, 1e3, 0.01, 1e3, 8, 2.0, False, 4.0, (-0.0025, -0.00125, 0.0, 0.00125, 0.0025, 0.00375, 0.005, 0.00625, 0.0075, 0.00875, 0.01, 0.01125, 0.0125, 0.015, 0.01625, 0.0175, 0.01875, 0.02, 0.02125, 0.0225, 0.02375, 0.025, 0.0275, 0.02875, 0.03, 0.03125, 0.0325, 0.03375, 0.035, 0.03625, 0.0375, 0.03875, 0.04, 0.04125, 0.0425, 0.04375, 0.045, 0.04625, 0.0475, 0.05125, 0.0525, 0.055, 0.05625, 0.0575, 0.06, 0.06375, 0.065, 0.06625, 0.0675, 0.06875, 0.0725, 0.08, 0.08125, 0.085, 0.08625, 0.0875, 0.08875, 0.09125, 0.0925, 0.09375, 0.095, 0.09875, 0.1, 0.1075, 0.10875, 0.11, 0.11125, 0.13125, 0.1325), (0.16529889, 0.46954084, 0.58274825, 0.24561255, 0.50459457, 0.69767633, 1.0, 0.77724474, 0.48675226, 0.46954084, 0.21267289, 0.19090106, 0.31600413, 0.45293801, 0.8057353, 0.64920938, 0.50459457, 0.1978987, 0.35204369, 0.54226525, 0.31600413, 0.15945397, 0.2204686, 0.35204369, 0.37832563, 0.37832563, 0.36494815, 0.2204686, 0.17763933, 0.45293801, 0.52309091, 0.52309091, 0.46954084, 0.35204369, 0.40656966, 0.25461568, 0.23692776, 0.32758753, 0.1978987, 0.21267289, 0.2204686, 0.19090106, 0.24561255, 0.17135806, 0.21267289, 0.16529889, 0.2204686, 0.30483032, 0.33959553, 0.18415085, 0.18415085, 0.22855006, 0.2940516, 0.19090106, 0.17135806, 0.18415085, 0.1978987, 0.17763933, 0.15945397, 0.26394884, 0.24561255, 0.21267289, 0.19090106, 0.17763933, 0.2204686, 0.21267289, 0.17135806, 0.17135806, 0.16529889), 8, 1.0, 0 )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=freq,
        	epsilon=timing,
        	taps=(1.0, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, '', 'packet_num'); self.blocks_tag_debug_0.set_display(True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, packet_len, len_tag_key)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))    
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_ofdm_tx_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.channels_dynamic_channel_model_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.channels_impairments_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_freq_sink_x_1_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_waterfall_sink_x_1_0, 0))    
        self.connect((self.channels_dynamic_channel_model_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.channels_impairments_0, 0), (self.digital_ofdm_rx_0, 0))    
        self.connect((self.channels_impairments_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.channels_impairments_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))    
        self.connect((self.channels_impairments_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.digital_ofdm_rx_0, 0), (self.blocks_tag_debug_0, 0))    
        self.connect((self.digital_ofdm_tx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.digital_ofdm_tx_0, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.digital_ofdm_tx_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.digital_ofdm_tx_0, 0), (self.qtgui_waterfall_sink_x_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ofdm_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_timing(self):
        return self.timing

    def set_timing(self, timing):
        self.timing = timing
        self.channels_channel_model_0.set_timing_offset(self.timing)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.channels_dynamic_channel_model_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_q_offset(self):
        return self.q_offset

    def set_q_offset(self, q_offset):
        self.q_offset = q_offset
        self.channels_impairments_0.set_q_ofs(self.q_offset)

    def get_phase_noise(self):
        return self.phase_noise

    def set_phase_noise(self, phase_noise):
        self.phase_noise = phase_noise
        self.channels_impairments_0.set_phase_noise_mag(self.phase_noise)

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.packet_len)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.packet_len)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_len_tag_key(self):
        return self.len_tag_key

    def set_len_tag_key(self, len_tag_key):
        self.len_tag_key = len_tag_key

    def get_iq_ph(self):
        return self.iq_ph

    def set_iq_ph(self, iq_ph):
        self.iq_ph = iq_ph
        self.channels_impairments_0.set_phasebal(self.iq_ph)

    def get_iq_mag(self):
        return self.iq_mag

    def set_iq_mag(self, iq_mag):
        self.iq_mag = iq_mag
        self.channels_impairments_0.set_magbal(self.iq_mag)

    def get_i_offset(self):
        return self.i_offset

    def set_i_offset(self, i_offset):
        self.i_offset = i_offset
        self.channels_impairments_0.set_i_ofs(self.i_offset)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.channels_channel_model_0.set_frequency_offset(self.freq)

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len

    def get_dist3(self):
        return self.dist3

    def set_dist3(self, dist3):
        self.dist3 = dist3
        self.channels_impairments_0.set_beta(self.dist3)

    def get_dist2(self):
        return self.dist2

    def set_dist2(self, dist2):
        self.dist2 = dist2
        self.channels_impairments_0.set_gamma(self.dist2)


def main(top_block_cls=ofdm_simulation, options=None):

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
