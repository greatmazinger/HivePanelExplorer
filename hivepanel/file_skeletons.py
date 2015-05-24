'''
created  05/15/2014

by sperez

Contains skeletons of files needed to make hive panel files.
'''

parameters_file = '''  // ****************************************** //


 //         USER DEFINED PARAMETERS            //


// ****************************************** //

var numAxes = {0}
    doubleAxes = {1}

var nodeColor = 'darkgrey'
    edgeColor = ['darkgrey']
    linkwidth = 1.2
    oplink = 0.3
    opnode = 0.2
    opnode_more = 0.6
    nodesize = 5
    nodestroke = 0.2
    nodestrokecolor = "grey"

var columntraits = [{2}];
    rowtraits = [{3}];

var columnTraitScales = {{{4}}}
var rowTraitScales = {{{5}}}'''




html_file = '''<!comment This is a hive panel developed using HivePlotter.>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link type="text/css" rel="stylesheet" href="panel_style.css"/>
    </head>
    <body>
        <script src="d3.v3.min.js"></script>
        <script src="d3.hive.v0.min.js"></script>
        <div id="container">
            <div id="title">
                <div id="thetitle" class="darktext"></div>
                <div id="info" class="darktext"></div>
            </div>
            <div id="panel"></div>
            <div id="search">
                <center>
                    <form>
                        <input type="text" id="lostNode" size="25" />
                        <input value="Search" onclick="show_node();" type="button" class="darktext" />
                    </form>
                </center>
            </div>
            <div id="revealwrapper">
                <div id="reveal"></div>
            </div>
            <div id="controlpanel" class="darktext">
                <form action="" class="darktext rules" id="ruleForm1" name = "ruleForm" >If a
                    <select id="node_or_link1" onchange="update_properties(this)" class="darktext">
                        <option>node</option>
                        <option>link</option>
                    </select>'s
                    <select id="property1" onchange="update_values(this)" class="darktext" maxwidth="5px">
                        <option>property</option>
                    </select>
                    <select id="equality1" class="darktext">
                        <option>=</option>
                    </select>
                    <select id="value1" class="darktext">
                        <option>value</option>
                    </select>, color:
                    <input type="text" id="node_color1" size="7" value="" />
                    <input value="Highlight" id="ruleButton1" name = "ruleButton" onclick="color_filter_or_undo(this);" type="button" class="darktext highlight" />
                </form>
                <form action="" class="darktext leftrule">
                    <input value="Add coloring rule" id="addColorRule" onclick="add_rule(this);" type="button" class="darktext addbutton" />
                </form>
                <form action="" class="darktext">
                    <input value="Add filtering rule" id="addFilterRule" onclick="add_rule(this);" type="button" class="darktext filter addbutton" />
                </form>
            </div>
        </div>
        <script src="{0}_nodes.js"></script>
        <script src="{0}_edges.js"></script>
        <script src="{0}_parameters.js"></script>
        <script src="panel_methods.js"></script>
    </body>
</html>'''