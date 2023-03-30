#!/usr/bin/env python3

"""
Convert GBI Syntax Trees to a flat, dependency representation.

Original code by @jtauber, modified by @ryderwishart in 2023 and adapted for UGNT trees.
"""

from xml.etree import ElementTree


def morph_id(gbi_code):
    """
    Convert the morphId to use book numbers starting at 61 like SBLGNT.

    Note: This function is no longer used as this function breaks mapping between the output and existing resources using similar trees created by Andi Wu and Randall Tan.
    """
    if gbi_code is None:
        return None
    return str(int(gbi_code[0:2]) + 21) + gbi_code[2:]


def head(node):
    """
    Get the child of the given node that is the head.
    """
    if "Head" not in node.attrib:
        # In these cases no head is given so we explictly choose which one
        # to use ourselves. Note: we could use a similar approach to
        # systematically *change* the head if we don't agree with the GBI
        # choice.
        assert node.attrib["Rule"] in ["Conj-CL", "sub-CL", "that-VP"]
        return node[1]
    else:
        return node[int(node.attrib["Head"])]


def recursive_head(node):
    """
    Follow the heads down from the given node to get the leaf node
    """
    if len(node) == 0:
        return node
    else:
        return recursive_head(head(node))


def output_node(node, ancestors=None):
    """
    Recurse the node, outputting rows with dependency information.

    The head of each leaf node is basically found by walking up the tree until
    hitting a node whose head has changed from the node came from. If the head
    never changes, we have the head over the overall sentence.
    """
    ancestors = ancestors or []

    if len(node) == 0:  # a leaf node
        # word_id = morph_id(node.attrib["morphId"])
        word_id = node.attrib["morphId"]
        text = node.attrib["Unicode"].strip()
        path = [node]

        # build path, stopping at (but including) point where the head of the
        # current node is not the child we just came from
        for ancestor in ancestors:
            path.append(ancestor)
            if head(ancestor) != path[-2]:
                break

        # now need to follow the Head attribute from the last in the path
        # back down to get the morphId
        head_id = recursive_head(path[-1]).attrib["morphId"]

        # if we got back the same id, there is no head so use None
        if head_id == word_id:
            head_id = None

        # the dependency type is the Cat of the node one level down in the path
        dependency_type = path[-2].attrib.get("Cat")
        all_attrs = [
            f'{k.replace("{http://www.w3.org/XML/1998/namespace}", "")}="{v}"' for k, v in node.attrib.items()]

        print("{}|{}|{}|{}|".format(word_id, text, head_id,
              dependency_type) + '|'.join(all_attrs))

    else:  # a non-leaf node
        for child in node:
            output_node(child, [node] + ancestors)


def convert(filename):
    tree = ElementTree.parse(filename)
    root = tree.getroot()

    # just uses the first tree when there is more than one analysis (for now)
    for tree in root.findall("./Sentence/Trees/Tree[1]"):
        output_node(tree[0])


if __name__ == "__main__":
    import sys
    convert(sys.argv[1])
