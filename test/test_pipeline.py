import unittest
import time
import logging
import skimage.io as skio
import numpy as np
import pandas as pd
from glob import glob

import microtaspy.segmentation as mseg
import cytoflow as flow

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class TestPipeline(unittest.TestCase):

    def _microtaspy_get_events(self):
        path = 'data/'
        data = {}
        for chan in ['green','red','blue']:
            data[chan] = skio.imread_collection(sorted(glob(path + '%s_*.tif' % chan)))

        df = {}
        for chan in ['green','red','blue']:
            df[chan] = pd.DataFrame()
            for i in range(len(data[chan])):
                frame,seg,_ = mseg.get_events(data[chan][i],(data['green'][i],data['red'][i],data['blue'][i]),['g','r','b'])
                df[chan] = df[chan].append(frame)
            df[chan] = df[chan].reset_index(drop=True)
        return df
            
    def test_microtaspy_cytoflow(self):
        df = self._microtaspy_get_events()
        # flow...

    def test_microtaspy_tasbe(self):
        df = self._microtaspy_get_events()
        # oct2py or system

if __name__ == '__main__':
    unittest.main()
