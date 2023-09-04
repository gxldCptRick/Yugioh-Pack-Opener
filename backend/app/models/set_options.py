from .base import Base


class Weight(Base):
    rarity: str
    weight: float


class Option(Base):
    rarity: str | None = None
    amount_for: int | None = None
    weighted_rarities: list[Weight] | None = None


class SetOptions(Base):
    options: list[Option]


DEFAULT_SET_OPTIONS = SetOptions(
    options=[
        Option(rarity="Common", amount_for=7),
        Option(rarity="Rare", amount_for=1),
        Option(
            weighted_rarities=[
                Weight(rarity="Common", weight=0.9),
                Weight(rarity="Foil", weight=0.1),
            ]
        ),
    ]
)
