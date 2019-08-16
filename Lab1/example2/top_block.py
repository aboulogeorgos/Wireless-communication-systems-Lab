#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Author: Alexandros-Apostolos A. Boulgoergos
# Generated: Thu Aug 15 13:39:02 2019
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
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
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
        self.waveform1 = waveform1 = 102
        self.samp_rate = samp_rate = 32000
        self.f0 = f0 = 1000

        ##################################################
        # Blocks
        ##################################################
        self._waveform1_options = (101, 102, 103, 104, 105, )
        self._waveform1_labels = ('Sine', 'Cosine', 'Rectangular', 'Triangular', 'Saw tooth', )
        self._waveform1_tool_bar = Qt.QToolBar(self)
        self._waveform1_tool_bar.addWidget(Qt.QLabel('Waveform of signal source 1'+": "))
        self._waveform1_combo_box = Qt.QComboBox()
        self._waveform1_tool_bar.addWidget(self._waveform1_combo_box)
        for label in self._waveform1_labels: self._waveform1_combo_box.addItem(label)
        self._waveform1_callback = lambda i: Qt.QMetaObject.invokeMethod(self._waveform1_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._waveform1_options.index(i)))
        self._waveform1_callback(self.waveform1)
        self._waveform1_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_waveform1(self._waveform1_options[i]))
        self.top_grid_layout.addWidget(self._waveform1_tool_bar, 0,0,1,1)
        self._f0_range = Range(-5000, 5000, 1, 1000, 200)
        self._f0_win = RangeWidget(self._f0_range, self.set_f0, "f0", "counter_slider", float)
        self.top_layout.addWidget(self._f0_win)
        self.qtgui_sink_x_0 = qtgui.sink_f(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        self.audio_sink_0 = audio.sink(samp_rate, '', True)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, waveform1, f0, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.qtgui_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_waveform1(self):
        return self.waveform1

    def set_waveform1(self, waveform1):
        self.waveform1 = waveform1
        self._waveform1_callback(self.waveform1)
        self.analog_sig_source_x_0.set_waveform(self.waveform1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_f0(self):
        return self.f0

    def set_f0(self, f0):
        self.f0 = f0
        self.analog_sig_source_x_0.set_frequency(self.f0)


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
