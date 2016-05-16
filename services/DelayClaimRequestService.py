
from models import Journey, DelayClaim, PaymentDetails, ContactDetails, ClaimValidation, db
from .ServiceEnums import *

class DelayClaimRequestService:
    def __init__(self):
        pass

    @db.atomic()
    def save_claim_request(self, delay_claim_request):

        image_64 = delay_claim_request["image_64"]
        journey_request = delay_claim_request["journey"]
        contact_request = delay_claim_request["contact_details"]
        payment_request = delay_claim_request["payment"]

        payment = self.save_payment_request(payment_request)
        contact = self.save_contact_request(contact_request)
        journey = self.save_journey_request(journey_request, image_64)

        claim_validation = ClaimValidation()
        claim_validation.status = ClaimValidationStatus.OUTSTANDING
        claim_validation.save()

        delay_claim = DelayClaim()
        delay_claim.payment_details = payment
        delay_claim.contact_details = contact
        delay_claim.journey = journey
        delay_claim.claim_validation = claim_validation

        delay_claim.save()

        return delay_claim

    def save_payment_request(self, payment_request):

        payment = PaymentDetails()
        payment.payment_type = payment_request["payment_type"]
        payment.account_number = payment_request["account_number"]
        payment.sort_code = payment_request["sort_code"]
        payment.payment_type = payment_request["payment_type"]

        payment.save()
        return payment

    def save_contact_request(self, contact_request):

        contact = ContactDetails()
        contact.title = contact_request["title"]
        contact.first_name = contact_request["first_name"]
        contact.last_name = contact_request["last_name"]
        contact.address = contact_request["address"]
        contact.email = contact_request["email"]
        contact.post_code = contact_request["post_code"]

        contact.save()
        return contact

    def save_journey_request(self, journey_request, image_64):
        print(journey_request)

        journey = Journey()
        journey.image_64 = image_64
        journey.from_station = journey_request["from_station"]
        journey.to_station = journey_request["to_station"]
        journey.ticket_class = journey_request["ticket_class"]
        journey.ticket_type = journey_request["ticket_type"]
        journey.from_date = journey_request["from_date"]
        journey.to_date = journey_request["to_date"]
        journey.cost = journey_request["cost"]
        journey.journey_date = journey_request["journey_date"]

        journey.save()
        return journey


