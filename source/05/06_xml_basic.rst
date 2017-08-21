.. _xml_basics:

XML files basics
==================

In this section, the basics of XML file format are described. XML file format
is adopted as file format for solver definition file and grid
generating program definitioin file.


Defining Elements
-------------------


Element start tag is described with \"<\" and \">\".

Element end tag is described with \"</\" and \">\".

:numref:`xml_element_example` shows an example of Item element definition.


.. code-block:: xml
   :caption: Example of Item element
   :name: xml_element_example

   <Item>
   
   </Item>

An element can have the followings:

- Child element
- Attributes

An element can have multiple child elements that have the same name.
On the other hand, an element can have only one attribute for each name.
:numref:`xml_element_example2` shows an example of a definition of
Item element with two \"Subitem\" child elements and \"name\" attribute.

.. code-block:: xml
   :caption: Example of Item element
   :name: xml_element_example2

   <Item name="sample">
     <SubItem>
     </SubItem>
     
     <SubItem>
     </SubItem>
   </Item>

An element that do not have a child element can be delimited with \"<\" and \"/>\". 
For example, :numref:`xml_element_without_child_example` and
:numref:`xml_element_without_child_example2` are processed as the same data
by XML parsers.

.. code-block:: xml
   :caption: Example of item without a child element 
   :name: xml_element_without_child_example

   <Item name="sample">
   
   </Item>

.. code-block:: xml
   :caption: Example of item without a child element
   :name: xml_element_without_child_example2

   <Item name="sample" />

About tabs, spaces, and line breaks
---------------------------------------

In XML files, tabs, spaces, and line breaks are ignored, so you can add them
freely to make XML files easier to read. Please note that spaces in
attribute values are not ignored. Elements in
:numref:`xml_element_spaces_example`,
:numref:`xml_element_spaces_example2`,
:numref:`xml_element_spaces_example3` are processed as the same data by
XML parsers.

.. code-block:: xml
   :caption: Example of element
   :name: xml_element_spaces_example

   <Item name="sample">
     <SubItem>
     </SubItem>
   </Item>

.. code-block:: xml
   :caption: Example of element
   :name: xml_element_spaces_example2

   <Item
     name="sample"
   >
     <SubItem></SubItem>
   </Item>

.. code-block:: xml
   :caption: Example of element
   :name: xml_element_spaces_example3

   <Item name="sample"><SubItem></SubItem></Item>

Comments
---------

In XML files, strings between \"<!--\" and \"-->\" are treated as comments. 
:numref:`xml_element_comment_example` shows an example of a comment.

.. code-block:: xml
   :caption: Example of comment
   :name: xml_element_comment_example

   <!—This is a comment -->
   <Item name="sample">
     <SubItem>
     </SubItem>
   </Item>
