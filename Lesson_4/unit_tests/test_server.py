import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))

from server import process_client_message
from common.variables import *
import unittest

class TestServer(unittest.TestCase):
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    ok_dict = {RESPONSE: 200}
    def test_no_action(self):
        self.assertEqual(process_client_message({TIME : '1.1' , USER : {ACCOUNT_NAME : 'Guest'}}), self.err_dict)
    def test_wrong_action(self):
        self.assertEqual(process_client_message({ACTION : 'Wrong' , TIME : '1.1' , USER : {ACCOUNT_NAME : 'Guest'}}), self.err_dict)
    def test_no_time(self):
        self.assertEqual(process_client_message({ACTION : PRESENCE , USER : {ACCOUNT_NAME : 'Guest'}}), self.err_dict)
    def test_no_user(self):
        self.assertEqual(process_client_message({ACTION : PRESENCE ,TIME : '1.1' }), self.err_dict)
    def test_unknown_user(self):
        self.assertEqual( process_client_message( {ACTION : PRESENCE , TIME : 1.1 , USER : {ACCOUNT_NAME : 'Guest1'}}) , self.err_dict)
    def test_ok_check(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)

if __name__ == '__main__':
    unittest.main()


