# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np


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


def word_level_edit_distance(s1, s2):
    words1, words2 = s1.split(), s2.split()
    m, n = len(words1), len(words2)
    dp = np.zeros((m + 1, n + 1), dtype=int)

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif words1[i - 1] == words2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    visualize_matrix(dp, words1, words2)
    return dp[m][n]


def visualize_matrix(matrix, words1, words2):
    fig, ax = plt.subplots()
    cax = ax.matshow(matrix, cmap="viridis_r")

    ax.set_xticklabels([""] + words1, rotation=45)
    ax.set_yticklabels([""] + words2)
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))

    for (i, j), z in np.ndenumerate(matrix):
        ax.text(
            j,
            i,
            f"{z}",
            ha="center",
            va="center",
            bbox=dict(boxstyle="round", facecolor="white", edgecolor="0.3"),
        )

    plt.xlabel("Transcript")
    plt.ylabel("Gold Standard")
    plt.title("Edit Distance Matrix")
    plt.colorbar(cax)
    st.pyplot(fig)


# gold = "she had your dark suit in greasy washwater all year."
# transcript = "she had your dark suit"

# word_dist = word_level_edit_distance(transcript, gold)
# print(f"Word-level edit distance: {word_dist}")
