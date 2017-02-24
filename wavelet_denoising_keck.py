from PynPoint import Pypeline
import numpy as np
from PynPoint.processing_modules import CwtWaveletConfiguration, WaveletTimeDenoisingModule

pipeline = Pypeline("/Users/markusbonse/Desktop/",
                    "/Users/markusbonse/Desktop/Science",
                    "/Users/markusbonse/Desktop/results")

# 07 Wavelet Analysis
wavelet = CwtWaveletConfiguration(wavelet="dog",
                                  wavelet_order=2.0,
                                  keep_mean=True,
                                  resolution=0.2)

k = 1

for j in [[1.0,], ]:

    wavelet_thresholds = j

    wavelet_names = []
    for i in wavelet_thresholds:
        wavelet_names.append("07_wavelet_denoised_" + str(int(i)) + "_" + str(int(round((i % 1.0)*10))))

    denoising = WaveletTimeDenoisingModule(wavelet_configuration=wavelet,
                                           name_in="wavelet_time_denoising" + str(k),
                                           image_in_tag="04_star_aligned",
                                           image_out_tag=wavelet_names,
                                           denoising_threshold=wavelet_thresholds,
                                           padding="const_mean",
                                           num_rows_in_memory=None)
    pipeline.add_module(denoising)
    k += 1

pipeline.run()
