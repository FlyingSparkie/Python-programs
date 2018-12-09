# tkuibuilder.py
#
# PURPOSE
#   Classes to simplify inside-out assembly of frames and other widgets
#   into a Tkinter application UI.
#
# NOTES
#   1. Revision history is maintained in the file CHANGELOG.rst.
#
# AUTHORS
#   Dreas Nielsen (RDN)
#
# COPYRIGHT AND LICENSE
#   Copyright (c) 2018, R.Dreas Nielsen
#   This program is free software: you can redistribute it and/or modify it 
#   under the terms of the GNU General Public License as published by the Free 
#   Software Foundation, either version 3 of the License, or (at your option) 
#   any later version. This program is distributed in the hope that it will be 
#   useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General 
#   Public License for more details. The GNU General Public License is available 
#   at http://www.gnu.org/licenses/.
#
#===============================================================================

"""Provides the AppLayout class to simplify inside-out assembly of frames and 
other widgets to create a Tkinter UI.
"""

__version__ = '1.0.0'

try:
    import Tkinter as tk
except:
    import tkinter as tk

import uuid



def replist(input_list, length):
    """ Return a list that is *at least* 'length' long by repeating 'input_list'
    as many times as necessary.
    """
    if len(input_list) < length:
        output_list = []
        while len(output_list) < length:
            output_list.extend(input_list)
        return output_list
    return input_list

class AppLayoutError(Exception):
    pass

