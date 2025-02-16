# utils/ris.py
import numpy as np

class RIS:
    def __init__(self, num_ris_elements=16, alpha_min=1.1, alpha_max=2.0):
        self.num_ris_elements = num_ris_elements
        self.alpha_min = alpha_min
        self.alpha_max = alpha_max
        self.current_beamforming = np.ones(self.num_ris_elements) * self.alpha_min
        self.current_reflection = np.zeros(self.num_ris_elements)

    def update_ris(self, beamforming, reflection):
        self.current_beamforming = np.clip(beamforming, self.alpha_min, self.alpha_max)
        self.current_reflection = np.clip(reflection, 0, 2 * np.pi)

class PassiveRIS(RIS):
    def __init__(self, num_ris_elements=16, alpha_min=1.0, alpha_max=1.0):
        super().__init__(num_ris_elements, alpha_min, alpha_max)
        self.current_beamforming = np.ones(self.num_ris_elements) * self.alpha_min

    def update_ris(self, beamforming, reflection):
        self.current_reflection = np.clip(reflection, 0, 2 * np.pi)
