import unittest
from test.aiml_tests.client import TestClient
from programy.config import BrainFileConfiguration
import logging

class BasicTestClient(TestClient):

    def __init__(self):
        TestClient.__init__(self)

    def load_configuration(self, arguments):
        super(BasicTestClient, self).load_configuration(arguments)
        self.configuration.brain_configuration._aiml_files = BrainFileConfiguration("/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/src/test/aiml_tests/test_files/set", ".aiml", False)

class SetAIMLTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        SetAIMLTests.test_client = BasicTestClient()

    def test_name_set_topic(self):
        response = SetAIMLTests.test_client.bot.ask_question("test",  "NAME SET")
        self.assertIsNotNone(response)
        self.assertEqual(response, "OK test1")
        self.assertEqual(SetAIMLTests.test_client.bot.conversation("test").predicate("var1"), "test1")

    def test_multi_word_name_set_topic(self):
        response = SetAIMLTests.test_client.bot.ask_question("test",  "MULTI WORD NAME SET")
        self.assertIsNotNone(response)
        self.assertEqual(response, "OK test1 test2")
        self.assertEqual(SetAIMLTests.test_client.bot.conversation("test").predicate("var1 var2"), "test1 test2")

    def test_var_set_topic(self):
        response = SetAIMLTests.test_client.bot.ask_question("test",  "VAR SET")
        self.assertIsNotNone(response)
        self.assertEqual(response, "OK test2")
        self.assertEqual(SetAIMLTests.test_client.bot.conversation("test").predicate("var2"), "test2")

    def test_multi_word_var_set_topic(self):
        response = SetAIMLTests.test_client.bot.ask_question("test",  "MULTI WORD VAR SET")
        self.assertIsNotNone(response)
        self.assertEqual(response, "OK test2 test3")
        self.assertEqual(SetAIMLTests.test_client.bot.conversation("test").predicate("var2 var3"), "test2 test3")

    def test_topic_set(self):
        response = SetAIMLTests.test_client.bot.ask_question("test", "TOPIC SET")
        self.assertIsNotNone(response)
        self.assertEqual(response, "OK topic1")
        self.assertEqual(SetAIMLTests.test_client.bot.conversation("test").predicate("topic"), "topic1")

        response = SetAIMLTests.test_client.bot.ask_question("test", "TOPIC UNSET")
        self.assertIsNotNone(response)
        self.assertEqual(response, "OK")
        self.assertEqual(SetAIMLTests.test_client.bot.conversation("test").predicate("topic"), "*")

    def test_multi_word_topic_set(self):
        response = SetAIMLTests.test_client.bot.ask_question("test", "SET MULTI WORD TOPIC")
        self.assertIsNotNone(response)
        self.assertEqual(response, "OK topic2 topic3")
        self.assertEqual(SetAIMLTests.test_client.bot.conversation("test").predicate("topic"), "topic2 topic3")