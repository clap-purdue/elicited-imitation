# -*- coding: utf-8 -*-

import unittest
import random
from gricean_pragmatics.metrics import GPMetrics


class TestGPMetrics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set the seed for random module
        random.seed(42)

    def test_calculate_naturalness(self):
        
        utterance_surprisal = 2.5
        interpretation_a_surprisal = 3.8
        interpretation_b_surprisal = 2.9
        result = GPMetrics.calculate_naturalness(utterance_surprisal, interpretation_a_surprisal, interpretation_b_surprisal)
        output = {'difference_a': 1.2999999999999998, 'difference_b': 0.3999999999999999, 'preferred_interpretation': 'b'}
        self.assertEqual(result, output)

    def test_calculate_ssm(self):
        
        embedding_a = [1, 2, 3]
        embedding_b = [2, 3, 4]
        embedding_c = [3, 4, 5]
        result = GPMetrics.calculate_ssm(embedding_a, embedding_b, embedding_c)
        
        # Expected output
        expected_similarity_ab = 0.993
        expected_similarity_bc = 0.997
        #expected_ranking = 
        
        # Use assertAlmostEqual for floating-point comparisons
        self.assertAlmostEqual(result['similarity_ab'], expected_similarity_ab, places=2)
        self.assertAlmostEqual(result['similarity_bc'], expected_similarity_bc, places=2)
        #self.assertEqual(result['ranking'], expected_ranking)  

    def test_evaluate_prc(self):
        
        llm_responses = [
            "The speaker said 'some', which can mean one or more, including all.",
            "You can say 'I ate some of the cookies' even if you ate them all.",
            "But if you had eaten them all, and that was important, you would have said 'all'.",
            "The fact that the speaker didn't say 'all' implies that 'all' doesn't hold.",
            "This leads to the interpretation 'I ate some, but not all'."
        ]

        expected_steps = [
            "The speaker said 'some'. It literally means 'one or more, possibly all.' Thus, 'some' is logically compatible with 'all'.",
            "You can say 'I ate some of the cookies' even when you ate them all.",
            "However, if you in fact ate them all and if that is relevant to the purpose of the current exchange, S would have said 'all'.",
            "The fact that S didn’t choose 'all' then implicates that the stronger 'all' proposition doesn’t hold.",
            "This results in the interpretation 'I ate some, but not all'."
        ]

        result = GPMetrics.evaluate_prc(llm_responses, expected_steps)
        #output = {'accuracy': 0.0, 'step_scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
        self.assertAlmostEqual(result['accuracy'], 0.0, places=2)
        self.assertAlmostEqual(result['step_scores'], [0.0, 0.0, 0.0, 0.0, 0.0])

    def test_calculate_irr(self):

        successful_recoveries = 3
        total_errors = 5

        irr = GPMetrics.calculate_irr(successful_recoveries, total_errors)
        self.assertAlmostEqual(irr, 0.60, places=2)


    def test_calculate_psi(self):
        original_accuracy = 0.85  # 85% accuracy in original context
        changed_accuracy = 0.70   # 70% accuracy after subtle contextual changes

        psi = GPMetrics.calculate_psi(original_accuracy, changed_accuracy)
        self.assertAlmostEqual(psi, 0.15, places=2)
        

if __name__ == '__main__':
    unittest.main()



