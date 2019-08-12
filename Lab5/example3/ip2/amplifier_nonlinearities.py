#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: IP2
# Author: Alexandros-Apostolos A. Boulogeorgos
# Generated: Mon Aug 12 09:04:24 2019
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import math
import sip
import sys


class amplifier_nonlinearities(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "IP2")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("IP2")
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

        self.settings = Qt.QSettings("GNU Radio", "amplifier_nonlinearities")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000
        self.signal_amp = signal_amp = 0
        self.sigfreq = sigfreq = samp_rate*1.0247385/21.0
        self.ip2 = ip2 = 0

        ##################################################
        # Blocks
        ##################################################
        self._signal_amp_range = Range(-150, 10, 5, 0, 200)
        self._signal_amp_win = RangeWidget(self._signal_amp_range, self.set_signal_amp, 'Singal Power', "counter_slider", float)
        self.top_grid_layout.addWidget(self._signal_amp_win, 2,0,1,1)
        self._sigfreq_range = Range(0, samp_rate/2, 1000, samp_rate*1.0247385/21.0, 200)
        self._sigfreq_win = RangeWidget(self._sigfreq_range, self.set_sigfreq, 'Signal Freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._sigfreq_win, 3,0,1,1)
        self._ip2_range = Range(0, 1, 0.01, 0, 200)
        self._ip2_win = RangeWidget(self._ip2_range, self.set_ip2, 'IP2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._ip2_win, 3,1,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_FLATTOP, #wintype
        	0, #fc
        	samp_rate, #bw
        	'', #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-200, 0)
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
        
        labels = ['Input', 'With IP2', '', '', '',
                  '', '', '', '', '']
        widths = [2, 2, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [0.5, 0.5, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,2)
        self.channels_distortion_2_gen_0 = channels.distortion_2_gen(ip2)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 2.45*sigfreq, pow(10.0,signal_amp/20.0), 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, sigfreq, pow(10.0,signal_amp/20.0), 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.channels_distortion_2_gen_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.channels_distortion_2_gen_0, 0), (self.qtgui_freq_sink_x_0, 1))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "amplifier_nonlinearities")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sigfreq(self.samp_rate*1.0247385/21.0)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_signal_amp(self):
        return self.signal_amp

    def set_signal_amp(self, signal_amp):
        self.signal_amp = signal_amp
        self.analog_sig_source_x_0_0.set_amplitude(pow(10.0,self.signal_amp/20.0))
        self.analog_sig_source_x_0.set_amplitude(pow(10.0,self.signal_amp/20.0))

    def get_sigfreq(self):
        return self.sigfreq

    def set_sigfreq(self, sigfreq):
        self.sigfreq = sigfreq
        self.analog_sig_source_x_0_0.set_frequency(2.45*self.sigfreq)
        self.analog_sig_source_x_0.set_frequency(self.sigfreq)

    def get_ip2(self):
        return self.ip2

    def set_ip2(self, ip2):
        self.ip2 = ip2
        self.channels_distortion_2_gen_0.set_beta(self.ip2)


def main(top_block_cls=amplifier_nonlinearities, options=None):

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
