#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Packet Encoder_Decoder
# Author: Alexandros-Apostolos A. Boulogeorgos
# Generated: Thu Aug 15 13:35:51 2019
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

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class packet_encoder_decoder_example(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Packet Encoder_Decoder")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32E3
        self.code2 = code2 = '11011010110111011000110011110101100010010011110111'
        self.code1 = code1 = '010110011011101100010101011111101001001110001011010001101010001'

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(2)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bf((0,1), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_packed_to_unpacked_xx_1 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/Users/ampoulog/Documents/gnuradio/Wireless-communication-systems-Lab/Lab3/example6/cat.png', True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/Users/ampoulog/Documents/gnuradio/Wireless-communication-systems-Lab/Lab3/example6/hello_out.png', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blks2_packet_encoder_0_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=1,
        		bits_per_symbol=1,
        		preamble='',
        		access_code=code1,
        		pad_for_usrp=False,
        	),
        	payload_length=4,
        )
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code=code1,
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blks2_packet_encoder_0_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_packed_to_unpacked_xx_1, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_diff_encoder_bb_0, 0))    
        self.connect((self.blocks_packed_to_unpacked_xx_1, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blks2_packet_encoder_0_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blks2_packet_decoder_0, 0))    
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_diff_decoder_bb_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_code2(self):
        return self.code2

    def set_code2(self, code2):
        self.code2 = code2

    def get_code1(self):
        return self.code1

    def set_code1(self, code1):
        self.code1 = code1


def main(top_block_cls=packet_encoder_decoder_example, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
