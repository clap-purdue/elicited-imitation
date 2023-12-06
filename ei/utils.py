# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import os


def plot(data, output_dir):
    plt.figure(figsize=(20, 10))

    plt.plot(data['audio'], data['score'], label='Score', marker='o')
    plt.plot(data['audio'], data['scaled_accuracy'], label='Scaled Accuracy', marker='x')

    plt.title('Score vs Scaled Accuracy with Audio Names')
    plt.xlabel('Audio Sample')
    plt.ylabel('Value')
    plt.xticks(rotation=90)
    plt.legend()
    plt.grid(True)
    plt.tight_layout() 
    plt.savefig(os.path.join(output_dir, 'ei_plot.png'))