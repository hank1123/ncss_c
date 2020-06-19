from django.test import TestCase

from mixer.backend.django import mixer
from user.models import Users

# # Create your tests here.
# class LoginTest(TestCase):
#     def setUp(self):
#         self.users = [
#             mixer.blend(Users)
#             for _ in range(20)
#         ]
#
#     def test_login(self):
#         url='/user/login/'
#         for user in self.users:
#             response = self.client.post(url, {
#                 'account':user.account,
#                 'password':user.password
#             })
#             self.assertEqual(response.status_code, 200)
#             data = response.json()
#             self.assertEqual(data['errMsg'], '登陆成功')
