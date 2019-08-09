#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Interpolating and decimating FIR filters
# Author: Alexandros-Apostolos A. Boulgoergos
# Generated: Fri Aug  9 08:19:10 2019
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
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Interpolating and decimating FIR filters")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Interpolating and decimating FIR filters")
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
        self.ntaps = ntaps = 45
        self.eb = eb = 0.25
        self.samp_rate = samp_rate = 32000
        self.rrc_tx = rrc_tx = firdes.root_raised_cosine(sps, sps, 1, eb, sps*ntaps)
        self.rrc_rx = rrc_rx = firdes.root_raised_cosine(1, sps, 1, eb, ntaps)

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	27, #size
        	samp_rate, #samp_rate
        	'QT GUI Plot', #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0_0.set_y_axis(-0.5, 1.25)
        
        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.9, 0.0002, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ['Rx Symbol 1', 'Rx Symbol 2', 'Rx Symbol 3', 'Rx Symbol 4', '',
                  '', '', '', '', '']
        widths = [2, 2, 2, 2, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, 0, 0, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(4):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 0,1,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	27, #size
        	samp_rate, #samp_rate
        	'QT GUI Plot', #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0.set_y_axis(-0.5, 1.25)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.99, 0.0002, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['Symbol 1', 'Symbol 2', 'Symbol 3', 'Symbol 4', '',
                  '', '', '', '', '']
        widths = [2, 2, 2, 2, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, 0, 0, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(4):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 0,0,1,1)
        self.interp_fir_filter_xxx_0_1 = filter.interp_fir_filter_fff(sps, (rrc_tx))
        self.interp_fir_filter_xxx_0_1.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_0 = filter.interp_fir_filter_fff(sps, (rrc_tx))
        self.interp_fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(sps, (rrc_tx))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(sps, (rrc_tx))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_1 = filter.fir_filter_fff(1, (rrc_rx))
        self.fir_filter_xxx_0_1.declare_sample_delay(0)
        self.fir_filter_xxx_0_0_0 = filter.fir_filter_fff(1, (rrc_rx))
        self.fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(1, (rrc_rx))
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(1, (rrc_rx))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_vector_source_x_0_1 = blocks.vector_source_f(51*[0,] + [1,] + 48*[0,], True, 1, [])
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_f(52*[0,] + [1,] + 47*[0,], True, 1, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_f(50*[0,] + [1,] + 49*[0,], True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_f(49*[0,] + [1,] + 50*[0,], True, 1, [])
        self.blocks_throttle_0_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.interp_fir_filter_xxx_0, 0))    
        self.connect((self.blocks_throttle_0_0, 0), (self.interp_fir_filter_xxx_0_0, 0))    
        self.connect((self.blocks_throttle_0_0_0, 0), (self.interp_fir_filter_xxx_0_0_0, 0))    
        self.connect((self.blocks_throttle_0_1, 0), (self.interp_fir_filter_xxx_0_1, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_throttle_0_0, 0))    
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_throttle_0_0_0, 0))    
        self.connect((self.blocks_vector_source_x_0_1, 0), (self.blocks_throttle_0_1, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.fir_filter_xxx_0_0, 0), (self.qtgui_time_sink_x_0_0, 1))    
        self.connect((self.fir_filter_xxx_0_0_0, 0), (self.qtgui_time_sink_x_0_0, 3))    
        self.connect((self.fir_filter_xxx_0_1, 0), (self.qtgui_time_sink_x_0_0, 2))    
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.fir_filter_xxx_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.fir_filter_xxx_0_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.fir_filter_xxx_0_0_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.qtgui_time_sink_x_0, 3))    
        self.connect((self.interp_fir_filter_xxx_0_1, 0), (self.fir_filter_xxx_0_1, 0))    
        self.connect((self.interp_fir_filter_xxx_0_1, 0), (self.qtgui_time_sink_x_0, 2))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_tx(firdes.root_raised_cosine(self.sps, self.sps, 1, self.eb, self.sps*self.ntaps))
        self.set_rrc_rx(firdes.root_raised_cosine(1, self.sps, 1, self.eb, self.ntaps))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_rrc_tx(firdes.root_raised_cosine(self.sps, self.sps, 1, self.eb, self.sps*self.ntaps))
        self.set_rrc_rx(firdes.root_raised_cosine(1, self.sps, 1, self.eb, self.ntaps))

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_rrc_tx(firdes.root_raised_cosine(self.sps, self.sps, 1, self.eb, self.sps*self.ntaps))
        self.set_rrc_rx(firdes.root_raised_cosine(1, self.sps, 1, self.eb, self.ntaps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rrc_tx(self):
        return self.rrc_tx

    def set_rrc_tx(self, rrc_tx):
        self.rrc_tx = rrc_tx
        self.interp_fir_filter_xxx_0_1.set_taps((self.rrc_tx))
        self.interp_fir_filter_xxx_0_0_0.set_taps((self.rrc_tx))
        self.interp_fir_filter_xxx_0_0.set_taps((self.rrc_tx))
        self.interp_fir_filter_xxx_0.set_taps((self.rrc_tx))

    def get_rrc_rx(self):
        return self.rrc_rx

    def set_rrc_rx(self, rrc_rx):
        self.rrc_rx = rrc_rx
        self.fir_filter_xxx_0_1.set_taps((self.rrc_rx))
        self.fir_filter_xxx_0_0_0.set_taps((self.rrc_rx))
        self.fir_filter_xxx_0_0.set_taps((self.rrc_rx))
        self.fir_filter_xxx_0.set_taps((self.rrc_rx))


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
