# VizLabPG4
# Hunter Turner, Alexander Gjurich, Jake Ballenger, David Romagnuolo [Group 4]

# https://github.com/3155-Project-Group-4/VizLabPG4.git

# Looking at the # Preparing data comments in each chunk of source code we can find various references to the actual data represented within each graph, bars in the stack bar chart and all three lines in the multi line chart. Firstly the stack bar chart includes a go.Bar for each bar shown in the final graph, with each having the three fields passed in. Next the line chart has a single line referencing the actual line of data shown later with go.Scatter, and again the confirmed field passed in. Further in the Multi line chart there is a similar method to the single line chart, but with more of the same line under different traces, similar to the traces in the box chart. The bubble chart functions a bit differently with the all data being fed through a function at different times to create the separate identities, with the only difference being the fields passed in. Lastly, the heatmap reflects data in a different way than previous graphs but is functionally similar to the bubbles. Each square is again run through the exact same function, but with different fields, only this time the organization of data is by a fixed unit of time - 7 days of the week and 4 weeks of the month.

# [2] Designates a bar that has a NOC x axis and a Total y axis

# [3] Designates 3 bars that correspond to each total of gold, silver and bronze medals

# [4] Designates scatter points with month on the x axis and max temps on the y axis, these points are then connected by a line

# [5] Designates scatter points with month on the x axis and max, min ,and mean temps on the y axis, these points are then connected by separate lines

# [6] Designate a grid of with temperature on the y axis and month on the x axis. Using a color chart on the x axis with bubbles plotted to display the average minimum and maximum temperatures in each month.

# [7] Designates a grid of the highest maximum temperatures with month on the y axis and the day of the week on the x axis. There is a bar on the right with the colours based on max temperature , which are plotted on the heat map.

# Using plotly as the package for our gui solution takes a large amount of the effort from developing an actual scalable gui and transfers it to the organization of our data prior to delivery. The process for creating each type of visualization is documented within plotly and is routine for the creation of multiple graphs for a large amount of data. Outside of development, the usefulness of visualizations and graphics are tremendous when attempting to convey information. Our topic with coronavirus is no different, the graphs allow for an easily digestible medium of information for the readers - while at the same time streamlining the process of their creation.

~~~~~
