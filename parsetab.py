
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xe9-g}\xfc\x1b\xf5\x95\xf2\xdc\x06\xe5\xc8\xd3\xd6\xdc'
    
_lr_action_items = {'FUNCTION':([50,56,58,60,66,],[53,53,53,53,53,]),'LPAREN':([46,50,53,56,58,60,66,],[50,56,60,56,56,56,56,]),'SUBPART':([2,6,7,9,10,11,13,16,20,21,22,23,34,37,],[7,21,-17,7,-20,-16,-12,-19,34,-10,7,7,-11,-18,]),'NUMBER':([50,56,58,60,66,],[54,54,54,54,54,]),'LSQBRACE':([2,6,7,9,10,11,13,16,20,21,22,23,34,37,],[12,-8,-17,12,-20,-16,-12,-19,-9,-10,12,12,-11,-18,]),'RPAREN':([52,54,55,57,61,62,63,64,65,67,68,],[59,-37,-40,-36,65,-38,-41,67,-39,-43,-42,]),'SEMICOLON':([17,33,],[32,43,]),'ZOOM':([6,],[20,]),'COLON':([30,],[41,]),'COMMA':([2,6,7,9,10,11,13,16,20,21,22,23,34,37,54,55,57,62,63,64,65,67,68,],[11,-8,-17,11,-20,-16,-12,-19,-9,-10,11,11,-11,-18,-37,-40,-36,-38,-41,66,-39,-43,66,]),'OPERATION':([52,54,55,57,61,62,63,65,67,],[58,-37,-40,-36,58,58,58,-39,-43,]),'IDENTIFIER':([12,24,36,],[25,35,45,]),'CLASS':([2,6,7,9,10,11,13,16,20,21,22,23,30,34,37,],[16,-8,-17,16,-20,-16,-12,-19,-9,-10,16,16,40,-11,-18,]),'$end':([1,4,5,14,18,19,27,31,32,39,43,],[-1,-2,0,-7,-3,-4,-27,-25,-6,-26,-5,]),'REGEX':([36,],[44,]),'STRING':([50,56,58,60,66,],[57,57,57,57,57,]),'URL':([3,],[17,]),'MEMBEROF':([2,6,7,9,10,11,13,16,20,21,22,23,34,37,],[8,-8,-17,8,-20,-16,-12,-19,-9,-10,8,8,-11,-18,]),'EQUALS':([42,],[49,]),'VALUE':([41,49,],[47,47,]),'SIGN':([25,],[36,]),'PSEUDOCLASS':([2,6,7,9,10,11,13,16,17,20,21,22,23,34,37,],[10,-8,-17,10,-20,-16,-12,-19,33,-9,-10,10,10,-11,-18,]),'EVAL':([41,49,],[46,46,]),'IMPORT':([0,1,4,5,14,18,19,27,31,32,39,43,],[3,-1,-2,3,-7,-3,-4,-27,-25,-6,-26,-5,]),'LCBRACE':([2,6,7,9,10,11,13,14,16,20,21,22,23,27,31,34,37,39,],[15,-8,-17,-14,-20,-16,-12,15,-19,-9,-10,-13,-15,15,-25,-11,-18,-26,]),'RSQBRACE':([25,26,35,44,45,],[-23,37,-24,-22,-21,]),'EXIT':([15,28,29,38,40,42,47,48,51,59,],[29,29,-28,29,-34,-33,-29,-31,-32,-30,]),'KEY':([15,28,29,30,38,40,42,47,48,51,59,],[30,30,-28,42,30,-34,-33,-29,-31,-32,-30,]),'NOT':([12,],[24,]),'RCBRACE':([15,28,29,38,40,42,47,48,51,59,],[31,39,-28,-35,-34,-33,-29,-31,-32,-30,]),'SUBJECT':([0,1,2,4,5,6,7,8,9,10,11,13,14,16,18,19,20,21,22,23,27,31,32,34,37,39,43,],[6,-1,6,-2,6,-8,-17,6,6,-20,6,-12,-7,-19,-3,-4,-9,-10,6,6,-27,-25,-6,-11,-18,-26,-5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'eval_expression':([50,56,58,60,66,],[52,61,62,63,63,]),'value':([41,49,],[48,51,]),'statements':([15,28,38,],[28,38,38,]),'rule':([0,5,],[1,18,]),'selector':([0,2,5,8,9,11,22,23,],[2,9,2,22,9,23,9,9,]),'function_argument':([60,66,],[64,68,]),'eval_function':([50,56,58,60,66,],[55,55,55,55,55,]),'condition':([12,],[26,]),'criteria':([2,9,22,23,],[13,13,13,13,]),'action':([2,14,27,],[14,27,27,]),'import':([0,5,],[4,19,]),'css':([0,],[5,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> css","S'",1,None,None,None),
  ('css -> rule','css',1,'p_mapcss','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',16),
  ('css -> import','css',1,'p_mapcss_import','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',21),
  ('css -> css rule','css',2,'p_mapcss_multiple_rules','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',26),
  ('css -> css import','css',2,'p_mapcss_multiple_imports','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',31),
  ('import -> IMPORT URL PSEUDOCLASS SEMICOLON','import',4,'p_import_pseudoclass','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',36),
  ('import -> IMPORT URL SEMICOLON','import',3,'p_import','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',40),
  ('rule -> selector action','rule',2,'p_rule','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',44),
  ('selector -> SUBJECT','selector',1,'p_selector_empty','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',48),
  ('selector -> SUBJECT ZOOM','selector',2,'p_selector_zoom_empty','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',52),
  ('selector -> SUBJECT SUBPART','selector',2,'p_selector_empty_subpart','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',56),
  ('selector -> SUBJECT ZOOM SUBPART','selector',3,'p_selector_zoom_empty_subpart','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',60),
  ('selector -> selector criteria','selector',2,'p_selector_and','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',64),
  ('selector -> selector MEMBEROF selector','selector',3,'p_selector_memberof','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',69),
  ('selector -> selector selector','selector',2,'p_selector_within','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',74),
  ('selector -> selector COMMA selector','selector',3,'p_selector_or','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',79),
  ('selector -> selector COMMA','selector',2,'p_selecotr_last','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',84),
  ('selector -> selector SUBPART','selector',2,'p_selector_subpart','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',88),
  ('criteria -> LSQBRACE condition RSQBRACE','criteria',3,'p_criteria_check','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',95),
  ('criteria -> CLASS','criteria',1,'p_criteria_class','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',99),
  ('criteria -> PSEUDOCLASS','criteria',1,'p_criteria_pseudoclass','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',103),
  ('condition -> IDENTIFIER SIGN IDENTIFIER','condition',3,'p_condition_check','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',107),
  ('condition -> IDENTIFIER SIGN REGEX','condition',3,'p_condition_regex','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',111),
  ('condition -> IDENTIFIER','condition',1,'p_condition_set','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',115),
  ('condition -> NOT IDENTIFIER','condition',2,'p_condition_not_set','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',119),
  ('action -> LCBRACE RCBRACE','action',2,'p_empty_action','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',123),
  ('action -> LCBRACE statements RCBRACE','action',3,'p_action','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',127),
  ('action -> action action','action',2,'p_action_multiple','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',131),
  ('statements -> EXIT','statements',1,'p_exit','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',136),
  ('value -> VALUE','value',1,'p_value','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',140),
  ('value -> EVAL LPAREN eval_expression RPAREN','value',4,'p_value_eval','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',144),
  ('statements -> KEY COLON value','statements',3,'p_properties','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',148),
  ('statements -> KEY KEY EQUALS value','statements',4,'p_set_tag_value','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',152),
  ('statements -> KEY KEY','statements',2,'p_set_tag','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',156),
  ('statements -> KEY CLASS','statements',2,'p_set_class','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',160),
  ('statements -> statements statements','statements',2,'p_properties_multiple','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',164),
  ('eval_expression -> STRING','eval_expression',1,'p_eval_expression_string','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',170),
  ('eval_expression -> NUMBER','eval_expression',1,'p_eval_expression_number','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',174),
  ('eval_expression -> eval_expression OPERATION eval_expression','eval_expression',3,'p_eval_expression_operation','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',178),
  ('eval_expression -> LPAREN eval_expression RPAREN','eval_expression',3,'p_eval_expression_parens','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',182),
  ('eval_expression -> eval_function','eval_expression',1,'p_eval_expression_function','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',186),
  ('function_argument -> eval_expression','function_argument',1,'p_eval_function_argument_expression','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',190),
  ('function_argument -> function_argument COMMA function_argument','function_argument',3,'p_eval_function_argument_multiple','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',194),
  ('eval_function -> FUNCTION LPAREN function_argument RPAREN','eval_function',4,'p_eval_function','/usr/local/lib/python2.7/dist-packages/mapcss_parser/parse.py',199),
]