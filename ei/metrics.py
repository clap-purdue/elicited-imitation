# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np


class NeedlemanWunsch:
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





class EditDistance:
    """
    An Edit Distance Approach
    """

    pass


class ElicitedImitation:
    """
    An Needleman-Wunsch algorithm Approach
    """

    pass


class SentenceSimilarity:
    """
    SentenceBert Approach
    """

    pass


# def word_level_edit_distance(s1, s2):
#     words1, words2 = s1.split(), s2.split()
#     m, n = len(words1), len(words2)
#     dp = np.zeros((m + 1, n + 1), dtype=int)

#     for i in range(m + 1):
#         for j in range(n + 1):
#             if i == 0:
#                 dp[i][j] = j
#             elif j == 0:
#                 dp[i][j] = i
#             elif words1[i - 1] == words2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

#     visualize_matrix(dp, words1, words2)
#     return dp[m][n]


# def visualize_matrix(matrix, words1, words2):
#     fig, ax = plt.subplots()
#     cax = ax.matshow(matrix, cmap="viridis_r")

#     ax.set_xticklabels([""] + words1, rotation=45)
#     ax.set_yticklabels([""] + words2)
#     ax.xaxis.set_major_locator(plt.MultipleLocator(1))
#     ax.yaxis.set_major_locator(plt.MultipleLocator(1))

#     for (i, j), z in np.ndenumerate(matrix):
#         ax.text(
#             j,
#             i,
#             f"{z}",
#             ha="center",
#             va="center",
#             bbox=dict(boxstyle="round", facecolor="white", edgecolor="0.3"),
#         )

#     plt.xlabel("Transcript")
#     plt.ylabel("Gold Standard")
#     plt.title("Edit Distance Matrix")
#     plt.colorbar(cax)
#     st.pyplot(fig)

# if __name__ == "__main__":

#     gold = "she had your dark suit in greasy washwater all year."
#     transcript = "she had your dark suit"
#     n = NeedlemanWunsch()
#     n.align_sequences(gold, transcript)

    # word_dist = word_level_edit_distance(transcript, gold)
    # print(f"Word-level edit distance: {word_dist}")
