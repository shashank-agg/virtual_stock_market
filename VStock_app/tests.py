from django.test import TestCase
from django.contrib.auth.models import User
from models import UserProfile

# Create your tests here.
class SimpleTest(TestCase):
    def test_portal_page(self):
        """
        Test availability of login page
        """
        print "Testing availability of login page"
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_redirection(self):
        """
        Test availability of portal page
        """
        print "Test availability of portal page"
        resp = self.client.get('/portal/')
        self.assertEqual(resp.status_code, 302) 


    def test_login(self):
        """
        Test login
        """
        print "Testing login functionality with temporary user "
        test_user = User.objects.create(username="test",password="test")
        test_user.set_password('test')
        test_user.save()

        test_user_profile = UserProfile.objects.create(user=test_user)
        test_user_profile.save()
        self.client.login(username='test', password='test')
        resp = self.client.post('/portal/')
        self.assertEqual(resp.status_code, 200)