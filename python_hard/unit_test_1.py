# -*- coding:utf-8 -*-
import unittest
#lianxi
from python_hard.unit_test import Dict


class TestDict(unittest.TestCase):

    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEquals(d.a,1)
        self.assertEquals(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEquals(d.key,'value')

    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'],'value')

    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(KeyError):
            value=d['empty']

    def test_attrituteerr(self):
        d=Dict()
        with self.assertRaises(AttributeError):
            value=d.empty

    def setUp(self):
        print("setUP...")

    def tearDown(self):
        print("tearDown...")

if __name__=='__main__':
    unittest.main()




