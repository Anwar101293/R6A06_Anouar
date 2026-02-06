import Strategies.protocols.rumination_strategy

class NoMilkStrategy(RuminationStrategy):
    def _calculer_lait(self):
        return 0.0

    def _stocker_lait(self):
        return

    def _post_rumination(self):
        return