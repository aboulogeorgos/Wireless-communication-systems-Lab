#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fast Fading Channel
# Author: Alexandros-Apostolos A. Boulogeorgos
# Description: Channel type: Rayleigh
# Generated: Mon Aug 12 10:06:23 2019
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
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys


class fastFadingChannel(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Fast Fading Channel")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fast Fading Channel")
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

        self.settings = Qt.QSettings("GNU Radio", "fastFadingChannel")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.trig_umts_ped_b = trig_umts_ped_b = 1.5
        self.trig_umts_ped_a = trig_umts_ped_a = 0.5
        self.trig_del_umts_ped_b = trig_del_umts_ped_b = 0.000001
        self.trig_del_umts_ped_a = trig_del_umts_ped_a = 0.000001
        self.trig_del_ca0 = trig_del_ca0 = 2e-9
        self.trig_ca0 = trig_ca0 = 2.8
        self.samp_rate_umts_ped_b = samp_rate_umts_ped_b = 7.68e6
        self.samp_rate_umts_ped_a = samp_rate_umts_ped_a = 7.68e6
        self.samp_rate_ca0 = samp_rate_ca0 = 4e9
        self.pdp_times_umts_ped_b = pdp_times_umts_ped_b = [0, 1.536, 6.144, 9.216, 17.664, 28.416]
        self.pdp_times_umts_ped_a = pdp_times_umts_ped_a = [0, 0.8448, 1.4592, 3.1488]
        self.pdp_times_ca0 = pdp_times_ca0 = [-0.25, -0.125, 0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0, 1.125, 1.25, 1.5, 1.625, 1.75, 1.875, 2.0, 2.125, 2.25, 2.375, 2.5, 2.75, 2.875, 3.0, 3.125, 3.25, 3.375, 3.5, 3.625, 3.75, 3.875, 4.0, 4.125, 4.25, 4.375, 4.5, 4.625, 4.75, 5.125, 5.25, 5.5, 5.625, 5.75, 6.0, 6.375, 6.5, 6.625, 6.75, 6.875, 7.25, 8.0, 8.125, 8.5, 8.625, 8.75, 8.875, 9.125, 9.25, 9.375, 9.5, 9.875, 10.0, 10.75, 10.875, 11.0, 11.125, 13.125, 13.25]
        self.pdp_mags_umts_ped_b = pdp_mags_umts_ped_b = [1, 0.9139311853, 0.6126263942, 0.4493289641, 0.4584060113, 0.0916296839]
        self.pdp_mags_umts_ped_a = pdp_mags_umts_ped_a = [1, 0.3790830381, 0.1466069621, 0.1022842067]
        self.pdp_mags_ca0 = pdp_mags_ca0 = [0.16529889, 0.46954084, 0.58274825, 0.24561255, 0.50459457, 0.69767633, 1.0, 0.77724474, 0.48675226, 0.46954084, 0.21267289, 0.19090106, 0.31600413, 0.45293801, 0.8057353, 0.64920938, 0.50459457, 0.1978987, 0.35204369, 0.54226525, 0.31600413, 0.15945397, 0.2204686, 0.35204369, 0.37832563, 0.37832563, 0.36494815, 0.2204686, 0.17763933, 0.45293801, 0.52309091, 0.52309091, 0.46954084, 0.35204369, 0.40656966, 0.25461568, 0.23692776, 0.32758753, 0.1978987, 0.21267289, 0.2204686, 0.19090106, 0.24561255, 0.17135806, 0.21267289, 0.16529889, 0.2204686, 0.30483032, 0.33959553, 0.18415085, 0.18415085, 0.22855006, 0.2940516, 0.19090106, 0.17135806, 0.18415085, 0.1978987, 0.17763933, 0.15945397, 0.26394884, 0.24561255, 0.21267289, 0.19090106, 0.17763933, 0.2204686, 0.21267289, 0.17135806, 0.17135806, 0.16529889]
        self.model = model = 2
        self.trig_del = trig_del = [trig_del_ca0, trig_del_umts_ped_a, trig_del_umts_ped_b][model]
        self.trig = trig = [trig_ca0, trig_umts_ped_a, trig_umts_ped_b][model]
        self.timing = timing = 1.000
        self.samp_rate = samp_rate = [samp_rate_ca0, samp_rate_umts_ped_a, samp_rate_umts_ped_b][model]
        self.pdp_times = pdp_times = [pdp_times_ca0, pdp_times_umts_ped_a, pdp_times_umts_ped_b][model]
        self.pdp_mags = pdp_mags = [pdp_mags_ca0, pdp_mags_umts_ped_a, pdp_mags_umts_ped_b][model]
        self.noise = noise = 0.01
        self.freq = freq = 0.0

        ##################################################
        # Blocks
        ##################################################
        self._timing_range = Range(0.999, 1.001, 0.0001, 1.000, 200)
        self._timing_win = RangeWidget(self._timing_range, self.set_timing, 'Timing Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._timing_win, 3,0,1,1)
        self._noise_range = Range(0, 1, 0.01, 0.01, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, 'Noise Voltage', "counter_slider", float)
        self.top_grid_layout.addWidget(self._noise_win, 2,0,1,1)
        self._freq_range = Range(-1, 1, 0.01, 0.0, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Frequency Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_win, 2,1,1,1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'QT GUI Plot', #name
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
        colors = [0, 0, 0, 0, 0,
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
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 0,1,1,1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	30, #size
        	samp_rate, #samp_rate
        	'QT GUI Plot', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, trig, trig_del, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ['PDP', '', '', '', '',
                  '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [2, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [0.75, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 1,1,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	'QT GUI Plot', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-3, 3)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['Re{Impulse}', '', '', '', '',
                  '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 1,0,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'QT GUI Plot', #name
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
        widths = [2, 1, 1, 1, 1,
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,1)
        self.channels_selective_fading_model_0 = channels.selective_fading_model( 8, 10.0/samp_rate, False, 4.0, 0, (pdp_times), (pdp_mags), 8 )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=freq,
        	epsilon=timing,
        	taps=(1.0, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_vector_source_x_0 = blocks.vector_source_c(511*[0,] + [1,] + 512*[0,], True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.channels_selective_fading_model_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.channels_selective_fading_model_0, 0), (self.channels_channel_model_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fastFadingChannel")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_trig_umts_ped_b(self):
        return self.trig_umts_ped_b

    def set_trig_umts_ped_b(self, trig_umts_ped_b):
        self.trig_umts_ped_b = trig_umts_ped_b
        self.set_trig([self.trig_ca0, self.trig_umts_ped_a, self.trig_umts_ped_b][self.model])

    def get_trig_umts_ped_a(self):
        return self.trig_umts_ped_a

    def set_trig_umts_ped_a(self, trig_umts_ped_a):
        self.trig_umts_ped_a = trig_umts_ped_a
        self.set_trig([self.trig_ca0, self.trig_umts_ped_a, self.trig_umts_ped_b][self.model])

    def get_trig_del_umts_ped_b(self):
        return self.trig_del_umts_ped_b

    def set_trig_del_umts_ped_b(self, trig_del_umts_ped_b):
        self.trig_del_umts_ped_b = trig_del_umts_ped_b
        self.set_trig_del([self.trig_del_ca0, self.trig_del_umts_ped_a, self.trig_del_umts_ped_b][self.model])

    def get_trig_del_umts_ped_a(self):
        return self.trig_del_umts_ped_a

    def set_trig_del_umts_ped_a(self, trig_del_umts_ped_a):
        self.trig_del_umts_ped_a = trig_del_umts_ped_a
        self.set_trig_del([self.trig_del_ca0, self.trig_del_umts_ped_a, self.trig_del_umts_ped_b][self.model])

    def get_trig_del_ca0(self):
        return self.trig_del_ca0

    def set_trig_del_ca0(self, trig_del_ca0):
        self.trig_del_ca0 = trig_del_ca0
        self.set_trig_del([self.trig_del_ca0, self.trig_del_umts_ped_a, self.trig_del_umts_ped_b][self.model])

    def get_trig_ca0(self):
        return self.trig_ca0

    def set_trig_ca0(self, trig_ca0):
        self.trig_ca0 = trig_ca0
        self.set_trig([self.trig_ca0, self.trig_umts_ped_a, self.trig_umts_ped_b][self.model])

    def get_samp_rate_umts_ped_b(self):
        return self.samp_rate_umts_ped_b

    def set_samp_rate_umts_ped_b(self, samp_rate_umts_ped_b):
        self.samp_rate_umts_ped_b = samp_rate_umts_ped_b
        self.set_samp_rate([self.samp_rate_ca0, self.samp_rate_umts_ped_a, self.samp_rate_umts_ped_b][self.model])

    def get_samp_rate_umts_ped_a(self):
        return self.samp_rate_umts_ped_a

    def set_samp_rate_umts_ped_a(self, samp_rate_umts_ped_a):
        self.samp_rate_umts_ped_a = samp_rate_umts_ped_a
        self.set_samp_rate([self.samp_rate_ca0, self.samp_rate_umts_ped_a, self.samp_rate_umts_ped_b][self.model])

    def get_samp_rate_ca0(self):
        return self.samp_rate_ca0

    def set_samp_rate_ca0(self, samp_rate_ca0):
        self.samp_rate_ca0 = samp_rate_ca0
        self.set_samp_rate([self.samp_rate_ca0, self.samp_rate_umts_ped_a, self.samp_rate_umts_ped_b][self.model])

    def get_pdp_times_umts_ped_b(self):
        return self.pdp_times_umts_ped_b

    def set_pdp_times_umts_ped_b(self, pdp_times_umts_ped_b):
        self.pdp_times_umts_ped_b = pdp_times_umts_ped_b
        self.set_pdp_times([self.pdp_times_ca0, self.pdp_times_umts_ped_a, self.pdp_times_umts_ped_b][self.model])

    def get_pdp_times_umts_ped_a(self):
        return self.pdp_times_umts_ped_a

    def set_pdp_times_umts_ped_a(self, pdp_times_umts_ped_a):
        self.pdp_times_umts_ped_a = pdp_times_umts_ped_a
        self.set_pdp_times([self.pdp_times_ca0, self.pdp_times_umts_ped_a, self.pdp_times_umts_ped_b][self.model])

    def get_pdp_times_ca0(self):
        return self.pdp_times_ca0

    def set_pdp_times_ca0(self, pdp_times_ca0):
        self.pdp_times_ca0 = pdp_times_ca0
        self.set_pdp_times([self.pdp_times_ca0, self.pdp_times_umts_ped_a, self.pdp_times_umts_ped_b][self.model])

    def get_pdp_mags_umts_ped_b(self):
        return self.pdp_mags_umts_ped_b

    def set_pdp_mags_umts_ped_b(self, pdp_mags_umts_ped_b):
        self.pdp_mags_umts_ped_b = pdp_mags_umts_ped_b
        self.set_pdp_mags([self.pdp_mags_ca0, self.pdp_mags_umts_ped_a, self.pdp_mags_umts_ped_b][self.model])

    def get_pdp_mags_umts_ped_a(self):
        return self.pdp_mags_umts_ped_a

    def set_pdp_mags_umts_ped_a(self, pdp_mags_umts_ped_a):
        self.pdp_mags_umts_ped_a = pdp_mags_umts_ped_a
        self.set_pdp_mags([self.pdp_mags_ca0, self.pdp_mags_umts_ped_a, self.pdp_mags_umts_ped_b][self.model])

    def get_pdp_mags_ca0(self):
        return self.pdp_mags_ca0

    def set_pdp_mags_ca0(self, pdp_mags_ca0):
        self.pdp_mags_ca0 = pdp_mags_ca0
        self.set_pdp_mags([self.pdp_mags_ca0, self.pdp_mags_umts_ped_a, self.pdp_mags_umts_ped_b][self.model])

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model
        self.set_trig_del([self.trig_del_ca0, self.trig_del_umts_ped_a, self.trig_del_umts_ped_b][self.model])
        self.set_trig([self.trig_ca0, self.trig_umts_ped_a, self.trig_umts_ped_b][self.model])
        self.set_samp_rate([self.samp_rate_ca0, self.samp_rate_umts_ped_a, self.samp_rate_umts_ped_b][self.model])
        self.set_pdp_times([self.pdp_times_ca0, self.pdp_times_umts_ped_a, self.pdp_times_umts_ped_b][self.model])
        self.set_pdp_mags([self.pdp_mags_ca0, self.pdp_mags_umts_ped_a, self.pdp_mags_umts_ped_b][self.model])

    def get_trig_del(self):
        return self.trig_del

    def set_trig_del(self, trig_del):
        self.trig_del = trig_del
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.trig, self.trig_del, 0, "")

    def get_trig(self):
        return self.trig

    def set_trig(self, trig):
        self.trig = trig
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.trig, self.trig_del, 0, "")

    def get_timing(self):
        return self.timing

    def set_timing(self, timing):
        self.timing = timing
        self.channels_channel_model_0.set_timing_offset(self.timing)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.channels_selective_fading_model_0.set_fDTs(10.0/self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_pdp_times(self):
        return self.pdp_times

    def set_pdp_times(self, pdp_times):
        self.pdp_times = pdp_times

    def get_pdp_mags(self):
        return self.pdp_mags

    def set_pdp_mags(self, pdp_mags):
        self.pdp_mags = pdp_mags

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.channels_channel_model_0.set_frequency_offset(self.freq)


def main(top_block_cls=fastFadingChannel, options=None):

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
