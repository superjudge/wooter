# -*- coding: utf-8 -*-

# Copyright (c) 2009, Johan Liseborn <johan.liseborn@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from django import template

from django.template import Node, NodeList, Variable
from django.template import VariableDoesNotExist

register = template.Library()

class IfMemberNode(Node):
    def __init__(self, var1, var2, nodelist_true, nodelist_false, negate):
        self.var1, self.var2 = Variable(var1), Variable(var2)
        self.nodelist_true, self.nodelist_false = nodelist_true, nodelist_false
        self.negate = negate
        
    def __repr__(self):
        return "<IfMemberNode>"

    def render(self, context):
        try:
            val1 = self.var1.resolve(context)
        except VariableDoesNotExist:
            val1 = None
        try:
            val2 = self.var2.resolve(context)
        except VariableDoesNotExist:
            val2 = None
        if (self.negate and val1 not in val2) or (not self.negate and val1 in val2):
            return self.nodelist_true.render(context)
        return self.nodelist_false.render(context)

def do_ifmember(parser, token, negate):
    bits = list(token.split_contents())
    if len(bits) != 3:
        raise TemplateSyntaxError, "%r takes two arguments" % bits[0]
    end_tag = 'end' + bits[0]
    nodelist_true = parser.parse(('else', end_tag))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse((end_tag,))
        parser.delete_first_token()
    else:
        nodelist_false = NodeList()
    return IfMemberNode(bits[1], bits[2], nodelist_true, nodelist_false, negate)

#@register.tag
def ifmember(parser, token):
    """
    Outputs the contents of the block if the first argument is a member of the second.

    Examples::

        {% ifmember user users %}
            ...
        {% endifequal %}

        {% ifnotmember user users %}
            ...
        {% else %}
            ...
        {% endifnotequal %}
    """
    return do_ifmember(parser, token, False)
ifmember = register.tag(ifmember)

#@register.tag
def ifnotmember(parser, token):
    """
    Outputs the contents of the block if the first argument is not a member of the second.
    See ifmember.
    """
    return do_ifmember(parser, token, True)
ifnotmember = register.tag(ifnotmember)
