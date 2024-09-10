#!/usr/bin/env python3
""" Module for testing GithubOrgClient """

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(TestCase):
    """ Class for Testing GithubOrgClient """

    @parameterized.expand([
        ('google', {'org': 'google'}),
        ('abc', {'org': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """ Test that GithubOrgClient.org returns the correct value """
        # Set up the mock to return a dictionary with the 'org' key
        mock_get_json.return_value = {'org': org}
        
        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org)
        
        # Assert that org method returns the expected value
        self.assertEqual(client.org, {'org': org})
        
        # Verify get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org}')
