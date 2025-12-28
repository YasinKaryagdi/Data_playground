# Icon Viewer
Inspired by The Icon Viewer by Karel Martens. The goal of the project is to preprocess the frames that a camera captures, and to display these frames afterwards. 

## Current issues
Flexibility comes at the cost of computational recources. 
I want the ability to change between certain configurations, therefore I'm going with a class based approach where I can modify members in order to decide what to draw within the cells. This allows for easy experimentation with the various configurations.

This comes with additional overhead though and I'll most likely skip this for the final product in order to optimize the computation. The current class based approach will still be supported, which can be used to experiment with the various adjustable arguments.