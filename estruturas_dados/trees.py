#-*- coding: utf-8 -*-

__author__ = 'infante'

from uuid import uuid4

class BTree(object):
    u"""
        Implementa estrutura de dados de Árvore B (2-3) para fins de aprendizado.
    """

    class TreeNode(object):
        u"""
            Implementa definição e operações de nó da Árvore B.
        """

        # TODO: implementar navegacao nos nós com iterator

        def __init__(self):
            self.id_ = uuid4().hex
            self.elements_ = []
            self.max_elements_ = 2
            self.child_nodes_ = {'left': None, 'middle': None, 'right': None}

        def add_element(self, element):
            self.elements_.append(element)
            self.elements_.sort()

        def rem_element(self, element):
            return self.elements_.pop(self.elements_.index(element))

        def add_child_node(self, node, direction):
            self.child_nodes_[direction] = node

        def rem_child_node(self, node_id):
            for key in self.child_nodes_.keys():
                if repr(self.child_nodes_[key]) == node_id:
                    self.child_nodes_[key] = None
                    break

        def is_available(self):
            if len(self.elements_) < self.max_elements_:
                return True
            return False

        def __repr__(self):
            return str(self.id_)


    def __init__(self):
        self.tree_id_ = uuid4().hex
        self.root_node_ = None


    def create_node(self):
        return BTree.TreeNode()

    def process_element_insertion(self, element, node):
        # implement logic of node insertion
        pass

    def insert_element(self, element):
        if self.root_node_ is None:
            self.root_node_ = self.create_node()
        self.process_element_insertion(element, self.root_node_)

    def __repr__(self):
        return str("Tree: {0}".format(self.tree_id_))