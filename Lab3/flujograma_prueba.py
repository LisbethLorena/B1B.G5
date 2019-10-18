#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: If Else
# Generated: Thu Sep 13 11:39:57 2018
##################################################

##################################################
# LO QUE HAY QUE IMPORTAR
##################################################
from gnuradio import audio
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio.filter import firdes

from PyQt5 import Qt
import sys, sip
#######################################################
# LA CLASE QUE DESCRIBE TODO EL FLUJOGRAMA
######################################################
class my_top_block(gr.top_block):        # hereda de gr.top_block
     def __init__(self):
         gr.top_block.__init__(self)     # otra vez la herencia
         self.qapp = Qt.QApplication(sys.argv)
         sample_rate = 32000
         fftsize=2048
         ampl = 0.5
 
         self.src0 = analog.sig_source_c(sample_rate, analog.GR_SIN_WAVE, 1000, ampl)
         self.src1 = analog.sig_source_c(sample_rate, analog.GR_SIN_WAVE, 500, ampl)
         self.add = blocks.add_cc()
         self.thr = blocks.throttle(gr.sizeof_gr_complex, sample_rate, True)
         self.snk = qtgui.sink_c(
            fftsize, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            sample_rate, #bw
            "", #name
            True, #plotfreq
            False, #plotwaterfall
            True, #plottime
            False, #plotconst
         )
         self.connect(self.src0, (self.add, 0))
         self.connect(self.src1, (self.add, 1))
         self.connect(self.add, self.thr, self.snk)
         # Se establece como deseamos ver los resultados graficos
         self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), Qt.QWidget)
         self.pyobj.show()
         #self.dst = audio.sink(sample_rate, "")
         #self.connect(src0, (dst, 0))
         #self.connect(src1, (dst, 1))
         
#######################################################
# EL CÓDIGO PARA LLAMAR EL FLUJOGRAMA “my_top_block”
######################################################

def main():
    tb = my_top_block()
    tb.start()
    tb.qapp.exec_()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
#if __name__ == '__main__':
#    try:
#         my_top_block().run()
#    except [[KeyboardInterrupt]]:
#         pass
