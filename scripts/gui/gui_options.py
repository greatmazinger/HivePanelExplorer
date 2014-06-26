'''
created  20/06/2014

by sperez

stores options for input of menus in gui
'''

colors = {}
colors['red'] = ['#a30000', '#730000', '#b80000', '#660000', '#cc0000', '#520000', '#e00000', '#3d0000', '#ff0a0a', '#290000', '#ff3333' ]
colors['blue'] = ['#0000a3', '#0000b8', '#00008f', '#0000cc', '#00007a', '#0000e0', '#0000f5', '#0000ff', '#1f1fff', '#3333ff', '#4747ff']
colors['green'] = ['#00a300', '#008f00', '#002900', '#006600', '#008000', '#005200', '#00b800', '#003d00', '#00cc00', '#00e000', '#33ff33']
colors['purple'] = ['#8f008f', '#a300a3', '#800080', '#b800b8', '#660066', '#cc00cc', '#520052', '#e000e0', '#3d003d', '#290029', '#ff0aff']
colors['yellow'] = ['#666600', '#7a7a00', '#525200', '#8f8f00', '#3d3d00', '#cccc00']
colors['grey'] = ['#5c5c5c', '#525252', '#666666', '#474747', '#707070', '#3d3d3d', '#7a7a7a', '#333333', '#808080', '#292929', '#8f8f8f']
colors['cyan'] = ['#00a3a3', '#00b8b8', '#00cccc', '#008f8f', '#00e0e0', '#007a7a', '#00f5f5', '#006666', '#70ffff', '#005252', '#40bfbf']
colors['orange'] = ['#8f5d00', '#a36a00', '#b87700', '#7a5000', '#cc8500', '#664200', '#e09200', '#523500', '#f59f00', '#3d2800', '#ffa500']

colorOptions = colors.keys()

debugOptions = ['True', 'False']

axesOptions = [2,3,4,5]

doubleOptions = ['True', 'False']

assignmentOptions = ['degree', 'betweeness', 'clustering', 'centrality']

positionOptions = ['degree', 'betweeness', 'clustering', 'centrality']

edgeStyleOptions = ['uniform']