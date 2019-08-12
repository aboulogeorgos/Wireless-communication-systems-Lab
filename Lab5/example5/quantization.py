#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Quantization
# Author: Alexandros-Apostolos A. Boulogeorgos
# Generated: Mon Aug 12 09:37:47 2019
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
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import math
import sip
import sys


class quantization(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Quantization")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Quantization")
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

        self.settings = Qt.QSettings("GNU Radio", "quantization")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000
        self.signal_amp = signal_amp = -150
        self.sigfreq = sigfreq = samp_rate*1.0247385/11.0
        self.noise_amp = noise_amp = -150
        self.center = center = samp_rate/11.0
        self.bw = bw = samp_rate/2
        self.bits = bits = 2

        ##################################################
        # Blocks
        ##################################################
        self._signal_amp_range = Range(-150, 20, 5, -150, 200)
        self._signal_amp_win = RangeWidget(self._signal_amp_range, self.set_signal_amp, 'Singal Power', "counter_slider", float)
        self.top_grid_layout.addWidget(self._signal_amp_win, 2,0,1,1)
        self._sigfreq_range = Range(0, samp_rate/2, 1000, samp_rate*1.0247385/11.0, 200)
        self._sigfreq_win = RangeWidget(self._sigfreq_range, self.set_sigfreq, 'Signal Freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._sigfreq_win, 3,0,1,1)
        self._noise_amp_range = Range(-150, 0, 5, -150, 200)
        self._noise_amp_win = RangeWidget(self._noise_amp_range, self.set_noise_amp, 'Noise Power', "counter_slider", float)
        self.top_grid_layout.addWidget(self._noise_amp_win, 2,1,1,1)
        self._center_range = Range(0, samp_rate/2, 100, samp_rate/11.0, 200)
        self._center_win = RangeWidget(self._center_range, self.set_center, 'Center Freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._center_win, 3,1,1,1)
        self._bw_range = Range(samp_rate/100.0, samp_rate/2, 100, samp_rate/2, 200)
        self._bw_win = RangeWidget(self._bw_range, self.set_bw, 'BW', "counter_slider", float)
        self.top_grid_layout.addWidget(self._bw_win, 4,1,1,1)
        self._bits_options = [2,4,6,8,10,12,14,16]
        self._bits_labels = map(str, self._bits_options)
        self._bits_tool_bar = Qt.QToolBar(self)
        self._bits_tool_bar.addWidget(Qt.QLabel('Bits'+": "))
        self._bits_combo_box = Qt.QComboBox()
        self._bits_tool_bar.addWidget(self._bits_combo_box)
        for label in self._bits_labels: self._bits_combo_box.addItem(label)
        self._bits_callback = lambda i: Qt.QMetaObject.invokeMethod(self._bits_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._bits_options.index(i)))
        self._bits_callback(self.bits)
        self._bits_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_bits(self._bits_options[i]))
        self.top_grid_layout.addWidget(self._bits_tool_bar, 4,0,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	128, #size
        	samp_rate, #samp_rate
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-bits, bits)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [0.5, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 1,0,1,2)
        self.qtgui_histogram_sink_x_0 = qtgui.histogram_sink_f(
        	10000,
        	100,
                -1 - pow(2,bits-1),
                1 + pow(2,bits-1),
        	'',
        	1
        )
        
        self.qtgui_histogram_sink_x_0.set_update_time(0.10)
        self.qtgui_histogram_sink_x_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0.enable_accumulate(False)
        self.qtgui_histogram_sink_x_0.enable_grid(False)
        self.qtgui_histogram_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_histogram_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_histogram_sink_x_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_histogram_sink_x_0_win, 0,1,1,1)
          
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	2048, #size
        	firdes.WIN_FLATTOP, #wintype
        	0, #fc
        	samp_rate, #bw
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-180, 0)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,1)
        self.channels_quantizer_0 = channels.quantizer(bits)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((1, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, samp_rate, max(bw/15.0,center-bw/2.0), min(samp_rate/2.0-bw/15.0,center+bw/2.0), bw/5.0, firdes.WIN_HANN, 6.76))
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, sigfreq, pow(10.0,signal_amp/20.0), 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, pow(10.0,noise_amp/20.0), 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_histogram_sink_x_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.channels_quantizer_0, 0))    
        self.connect((self.channels_quantizer_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.channels_quantizer_0, 0), (self.qtgui_freq_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "quantization")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sigfreq(self.samp_rate*1.0247385/11.0)
        self.set_center(self.samp_rate/11.0)
        self.set_bw(self.samp_rate/2)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, max(self.bw/15.0,self.center-self.bw/2.0), min(self.samp_rate/2.0-self.bw/15.0,self.center+self.bw/2.0), self.bw/5.0, firdes.WIN_HANN, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_signal_amp(self):
        return self.signal_amp

    def set_signal_amp(self, signal_amp):
        self.signal_amp = signal_amp
        self.analog_sig_source_x_0.set_amplitude(pow(10.0,self.signal_amp/20.0))

    def get_sigfreq(self):
        return self.sigfreq

    def set_sigfreq(self, sigfreq):
        self.sigfreq = sigfreq
        self.analog_sig_source_x_0.set_frequency(self.sigfreq)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_0.set_amplitude(pow(10.0,self.noise_amp/20.0))

    def get_center(self):
        return self.center

    def set_center(self, center):
        self.center = center
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, max(self.bw/15.0,self.center-self.bw/2.0), min(self.samp_rate/2.0-self.bw/15.0,self.center+self.bw/2.0), self.bw/5.0, firdes.WIN_HANN, 6.76))

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, max(self.bw/15.0,self.center-self.bw/2.0), min(self.samp_rate/2.0-self.bw/15.0,self.center+self.bw/2.0), self.bw/5.0, firdes.WIN_HANN, 6.76))

    def get_bits(self):
        return self.bits

    def set_bits(self, bits):
        self.bits = bits
        self._bits_callback(self.bits)
        self.qtgui_time_sink_x_0.set_y_axis(-self.bits, self.bits)
        self.qtgui_histogram_sink_x_0.set_x_axis(-1 - pow(2,self.bits-1), 1 + pow(2,self.bits-1))
        self.channels_quantizer_0.set_bits(self.bits)


def main(top_block_cls=quantization, options=None):

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
