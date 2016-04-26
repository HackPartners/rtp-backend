import unittest, base64, requests, sys, os

project_path = os.path.abspath(os.path.join(__file__, '../../..'))
sys.path.append(project_path)

from SystemTestSettings import HOST, PORT
from models import DelayClaim

class DelayClaimSystemTests(unittest.TestCase):

	def setUp(self):
		self.url = HOST + ":" + PORT + "/delayClaim"

	def test_create_claim(self):
		r = requests.get(self.url)
		self.assertEqual(r.status_code, 200)

		r_json = r.json()

		self.assertTrue(len(r_json) > 0)

		for d in r_json:
			self.assertIn("claim_validation", d)
			self.assertIn("journey", d)
			self.assertIn("contact_details", d)
			self.assertIn("payment_details", d)

	def test_get_claims(self):
		delay_claim = { 
			"image_64": "test_image_base64",
			"journey": {
				"from_station": "London Euston",
				"to_station": "Manchester Picadilly",
				"ticket_class": "FIRST_CLASS",
				"ticket_type": "OFF_PEAK",
				"from_date": "2016-04-15",
				"to_date": "2016-04-18",
				"cost": 81.20,
				"journey_date": "2016-04-18T08:43:22"
			},
			"contact_details": {
				"title": "MR",
				"first_name": "Alejandro",
				"last_name": "Saucedo",
				"address": "70 Pentonville",
				"email": "alejandro@hackpartners.com",
				"post_code": "N1 9PR"
			},
			"payment": {
				"payment_type": "BANK_TRANSFER",
				"account_number": "07827362",
				"sort_code": "029238"
			}
		}

		r = requests.put(self.url, json=delay_claim)
		self.assertEqual(r.status_code, 200)

		delay_id = r.json()["id"]

		found = None
		try:
			found = DelayClaim.get(DelayClaim.id == delay_id)
		except:
			self.assertEqual(False, msg="Delay Claim not found in the database")

		# Cleaning up
		found.delete_instance()





