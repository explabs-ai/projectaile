from ..pipeline import PIPELINE

class AUGMENTATIONS:
    def __init__(self, config):
        super(AUGMENTATIONS, self).__init__('augmentations', config)
        
    def apply(self):
        # apply according to probability
        return