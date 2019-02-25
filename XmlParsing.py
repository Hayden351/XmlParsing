# https://www.tutorialspoint.com/python/python_xml_processing.htm

import xml.dom.minidom as dom
# import inspect
# import re
# import sys

xmlValue = '''
<txn xmlns="asdf">
    <wrapper>
        <orderSource>     
        ecommerce
        </orderSource>
    </wrapper>
</txn>
'''

print(type('asdf'))
def mutate_xml_string(xml_string, local_name, new_text_value):
    '''
    will replace the text of the first text node to have the value given by
    the given text value for each element with the given local name in the
    given string
    :param xml_string: the xml of type <class 'str'>
    :param local_name: the tag that will have its text replaced
    :param new_text_value: new text under the tag
    :return: the xml with the text replaced
    '''
    tree = dom.parseString(xml_string)

    for node in tree.getElementsByTagName(local_name):
        # find first text node under the supplied tag name
        textNode = next(x for x in node.childNodes if x.nodeType == dom.Node.TEXT_NODE)
        textNode.replaceData(0, len(textNode), new_text_value)

    # reach through to documentElement to get rid of xml version tag
    return tree.documentElement.toxml()
print(help(mutate_xml_string))
print(mutate_xml_string(xmlValue, 'orderSource', 'recurring'))
# tree = dom.parseString(xmlValue)
# # tree = dom.parse("data.xml")
#
# for node in tree.getElementsByTagName('orderSource'):
#     # find first text node under the supplied tag name
#     textNode = next(x for x in node.childNodes if x.nodeType == dom.Node.TEXT_NODE)
#     textNode.replaceData(0, len(textNode), 'recurring')
#
# # reach through to documentElement to get rid of xml version tag
# print(tree.documentElement.toxml())
#
# # with open("output.xml", "w") as xml_file:
# #     tree.writexml(xml_file)
# # tree.documentElement.writexml(sys.stdout)

