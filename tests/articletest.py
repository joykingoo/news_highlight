import unittest
from .models import Articles


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles("wired","Bitcoin Exposed Silicon Valley's Ultimate Aim: Making Money","Bitcoin is a prime example of how Silicon Valley touts \\\"democratization\\\" and \\\"decentralization\\\" as righteous motives when wealth is the ultimate goal.", "Noam Cohen","https://media.wired.com/photos/5c2feca7b49dea0ea6833687/191:100/pass/Ideas_Art_Bitcoin-167577080.jpg","2019-01-07T12:00:00Z", "https://www.wired.com/story/bitcoin-exposed-silicon-valley-aim-making-money/")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


