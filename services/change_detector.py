from models.stock import Stock
from typing import Optional


class PriceChangeDetector:
    @staticmethod
    def has_changed(old: Optional[Stock], new: Stock) -> bool:
        if old is None:
            return True

        return old.price != new.price

# TODO can be extended with:
#       - percentage thresholds
#       - spike/drop detecting
#       - track time since last change