#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: uhd_to_power_spectrum
# Author: Alexandros-Apostolos A. Boulogeorgos
# Generated: Sun Aug 18 14:03:35 2019
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
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import gr, blocks
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sys
import time


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "uhd_to_power_spectrum")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("uhd_to_power_spectrum")
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
        self.samp_rate = samp_rate = 100e3
        self.fft_size = fft_size = 8192
        self.vector_cut_offset = vector_cut_offset = 4096
        self.vector_cut_length = vector_cut_length = 8192/16
        self.v_gain = v_gain = 42
        self.output_vector_sample_rate = output_vector_sample_rate = samp_rate/fft_size
        self.f_c = f_c = 1296960000

        ##################################################
        # Blocks
        ##################################################
        self._v_gain_range = Range(0, 80, 1, 42, 200)
        self._v_gain_win = RangeWidget(self._v_gain_range, self.set_v_gain, 'Gain', "counter_slider", float)
        self.top_layout.addWidget(self._v_gain_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_clock_source('external', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_center_freq(f_c, 0)
        self.uhd_usrp_source_0.set_gain(v_gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.fft_vxx_0_0 = fft.fft_vcc(fft_size, True, (window.blackmanharris(fft_size)), True, 1)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, fft_size)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, vector_cut_length)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, fft_size, 0)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_float, vector_cut_length, fft_size, vector_cut_offset)
        self.blocks_file_meta_sink_0 = blocks.file_meta_sink(gr.sizeof_float*vector_cut_length, 'power_spectrum.dat', samp_rate, output_vector_sample_rate/samp_rate, blocks.GR_FILE_FLOAT, False, 1000, "", True)
        self.blocks_file_meta_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(fft_size)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_nlog10_ff_0_0, 0))    
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_stream_to_vector_0_0_0, 0))    
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.blocks_vector_to_stream_0_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.blocks_file_meta_sink_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.blocks_keep_m_in_n_0, 0))    
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_stream_to_vector_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_output_vector_sample_rate(self.samp_rate/self.fft_size)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size
        self.set_output_vector_sample_rate(self.samp_rate/self.fft_size)
        self.blocks_keep_m_in_n_0.set_n(self.fft_size)

    def get_vector_cut_offset(self):
        return self.vector_cut_offset

    def set_vector_cut_offset(self, vector_cut_offset):
        self.vector_cut_offset = vector_cut_offset
        self.blocks_keep_m_in_n_0.set_offset(self.vector_cut_offset)

    def get_vector_cut_length(self):
        return self.vector_cut_length

    def set_vector_cut_length(self, vector_cut_length):
        self.vector_cut_length = vector_cut_length
        self.blocks_keep_m_in_n_0.set_m(self.vector_cut_length)

    def get_v_gain(self):
        return self.v_gain

    def set_v_gain(self, v_gain):
        self.v_gain = v_gain
        self.uhd_usrp_source_0.set_gain(self.v_gain, 0)
        	

    def get_output_vector_sample_rate(self):
        return self.output_vector_sample_rate

    def set_output_vector_sample_rate(self, output_vector_sample_rate):
        self.output_vector_sample_rate = output_vector_sample_rate

    def get_f_c(self):
        return self.f_c

    def set_f_c(self, f_c):
        self.f_c = f_c
        self.uhd_usrp_source_0.set_center_freq(self.f_c, 0)


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
