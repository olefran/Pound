
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAMleftPLUSMINUSleftMULTDIVMODrightEQUALleftANDORAND CHAR COMA COMMENT COMPARE CTE_CH CTE_F CTE_I CTE_STRING DESDE DET_ARR DIFFERENT DIV DOTCOMA ENTONCES EQUAL ESCRIBE FLOAT FUNCION HACER HASTA HAZ ID INT INV_ARR LBRACKET LEE LESS LESSEQUAL LPAREN LSTAPLE MIENTRAS MINUS MOD MORE MOREEQUAL MULT NOT NULL OR PLUS PRINCIPAL PROGRAMA RBRACKET REGRESA RPAREN RSTAPLE SI SINO STRING TRANS_ARR VAR VOIDempty :PROGRAM : PROGRAMA ID DOTCOMA VARS FUNCTIONS MAINMAIN : PRINCIPAL r_save_func LPAREN RPAREN VARS r_register_func BLOQUEVARS : VAR VAR_AUX\n    | emptyVAR_AUX : TIPO IDS VAR_AUX\n    | emptyTIPO : INT r_save_type\n    | FLOAT r_save_type\n    | CHAR r_save_type\n    | STRING r_save_typeIDS : ID  ARRDIM DOTCOMA\n    | ID  ARRDIM COMA IDSARRDIM : LSTAPLE EXPRESION RSTAPLE\n    | LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE\n    | LSTAPLE EXPRESION COMA EXPRESION RSTAPLE\n    | emptyFUNCTIONS : FUNCTION FUNCTIONS\n    | emptyFUNCTION : FUNCION TIPO ID r_save_func LPAREN PARAM RPAREN VARS r_register_func BLOQUE\n    | FUNCION VOID r_save_type ID r_save_func LPAREN PARAM RPAREN VARS r_register_func BLOQUEPARAM : TIPO ID  PARENTESIS PARAM_AUXPARAM_AUX : COMA PARAM\n    | emptyPARENTESIS : LSTAPLE RSTAPLE\n    | LSTAPLE RSTAPLE LSTAPLE RSTAPLE\n    | emptyBLOQUE : LBRACKET ESTATUTOS RBRACKETESTATUTOS : ESTATUTO ESTATUTOS\n    | emptyESTATUTO : ASIGNACION DOTCOMA\n    | FUN DOTCOMA\n    | COND\n    | WRITE DOTCOMA\n    | READ DOTCOMA\n    | RETURN DOTCOMAASIGNACION : ID ARRDIM EQUAL EXPRESION\n    | ID ARRDIM EQUAL CTE_ARREXPRESION : SUBEXP AND SUBEXP\n    | SUBEXP OR SUBEXP\n    | SUBEXPSUBEXP : EXP\n    | EXP COMPARACION EXPCOMPARACION : MORE\n    | LESS\n    | COMPARE\n    | DIFFERENT\n    | MOREEQUAL\n    | LESSEQUALEXP : TERMINO\n    | TERMINO PLUS EXP\n    | TERMINO MINUS EXPTERMINO : FACTOR\n    | FACTOR MULT TERMINO\n    | FACTOR DIV TERMINO\n    | FACTOR MOD TERMINOFACTOR : LPAREN EXPRESION RPAREN\n    | PLUS CTE\n    | MINUS CTE\n    | NOT CTE\n    | CTE ARROP\n    | CTECTE : CTE_I\n    | CTE_F\n    | CTE_CH\n    | CTE_STRING\n    | FUN\n    | ID ARRDIMARROP : DET_ARR\n    | TRANS_ARR\n    | INV_ARRFUN : ID LPAREN FUN_AUX RPARENFUN_AUX : EXPRESION COMA FUN_AUX\n    | EXPRESION\n    | emptyCOND : IF\n    | FOR\n    | WHILEIF : SI LPAREN EXPRESION RPAREN ENTONCES BLOQUE IF_AUX\n    | SI LPAREN EXPRESION RPAREN ENTONCES COND IF_AUX : SINO BLOQUE\n    | emptyWHILE :  MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX BLOQUE\n    | MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX CONDWHILE_AUX :  HAZ\n    | empty FOR :  DESDE ASIGNACION HASTA EXPRESION HACER BLOQUE\n    | DESDE ASIGNACION HASTA EXPRESION HACER CONDWRITE : ESCRIBE LPAREN WRITE_AUX RPARENWRITE_AUX : EXPRESION WRITE_AUXSUBWRITE_AUXSUB : COMA WRITE_AUX\n    | emptyREAD : LEE LPAREN READ_AUX RPARENREAD_AUX : ID ARRDIM READ_AUXSUBREAD_AUXSUB : COMA READ_AUX\n    | emptyRETURN : REGRESA LPAREN EXPRESION RPAREN\n    | REGRESA LPAREN NULL RPARENCTE_ARR : LBRACKET CTE_ARR_AUX RBRACKET\n    | LBRACKET CTE_ARR_AUX2 RBRACKET CTE_ARR_AUX : CTE\n    | CTE_ARR_AUXSUB CTE_ARR_AUXSUB : COMA CTE_ARR_AUX\n    | empty CTE_ARR_AUX2 : LBRACKET CTE_ARR_AUX RBRACKET  CTE_ARR_AUX2SUBCTE_ARR_AUX2SUB : COMA CTE_ARR_AUX2\n    | empty r_save_type : r_save_func : r_register_var : r_register_func : '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,19,114,148,],[0,-2,-3,-28,]),'ID':([2,13,15,16,17,18,22,23,26,27,28,29,32,35,41,46,47,49,51,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,87,89,92,113,115,124,128,133,134,135,140,148,150,151,152,153,154,156,157,158,159,162,167,175,181,184,193,198,202,214,215,216,217,218,219,221,223,227,],[3,25,-108,-108,-108,-108,31,-108,-8,-9,-10,-11,39,57,25,57,57,57,57,57,57,57,57,-44,-45,-46,-47,-48,-49,57,57,57,57,57,57,107,57,57,132,132,-33,-76,-77,-78,161,-28,-31,-32,-34,-35,-36,57,171,57,57,57,57,57,57,57,57,57,171,-1,-80,-87,-88,-83,-84,-79,-82,-81,]),'DOTCOMA':([3,25,34,36,43,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,94,95,96,97,98,99,100,101,102,111,112,121,126,127,129,130,131,179,180,182,186,188,189,210,211,],[4,-1,40,-17,-41,-42,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-39,-40,-43,-51,-52,-54,-55,-56,-57,-16,-72,-15,150,151,152,153,154,-37,-38,-89,-93,-97,-98,-99,-100,]),'VAR':([4,58,108,120,],[6,6,6,6,]),'FUNCION':([4,5,6,7,9,12,14,24,33,40,61,148,165,178,],[-1,11,-1,-5,11,-4,-7,-1,-6,-12,-13,-28,-20,-21,]),'PRINCIPAL':([4,5,6,7,8,9,10,12,14,21,24,33,40,61,148,165,178,],[-1,-1,-1,-5,20,-1,-19,-4,-7,-18,-1,-6,-12,-13,-28,-20,-21,]),'INT':([6,11,24,40,59,61,91,143,],[15,15,15,-12,15,-13,15,15,]),'FLOAT':([6,11,24,40,59,61,91,143,],[16,16,16,-12,16,-13,16,16,]),'CHAR':([6,11,24,40,59,61,91,143,],[17,17,17,-12,17,-13,17,17,]),'STRING':([6,11,24,40,59,61,91,143,],[18,18,18,-12,18,-13,18,18,]),'LBRACKET':([6,7,12,14,24,33,40,58,61,88,106,108,119,120,146,147,166,167,181,192,204,205,206,207,208,222,225,],[-1,-5,-4,-7,-1,-6,-12,-1,-13,-111,115,-1,-111,-1,115,-111,115,181,193,-1,115,115,115,-85,-86,115,193,]),'VOID':([11,],[23,]),'LPAREN':([20,30,31,35,38,39,49,57,60,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,87,92,113,132,136,137,138,139,141,156,158,159,162,167,175,184,],[-109,37,-109,49,59,-109,49,87,91,49,49,49,49,-44,-45,-46,-47,-48,-49,49,49,49,49,49,49,49,49,87,156,157,158,159,162,49,49,49,49,49,49,49,]),'LSTAPLE':([25,57,62,107,132,145,161,171,],[35,35,92,117,35,164,35,35,]),'COMA':([25,34,36,42,43,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,94,95,96,97,98,99,100,101,102,104,107,111,112,116,118,121,145,169,171,177,181,187,193,198,220,],[-1,41,-17,63,-41,-42,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-39,-40,-43,-51,-52,-54,-55,-56,-57,113,-1,-16,-72,143,-27,-15,-25,184,-1,-26,198,202,198,198,225,]),'PLUS':([35,36,45,48,49,50,52,53,54,55,56,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,92,99,100,101,102,111,112,113,121,156,158,159,162,167,175,184,],[46,-17,73,-53,46,-62,-63,-64,-65,-66,-67,-1,-14,46,46,46,46,-44,-45,-46,-47,-48,-49,46,46,-58,-59,46,46,46,-61,-69,-70,-71,-60,-68,46,46,-54,-55,-56,-57,-16,-72,46,-15,46,46,46,46,46,46,46,]),'MINUS':([35,36,45,48,49,50,52,53,54,55,56,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,92,99,100,101,102,111,112,113,121,156,158,159,162,167,175,184,],[47,-17,74,-53,47,-62,-63,-64,-65,-66,-67,-1,-14,47,47,47,47,-44,-45,-46,-47,-48,-49,47,47,-58,-59,47,47,47,-61,-69,-70,-71,-60,-68,47,47,-54,-55,-56,-57,-16,-72,47,-15,47,47,47,47,47,47,47,]),'NOT':([35,49,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,87,92,113,156,158,159,162,167,175,184,],[51,51,51,51,51,51,-44,-45,-46,-47,-48,-49,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'CTE_I':([35,46,47,49,51,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,87,92,113,156,158,159,162,167,175,181,184,193,198,],[52,52,52,52,52,52,52,52,52,-44,-45,-46,-47,-48,-49,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'CTE_F':([35,46,47,49,51,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,87,92,113,156,158,159,162,167,175,181,184,193,198,],[53,53,53,53,53,53,53,53,53,-44,-45,-46,-47,-48,-49,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'CTE_CH':([35,46,47,49,51,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,87,92,113,156,158,159,162,167,175,181,184,193,198,],[54,54,54,54,54,54,54,54,54,-44,-45,-46,-47,-48,-49,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'CTE_STRING':([35,46,47,49,51,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,87,92,113,156,158,159,162,167,175,181,184,193,198,],[55,55,55,55,55,55,55,55,55,-44,-45,-46,-47,-48,-49,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'DET_ARR':([36,50,52,53,54,55,56,57,62,86,111,112,121,],[-17,82,-63,-64,-65,-66,-67,-1,-14,-68,-16,-72,-15,]),'TRANS_ARR':([36,50,52,53,54,55,56,57,62,86,111,112,121,],[-17,83,-63,-64,-65,-66,-67,-1,-14,-68,-16,-72,-15,]),'INV_ARR':([36,50,52,53,54,55,56,57,62,86,111,112,121,],[-17,84,-63,-64,-65,-66,-67,-1,-14,-68,-16,-72,-15,]),'MULT':([36,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,102,111,112,121,],[-17,77,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-57,-16,-72,-15,]),'DIV':([36,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,102,111,112,121,],[-17,78,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-57,-16,-72,-15,]),'MOD':([36,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,102,111,112,121,],[-17,79,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-57,-16,-72,-15,]),'MORE':([36,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,97,98,99,100,101,102,111,112,121,],[-17,67,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-51,-52,-54,-55,-56,-57,-16,-72,-15,]),'LESS':([36,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,97,98,99,100,101,102,111,112,121,],[-17,68,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-51,-52,-54,-55,-56,-57,-16,-72,-15,]),'COMPARE':([36,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,97,98,99,100,101,102,111,112,121,],[-17,69,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-51,-52,-54,-55,-56,-57,-16,-72,-15,]),'DIFFERENT':([36,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,97,98,99,100,101,102,111,112,121,],[-17,70,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-51,-52,-54,-55,-56,-57,-16,-72,-15,]),'MOREEQUAL':([36,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,97,98,99,100,101,102,111,112,121,],[-17,71,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-51,-52,-54,-55,-56,-57,-16,-72,-15,]),'LESSEQUAL':([36,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,97,98,99,100,101,102,111,112,121,],[-17,72,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-51,-52,-54,-55,-56,-57,-16,-72,-15,]),'AND':([36,43,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,96,97,98,99,100,101,102,111,112,121,],[-17,64,-42,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-43,-51,-52,-54,-55,-56,-57,-16,-72,-15,]),'OR':([36,43,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,96,97,98,99,100,101,102,111,112,121,],[-17,65,-42,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-43,-51,-52,-54,-55,-56,-57,-16,-72,-15,]),'RSTAPLE':([36,42,43,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,93,94,95,96,97,98,99,100,101,102,110,111,112,117,121,164,],[-17,62,-41,-42,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,111,-39,-40,-43,-51,-52,-54,-55,-56,-57,121,-16,-72,145,-15,177,]),'RPAREN':([36,37,43,44,45,48,50,52,53,54,55,56,57,62,75,76,80,81,82,83,84,85,86,87,90,94,95,96,97,98,99,100,101,102,103,104,105,107,109,111,112,113,116,118,121,122,142,144,145,163,168,169,170,171,172,173,174,176,177,183,185,187,200,201,203,213,],[-17,58,-41,-42,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,102,-61,-69,-70,-71,-60,-68,-1,108,-39,-40,-43,-51,-52,-54,-55,-56,-57,112,-74,-75,-1,120,-16,-72,-1,-1,-27,-15,-73,-22,-24,-25,-23,182,-1,186,-1,188,189,190,192,-26,-90,-92,-1,-91,-94,-96,-95,]),'HASTA':([36,43,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,94,95,96,97,98,99,100,101,102,111,112,121,160,179,180,210,211,],[-17,-41,-42,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-39,-40,-43,-51,-52,-54,-55,-56,-57,-16,-72,-15,175,-37,-38,-99,-100,]),'HACER':([36,43,44,45,48,50,52,53,54,55,56,57,62,75,76,81,82,83,84,85,86,94,95,96,97,98,99,100,101,102,111,112,121,191,],[-17,-41,-42,-50,-53,-62,-63,-64,-65,-66,-67,-1,-14,-58,-59,-61,-69,-70,-71,-60,-68,-39,-40,-43,-51,-52,-54,-55,-56,-57,-16,-72,-15,205,]),'RBRACKET':([36,52,53,54,55,56,57,62,86,111,112,115,121,123,124,125,128,133,134,135,148,149,150,151,152,153,154,181,193,194,195,196,197,198,199,209,212,214,215,216,217,218,219,220,221,223,224,226,227,228,],[-17,-63,-64,-65,-66,-67,-1,-14,-68,-16,-72,-1,-15,148,-1,-30,-33,-76,-77,-78,-28,-29,-31,-32,-34,-35,-36,-1,-1,210,211,-101,-102,-1,-104,220,-103,-1,-80,-87,-88,-83,-84,-1,-79,-82,-105,-107,-81,-106,]),'EQUAL':([36,62,111,121,132,155,161,],[-17,-14,-16,-15,-1,167,-1,]),'ESCRIBE':([115,124,128,133,134,135,148,150,151,152,153,154,214,215,216,217,218,219,221,223,227,],[136,136,-33,-76,-77,-78,-28,-31,-32,-34,-35,-36,-1,-80,-87,-88,-83,-84,-79,-82,-81,]),'LEE':([115,124,128,133,134,135,148,150,151,152,153,154,214,215,216,217,218,219,221,223,227,],[137,137,-33,-76,-77,-78,-28,-31,-32,-34,-35,-36,-1,-80,-87,-88,-83,-84,-79,-82,-81,]),'REGRESA':([115,124,128,133,134,135,148,150,151,152,153,154,214,215,216,217,218,219,221,223,227,],[138,138,-33,-76,-77,-78,-28,-31,-32,-34,-35,-36,-1,-80,-87,-88,-83,-84,-79,-82,-81,]),'SI':([115,124,128,133,134,135,148,150,151,152,153,154,192,204,205,206,207,208,214,215,216,217,218,219,221,223,227,],[139,139,-33,-76,-77,-78,-28,-31,-32,-34,-35,-36,-1,139,139,139,-85,-86,-1,-80,-87,-88,-83,-84,-79,-82,-81,]),'DESDE':([115,124,128,133,134,135,148,150,151,152,153,154,192,204,205,206,207,208,214,215,216,217,218,219,221,223,227,],[140,140,-33,-76,-77,-78,-28,-31,-32,-34,-35,-36,-1,140,140,140,-85,-86,-1,-80,-87,-88,-83,-84,-79,-82,-81,]),'MIENTRAS':([115,124,128,133,134,135,148,150,151,152,153,154,192,204,205,206,207,208,214,215,216,217,218,219,221,223,227,],[141,141,-33,-76,-77,-78,-28,-31,-32,-34,-35,-36,-1,141,141,141,-85,-86,-1,-80,-87,-88,-83,-84,-79,-82,-81,]),'SINO':([148,214,],[-28,222,]),'NULL':([158,],[173,]),'ENTONCES':([190,],[204,]),'HAZ':([192,],[207,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'VARS':([4,58,108,120,],[5,88,119,147,]),'empty':([4,5,6,9,24,25,57,58,87,107,108,113,115,116,120,124,132,161,169,171,181,187,192,193,198,214,220,],[7,10,14,10,14,36,36,7,105,118,7,105,125,144,7,125,36,36,185,36,199,203,208,199,199,223,226,]),'FUNCTIONS':([5,9,],[8,21,]),'FUNCTION':([5,9,],[9,9,]),'VAR_AUX':([6,24,],[12,33,]),'TIPO':([6,11,24,59,91,143,],[13,22,13,89,89,89,]),'MAIN':([8,],[19,]),'IDS':([13,41,],[24,61,]),'r_save_type':([15,16,17,18,23,],[26,27,28,29,32,]),'r_save_func':([20,31,39,],[30,38,60,]),'ARRDIM':([25,57,132,161,171,],[34,86,155,155,187,]),'EXPRESION':([35,49,63,87,92,113,156,158,159,162,167,175,184,],[42,80,93,104,110,104,169,172,174,176,179,191,169,]),'SUBEXP':([35,49,63,64,65,87,92,113,156,158,159,162,167,175,184,],[43,43,43,94,95,43,43,43,43,43,43,43,43,43,43,]),'EXP':([35,49,63,64,65,66,73,74,87,92,113,156,158,159,162,167,175,184,],[44,44,44,44,44,96,97,98,44,44,44,44,44,44,44,44,44,44,]),'TERMINO':([35,49,63,64,65,66,73,74,77,78,79,87,92,113,156,158,159,162,167,175,184,],[45,45,45,45,45,45,45,45,99,100,101,45,45,45,45,45,45,45,45,45,45,]),'FACTOR':([35,49,63,64,65,66,73,74,77,78,79,87,92,113,156,158,159,162,167,175,184,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'CTE':([35,46,47,49,51,63,64,65,66,73,74,77,78,79,87,92,113,156,158,159,162,167,175,181,184,193,198,],[50,75,76,50,85,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,196,50,196,196,]),'FUN':([35,46,47,49,51,63,64,65,66,73,74,77,78,79,87,92,113,115,124,156,158,159,162,167,175,181,184,193,198,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,127,127,56,56,56,56,56,56,56,56,56,56,]),'COMPARACION':([44,],[66,]),'ARROP':([50,],[81,]),'PARAM':([59,91,143,],[90,109,163,]),'FUN_AUX':([87,113,],[103,122,]),'r_register_func':([88,119,147,],[106,146,166,]),'BLOQUE':([106,146,166,204,205,206,222,],[114,165,178,214,216,218,227,]),'PARENTESIS':([107,],[116,]),'ESTATUTOS':([115,124,],[123,149,]),'ESTATUTO':([115,124,],[124,124,]),'ASIGNACION':([115,124,140,],[126,126,160,]),'COND':([115,124,204,205,206,],[128,128,215,217,219,]),'WRITE':([115,124,],[129,129,]),'READ':([115,124,],[130,130,]),'RETURN':([115,124,],[131,131,]),'IF':([115,124,204,205,206,],[133,133,133,133,133,]),'FOR':([115,124,204,205,206,],[134,134,134,134,134,]),'WHILE':([115,124,204,205,206,],[135,135,135,135,135,]),'PARAM_AUX':([116,],[142,]),'WRITE_AUX':([156,184,],[168,200,]),'READ_AUX':([157,202,],[170,213,]),'CTE_ARR':([167,],[180,]),'WRITE_AUXSUB':([169,],[183,]),'CTE_ARR_AUX':([181,193,198,],[194,209,212,]),'CTE_ARR_AUX2':([181,225,],[195,228,]),'CTE_ARR_AUXSUB':([181,193,198,],[197,197,197,]),'READ_AUXSUB':([187,],[201,]),'WHILE_AUX':([192,],[206,]),'IF_AUX':([214,],[221,]),'CTE_ARR_AUX2SUB':([220,],[224,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','PatitoPlusPlus.py',91),
  ('PROGRAM -> PROGRAMA ID DOTCOMA VARS FUNCTIONS MAIN','PROGRAM',6,'p_PROGRAM','PatitoPlusPlus.py',96),
  ('MAIN -> PRINCIPAL r_save_func LPAREN RPAREN VARS r_register_func BLOQUE','MAIN',7,'p_MAIN','PatitoPlusPlus.py',101),
  ('VARS -> VAR VAR_AUX','VARS',2,'p_VARS','PatitoPlusPlus.py',106),
  ('VARS -> empty','VARS',1,'p_VARS','PatitoPlusPlus.py',107),
  ('VAR_AUX -> TIPO IDS VAR_AUX','VAR_AUX',3,'p_VAR_AUX','PatitoPlusPlus.py',113),
  ('VAR_AUX -> empty','VAR_AUX',1,'p_VAR_AUX','PatitoPlusPlus.py',114),
  ('TIPO -> INT r_save_type','TIPO',2,'p_TIPO','PatitoPlusPlus.py',119),
  ('TIPO -> FLOAT r_save_type','TIPO',2,'p_TIPO','PatitoPlusPlus.py',120),
  ('TIPO -> CHAR r_save_type','TIPO',2,'p_TIPO','PatitoPlusPlus.py',121),
  ('TIPO -> STRING r_save_type','TIPO',2,'p_TIPO','PatitoPlusPlus.py',122),
  ('IDS -> ID ARRDIM DOTCOMA','IDS',3,'p_IDS','PatitoPlusPlus.py',127),
  ('IDS -> ID ARRDIM COMA IDS','IDS',4,'p_IDS','PatitoPlusPlus.py',128),
  ('ARRDIM -> LSTAPLE EXPRESION RSTAPLE','ARRDIM',3,'p_ARRDIM','PatitoPlusPlus.py',133),
  ('ARRDIM -> LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE','ARRDIM',6,'p_ARRDIM','PatitoPlusPlus.py',134),
  ('ARRDIM -> LSTAPLE EXPRESION COMA EXPRESION RSTAPLE','ARRDIM',5,'p_ARRDIM','PatitoPlusPlus.py',135),
  ('ARRDIM -> empty','ARRDIM',1,'p_ARRDIM','PatitoPlusPlus.py',136),
  ('FUNCTIONS -> FUNCTION FUNCTIONS','FUNCTIONS',2,'p_FUNCTIONS','PatitoPlusPlus.py',141),
  ('FUNCTIONS -> empty','FUNCTIONS',1,'p_FUNCTIONS','PatitoPlusPlus.py',142),
  ('FUNCTION -> FUNCION TIPO ID r_save_func LPAREN PARAM RPAREN VARS r_register_func BLOQUE','FUNCTION',10,'p_FUNCTION','PatitoPlusPlus.py',147),
  ('FUNCTION -> FUNCION VOID r_save_type ID r_save_func LPAREN PARAM RPAREN VARS r_register_func BLOQUE','FUNCTION',11,'p_FUNCTION','PatitoPlusPlus.py',148),
  ('PARAM -> TIPO ID PARENTESIS PARAM_AUX','PARAM',4,'p_PARAM','PatitoPlusPlus.py',153),
  ('PARAM_AUX -> COMA PARAM','PARAM_AUX',2,'p_PARAM_AUX','PatitoPlusPlus.py',158),
  ('PARAM_AUX -> empty','PARAM_AUX',1,'p_PARAM_AUX','PatitoPlusPlus.py',159),
  ('PARENTESIS -> LSTAPLE RSTAPLE','PARENTESIS',2,'p_PARENTESIS','PatitoPlusPlus.py',164),
  ('PARENTESIS -> LSTAPLE RSTAPLE LSTAPLE RSTAPLE','PARENTESIS',4,'p_PARENTESIS','PatitoPlusPlus.py',165),
  ('PARENTESIS -> empty','PARENTESIS',1,'p_PARENTESIS','PatitoPlusPlus.py',166),
  ('BLOQUE -> LBRACKET ESTATUTOS RBRACKET','BLOQUE',3,'p_BLOQUE','PatitoPlusPlus.py',171),
  ('ESTATUTOS -> ESTATUTO ESTATUTOS','ESTATUTOS',2,'p_ESTATUTOS','PatitoPlusPlus.py',176),
  ('ESTATUTOS -> empty','ESTATUTOS',1,'p_ESTATUTOS','PatitoPlusPlus.py',177),
  ('ESTATUTO -> ASIGNACION DOTCOMA','ESTATUTO',2,'p_ESTATUTO','PatitoPlusPlus.py',182),
  ('ESTATUTO -> FUN DOTCOMA','ESTATUTO',2,'p_ESTATUTO','PatitoPlusPlus.py',183),
  ('ESTATUTO -> COND','ESTATUTO',1,'p_ESTATUTO','PatitoPlusPlus.py',184),
  ('ESTATUTO -> WRITE DOTCOMA','ESTATUTO',2,'p_ESTATUTO','PatitoPlusPlus.py',185),
  ('ESTATUTO -> READ DOTCOMA','ESTATUTO',2,'p_ESTATUTO','PatitoPlusPlus.py',186),
  ('ESTATUTO -> RETURN DOTCOMA','ESTATUTO',2,'p_ESTATUTO','PatitoPlusPlus.py',187),
  ('ASIGNACION -> ID ARRDIM EQUAL EXPRESION','ASIGNACION',4,'p_ASIGNACION','PatitoPlusPlus.py',192),
  ('ASIGNACION -> ID ARRDIM EQUAL CTE_ARR','ASIGNACION',4,'p_ASIGNACION','PatitoPlusPlus.py',193),
  ('EXPRESION -> SUBEXP AND SUBEXP','EXPRESION',3,'p_EXPRESION','PatitoPlusPlus.py',198),
  ('EXPRESION -> SUBEXP OR SUBEXP','EXPRESION',3,'p_EXPRESION','PatitoPlusPlus.py',199),
  ('EXPRESION -> SUBEXP','EXPRESION',1,'p_EXPRESION','PatitoPlusPlus.py',200),
  ('SUBEXP -> EXP','SUBEXP',1,'p_SUBEXP','PatitoPlusPlus.py',205),
  ('SUBEXP -> EXP COMPARACION EXP','SUBEXP',3,'p_SUBEXP','PatitoPlusPlus.py',206),
  ('COMPARACION -> MORE','COMPARACION',1,'p_COMPARACION','PatitoPlusPlus.py',211),
  ('COMPARACION -> LESS','COMPARACION',1,'p_COMPARACION','PatitoPlusPlus.py',212),
  ('COMPARACION -> COMPARE','COMPARACION',1,'p_COMPARACION','PatitoPlusPlus.py',213),
  ('COMPARACION -> DIFFERENT','COMPARACION',1,'p_COMPARACION','PatitoPlusPlus.py',214),
  ('COMPARACION -> MOREEQUAL','COMPARACION',1,'p_COMPARACION','PatitoPlusPlus.py',215),
  ('COMPARACION -> LESSEQUAL','COMPARACION',1,'p_COMPARACION','PatitoPlusPlus.py',216),
  ('EXP -> TERMINO','EXP',1,'p_EXP','PatitoPlusPlus.py',221),
  ('EXP -> TERMINO PLUS EXP','EXP',3,'p_EXP','PatitoPlusPlus.py',222),
  ('EXP -> TERMINO MINUS EXP','EXP',3,'p_EXP','PatitoPlusPlus.py',223),
  ('TERMINO -> FACTOR','TERMINO',1,'p_TERMINO','PatitoPlusPlus.py',228),
  ('TERMINO -> FACTOR MULT TERMINO','TERMINO',3,'p_TERMINO','PatitoPlusPlus.py',229),
  ('TERMINO -> FACTOR DIV TERMINO','TERMINO',3,'p_TERMINO','PatitoPlusPlus.py',230),
  ('TERMINO -> FACTOR MOD TERMINO','TERMINO',3,'p_TERMINO','PatitoPlusPlus.py',231),
  ('FACTOR -> LPAREN EXPRESION RPAREN','FACTOR',3,'p_FACTOR','PatitoPlusPlus.py',236),
  ('FACTOR -> PLUS CTE','FACTOR',2,'p_FACTOR','PatitoPlusPlus.py',237),
  ('FACTOR -> MINUS CTE','FACTOR',2,'p_FACTOR','PatitoPlusPlus.py',238),
  ('FACTOR -> NOT CTE','FACTOR',2,'p_FACTOR','PatitoPlusPlus.py',239),
  ('FACTOR -> CTE ARROP','FACTOR',2,'p_FACTOR','PatitoPlusPlus.py',240),
  ('FACTOR -> CTE','FACTOR',1,'p_FACTOR','PatitoPlusPlus.py',241),
  ('CTE -> CTE_I','CTE',1,'p_CTE','PatitoPlusPlus.py',246),
  ('CTE -> CTE_F','CTE',1,'p_CTE','PatitoPlusPlus.py',247),
  ('CTE -> CTE_CH','CTE',1,'p_CTE','PatitoPlusPlus.py',248),
  ('CTE -> CTE_STRING','CTE',1,'p_CTE','PatitoPlusPlus.py',249),
  ('CTE -> FUN','CTE',1,'p_CTE','PatitoPlusPlus.py',250),
  ('CTE -> ID ARRDIM','CTE',2,'p_CTE','PatitoPlusPlus.py',251),
  ('ARROP -> DET_ARR','ARROP',1,'p_ARROP','PatitoPlusPlus.py',256),
  ('ARROP -> TRANS_ARR','ARROP',1,'p_ARROP','PatitoPlusPlus.py',257),
  ('ARROP -> INV_ARR','ARROP',1,'p_ARROP','PatitoPlusPlus.py',258),
  ('FUN -> ID LPAREN FUN_AUX RPAREN','FUN',4,'p_FUN','PatitoPlusPlus.py',263),
  ('FUN_AUX -> EXPRESION COMA FUN_AUX','FUN_AUX',3,'p_FUN_AUX','PatitoPlusPlus.py',268),
  ('FUN_AUX -> EXPRESION','FUN_AUX',1,'p_FUN_AUX','PatitoPlusPlus.py',269),
  ('FUN_AUX -> empty','FUN_AUX',1,'p_FUN_AUX','PatitoPlusPlus.py',270),
  ('COND -> IF','COND',1,'p_COND','PatitoPlusPlus.py',275),
  ('COND -> FOR','COND',1,'p_COND','PatitoPlusPlus.py',276),
  ('COND -> WHILE','COND',1,'p_COND','PatitoPlusPlus.py',277),
  ('IF -> SI LPAREN EXPRESION RPAREN ENTONCES BLOQUE IF_AUX','IF',7,'p_IF','PatitoPlusPlus.py',282),
  ('IF -> SI LPAREN EXPRESION RPAREN ENTONCES COND','IF',6,'p_IF','PatitoPlusPlus.py',283),
  ('IF_AUX -> SINO BLOQUE','IF_AUX',2,'p_IF_AUX','PatitoPlusPlus.py',288),
  ('IF_AUX -> empty','IF_AUX',1,'p_IF_AUX','PatitoPlusPlus.py',289),
  ('WHILE -> MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX BLOQUE','WHILE',6,'p_WHILE','PatitoPlusPlus.py',294),
  ('WHILE -> MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX COND','WHILE',6,'p_WHILE','PatitoPlusPlus.py',295),
  ('WHILE_AUX -> HAZ','WHILE_AUX',1,'p_WHILE_AUX','PatitoPlusPlus.py',300),
  ('WHILE_AUX -> empty','WHILE_AUX',1,'p_WHILE_AUX','PatitoPlusPlus.py',301),
  ('FOR -> DESDE ASIGNACION HASTA EXPRESION HACER BLOQUE','FOR',6,'p_FOR','PatitoPlusPlus.py',306),
  ('FOR -> DESDE ASIGNACION HASTA EXPRESION HACER COND','FOR',6,'p_FOR','PatitoPlusPlus.py',307),
  ('WRITE -> ESCRIBE LPAREN WRITE_AUX RPAREN','WRITE',4,'p_WRITE','PatitoPlusPlus.py',312),
  ('WRITE_AUX -> EXPRESION WRITE_AUXSUB','WRITE_AUX',2,'p_WRITE_AUX','PatitoPlusPlus.py',317),
  ('WRITE_AUXSUB -> COMA WRITE_AUX','WRITE_AUXSUB',2,'p_WRITE_AUXSUB','PatitoPlusPlus.py',322),
  ('WRITE_AUXSUB -> empty','WRITE_AUXSUB',1,'p_WRITE_AUXSUB','PatitoPlusPlus.py',323),
  ('READ -> LEE LPAREN READ_AUX RPAREN','READ',4,'p_READ','PatitoPlusPlus.py',328),
  ('READ_AUX -> ID ARRDIM READ_AUXSUB','READ_AUX',3,'p_READ_AUX','PatitoPlusPlus.py',333),
  ('READ_AUXSUB -> COMA READ_AUX','READ_AUXSUB',2,'p_READ_AUXSUB','PatitoPlusPlus.py',338),
  ('READ_AUXSUB -> empty','READ_AUXSUB',1,'p_READ_AUXSUB','PatitoPlusPlus.py',339),
  ('RETURN -> REGRESA LPAREN EXPRESION RPAREN','RETURN',4,'p_RETURN','PatitoPlusPlus.py',344),
  ('RETURN -> REGRESA LPAREN NULL RPAREN','RETURN',4,'p_RETURN','PatitoPlusPlus.py',345),
  ('CTE_ARR -> LBRACKET CTE_ARR_AUX RBRACKET','CTE_ARR',3,'p_CTE_ARR','PatitoPlusPlus.py',350),
  ('CTE_ARR -> LBRACKET CTE_ARR_AUX2 RBRACKET','CTE_ARR',3,'p_CTE_ARR','PatitoPlusPlus.py',351),
  ('CTE_ARR_AUX -> CTE','CTE_ARR_AUX',1,'p_CTE_ARR_AUX','PatitoPlusPlus.py',356),
  ('CTE_ARR_AUX -> CTE_ARR_AUXSUB','CTE_ARR_AUX',1,'p_CTE_ARR_AUX','PatitoPlusPlus.py',357),
  ('CTE_ARR_AUXSUB -> COMA CTE_ARR_AUX','CTE_ARR_AUXSUB',2,'p_CTE_ARR_AUXSUB','PatitoPlusPlus.py',362),
  ('CTE_ARR_AUXSUB -> empty','CTE_ARR_AUXSUB',1,'p_CTE_ARR_AUXSUB','PatitoPlusPlus.py',363),
  ('CTE_ARR_AUX2 -> LBRACKET CTE_ARR_AUX RBRACKET CTE_ARR_AUX2SUB','CTE_ARR_AUX2',4,'p_CTE_ARR_AUX2','PatitoPlusPlus.py',368),
  ('CTE_ARR_AUX2SUB -> COMA CTE_ARR_AUX2','CTE_ARR_AUX2SUB',2,'p_CTE_ARR_AUX2SUB','PatitoPlusPlus.py',373),
  ('CTE_ARR_AUX2SUB -> empty','CTE_ARR_AUX2SUB',1,'p_CTE_ARR_AUX2SUB','PatitoPlusPlus.py',374),
  ('r_save_type -> <empty>','r_save_type',0,'p_r_save_type','PatitoPlusPlus.py',409),
  ('r_save_func -> <empty>','r_save_func',0,'p_r_save_func','PatitoPlusPlus.py',415),
  ('r_register_var -> <empty>','r_register_var',0,'p_r_register_var','PatitoPlusPlus.py',420),
  ('r_register_func -> <empty>','r_register_func',0,'p_r_register_func','PatitoPlusPlus.py',429),
]
