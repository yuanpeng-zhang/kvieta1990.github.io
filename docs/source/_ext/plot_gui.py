from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils import nodes
import os
import sys
import json
from importlib import import_module

class PlotGUI(Directive):
    """
    Similar to Figure class, but it generates the image before.
    It requires a module and a function that will generate the plot.
    It accepts arguments to pass to the function.
    It assumes ../images is a folder with write access, that contains
    images
    """

    required_arguments = 3
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'alt': directives.unchanged,
                   'height': directives.unchanged,
                   'width': directives.unchanged,
                   'scale': directives.nonnegative_int,
                   'align': directives.unchanged,
                   'name': directives.unchanged,
                   'function_parameters': directives.unchanged,
                   }
    has_content = True


    def run(self):
        module_name, function_name, output_filename = self.arguments
        mod = import_module(module_name)
        image_function = getattr(mod, function_name)
        
        params_str = self.options.pop('function_parameters', None)
        params = dict()
        if params_str:
            params = json.loads(params_str)
        
        image_folder = os.path.dirname(__file__)
        output_filename = os.path.basename(output_filename)
        image_function(os.path.join(image_folder, '../images', output_filename), **params)



        paragraph_node = []#[nodes.paragraph(text=template)]
        reference = directives.uri(f'images/{output_filename}')
        self.options['uri'] = reference
        
        align = self.options.pop('align', None)
        
        figure_node = nodes.figure(self.block_text,nodes.image('',
                                 **self.options))
        if align:
            figure_node['align'] = align                         

        if self.content:
            node = nodes.Element()          # anonymous container for parsing
            self.state.nested_parse(self.content, self.content_offset, node)

            first_node = node[0]
            if isinstance(first_node, nodes.paragraph):
                caption = nodes.caption(first_node.rawsource, '',
                                        *first_node.children)
                caption.source = first_node.source
                caption.line = first_node.line
                figure_node += caption

        self.add_name(figure_node)
        paragraph_node.append(figure_node)
        return paragraph_node

def mark_plot_labels(app, document):
    """
    To make plots referenceable, we need to move the reference from
    the "htmlonly" (or "latexonly") node to the actual figure node
    itself.
    """
    print('Function called')
    for name, explicit in document.nametypes.items():
        print(name,explicit)
        if not explicit:
            continue
        labelid = document.nameids[name]
        if labelid is None:
            continue
        node = document.ids[labelid]
        if node.tagname in ('html_only', 'latex_only'):
            for n in node:
                if n.tagname == 'figure':
                    sectname = name
                    for c in n:
                        if c.tagname == 'caption':
                            sectname = c.astext()
                            break

                    node['ids'].remove(labelid)
                    node['names'].remove(name)
                    n['ids'].append(labelid)
                    n['names'].append(name)
                    document.settings.env.labels[name] = \
                        document.settings.env.docname, labelid, sectname
                    break

def setup(app):
    app.add_directive("plot_gui", PlotGUI)
#    app.connect('doctree-read', mark_plot_labels)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
