#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Create AWGN noise
# Author: Alexandros-Apostolos A. Boulogeorgos
# Description: Import python modules in gnuradio
# Generated: Sat Oct  5 08:20:04 2019
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
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import create_noise  # embedded python module
import sip
import sys


class createNoise(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Create AWGN noise")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Create AWGN noise")
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

        self.settings = Qt.QSettings("GNU Radio", "createNoise")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sampleRate_Hz = sampleRate_Hz = 30000
        self.samp_rate = samp_rate = sampleRate_Hz
        self.numSamples = numSamples = 1000000
        self.centerFreq_Hz = centerFreq_Hz = 7500
        self.bandwidth_Hz = bandwidth_Hz = 5000

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'AWGN')
        self.top_layout.addWidget(self.tab)
        self._sampleRate_Hz_tool_bar = Qt.QToolBar(self)
        self._sampleRate_Hz_tool_bar.addWidget(Qt.QLabel('Sample Rate (Hz)'+": "))
        self._sampleRate_Hz_line_edit = Qt.QLineEdit(str(self.sampleRate_Hz))
        self._sampleRate_Hz_tool_bar.addWidget(self._sampleRate_Hz_line_edit)
        self._sampleRate_Hz_line_edit.returnPressed.connect(
        	lambda: self.set_sampleRate_Hz(int(str(self._sampleRate_Hz_line_edit.text().toAscii()))))
        self.tab_grid_layout_0.addWidget(self._sampleRate_Hz_tool_bar, 0,2,1,1)
        self._numSamples_tool_bar = Qt.QToolBar(self)
        self._numSamples_tool_bar.addWidget(Qt.QLabel('Number of Points'+": "))
        self._numSamples_line_edit = Qt.QLineEdit(str(self.numSamples))
        self._numSamples_tool_bar.addWidget(self._numSamples_line_edit)
        self._numSamples_line_edit.returnPressed.connect(
        	lambda: self.set_numSamples(int(str(self._numSamples_line_edit.text().toAscii()))))
        self.tab_grid_layout_0.addWidget(self._numSamples_tool_bar, 0,3,1,1)
        self._centerFreq_Hz_tool_bar = Qt.QToolBar(self)
        self._centerFreq_Hz_tool_bar.addWidget(Qt.QLabel('Center Frequency (Hz)'+": "))
        self._centerFreq_Hz_line_edit = Qt.QLineEdit(str(self.centerFreq_Hz))
        self._centerFreq_Hz_tool_bar.addWidget(self._centerFreq_Hz_line_edit)
        self._centerFreq_Hz_line_edit.returnPressed.connect(
        	lambda: self.set_centerFreq_Hz(eng_notation.str_to_num(str(self._centerFreq_Hz_line_edit.text().toAscii()))))
        self.tab_grid_layout_0.addWidget(self._centerFreq_Hz_tool_bar, 0,0,1,1)
        self._bandwidth_Hz_tool_bar = Qt.QToolBar(self)
        self._bandwidth_Hz_tool_bar.addWidget(Qt.QLabel('Bandwidth (Hz)'+": "))
        self._bandwidth_Hz_line_edit = Qt.QLineEdit(str(self.bandwidth_Hz))
        self._bandwidth_Hz_tool_bar.addWidget(self._bandwidth_Hz_line_edit)
        self._bandwidth_Hz_line_edit.returnPressed.connect(
        	lambda: self.set_bandwidth_Hz(eng_notation.str_to_num(str(self._bandwidth_Hz_line_edit.text().toAscii()))))
        self.tab_grid_layout_0.addWidget(self._bandwidth_Hz_tool_bar, 0,1,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-225, -75)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
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
        self.tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 1,0,1,4)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, numSamples)
        self.blocks_vector_source_x_0 = blocks.vector_source_c(create_noise.createNoise(centerFreq_Hz, bandwidth_Hz, sampleRate_Hz, numSamples), True, numSamples, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*numSamples, samp_rate,True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.qtgui_freq_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "createNoise")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sampleRate_Hz(self):
        return self.sampleRate_Hz

    def set_sampleRate_Hz(self, sampleRate_Hz):
        self.sampleRate_Hz = sampleRate_Hz
        Qt.QMetaObject.invokeMethod(self._sampleRate_Hz_line_edit, "setText", Qt.Q_ARG("QString", str(self.sampleRate_Hz)))
        self.set_samp_rate(self.sampleRate_Hz)
        self.blocks_vector_source_x_0.set_data(create_noise.createNoise(self.centerFreq_Hz, self.bandwidth_Hz, self.sampleRate_Hz, self.numSamples), [])

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_numSamples(self):
        return self.numSamples

    def set_numSamples(self, numSamples):
        self.numSamples = numSamples
        Qt.QMetaObject.invokeMethod(self._numSamples_line_edit, "setText", Qt.Q_ARG("QString", str(self.numSamples)))
        self.blocks_vector_source_x_0.set_data(create_noise.createNoise(self.centerFreq_Hz, self.bandwidth_Hz, self.sampleRate_Hz, self.numSamples), [])

    def get_centerFreq_Hz(self):
        return self.centerFreq_Hz

    def set_centerFreq_Hz(self, centerFreq_Hz):
        self.centerFreq_Hz = centerFreq_Hz
        Qt.QMetaObject.invokeMethod(self._centerFreq_Hz_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.centerFreq_Hz)))
        self.blocks_vector_source_x_0.set_data(create_noise.createNoise(self.centerFreq_Hz, self.bandwidth_Hz, self.sampleRate_Hz, self.numSamples), [])

    def get_bandwidth_Hz(self):
        return self.bandwidth_Hz

    def set_bandwidth_Hz(self, bandwidth_Hz):
        self.bandwidth_Hz = bandwidth_Hz
        Qt.QMetaObject.invokeMethod(self._bandwidth_Hz_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.bandwidth_Hz)))
        self.blocks_vector_source_x_0.set_data(create_noise.createNoise(self.centerFreq_Hz, self.bandwidth_Hz, self.sampleRate_Hz, self.numSamples), [])


def main(top_block_cls=createNoise, options=None):

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
