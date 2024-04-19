# -*- coding: utf-8 -*-
from minineedle import needle, smith
from Levenshtein import distance
import librosa
import torchaudio
import torchaudio.transforms as T
import numpy as np

__all__ = ["Metrics"]

class Metrics:
    """
    This class include metrics that can be used to compute Elicited Imitation.

    1. Needleman-Wunsch
    2. Smith Waterman
    3. Edit Distance
    4. MFCCs 
    5. Semantic Similarity
    """
    def __init__(self):
        pass

    @staticmethod
    def needleman_wunsch(str1: str, str2: str) -> int:
        """
        Needleman-Wunsch algorithm Approach
        # NOTE: see implementation:
        https://github.com/scastlara/minineedle
        """
        alignment = needle.NeedlemanWunsch(str1.split(), str2.split())
        alignment.gap_character = "-"
        alignment.align()
        return alignment.get_score()

    @staticmethod
    def smith_waterman(str1: str, str2: str) -> int:
        """
        Smith Waterman algorithm Approach
        # NOTE: see implementation:
        https://github.com/scastlara/minineedle
        """
        alignment = smith.SmithWaterman(str1.split(), str2.split())
        alignment.gap_character = "-"
        alignment.align()
        return alignment.get_score()
    
    @staticmethod
    def edit_distance(str1:str, str2:str) -> int:
        """
        An Edit Distance Approach
        # NOTE: see this implemetation:
        https://rapidfuzz.github.io/Levenshtein/levenshtein.html#distance

        # NOTE: the use of mecab renders more distances
        """
        return distance(str1, str2)

    def sentence_similarity():
        """
        SentenceBert Approach
        """
        pass
    
   

class NeedlemanWunsch:
    """
    An old implementation of NeedlemanWunsch we are no longer using.
    """
    def __init__(self):
        pass

    def align_sequences(self, s1, s2):
        score = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 or j == 0:
                    score[i][j] = 0
                elif s1[i-1] == s2[j-1]:
                    score[i][j] = score[i-1][j-1] + 1
                else:
                    score[i][j] = max(score[i-1][j], score[i][j-1])

        aligned_s1 = []
        aligned_s2 = []
        i, j = len(s1), len(s2)
        while i > 0 or j > 0:
            if i > 0 and (j == 0 or score[i][j] == score[i-1][j]):
                aligned_s1.append(s1[i-1])
                aligned_s2.append("-")
                i -= 1
            elif j > 0 and (i == 0 or score[i][j] == score[i][j-1]):
                aligned_s1.append("-")
                aligned_s2.append(s2[j-1])
                j -= 1
            else:
                aligned_s1.append(s1[i-1])
                aligned_s2.append(s2[j-1])
                i -= 1
                j -= 1

        return aligned_s1[::-1], aligned_s2[::-1]
    
    def elicited_imitation(self, source, target):
        original_words = source.split()
        imitation_words = target.split()
        
        # Align the two sequences
        aligned_original, aligned_imitation = self.align_sequences(original_words, imitation_words)
        matching_words = 0
        
        for o_word, i_word in zip(aligned_original, aligned_imitation):
            if o_word == i_word:
                matching_words += 1

        # Compute accuracy
        accuracy = (matching_words / len(original_words)) * 100
        scaled_accuracy= round(accuracy / 10)
        return accuracy, scaled_accuracy, matching_words, len(original_words)