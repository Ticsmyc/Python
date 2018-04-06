import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

	def setUp(self):
		"""创建一个调查对象和一组答案，供下面的测试方法使用"""
		question="What language did you first learn to speak"
		self.my_survey=AnonymousSurvey(question)
		self.responses=['English','Spanish','Mandarin']

	def test_store_single_responst(self):
		self.my_survey.store_response('English')

		self.assertIn(self.responses[0],self.my_survey.responses)

	def test_sotre_three_response(self):
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response,self.my_survey.responses)	



unittest.main()		
