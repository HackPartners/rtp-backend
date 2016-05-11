
from enum import Enum

class ClaimValidationStatus(Enum):
	OUTSTANDING 		= "OUTSTANDING"
	REJECTED 			= "REJECTED"
	ACCEPTED 			= "ACCEPTED"

class PaymentTypes(Enum):
	BANK_TRANSFER 		= "BANK_TRANSFER"
	CHEQUE 				= "CHEQUE"
	TRAVEL_VOUCHER		= "TRAVEL VOUCHER"

