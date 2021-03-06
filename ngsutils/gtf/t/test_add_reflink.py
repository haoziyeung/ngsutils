#!/usr/bin/env python
'''
Tests for gtfutils / add_reflink
'''

import os
import unittest
import StringIO

import ngsutils.gtf.add_reflink

gtf = os.path.join(os.path.dirname(__file__), 'test-iso.gtf')
reflink = os.path.join(os.path.dirname(__file__), 'test-reflink.txt')


class GTFAddReflinkTest(unittest.TestCase):
    def testAddReflink(self):
        valid = '''\
chr1|test|gene|1001|1100|0|+|.|gene_id "foo1"; transcript_id "txpt1"; gene_name "gene1"; isoform_id "iso1";
chr1|test|gene|1051|1100|0|+|.|gene_id "foo1"; transcript_id "txpt2"; gene_name "gene1"; isoform_id "iso1";
chr1|test|gene|2001|2100|0|+|.|gene_id "foo2"; transcript_id "txpt3"; gene_name "gene2"; isoform_id "iso2";
chr1|test|gene|3001|3100|0|+|.|gene_id "foo3"; transcript_id "txpt4"; gene_name "gene3"; isoform_id "iso3";
'''
        out = StringIO.StringIO('')
        ngsutils.gtf.add_reflink.gtf_addreflink(gtf, reflink, out=out, quiet=True)
        self.assertEquals(out.getvalue().replace('\t', '|'), valid)

if __name__ == '__main__':
    unittest.main()
