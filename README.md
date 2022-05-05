# Final Project - Searchfinding algorithms

We build pathfinding game as a final project for Intro to AI course at the University of New Haven. The project covers some of the search algorithms that we covered in class. Throughtout the project we use pyhthon and it's modules to build algorithms, vizualisations and interface.

### Instructions
We have included a requirements.txt for dependencies and versions. Here are the instructions on how to run the program: 

- Navigate to scr folder and run main.py
- Select grid size and search algorithm
- Select start and goal 
- Confirm your selection and the grid will appear
- Click and hold left mouse to add walls to the grid
- Press SPACEBAR to start the visualization 


**Tools used:** 
- Tkinter: To create a window with different options for the user to select which search technique and grid size to use.
- Pygame: Generates the actual visualization of the search algorithm in progress 

We used Pygame to create the visualizations since two of us has a little bit of experience in working with Pygame. Other vizualization tools might have worked better but since we didn't have any experience in other tools or libraries Pygame did well for us.


### Tkinter
For the interface, we used tkinter library that is included with Python. We needed an interface to capture user input and Tkinter seemed like a good choice since there is a lot of resoures for it and it is simple to use. We also helped ourselfs with stackoverflow

### PyGame 
Creating the grid in PyGame was one the easier parts of this project. It was fairly simple to generate a grid window with the draw.line method in PyGame. The only slightly tricky thing was converting locations on the PyGame grid to indices in the matrix used in the search algorithm.



### Conclusion

While working on the final project we learned a lot about the practical implementation of search algorithms tat we covered in class such as BFS, DFS and A*. Rather htan just learning theory behind the algorithms, working on a real work implementation helped understand the algorithms more clearly. We all can't wait to apply the skilled learned in this project in our future academic and professional projects.