class AppLayout(object):
    """Represents the structure of Tkinter widgets (e.g., frames) and provides
    methods to create and populate the nested set of frames.
    """
    class Element(object):
        """An Element object describes one Tkinter element--a Frame or other widget.

        An Element object consists of:
           * A list of component names (names are strings).
           * A dictionary of configuration values for the frame that will contain the components.
           * A dictionary of gridding options for the frame that will contain the components.
           * A string indicating whether the component elements are arranged horizontally, vertically, or on parallel pages.
           * A weight or list of weights for the rows or columns represented
             by the components.  If this list is shorter than the list of
             components, its members will be recycled as many times as necessary
             so that there is a weight for each component.  The default is [1].
           * The weight for the column or row in which all of the elements appear.
        """

        arrangements = {"vertical", "horizontal", "paged"}

        def __init__(self, components, config_dict=None, grid_opts=None, arrangement="vertical", component_weights=[1], element_weight=1):
            """Assign all data values to the new Element object."""
            if arrangement not in self.arrangements:
                raise AppLayoutError("Unrecognized arrangement: %s." % arrangement)
            self.components = components
            self.config_dict = config_dict
            self.grid_opts = grid_opts
            self.arrangement = arrangement
            self.component_weights = component_weights
            self.element_weight = element_weight
            self.frame = None              # Will be assigned by create_layout()

    def __init__(self):
        """Create a new AppLayout object.

        After initialization, a series of calls should be made to the
        'column_elements()' and 'row_elements()' methods to describe the layout
        of the UI.  Then the 'create_layout()' method should be called to
        create the frames for the specified layout.  Finally, the 'build_elements()'
        method should be called to populate each frame with widgets as appropriate.
        """
        # The partslist is a dictionary of Element objects.  The keys of this
        # dictionary may be component names for some elements.
        self.partslist = {}
        # synthnames is a list of all names synthesized by this class and which
        # therefore should not have a user-provided build function.
        self.synthnames = []
        # master_element_name is the name of the top-level element, and is
        # assigned by the create_layout method.
        self.master_element_name = None

    def column_elements(self, element_names, config_dict=None, grid_dict=None, row_weights=[1], column_weight=1):
        """Takes a list of names of elements to be vertically arranged, creates a new element
        that encloses those, and returns a synthesized name for the element that is created.
        
        :param element_names: A list of names (strings) of elements.
        :param config_dict: A dictionary of configuration specifications for the frame that will
                             contain the named elements.
        :param grid_dict: A dictionary of gridding options for the frame that will contain
                          the named elements.
        :param row_weights: A list of weights for the rows of the frame that will contain the
                            named elements.  If this list is shorter than the *element_names*
                            list, its members will be recycled when assigning weights.
        :param column_weight: A weight for the single column in the frame that will contain
                              the named elements.
        :return: A name (string) that is automatically assigned to the element that is created
                 to contain the named elements.  This name may be used in the *element_names*
                 argument to subsequent calls to *column_elements()*, *row_elements()*.
                 or *page_elements*.
        """
        wts = replist(row_weights, len(element_names))
        el = self.Element(element_names, config_dict, grid_dict, "vertical", component_weights=wts, element_weight=column_weight)
        el_id = uuid.uuid4()
        self.partslist[el_id] = el
        self.synthnames.append(el_id)
        for n in element_names:
            if n not in self.synthnames:
                el_n = self.Element(None)
                self.partslist[n] = el_n
        return el_id

    def row_elements(self, element_names, config_dict=None, grid_dict=None, column_weights=[1], row_weight=1):
        """Takes a list of names of elements to be horizontally arranged, creates a new element
        that encloses those, and returns a synthesized name for the element that is created.
        
        :param element_names: A list of names (strings) of elements.
        :param config_dict: A dictionary of configuration specifications for the frame that will
                             contain the named elements.
        :param grid_dict: A dictionary of gridding options for the frame that will contain
                          the named elements.
        :param column_weights: A list of weights for the columns of the frame that will contain the
                               named elements.  If this list is shorter than the *element_names*
                               list, its members will be recycled when assigning weights.
        :param row_weight: A weight for the single row in the frame that will contain
                           the named elements.
        :return: A name (string) that is automatically assigned to the element that is created
                 to contain the named elements.  This name may be used in the *element_names*
                 argument to subsequent calls to *column_elements()*, *row_elements()*.
                 or *page_elements*.
        """
        wts = replist(column_weights, len(element_names))
        el = self.Element(element_names, config_dict, grid_dict, "horizontal", component_weights=wts, element_weight=row_weight)
        el_id = uuid.uuid4()
        self.partslist[el_id] = el
        self.synthnames.append(el_id)
        for n in element_names:
            if n not in self.synthnames:
                el_n = self.Element(None)
                self.partslist[n] = el_n
        return el_id

    def page_elements(self, element_names, config_dict=None, grid_dict=None):
        """Takes a list of names of elements to be arranged on separate pages or panes
        (e.g., pages of a Notebook widget), creates a new element that contains
        those, and returns a synthesized name for the element that is created.
        
        :param element_names: A list of names (strings) of elements.
        :param config_dict: A dictionary of configuration specifications for the frame that will
                             contain the named elements.
        :param grid_dict: A dictionary of gridding options for the frame that will contain
                          the named elements.
        :return: A name (string) that is automatically assigned to the element that is created
                 to contain the named elements.  This name may be used in the *element_names*
                 argument to subsequent calls to *column_elements()*, *row_elements()*,
                 or *page_elements*.
        """
        el = self.Element(element_names, config_dict, grid_dict, "paged")
        el_id = uuid.uuid4()
        self.partslist[el_id] = el
        self.synthnames.append(el_id)
        for n in element_names:
            if n not in self.synthnames:
                el_n = self.Element(None)
                self.partslist[n] = el_n
        return el_id

    def create_layout(self, master_widget, master_element_name, row=0, column=0, row_weight=1, column_weight=1):
        """Creates a nested set of frames corresponding to the application layout that has been specified.

        The application layout must have been previously described by calls to the ``column_elements``,
        ``row_elements``, and ``page_elements`` methods.

        :param master_widget: A container widget (e.g., Frame) that will serve as the root for all the frames to be created.
        :param master_element_name: The name of the element to be placed in the top-level frame.  This name must be one of those supplied to 'row_elements()' or 'column_elements()', or returned by those methods.
        :param row: The row number within the master_widget for the top-level frame that will be created.  Optional; defaults to 0.
        :param column: The column number within the master widget for the top-level frame that will be created.  Optional; defaults to 0.
        :param row_weight: The row weight for the frame's row in the master_widget.  Optional; defaults to 1.
        :param column_weight: The column weight for the frame's column in the master widget.  Optional; defaults to 1.
        """
        if self.master_element_name is not None:
            return
        def layout_element(parent, name):
            el = self.partslist[name]
            el.frame = tk.Frame(parent)
            if el.config_dict is not None:
                el.frame.configure(**el.config_dict)
            el.frame.grid(row=row, column=column, sticky=tk.NSEW)
            if el.grid_opts is not None:
                el.frame.grid(**el.grid_opts)
            if el.components is not None:
                for i, comp in enumerate(el.components):
                    layout_element(el.frame, comp)
                    compframe = self.partslist[comp].frame
                    if el.arrangement == "vertical":
                        compframe.grid(row=i, column=0)
                        el.frame.rowconfigure(i, weight=el.component_weights[i])
                    elif el.arrangement == "horizontal":
                        compframe.grid(row=0, column=i)
                        el.frame.columnconfigure(i, weight=el.component_weights[i])
                if el.arrangement == "vertical":
                    el.frame.columnconfigure(0, weight=el.element_weight)
                elif el.arrangement == "horizontal":
                    el.frame.rowconfigure(0, weight=el.element_weight)
        layout_element(master_widget, master_element_name)
        master_widget.rowconfigure(row, weight=row_weight)
        master_widget.columnconfigure(column, weight=column_weight)
        self.master_element_name = master_element_name

    def frame(self, element_name):
        """Returns the frame for the given element name.
        
        The frame will only be valid after the 'create_layout()' method has been called.
        """
        if self.master_element_name is None:
            raise AppLayoutError(u"The layout has not been created yet, so no frames have been created, and thus there is no frame %s." % element_name)
        return self.partslist[element_name].frame

    def frame_widgets(self, element_name):
        """Returns a list of all widgets within the frame for the given element name.
        The list will only be populated if the 'create_layout()' method has been called
        and then a suitable 'build' function has been called for this element."""
        return self.frame(element_name).winfo_children()

    def build_element(self, element_name, build_function):
        """Runs the specified build_function to populate the frame identified by element_name.

        The 'create_layout()' method must have been called so that elements have
        frames assigned.  A build_function cannot be applied to an element that is synthesized
        by the AppLayout object (i.e., a name returned by 'column_elements()' or 'row_elements()').
        
        :param element_name: A user-assigned name for one of the layout elements.
        :param build_function: A callback function that takes a Frame as an argument and populates that frame with widgets to implement the specific layout element.
        """
        if self.master_element_name is None:
            raise AppLayoutError(u"The layout has not been created yet, so no layout elements can be built.")
        if element_name in self.synthnames:
            raise AppLayoutError(u"A build function cannot be applied to an automatically created frame (%s)." % element_name)
        element = self.partslist[element_name]
        build_function(element.frame)

    def build_elements(self, build_functions):
        """Populates a group of UI elements with widgets.
        
        :param build_functions: A dictionary where the keys are element names and the values are functions that 
                                take a frame as an argument and adds widgets or otherwise prepares that frame for display and use.
        
        The 'create_layout()' method must have been previously called so that elements have frames assigned.
        """
        for element_name in build_functions.keys():
            self.build_element(element_name, build_functions[element_name])

    def layout_as_json(self, show_attributes=False):
        """Return a representation of the structure as a JSON string.  Attribute names values may optionally be included.
        
        This is intended primarily for debugging.
        
        :return: A string formatted as JSON.
        """
        if self.master_element_name is None:
            raise AppLayoutError(u"The layout has not been created yet, so no JSON representation can be produced.")
        indent = 1
        indentstr = u"    "
        json = u"{"
        def describe_element(json_str, element_name, element_no, total_elements, indent, show_attributes):
            el = self.partslist[element_name]
            json_str = u'%s\n%s"%s" : {' % (json_str, indentstr*indent, element_name)
            if (el.components and len(el.components) > 0) or show_attributes:
                if show_attributes:
                    json_str = u'%s\n%s"attributes": {' % (json_str, indentstr * (indent+1))
                    for i, att in enumerate(self.partslist[element_name].frame.keys()):
                        json_str = u'%s\n%s"%s": "%s"' % (json_str, indentstr * (indent+2), att, self.partslist[element_name].frame.cget(att))
                    for i, att in enumerate(self.partslist[element_name].frame.grid_info().keys()):
                        if att != 'in':
                            json_str = u'%s\n%s"%s": "%s"' % (json_str, indentstr * (indent+2), att, self.partslist[element_name].frame.grid_info()[att])
                            if i < len(self.partslist[element_name].frame.grid_info().keys()) - 1:
                                json_str += u","
                    json_str = u"%s\n%s}" % (json_str, indentstr*(indent+1))
                    if el.components and len(el.components) > 0:
                        json_str += u","
                if el.components and len(el.components) > 0:
                    json_str = u'%s\n%s"orientation": "%s",\n' % (json_str, indentstr * (indent+1), el.arrangement)
                    json_str = u'\n%s%s"elements": {' % (json_str, indentstr * (indent+1))
                    for i, comp in enumerate(el.components):
                        json_str = describe_element(json_str, comp, i, len(el.components), indent+2, show_attributes)
                    json_str = u'%s\n%s}' % (json_str, indentstr * (indent+1))
                json_str = u"%s\n%s}" % (json_str, indentstr * indent)
            else:
                json_str = u'%s}' % json_str
            if element_no < total_elements-1:
                json_str += u","
            return json_str
        json = describe_element(json, self.master_element_name, 1, 1, indent, show_attributes)
        json += "\n}\n"
        return json
