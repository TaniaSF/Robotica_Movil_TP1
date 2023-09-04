'''
Created on Aug 23, 2023

@author: seb
'''

import matplotlib.pyplot as plt
import numpy as np

def draw_triangle(side_length):
    # Define the vertices of the triangle
    vertices = np.array([[0, 0], [side_length, 0], [side_length / 2, side_length * np.sqrt(3) / 2]])

    # Close the triangle by repeating the first vertex at the end
    vertices = np.vstack([vertices, vertices[0]])

    # Extract x and y coordinates for plotting
    x, y = vertices.T

    # Plot the triangle
    plt.plot(x, y)

    # Set axis limits and labels
    plt.xlim(-0.1 * side_length, 1.1 * side_length)
    plt.ylim(-0.1 * side_length, 1.1 * side_length)
    plt.xlabel('X')
    plt.ylabel('Y')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    draw_triangle(100)
