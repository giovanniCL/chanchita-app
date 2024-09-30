from dataclasses import dataclass

@dataclass
class Balance:
    type: str
    amount: str
    transaction: str
    member: str