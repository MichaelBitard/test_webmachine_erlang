# -*- coding: utf-8 -*-
 
#!/usr/bin/python
import requests
import unittest
 
class TestPaperAPI(unittest.TestCase):
 
    def setUp(self):
        self.base_url = "http://localhost:8000"
        self.paper_url = "http://localhost:8000/paper/"
        self.json_headers ={"Content-Type" : "application/json", "Accept" : "application/json"}
        self.new_paper = {"title": "ABC"}
        self.new_paper2 =  {"title": "DEF"}

    def test_get_on_root_returns_html_hello_world(self):
        resp = requests.get(self.base_url)
        self.assertEqual(resp.content, "<html><body>Hello, new world</body></html>")

    def test_get_on_paper_returns_id_in_html(self):
        for id in 1,2,3:
            resp = requests.get(self.paper_url + str(id))
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.content, "<html><body>" + str(id) + "</body></html>")

