# -*- coding: utf-8 -*-

import unittest

from ei.metrics import NeedlemanWunsch


class TestNeedlemanWunsch(unittest.TestCase):
    n = NeedlemanWunsch()
    def test_align_sequences(self):
        
        gold = "cat"
        transcript = "cats"
        res = self.n.align_sequences(gold, transcript)
        output = (['c', 'a', 't', '-'], ['c', 'a', 't', 's'])
        self.assertEqual(res, output)
    
    def test_elicited_imitation(self):
        source = '大学 に 授業 料 を 下げ て もらい たい です 。'
        target = '大学 に 授業 を もらい たい です 。'
        word_accuracy, scaled_accuracy, correct_words, total_words = self.n.elicited_imitation(source, target)
        
        self.assertEqual((word_accuracy, scaled_accuracy, correct_words, total_words), (72.72727272727273, 7, 8, 11))



if __name__ == '__main__':
    unittest.main()
