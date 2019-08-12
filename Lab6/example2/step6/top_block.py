#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Author: Alexandros-Apostolos A. Boulogeorgos
# Generated: Mon Aug 12 17:13:42 2019
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


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.samp_rate_umts_ped_b = samp_rate_umts_ped_b = 7.68e6
        self.samp_rate_umts_ped_a = samp_rate_umts_ped_a = 7.68e6
        self.samp_rate_ca0 = samp_rate_ca0 = 4e9
        self.pdp_times_umts_ped_b = pdp_times_umts_ped_b = [0, 1.536, 6.144, 9.216, 17.664, 28.416]
        self.pdp_times_umts_ped_a = pdp_times_umts_ped_a = [0, 0.8448, 1.4592, 3.1488]
        self.pdp_times_ca0 = pdp_times_ca0 = [-0.25, -0.125, 0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0, 1.125, 1.25, 1.5, 1.625, 1.75, 1.875, 2.0, 2.125, 2.25, 2.375, 2.5, 2.75, 2.875, 3.0, 3.125, 3.25, 3.375, 3.5, 3.625, 3.75, 3.875, 4.0, 4.125, 4.25, 4.375, 4.5, 4.625, 4.75, 5.125, 5.25, 5.5, 5.625, 5.75, 6.0, 6.375, 6.5, 6.625, 6.75, 6.875, 7.25, 8.0, 8.125, 8.5, 8.625, 8.75, 8.875, 9.125, 9.25, 9.375, 9.5, 9.875, 10.0, 10.75, 10.875, 11.0, 11.125, 13.125, 13.25]
        self.pdp_mags_umts_ped_b = pdp_mags_umts_ped_b = [1, 0.9139311853, 0.6126263942, 0.4493289641, 0.4584060113, 0.0916296839]
        self.pdp_mags_umts_ped_a = pdp_mags_umts_ped_a = [1, 0.3790830381, 0.1466069621, 0.1022842067]
        self.pdp_mags_ca0 = pdp_mags_ca0 = [0.16529889, 0.46954084, 0.58274825, 0.24561255, 0.50459457, 0.69767633, 1.0, 0.77724474, 0.48675226, 0.46954084, 0.21267289, 0.19090106, 0.31600413, 0.45293801, 0.8057353, 0.64920938, 0.50459457, 0.1978987, 0.35204369, 0.54226525, 0.31600413, 0.15945397, 0.2204686, 0.35204369, 0.37832563, 0.37832563, 0.36494815, 0.2204686, 0.17763933, 0.45293801, 0.52309091, 0.52309091, 0.46954084, 0.35204369, 0.40656966, 0.25461568, 0.23692776, 0.32758753, 0.1978987, 0.21267289, 0.2204686, 0.19090106, 0.24561255, 0.17135806, 0.21267289, 0.16529889, 0.2204686, 0.30483032, 0.33959553, 0.18415085, 0.18415085, 0.22855006, 0.2940516, 0.19090106, 0.17135806, 0.18415085, 0.1978987, 0.17763933, 0.15945397, 0.26394884, 0.24561255, 0.21267289, 0.19090106, 0.17763933, 0.2204686, 0.21267289, 0.17135806, 0.17135806, 0.16529889]
        self.nfilts = nfilts = 32
        self.model = model = 2
        self.timing_loop_bw = timing_loop_bw = 6.28/100.0
        self.samp_rate = samp_rate = [samp_rate_ca0, samp_rate_umts_ped_a, samp_rate_umts_ped_b][model]
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.phase_bw = phase_bw = 6.28/100.0
        self.pdp_times = pdp_times = [pdp_times_ca0, pdp_times_umts_ped_a, pdp_times_umts_ped_b][model]
        self.pdp_mags = pdp_mags = [pdp_mags_ca0, pdp_mags_umts_ped_a, pdp_mags_umts_ped_b][model]
        self.number_of_samples = number_of_samples = 1000
        self.noise_volt = noise_volt = 0.0001
        self.eq_gain = eq_gain = 0.01
        self.arity = arity = 4

        ##################################################
        # Blocks
        ##################################################
        self._timing_loop_bw_range = Range(0.0, 0.2, 0.01, 6.28/100.0, 200)
        self._timing_loop_bw_win = RangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, 'Time: BW', "slider", float)
        self.top_grid_layout.addWidget(self._timing_loop_bw_win, 0,1,1,1)
        self._phase_bw_range = Range(0.0, 1.0, 0.01, 6.28/100.0, 200)
        self._phase_bw_win = RangeWidget(self._phase_bw_range, self.set_phase_bw, 'Phase: Bandwidth', "slider", float)
        self.top_grid_layout.addWidget(self._phase_bw_win, 1,1,1,1)
        self._noise_volt_range = Range(0, 1, 0.01, 0.0001, 200)
        self._noise_volt_win = RangeWidget(self._noise_volt_range, self.set_noise_volt, 'Channel: Noise Voltage', "slider", float)
        self.top_grid_layout.addWidget(self._noise_volt_win, 0,0,1,1)
        self._eq_gain_range = Range(0.0, 0.1, 0.001, 0.01, 200)
        self._eq_gain_win = RangeWidget(self._eq_gain_range, self.set_eq_gain, 'Equalizer: rate', "slider", float)
        self.top_grid_layout.addWidget(self._eq_gain_win, 1,0,1,1)
        self.qtgui_const_sink_x_1_1 = qtgui.const_sink_c(
        	1024, #size
        	'After CMA equilizer @RX', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1_1.enable_grid(False)
        self.qtgui_const_sink_x_1_1.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_1_1.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_1_win, 3,1,1,1)
        self.qtgui_const_sink_x_1_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	'Channel output', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_1_0_0_0.enable_grid(False)
        self.qtgui_const_sink_x_1_0_0_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_1_0_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_0_0_0_win, 2,2,1,1)
        self.qtgui_const_sink_x_1_0_0 = qtgui.const_sink_c(
        	1024, #size
        	'After constant multiplication', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_1_0_0.enable_grid(False)
        self.qtgui_const_sink_x_1_0_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_1_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_0_0_win, 2,1,1,1)
        self.qtgui_const_sink_x_1_0 = qtgui.const_sink_c(
        	1024, #size
        	'Transmitted modulated symbols', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0.enable_autoscale(False)
        self.qtgui_const_sink_x_1_0.enable_grid(False)
        self.qtgui_const_sink_x_1_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_1_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_0_win, 2,0,1,1)
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
        	1024, #size
        	'After time synchronization @RX', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1.enable_grid(False)
        self.qtgui_const_sink_x_1.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_1.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_win, 3,0,1,1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	'After Costas Loop @RX', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 3,2,1,1)
        self.digital_psk_mod_0 = digital.psk.psk_mod(
          constellation_points=arity,
          mod_code="gray",
          differential=True,
          samples_per_symbol=sps,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, timing_loop_bw, (rrc_taps), nfilts, nfilts/2, 1.5, 2)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(phase_bw, arity, False)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(15, 1, eq_gain, 2)
        self.channels_dynamic_channel_model_0 = channels.dynamic_channel_model( samp_rate, 0.01, 1e3, 0.01, 1e3, 8, 2.0, False, 4.0, (pdp_times), (pdp_mags), 8, noise_volt, 0 )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, 100e3,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((.5+.5j, ))
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, number_of_samples)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_psk_mod_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_const_sink_x_1_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.channels_dynamic_channel_model_0, 0))    
        self.connect((self.channels_dynamic_channel_model_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    
        self.connect((self.channels_dynamic_channel_model_0, 0), (self.qtgui_const_sink_x_1_0_0_0, 0))    
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_costas_loop_cc_0, 0))    
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.qtgui_const_sink_x_1_1, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_const_sink_x_1, 0))    
        self.connect((self.digital_psk_mod_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.digital_psk_mod_0, 0), (self.qtgui_const_sink_x_1_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

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

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model
        self.set_samp_rate([self.samp_rate_ca0, self.samp_rate_umts_ped_a, self.samp_rate_umts_ped_b][self.model])
        self.set_pdp_times([self.pdp_times_ca0, self.pdp_times_umts_ped_a, self.pdp_times_umts_ped_b][self.model])
        self.set_pdp_mags([self.pdp_mags_ca0, self.pdp_mags_umts_ped_a, self.pdp_mags_umts_ped_b][self.model])

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_loop_bw)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.channels_dynamic_channel_model_0.set_samp_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.phase_bw)

    def get_pdp_times(self):
        return self.pdp_times

    def set_pdp_times(self, pdp_times):
        self.pdp_times = pdp_times

    def get_pdp_mags(self):
        return self.pdp_mags

    def set_pdp_mags(self, pdp_mags):
        self.pdp_mags = pdp_mags

    def get_number_of_samples(self):
        return self.number_of_samples

    def set_number_of_samples(self, number_of_samples):
        self.number_of_samples = number_of_samples

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt
        self.channels_dynamic_channel_model_0.set_noise_amp(self.noise_volt)

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain
        self.digital_cma_equalizer_cc_0.set_gain(self.eq_gain)

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity


def main(top_block_cls=top_block, options=None):

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
