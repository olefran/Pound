
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAMleftPLUSMINUSleftMULTDIVMODrightEQUALleftANDORAND CHAR COMA COMMENT COMPARE CTE_CH CTE_F CTE_I CTE_STRING DESDE DET_ARR DIFFERENT DIV DOTCOMA ENTONCES EQUAL ESCRIBE FLOAT FUNCION HACER HASTA HAZ ID INT INV_ARR LBRACKET LEE LESS LESSEQUAL LPAREN LSTAPLE MIENTRAS MINUS MOD MORE MOREEQUAL MULT NOT NULL OR PLUS PRINCIPAL PROGRAMA RBRACKET REGRESA RPAREN RSTAPLE SI SINO STRING TRANS_ARR VAR VOIDempty :PROGRAM : PROGRAMA r_goto_main ID DOTCOMA VARS r_save_vars  FUNCTIONS MAIN r_print_constantsMAIN : PRINCIPAL r_save_func LPAREN RPAREN r_register_princ r_save_param_func VARS r_save_vars r_end_princ r_func_set BLOQUE r_func_end VARS : VAR VAR_AUX\n    | emptyVAR_AUX : TIPO IDS VAR_AUX\n    | emptyTIPO : INT r_save_type\n    | FLOAT r_save_type\n    | CHAR r_save_type\n    | STRING r_save_typeIDS : ID r_register_var ARRDIM DOTCOMA\n    | ID r_register_var ARRDIM COMA IDSARRDIM : LSTAPLE EXPRESION RSTAPLE\n    | LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE\n    | LSTAPLE EXPRESION COMA EXPRESION RSTAPLE\n    | emptyFUNCTIONS : FUNCTION FUNCTIONS\n    | emptyFUNCTION : FUNCION TIPO ID r_save_func r_register_func LPAREN PARAM RPAREN r_save_param_func VARS r_save_vars r_func_set BLOQUE r_func_end\n    | FUNCION VOID r_save_type ID r_save_func r_register_func LPAREN PARAM RPAREN r_save_param_func VARS r_save_vars r_func_set BLOQUE r_func_endPARAM : TIPO ID r_register_var PARENTESIS PARAM_AUX\n    | emptyPARAM_AUX : COMA PARAM\n    | emptyPARENTESIS : LSTAPLE RSTAPLE\n    | LSTAPLE RSTAPLE LSTAPLE RSTAPLE\n    | emptyBLOQUE : LBRACKET ESTATUTOS RBRACKETESTATUTOS : ESTATUTO ESTATUTOS\n    | emptyESTATUTO : ASIGNACION DOTCOMA\n    | FUN DOTCOMA\n    | COND\n    | WRITE DOTCOMA\n    | READ DOTCOMA\n    | RETURN DOTCOMAASIGNACION : ID r_seen_operand_id ARRDIM EQUAL r_seen_operator EXPRESION r_seen_equal\n    | ID r_seen_operand_id ARRDIM EQUAL r_seen_operator CTE_ARREXPRESION : SUBEXP r_seen_subexp EXPRESION_AUXEXPRESION_AUX : AND r_seen_operator EXPRESION\n    | OR r_seen_operator EXPRESION\n    | emptySUBEXP : EXP r_seen_exp SUBEXP_AUXSUBEXP_AUX : COMPARACION SUBEXP\n    | emptyCOMPARACION : MORE r_seen_operator\n    | LESS r_seen_operator\n    | COMPARE r_seen_operator\n    | DIFFERENT r_seen_operator\n    | MOREEQUAL r_seen_operator\n    | LESSEQUAL r_seen_operatorEXP : TERMINO r_seen_term EXP_AUXEXP_AUX : PLUS r_seen_operator EXP\n    | MINUS r_seen_operator EXP\n    | emptyTERMINO : FACTOR r_seen_factor TERMINO_AUXTERMINO_AUX : MULT r_seen_operator TERMINO\n    | DIV r_seen_operator TERMINO r_seen_term\n    | MOD r_seen_operator TERMINO r_seen_term\n    | emptyFACTOR : NOT r_seen_unary_operator FACTOR_AUX\n    | FACTOR_AUXFACTOR_AUX : SIGN LPAREN r_seen_operator EXPRESION RPAREN r_pop_fake_bottom\n    | SIGN CTE ARROPSIGN : PLUS r_seen_unary_operator\n    | MINUS r_seen_unary_operator\n    | emptyCTE : CTE_I r_seen_operand\n    | CTE_F r_seen_operand\n    | CTE_CH r_seen_operand\n    | CTE_STRING r_seen_operand\n    | FUN\n    | ID r_seen_operand_id ARRDIM ARROP : DET_ARR r_seen_operator_mat\n    | TRANS_ARR r_seen_operator_mat\n    | INV_ARR r_seen_operator_mat\n    | emptyFUN : ID r_check_func LPAREN FUN_AUX RPAREN r_go_subFUN_AUX : EXPRESION r_check_param COMA FUN_AUX\n    | EXPRESION r_check_param\n    | emptyCOND : IF\n    | FOR\n    | WHILEIF : SI LPAREN EXPRESION r_check_int RPAREN ENTONCES IF2 r_if_endIF2 : BLOQUE IF_AUX\n    | CONDIF_AUX : SINO r_else_start BLOQUE\n    | emptyWHILE :  MIENTRAS r_set_while LPAREN EXPRESION r_check_int RPAREN WHILE_AUX WHILE2 r_while_endWHILE2 :  BLOQUE\n    | CONDWHILE_AUX : HAZ\n    | empty FOR : DESDE ASIGNACION HASTA EXPRESION r_for_gen HACER FOR2 r_for_endFOR2 : BLOQUE\n    | CONDWRITE : ESCRIBE LPAREN WRITE_AUX RPARENWRITE_AUX : EXPRESION r_escribe WRITE_AUXSUBWRITE_AUXSUB : COMA WRITE_AUX\n    | emptyREAD : LEE LPAREN READ_AUX RPARENREAD_AUX : ID r_seen_operand_id ARRDIM r_lee READ_AUXSUBREAD_AUXSUB : COMA READ_AUX\n    | emptyRETURN : REGRESA LPAREN EXPRESION RPAREN r_regresa\n    | REGRESA LPAREN NULL RPARENCTE_ARR : LBRACKET CTE_ARR_AUX RBRACKET\n    | LBRACKET CTE_ARR_AUX2 RBRACKET CTE_ARR_AUX : CTE\n    | CTE_ARR_AUXSUB CTE_ARR_AUXSUB : COMA CTE_ARR_AUX\n    | empty CTE_ARR_AUX2 : LBRACKET CTE_ARR_AUX RBRACKET  CTE_ARR_AUX2SUBCTE_ARR_AUX2SUB : COMA CTE_ARR_AUX2\n    | empty r_save_type : r_save_func : r_register_func : r_register_var : r_register_princ : r_end_princ : r_seen_operand : r_seen_operand_id :r_seen_operator : r_seen_unary_operator : r_seen_equal : r_seen_subexp : r_seen_exp : r_seen_term : r_seen_factor : r_seen_operator_mat : r_pop_fake_bottom : r_check_int : r_if_end : r_else_start : r_set_while : r_while_end : r_for_gen : r_for_end : r_save_param_func : r_save_vars : r_func_set : r_func_end : r_check_func : r_check_param : r_go_sub : r_goto_main : r_regresa : r_escribe : r_lee : r_print_constants : '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,27,34,186,192,215,],[0,-153,-2,-145,-3,-29,]),'ID':([2,3,11,13,14,15,16,23,24,25,26,30,31,37,39,45,51,53,54,55,56,62,67,68,76,77,81,84,85,88,90,91,92,93,94,95,97,98,101,102,103,106,119,125,126,128,129,130,131,132,133,134,135,136,137,138,144,160,177,187,194,198,203,204,205,210,215,217,218,219,220,221,223,224,225,226,240,241,243,253,255,264,271,276,279,281,282,283,284,285,286,295,296,298,299,300,301,302,305,309,],[-149,4,22,-118,-118,-118,-118,-8,-9,-10,-11,36,-118,43,-1,22,-127,75,-127,-127,-68,-1,-1,-126,-66,-67,-1,-126,-126,-1,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-1,146,-1,-1,-47,-48,-49,-50,-51,-52,-1,-1,-1,-1,-1,-1,-68,-1,202,202,-34,-83,-84,-85,228,-29,-32,-33,-35,-36,-37,-1,236,-1,-1,-1,-1,-126,-1,-1,75,75,75,236,-136,-1,-88,-141,-97,-98,-86,-87,-90,-96,-139,-92,-93,-91,-89,]),'DOTCOMA':([4,22,33,38,40,47,48,49,50,52,61,63,64,65,66,69,70,71,72,73,74,75,83,86,87,89,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,124,127,140,141,142,143,149,150,151,152,153,154,155,156,157,165,166,167,168,176,196,197,199,200,201,244,246,248,249,258,262,263,270,291,292,],[5,-121,-1,44,-17,-129,-130,-131,-132,-63,-14,-1,-1,-1,-1,-1,-124,-124,-124,-124,-73,-125,-40,-43,-44,-46,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-45,-75,-76,-77,-74,-15,-41,-42,-54,-55,-58,-131,-131,-134,-59,-60,-64,-148,-79,217,218,219,220,221,-99,-103,-150,-108,-107,-128,-39,-38,-109,-110,]),'VAR':([5,57,78,118,147,163,164,175,],[7,-122,-142,7,-142,7,-142,7,]),'FUNCION':([5,6,7,8,9,10,12,18,21,32,44,60,213,215,230,231,242,],[-1,-143,-1,-5,20,-4,-7,20,-1,-6,-12,-13,-145,-29,-20,-145,-21,]),'PRINCIPAL':([5,6,7,8,9,10,12,17,18,19,21,29,32,44,60,213,215,230,231,242,],[-1,-143,-1,-5,-1,-4,-7,28,-1,-19,-1,-18,-6,-12,-13,-145,-29,-20,-145,-21,]),'INT':([7,20,21,44,60,79,122,180,],[13,13,13,-12,-13,13,13,13,]),'FLOAT':([7,20,21,44,60,79,122,180,],[14,14,14,-12,-13,14,14,14,]),'CHAR':([7,20,21,44,60,79,122,180,],[15,15,15,-12,-13,15,15,15,]),'STRING':([7,20,21,44,60,79,122,180,],[16,16,16,-12,-13,16,16,16,]),'LBRACKET':([7,8,10,12,21,32,44,57,60,78,118,145,147,161,163,164,170,174,175,178,183,184,190,191,214,243,253,264,267,268,269,287,288,289,297,304,307,],[-1,-5,-4,-7,-1,-6,-12,-122,-13,-142,-1,-143,-142,-123,-1,-142,-144,-143,-1,187,-144,-143,187,-144,187,-126,264,271,187,187,-1,187,-94,-95,-137,187,271,]),'VOID':([20,],[31,]),'LSTAPLE':([22,33,61,75,116,146,162,182,202,222,228,236,247,],[-121,39,81,-125,39,-121,172,189,-125,39,-125,-125,39,]),'COMA':([22,33,38,40,46,47,48,49,50,52,61,63,64,65,66,69,70,71,72,73,74,75,83,86,87,89,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,124,127,140,141,142,143,146,149,150,151,152,153,154,155,156,157,159,162,165,166,167,168,169,171,173,176,182,212,234,236,245,247,257,264,266,271,276,303,],[-121,-1,45,-17,62,-129,-130,-131,-132,-63,-14,-1,-1,-1,-1,-1,-124,-124,-124,-124,-73,-125,-40,-43,-44,-46,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-45,-75,-76,-77,-74,-121,-15,-41,-42,-54,-55,-58,-131,-131,-134,-147,-1,-59,-60,-64,-148,177,180,-28,-79,-26,-27,-151,-125,255,-1,-152,276,279,276,276,307,]),'LPAREN':([28,35,36,39,42,43,51,53,54,55,56,58,59,62,67,68,75,76,77,80,81,84,85,88,90,91,92,93,94,95,97,98,101,102,103,106,117,125,126,128,129,130,131,132,133,134,135,136,137,138,144,160,177,202,206,207,208,209,211,223,225,226,229,240,241,243,253,255,],[-119,41,-119,-1,-120,-119,-127,68,-127,-127,-68,79,-120,-1,-1,-126,-146,-66,-67,122,-1,-126,-126,-1,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-1,144,-1,-1,-47,-48,-49,-50,-51,-52,-1,-1,-1,-1,-1,-1,-68,-1,-146,223,224,225,226,-138,-1,-1,-1,241,-1,-1,-126,-1,-1,]),'NOT':([39,62,68,81,84,85,88,90,91,92,93,94,95,97,98,101,102,103,106,125,126,128,129,130,131,132,133,134,135,136,137,138,144,177,223,225,226,240,241,243,253,255,],[51,51,-126,51,-126,-126,51,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,51,51,51,-47,-48,-49,-50,-51,-52,51,51,51,51,51,51,51,51,51,51,51,51,-126,51,51,]),'PLUS':([39,40,49,50,51,52,61,62,65,66,67,68,69,70,71,72,73,74,75,81,84,85,88,90,91,92,93,94,95,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,124,125,126,128,129,130,131,132,133,134,135,136,137,138,140,141,142,143,144,149,154,155,156,157,165,166,167,168,176,177,223,225,226,240,241,243,253,255,],[54,-17,-131,-132,-127,-63,-14,54,97,-1,54,-126,-1,-124,-124,-124,-124,-73,-125,54,-126,-126,54,-126,-126,-126,-126,-126,-126,-126,-126,-57,-126,-126,-126,-61,-62,54,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,54,54,-47,-48,-49,-50,-51,-52,54,54,54,54,54,-75,-76,-77,-74,54,-15,-58,-131,-131,-134,-59,-60,-64,-148,-79,54,54,54,54,54,54,-126,54,54,]),'MINUS':([39,40,49,50,51,52,61,62,65,66,67,68,69,70,71,72,73,74,75,81,84,85,88,90,91,92,93,94,95,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,124,125,126,128,129,130,131,132,133,134,135,136,137,138,140,141,142,143,144,149,154,155,156,157,165,166,167,168,176,177,223,225,226,240,241,243,253,255,],[55,-17,-131,-132,-127,-63,-14,55,98,-1,55,-126,-1,-124,-124,-124,-124,-73,-125,55,-126,-126,55,-126,-126,-126,-126,-126,-126,-126,-126,-57,-126,-126,-126,-61,-62,55,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,55,55,-47,-48,-49,-50,-51,-52,55,55,55,55,55,-75,-76,-77,-74,55,-15,-58,-131,-131,-134,-59,-60,-64,-148,-79,55,55,55,55,55,55,-126,55,55,]),'CTE_I':([39,51,53,54,55,56,62,67,68,76,77,81,84,85,88,90,91,92,93,94,95,97,98,101,102,103,106,125,126,128,129,130,131,132,133,134,135,136,137,138,144,160,177,223,225,226,240,241,243,253,255,264,271,276,],[-1,-127,70,-127,-127,-68,-1,-1,-126,-66,-67,-1,-126,-126,-1,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-1,-1,-1,-47,-48,-49,-50,-51,-52,-1,-1,-1,-1,-1,-1,-68,-1,-1,-1,-1,-1,-1,-126,-1,-1,70,70,70,]),'CTE_F':([39,51,53,54,55,56,62,67,68,76,77,81,84,85,88,90,91,92,93,94,95,97,98,101,102,103,106,125,126,128,129,130,131,132,133,134,135,136,137,138,144,160,177,223,225,226,240,241,243,253,255,264,271,276,],[-1,-127,71,-127,-127,-68,-1,-1,-126,-66,-67,-1,-126,-126,-1,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-1,-1,-1,-47,-48,-49,-50,-51,-52,-1,-1,-1,-1,-1,-1,-68,-1,-1,-1,-1,-1,-1,-126,-1,-1,71,71,71,]),'CTE_CH':([39,51,53,54,55,56,62,67,68,76,77,81,84,85,88,90,91,92,93,94,95,97,98,101,102,103,106,125,126,128,129,130,131,132,133,134,135,136,137,138,144,160,177,223,225,226,240,241,243,253,255,264,271,276,],[-1,-127,72,-127,-127,-68,-1,-1,-126,-66,-67,-1,-126,-126,-1,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-1,-1,-1,-47,-48,-49,-50,-51,-52,-1,-1,-1,-1,-1,-1,-68,-1,-1,-1,-1,-1,-1,-126,-1,-1,72,72,72,]),'CTE_STRING':([39,51,53,54,55,56,62,67,68,76,77,81,84,85,88,90,91,92,93,94,95,97,98,101,102,103,106,125,126,128,129,130,131,132,133,134,135,136,137,138,144,160,177,223,225,226,240,241,243,253,255,264,271,276,],[-1,-127,73,-127,-127,-68,-1,-1,-126,-66,-67,-1,-126,-126,-1,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-1,-1,-1,-47,-48,-49,-50,-51,-52,-1,-1,-1,-1,-1,-1,-68,-1,-1,-1,-1,-1,-1,-126,-1,-1,73,73,73,]),'DET_ARR':([40,61,69,70,71,72,73,74,75,112,113,114,115,116,124,143,149,168,176,],[-17,-14,108,-124,-124,-124,-124,-73,-125,-69,-70,-71,-72,-1,-16,-74,-15,-148,-79,]),'TRANS_ARR':([40,61,69,70,71,72,73,74,75,112,113,114,115,116,124,143,149,168,176,],[-17,-14,109,-124,-124,-124,-124,-73,-125,-69,-70,-71,-72,-1,-16,-74,-15,-148,-79,]),'INV_ARR':([40,61,69,70,71,72,73,74,75,112,113,114,115,116,124,143,149,168,176,],[-17,-14,110,-124,-124,-124,-124,-73,-125,-69,-70,-71,-72,-1,-16,-74,-15,-148,-79,]),'MULT':([40,50,52,61,66,69,70,71,72,73,74,75,105,107,108,109,110,111,112,113,114,115,116,124,140,141,142,143,149,157,167,168,176,],[-17,-132,-63,-14,101,-1,-124,-124,-124,-124,-73,-125,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-75,-76,-77,-74,-15,-134,-64,-148,-79,]),'DIV':([40,50,52,61,66,69,70,71,72,73,74,75,105,107,108,109,110,111,112,113,114,115,116,124,140,141,142,143,149,157,167,168,176,],[-17,-132,-63,-14,102,-1,-124,-124,-124,-124,-73,-125,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-75,-76,-77,-74,-15,-134,-64,-148,-79,]),'MOD':([40,50,52,61,66,69,70,71,72,73,74,75,105,107,108,109,110,111,112,113,114,115,116,124,140,141,142,143,149,157,167,168,176,],[-17,-132,-63,-14,103,-1,-124,-124,-124,-124,-73,-125,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-75,-76,-77,-74,-15,-134,-64,-148,-79,]),'MORE':([40,48,49,50,52,61,64,65,66,69,70,71,72,73,74,75,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,124,140,141,142,143,149,152,153,154,155,156,157,165,166,167,168,176,],[-17,-130,-131,-132,-63,-14,90,-1,-1,-1,-124,-124,-124,-124,-73,-125,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-75,-76,-77,-74,-15,-54,-55,-58,-131,-131,-134,-59,-60,-64,-148,-79,]),'LESS':([40,48,49,50,52,61,64,65,66,69,70,71,72,73,74,75,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,124,140,141,142,143,149,152,153,154,155,156,157,165,166,167,168,176,],[-17,-130,-131,-132,-63,-14,91,-1,-1,-1,-124,-124,-124,-124,-73,-125,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-75,-76,-77,-74,-15,-54,-55,-58,-131,-131,-134,-59,-60,-64,-148,-79,]),'COMPARE':([40,48,49,50,52,61,64,65,66,69,70,71,72,73,74,75,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,124,140,141,142,143,149,152,153,154,155,156,157,165,166,167,168,176,],[-17,-130,-131,-132,-63,-14,92,-1,-1,-1,-124,-124,-124,-124,-73,-125,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-75,-76,-77,-74,-15,-54,-55,-58,-131,-131,-134,-59,-60,-64,-148,-79,]),'DIFFERENT':([40,48,49,50,52,61,64,65,66,69,70,71,72,73,74,75,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,124,140,141,142,143,149,152,153,154,155,156,157,165,166,167,168,176,],[-17,-130,-131,-132,-63,-14,93,-1,-1,-1,-124,-124,-124,-124,-73,-125,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-75,-76,-77,-74,-15,-54,-55,-58,-131,-131,-134,-59,-60,-64,-148,-79,]),'MOREEQUAL':([40,48,49,50,52,61,64,65,66,69,70,71,72,73,74,75,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,124,140,141,142,143,149,152,153,154,155,156,157,165,166,167,168,176,],[-17,-130,-131,-132,-63,-14,94,-1,-1,-1,-124,-124,-124,-124,-73,-125,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-75,-76,-77,-74,-15,-54,-55,-58,-131,-131,-134,-59,-60,-64,-148,-79,]),'LESSEQUAL':([40,48,49,50,52,61,64,65,66,69,70,71,72,73,74,75,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,124,140,141,142,143,149,152,153,154,155,156,157,165,166,167,168,176,],[-17,-130,-131,-132,-63,-14,95,-1,-1,-1,-124,-124,-124,-124,-73,-125,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-75,-76,-77,-74,-15,-54,-55,-58,-131,-131,-134,-59,-60,-64,-148,-79,]),'AND':([40,47,48,49,50,52,61,63,64,65,66,69,70,71,72,73,74,75,87,89,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,124,127,140,141,142,143,149,152,153,154,155,156,157,165,166,167,168,176,],[-17,-129,-130,-131,-132,-63,-14,84,-1,-1,-1,-1,-124,-124,-124,-124,-73,-125,-44,-46,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-45,-75,-76,-77,-74,-15,-54,-55,-58,-131,-131,-134,-59,-60,-64,-148,-79,]),'OR':([40,47,48,49,50,52,61,63,64,65,66,69,70,71,72,73,74,75,87,89,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,124,127,140,141,142,143,149,152,153,154,155,156,157,165,166,167,168,176,],[-17,-129,-130,-131,-132,-63,-14,85,-1,-1,-1,-1,-124,-124,-124,-124,-73,-125,-44,-46,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-45,-75,-76,-77,-74,-15,-54,-55,-58,-131,-131,-134,-59,-60,-64,-148,-79,]),'RSTAPLE':([40,46,47,48,49,50,52,61,63,64,65,66,69,70,71,72,73,74,75,82,83,86,87,89,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,123,124,127,140,141,142,143,149,150,151,152,153,154,155,156,157,165,166,167,168,172,176,189,],[-17,61,-129,-130,-131,-132,-63,-14,-1,-1,-1,-1,-1,-124,-124,-124,-124,-73,-125,124,-40,-43,-44,-46,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,149,-16,-45,-75,-76,-77,-74,-15,-41,-42,-54,-55,-58,-131,-131,-134,-59,-60,-64,-148,182,-79,212,]),'RPAREN':([40,41,47,48,49,50,52,61,63,64,65,66,69,70,71,72,73,74,75,79,83,86,87,89,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,120,121,122,124,127,139,140,141,142,143,144,146,148,149,150,151,152,153,154,155,156,157,158,159,160,162,165,166,167,168,169,171,173,176,177,179,180,181,182,185,188,212,233,234,235,236,237,238,239,245,247,250,252,254,256,257,261,265,266,278,280,294,],[-17,57,-129,-130,-131,-132,-63,-14,-1,-1,-1,-1,-1,-124,-124,-124,-124,-73,-125,-1,-40,-43,-44,-46,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,147,-23,-1,-16,-45,157,-75,-76,-77,-74,-1,-121,164,-15,-41,-42,-54,-55,-58,-131,-131,-134,168,-147,-82,-1,-59,-60,-64,-148,-81,-1,-28,-79,-1,-22,-1,-25,-26,-80,-24,-27,244,-151,246,-125,248,249,-135,-1,-1,259,-135,-100,-102,-152,269,-101,-1,-104,-106,-105,]),'HACER':([40,47,48,49,50,52,61,63,64,65,66,69,70,71,72,73,74,75,83,86,87,89,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,124,127,140,141,142,143,149,150,151,152,153,154,155,156,157,165,166,167,168,176,251,260,],[-17,-129,-130,-131,-132,-63,-14,-1,-1,-1,-1,-1,-124,-124,-124,-124,-73,-125,-40,-43,-44,-46,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-45,-75,-76,-77,-74,-15,-41,-42,-54,-55,-58,-131,-131,-134,-59,-60,-64,-148,-79,-140,268,]),'HASTA':([40,47,48,49,50,52,61,63,64,65,66,69,70,71,72,73,74,75,83,86,87,89,96,99,100,104,105,107,108,109,110,111,112,113,114,115,116,124,127,140,141,142,143,149,150,151,152,153,154,155,156,157,165,166,167,168,176,227,262,263,270,291,292,],[-17,-129,-130,-131,-132,-63,-14,-1,-1,-1,-1,-1,-124,-124,-124,-124,-73,-125,-40,-43,-44,-46,-53,-56,-57,-61,-62,-65,-133,-133,-133,-78,-69,-70,-71,-72,-1,-16,-45,-75,-76,-77,-74,-15,-41,-42,-54,-55,-58,-131,-131,-134,-59,-60,-64,-148,-79,240,-128,-39,-38,-109,-110,]),'RBRACKET':([40,61,70,71,72,73,74,75,112,113,114,115,116,124,143,149,168,176,187,193,194,195,198,203,204,205,215,216,217,218,219,220,221,264,271,272,273,274,275,276,277,281,282,283,284,285,286,290,293,295,296,298,299,300,301,302,303,305,306,308,309,310,],[-17,-14,-124,-124,-124,-124,-73,-125,-69,-70,-71,-72,-1,-16,-74,-15,-148,-79,-1,215,-1,-31,-34,-83,-84,-85,-29,-30,-32,-33,-35,-36,-37,-1,-1,291,292,-111,-112,-1,-114,-136,-1,-88,-141,-97,-98,303,-113,-86,-87,-90,-96,-139,-92,-93,-1,-91,-115,-117,-89,-116,]),'EQUAL':([40,61,124,149,202,222,228,232,],[-17,-14,-16,-15,-125,-1,-125,243,]),'ESCRIBE':([187,194,198,203,204,205,215,217,218,219,220,221,281,282,283,284,285,286,295,296,298,299,300,301,302,305,309,],[206,206,-34,-83,-84,-85,-29,-32,-33,-35,-36,-37,-136,-1,-88,-141,-97,-98,-86,-87,-90,-96,-139,-92,-93,-91,-89,]),'LEE':([187,194,198,203,204,205,215,217,218,219,220,221,281,282,283,284,285,286,295,296,298,299,300,301,302,305,309,],[207,207,-34,-83,-84,-85,-29,-32,-33,-35,-36,-37,-136,-1,-88,-141,-97,-98,-86,-87,-90,-96,-139,-92,-93,-91,-89,]),'REGRESA':([187,194,198,203,204,205,215,217,218,219,220,221,281,282,283,284,285,286,295,296,298,299,300,301,302,305,309,],[208,208,-34,-83,-84,-85,-29,-32,-33,-35,-36,-37,-136,-1,-88,-141,-97,-98,-86,-87,-90,-96,-139,-92,-93,-91,-89,]),'SI':([187,194,198,203,204,205,215,217,218,219,220,221,267,268,269,281,282,283,284,285,286,287,288,289,295,296,298,299,300,301,302,305,309,],[209,209,-34,-83,-84,-85,-29,-32,-33,-35,-36,-37,209,209,-1,-136,-1,-88,-141,-97,-98,209,-94,-95,-86,-87,-90,-96,-139,-92,-93,-91,-89,]),'DESDE':([187,194,198,203,204,205,215,217,218,219,220,221,267,268,269,281,282,283,284,285,286,287,288,289,295,296,298,299,300,301,302,305,309,],[210,210,-34,-83,-84,-85,-29,-32,-33,-35,-36,-37,210,210,-1,-136,-1,-88,-141,-97,-98,210,-94,-95,-86,-87,-90,-96,-139,-92,-93,-91,-89,]),'MIENTRAS':([187,194,198,203,204,205,215,217,218,219,220,221,267,268,269,281,282,283,284,285,286,287,288,289,295,296,298,299,300,301,302,305,309,],[211,211,-34,-83,-84,-85,-29,-32,-33,-35,-36,-37,211,211,-1,-136,-1,-88,-141,-97,-98,211,-94,-95,-86,-87,-90,-96,-139,-92,-93,-91,-89,]),'SINO':([215,282,],[-29,297,]),'NULL':([225,],[238,]),'ENTONCES':([259,],[267,]),'HAZ':([269,],[288,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'r_goto_main':([2,],[3,]),'VARS':([5,118,163,175,],[6,145,174,184,]),'empty':([5,7,9,18,21,33,39,62,63,64,65,66,67,69,79,81,88,106,116,118,122,125,126,134,135,136,137,138,144,162,163,171,175,177,180,187,194,222,223,225,226,240,241,245,247,253,255,264,266,269,271,276,282,303,],[8,12,19,19,12,40,56,56,86,89,99,104,56,111,121,56,56,56,40,8,121,56,56,56,56,56,56,56,160,173,8,181,8,160,121,195,195,40,56,56,56,56,56,256,40,56,56,277,280,289,277,277,298,308,]),'r_save_vars':([6,145,174,184,],[9,161,183,191,]),'VAR_AUX':([7,21,],[10,32,]),'TIPO':([7,20,21,79,122,180,],[11,30,11,119,119,119,]),'FUNCTIONS':([9,18,],[17,29,]),'FUNCTION':([9,18,],[18,18,]),'IDS':([11,45,],[21,60,]),'r_save_type':([13,14,15,16,31,],[23,24,25,26,37,]),'MAIN':([17,],[27,]),'r_register_var':([22,146,],[33,162,]),'r_print_constants':([27,],[34,]),'r_save_func':([28,36,43,],[35,42,59,]),'ARRDIM':([33,116,222,247,],[38,143,232,257,]),'EXPRESION':([39,62,81,106,125,126,144,177,223,225,226,240,241,253,255,],[46,82,123,139,150,151,159,159,234,237,239,251,252,262,234,]),'SUBEXP':([39,62,81,88,106,125,126,144,177,223,225,226,240,241,253,255,],[47,47,47,127,47,47,47,47,47,47,47,47,47,47,47,47,]),'EXP':([39,62,81,88,106,125,126,134,135,144,177,223,225,226,240,241,253,255,],[48,48,48,48,48,48,48,152,153,48,48,48,48,48,48,48,48,48,]),'TERMINO':([39,62,81,88,106,125,126,134,135,136,137,138,144,177,223,225,226,240,241,253,255,],[49,49,49,49,49,49,49,49,49,154,155,156,49,49,49,49,49,49,49,49,49,]),'FACTOR':([39,62,81,88,106,125,126,134,135,136,137,138,144,177,223,225,226,240,241,253,255,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'FACTOR_AUX':([39,62,67,81,88,106,125,126,134,135,136,137,138,144,177,223,225,226,240,241,253,255,],[52,52,105,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'SIGN':([39,62,67,81,88,106,125,126,134,135,136,137,138,144,177,223,225,226,240,241,253,255,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'r_register_func':([42,59,],[58,80,]),'r_seen_subexp':([47,],[63,]),'r_seen_exp':([48,],[64,]),'r_seen_term':([49,155,156,],[65,165,166,]),'r_seen_factor':([50,],[66,]),'r_seen_unary_operator':([51,54,55,],[67,76,77,]),'CTE':([53,264,271,276,],[69,274,274,274,]),'FUN':([53,187,194,264,271,276,],[74,197,197,74,74,74,]),'r_register_princ':([57,],[78,]),'EXPRESION_AUX':([63,],[83,]),'SUBEXP_AUX':([64,],[87,]),'COMPARACION':([64,],[88,]),'EXP_AUX':([65,],[96,]),'TERMINO_AUX':([66,],[100,]),'r_seen_operator':([68,84,85,90,91,92,93,94,95,97,98,101,102,103,243,],[106,125,126,128,129,130,131,132,133,134,135,136,137,138,253,]),'ARROP':([69,],[107,]),'r_seen_operand':([70,71,72,73,],[112,113,114,115,]),'r_seen_operand_id':([75,202,228,236,],[116,222,222,247,]),'r_check_func':([75,202,],[117,117,]),'r_save_param_func':([78,147,164,],[118,163,175,]),'PARAM':([79,122,180,],[120,148,188,]),'r_seen_operator_mat':([108,109,110,],[140,141,142,]),'FUN_AUX':([144,177,],[158,185,]),'r_pop_fake_bottom':([157,],[167,]),'r_check_param':([159,],[169,]),'r_end_princ':([161,],[170,]),'PARENTESIS':([162,],[171,]),'r_go_sub':([168,],[176,]),'r_func_set':([170,183,191,],[178,190,214,]),'PARAM_AUX':([171,],[179,]),'BLOQUE':([178,190,214,267,268,287,304,],[186,213,231,282,285,301,309,]),'r_func_end':([186,213,231,],[192,230,242,]),'ESTATUTOS':([187,194,],[193,216,]),'ESTATUTO':([187,194,],[194,194,]),'ASIGNACION':([187,194,210,],[196,196,227,]),'COND':([187,194,267,268,287,],[198,198,283,286,302,]),'WRITE':([187,194,],[199,199,]),'READ':([187,194,],[200,200,]),'RETURN':([187,194,],[201,201,]),'IF':([187,194,267,268,287,],[203,203,203,203,203,]),'FOR':([187,194,267,268,287,],[204,204,204,204,204,]),'WHILE':([187,194,267,268,287,],[205,205,205,205,205,]),'r_set_while':([211,],[229,]),'WRITE_AUX':([223,255,],[233,265,]),'READ_AUX':([224,279,],[235,294,]),'r_escribe':([234,],[245,]),'r_check_int':([239,252,],[250,261,]),'WRITE_AUXSUB':([245,],[254,]),'r_regresa':([248,],[258,]),'r_for_gen':([251,],[260,]),'CTE_ARR':([253,],[263,]),'r_lee':([257,],[266,]),'r_seen_equal':([262,],[270,]),'CTE_ARR_AUX':([264,271,276,],[272,290,293,]),'CTE_ARR_AUX2':([264,307,],[273,310,]),'CTE_ARR_AUXSUB':([264,271,276,],[275,275,275,]),'READ_AUXSUB':([266,],[278,]),'IF2':([267,],[281,]),'FOR2':([268,],[284,]),'WHILE_AUX':([269,],[287,]),'r_if_end':([281,],[295,]),'IF_AUX':([282,],[296,]),'r_for_end':([284,],[299,]),'WHILE2':([287,],[300,]),'r_else_start':([297,],[304,]),'r_while_end':([300,],[305,]),'CTE_ARR_AUX2SUB':([303,],[306,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',17),
  ('PROGRAM -> PROGRAMA r_goto_main ID DOTCOMA VARS r_save_vars FUNCTIONS MAIN r_print_constants','PROGRAM',9,'p_PROGRAM','parser.py',22),
  ('MAIN -> PRINCIPAL r_save_func LPAREN RPAREN r_register_princ r_save_param_func VARS r_save_vars r_end_princ r_func_set BLOQUE r_func_end','MAIN',12,'p_MAIN','parser.py',27),
  ('VARS -> VAR VAR_AUX','VARS',2,'p_VARS','parser.py',32),
  ('VARS -> empty','VARS',1,'p_VARS','parser.py',33),
  ('VAR_AUX -> TIPO IDS VAR_AUX','VAR_AUX',3,'p_VAR_AUX','parser.py',38),
  ('VAR_AUX -> empty','VAR_AUX',1,'p_VAR_AUX','parser.py',39),
  ('TIPO -> INT r_save_type','TIPO',2,'p_TIPO','parser.py',44),
  ('TIPO -> FLOAT r_save_type','TIPO',2,'p_TIPO','parser.py',45),
  ('TIPO -> CHAR r_save_type','TIPO',2,'p_TIPO','parser.py',46),
  ('TIPO -> STRING r_save_type','TIPO',2,'p_TIPO','parser.py',47),
  ('IDS -> ID r_register_var ARRDIM DOTCOMA','IDS',4,'p_IDS','parser.py',52),
  ('IDS -> ID r_register_var ARRDIM COMA IDS','IDS',5,'p_IDS','parser.py',53),
  ('ARRDIM -> LSTAPLE EXPRESION RSTAPLE','ARRDIM',3,'p_ARRDIM','parser.py',58),
  ('ARRDIM -> LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE','ARRDIM',6,'p_ARRDIM','parser.py',59),
  ('ARRDIM -> LSTAPLE EXPRESION COMA EXPRESION RSTAPLE','ARRDIM',5,'p_ARRDIM','parser.py',60),
  ('ARRDIM -> empty','ARRDIM',1,'p_ARRDIM','parser.py',61),
  ('FUNCTIONS -> FUNCTION FUNCTIONS','FUNCTIONS',2,'p_FUNCTIONS','parser.py',66),
  ('FUNCTIONS -> empty','FUNCTIONS',1,'p_FUNCTIONS','parser.py',67),
  ('FUNCTION -> FUNCION TIPO ID r_save_func r_register_func LPAREN PARAM RPAREN r_save_param_func VARS r_save_vars r_func_set BLOQUE r_func_end','FUNCTION',14,'p_FUNCTION','parser.py',72),
  ('FUNCTION -> FUNCION VOID r_save_type ID r_save_func r_register_func LPAREN PARAM RPAREN r_save_param_func VARS r_save_vars r_func_set BLOQUE r_func_end','FUNCTION',15,'p_FUNCTION','parser.py',73),
  ('PARAM -> TIPO ID r_register_var PARENTESIS PARAM_AUX','PARAM',5,'p_PARAM','parser.py',79),
  ('PARAM -> empty','PARAM',1,'p_PARAM','parser.py',80),
  ('PARAM_AUX -> COMA PARAM','PARAM_AUX',2,'p_PARAM_AUX','parser.py',85),
  ('PARAM_AUX -> empty','PARAM_AUX',1,'p_PARAM_AUX','parser.py',86),
  ('PARENTESIS -> LSTAPLE RSTAPLE','PARENTESIS',2,'p_PARENTESIS','parser.py',91),
  ('PARENTESIS -> LSTAPLE RSTAPLE LSTAPLE RSTAPLE','PARENTESIS',4,'p_PARENTESIS','parser.py',92),
  ('PARENTESIS -> empty','PARENTESIS',1,'p_PARENTESIS','parser.py',93),
  ('BLOQUE -> LBRACKET ESTATUTOS RBRACKET','BLOQUE',3,'p_BLOQUE','parser.py',98),
  ('ESTATUTOS -> ESTATUTO ESTATUTOS','ESTATUTOS',2,'p_ESTATUTOS','parser.py',103),
  ('ESTATUTOS -> empty','ESTATUTOS',1,'p_ESTATUTOS','parser.py',104),
  ('ESTATUTO -> ASIGNACION DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',109),
  ('ESTATUTO -> FUN DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',110),
  ('ESTATUTO -> COND','ESTATUTO',1,'p_ESTATUTO','parser.py',111),
  ('ESTATUTO -> WRITE DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',112),
  ('ESTATUTO -> READ DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',113),
  ('ESTATUTO -> RETURN DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',114),
  ('ASIGNACION -> ID r_seen_operand_id ARRDIM EQUAL r_seen_operator EXPRESION r_seen_equal','ASIGNACION',7,'p_ASIGNACION','parser.py',119),
  ('ASIGNACION -> ID r_seen_operand_id ARRDIM EQUAL r_seen_operator CTE_ARR','ASIGNACION',6,'p_ASIGNACION','parser.py',120),
  ('EXPRESION -> SUBEXP r_seen_subexp EXPRESION_AUX','EXPRESION',3,'p_EXPRESION','parser.py',125),
  ('EXPRESION_AUX -> AND r_seen_operator EXPRESION','EXPRESION_AUX',3,'p_EXPRESION_AUX','parser.py',130),
  ('EXPRESION_AUX -> OR r_seen_operator EXPRESION','EXPRESION_AUX',3,'p_EXPRESION_AUX','parser.py',131),
  ('EXPRESION_AUX -> empty','EXPRESION_AUX',1,'p_EXPRESION_AUX','parser.py',132),
  ('SUBEXP -> EXP r_seen_exp SUBEXP_AUX','SUBEXP',3,'p_SUBEXP','parser.py',137),
  ('SUBEXP_AUX -> COMPARACION SUBEXP','SUBEXP_AUX',2,'p_SUBEXP_AUX','parser.py',142),
  ('SUBEXP_AUX -> empty','SUBEXP_AUX',1,'p_SUBEXP_AUX','parser.py',143),
  ('COMPARACION -> MORE r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',148),
  ('COMPARACION -> LESS r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',149),
  ('COMPARACION -> COMPARE r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',150),
  ('COMPARACION -> DIFFERENT r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',151),
  ('COMPARACION -> MOREEQUAL r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',152),
  ('COMPARACION -> LESSEQUAL r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',153),
  ('EXP -> TERMINO r_seen_term EXP_AUX','EXP',3,'p_EXP','parser.py',158),
  ('EXP_AUX -> PLUS r_seen_operator EXP','EXP_AUX',3,'p_EXP_AUX','parser.py',163),
  ('EXP_AUX -> MINUS r_seen_operator EXP','EXP_AUX',3,'p_EXP_AUX','parser.py',164),
  ('EXP_AUX -> empty','EXP_AUX',1,'p_EXP_AUX','parser.py',165),
  ('TERMINO -> FACTOR r_seen_factor TERMINO_AUX','TERMINO',3,'p_TERMINO','parser.py',170),
  ('TERMINO_AUX -> MULT r_seen_operator TERMINO','TERMINO_AUX',3,'p_TERMINO_AUX','parser.py',175),
  ('TERMINO_AUX -> DIV r_seen_operator TERMINO r_seen_term','TERMINO_AUX',4,'p_TERMINO_AUX','parser.py',176),
  ('TERMINO_AUX -> MOD r_seen_operator TERMINO r_seen_term','TERMINO_AUX',4,'p_TERMINO_AUX','parser.py',177),
  ('TERMINO_AUX -> empty','TERMINO_AUX',1,'p_TERMINO_AUX','parser.py',178),
  ('FACTOR -> NOT r_seen_unary_operator FACTOR_AUX','FACTOR',3,'p_FACTOR','parser.py',183),
  ('FACTOR -> FACTOR_AUX','FACTOR',1,'p_FACTOR','parser.py',184),
  ('FACTOR_AUX -> SIGN LPAREN r_seen_operator EXPRESION RPAREN r_pop_fake_bottom','FACTOR_AUX',6,'p_FACTOR_AUX','parser.py',191),
  ('FACTOR_AUX -> SIGN CTE ARROP','FACTOR_AUX',3,'p_FACTOR_AUX','parser.py',192),
  ('SIGN -> PLUS r_seen_unary_operator','SIGN',2,'p_SIGN','parser.py',199),
  ('SIGN -> MINUS r_seen_unary_operator','SIGN',2,'p_SIGN','parser.py',200),
  ('SIGN -> empty','SIGN',1,'p_SIGN','parser.py',201),
  ('CTE -> CTE_I r_seen_operand','CTE',2,'p_CTE','parser.py',205),
  ('CTE -> CTE_F r_seen_operand','CTE',2,'p_CTE','parser.py',206),
  ('CTE -> CTE_CH r_seen_operand','CTE',2,'p_CTE','parser.py',207),
  ('CTE -> CTE_STRING r_seen_operand','CTE',2,'p_CTE','parser.py',208),
  ('CTE -> FUN','CTE',1,'p_CTE','parser.py',209),
  ('CTE -> ID r_seen_operand_id ARRDIM','CTE',3,'p_CTE','parser.py',210),
  ('ARROP -> DET_ARR r_seen_operator_mat','ARROP',2,'p_ARROP','parser.py',216),
  ('ARROP -> TRANS_ARR r_seen_operator_mat','ARROP',2,'p_ARROP','parser.py',217),
  ('ARROP -> INV_ARR r_seen_operator_mat','ARROP',2,'p_ARROP','parser.py',218),
  ('ARROP -> empty','ARROP',1,'p_ARROP','parser.py',219),
  ('FUN -> ID r_check_func LPAREN FUN_AUX RPAREN r_go_sub','FUN',6,'p_FUN','parser.py',224),
  ('FUN_AUX -> EXPRESION r_check_param COMA FUN_AUX','FUN_AUX',4,'p_FUN_AUX','parser.py',229),
  ('FUN_AUX -> EXPRESION r_check_param','FUN_AUX',2,'p_FUN_AUX','parser.py',230),
  ('FUN_AUX -> empty','FUN_AUX',1,'p_FUN_AUX','parser.py',231),
  ('COND -> IF','COND',1,'p_COND','parser.py',236),
  ('COND -> FOR','COND',1,'p_COND','parser.py',237),
  ('COND -> WHILE','COND',1,'p_COND','parser.py',238),
  ('IF -> SI LPAREN EXPRESION r_check_int RPAREN ENTONCES IF2 r_if_end','IF',8,'p_IF','parser.py',243),
  ('IF2 -> BLOQUE IF_AUX','IF2',2,'p_IF2','parser.py',248),
  ('IF2 -> COND','IF2',1,'p_IF2','parser.py',249),
  ('IF_AUX -> SINO r_else_start BLOQUE','IF_AUX',3,'p_IF_AUX','parser.py',254),
  ('IF_AUX -> empty','IF_AUX',1,'p_IF_AUX','parser.py',255),
  ('WHILE -> MIENTRAS r_set_while LPAREN EXPRESION r_check_int RPAREN WHILE_AUX WHILE2 r_while_end','WHILE',9,'p_WHILE','parser.py',260),
  ('WHILE2 -> BLOQUE','WHILE2',1,'p_WHILE2','parser.py',265),
  ('WHILE2 -> COND','WHILE2',1,'p_WHILE2','parser.py',266),
  ('WHILE_AUX -> HAZ','WHILE_AUX',1,'p_WHILE_AUX','parser.py',271),
  ('WHILE_AUX -> empty','WHILE_AUX',1,'p_WHILE_AUX','parser.py',272),
  ('FOR -> DESDE ASIGNACION HASTA EXPRESION r_for_gen HACER FOR2 r_for_end','FOR',8,'p_FOR','parser.py',277),
  ('FOR2 -> BLOQUE','FOR2',1,'p_FOR2','parser.py',282),
  ('FOR2 -> COND','FOR2',1,'p_FOR2','parser.py',283),
  ('WRITE -> ESCRIBE LPAREN WRITE_AUX RPAREN','WRITE',4,'p_WRITE','parser.py',288),
  ('WRITE_AUX -> EXPRESION r_escribe WRITE_AUXSUB','WRITE_AUX',3,'p_WRITE_AUX','parser.py',293),
  ('WRITE_AUXSUB -> COMA WRITE_AUX','WRITE_AUXSUB',2,'p_WRITE_AUXSUB','parser.py',298),
  ('WRITE_AUXSUB -> empty','WRITE_AUXSUB',1,'p_WRITE_AUXSUB','parser.py',299),
  ('READ -> LEE LPAREN READ_AUX RPAREN','READ',4,'p_READ','parser.py',304),
  ('READ_AUX -> ID r_seen_operand_id ARRDIM r_lee READ_AUXSUB','READ_AUX',5,'p_READ_AUX','parser.py',309),
  ('READ_AUXSUB -> COMA READ_AUX','READ_AUXSUB',2,'p_READ_AUXSUB','parser.py',314),
  ('READ_AUXSUB -> empty','READ_AUXSUB',1,'p_READ_AUXSUB','parser.py',315),
  ('RETURN -> REGRESA LPAREN EXPRESION RPAREN r_regresa','RETURN',5,'p_RETURN','parser.py',320),
  ('RETURN -> REGRESA LPAREN NULL RPAREN','RETURN',4,'p_RETURN','parser.py',321),
  ('CTE_ARR -> LBRACKET CTE_ARR_AUX RBRACKET','CTE_ARR',3,'p_CTE_ARR','parser.py',326),
  ('CTE_ARR -> LBRACKET CTE_ARR_AUX2 RBRACKET','CTE_ARR',3,'p_CTE_ARR','parser.py',327),
  ('CTE_ARR_AUX -> CTE','CTE_ARR_AUX',1,'p_CTE_ARR_AUX','parser.py',332),
  ('CTE_ARR_AUX -> CTE_ARR_AUXSUB','CTE_ARR_AUX',1,'p_CTE_ARR_AUX','parser.py',333),
  ('CTE_ARR_AUXSUB -> COMA CTE_ARR_AUX','CTE_ARR_AUXSUB',2,'p_CTE_ARR_AUXSUB','parser.py',338),
  ('CTE_ARR_AUXSUB -> empty','CTE_ARR_AUXSUB',1,'p_CTE_ARR_AUXSUB','parser.py',339),
  ('CTE_ARR_AUX2 -> LBRACKET CTE_ARR_AUX RBRACKET CTE_ARR_AUX2SUB','CTE_ARR_AUX2',4,'p_CTE_ARR_AUX2','parser.py',344),
  ('CTE_ARR_AUX2SUB -> COMA CTE_ARR_AUX2','CTE_ARR_AUX2SUB',2,'p_CTE_ARR_AUX2SUB','parser.py',349),
  ('CTE_ARR_AUX2SUB -> empty','CTE_ARR_AUX2SUB',1,'p_CTE_ARR_AUX2SUB','parser.py',350),
  ('r_save_type -> <empty>','r_save_type',0,'p_r_save_type','parser.py',363),
  ('r_save_func -> <empty>','r_save_func',0,'p_r_save_func','parser.py',368),
  ('r_register_func -> <empty>','r_register_func',0,'p_r_register_func','parser.py',373),
  ('r_register_var -> <empty>','r_register_var',0,'p_r_register_var','parser.py',392),
  ('r_register_princ -> <empty>','r_register_princ',0,'p_r_register_princ','parser.py',418),
  ('r_end_princ -> <empty>','r_end_princ',0,'p_r_end_princ','parser.py',426),
  ('r_seen_operand -> <empty>','r_seen_operand',0,'p_r_seen_operand','parser.py',433),
  ('r_seen_operand_id -> <empty>','r_seen_operand_id',0,'p_r_seen_operand_id','parser.py',439),
  ('r_seen_operator -> <empty>','r_seen_operator',0,'p_r_seen_operator','parser.py',445),
  ('r_seen_unary_operator -> <empty>','r_seen_unary_operator',0,'p_r_seen_unary_operator','parser.py',451),
  ('r_seen_equal -> <empty>','r_seen_equal',0,'p_r_seen_equal','parser.py',465),
  ('r_seen_subexp -> <empty>','r_seen_subexp',0,'p_r_seen_subexp','parser.py',471),
  ('r_seen_exp -> <empty>','r_seen_exp',0,'p_r_seen_exp','parser.py',477),
  ('r_seen_term -> <empty>','r_seen_term',0,'p_r_seen_term','parser.py',483),
  ('r_seen_factor -> <empty>','r_seen_factor',0,'p_r_seen_factor','parser.py',489),
  ('r_seen_operator_mat -> <empty>','r_seen_operator_mat',0,'p_r_seen_operator_mat','parser.py',495),
  ('r_pop_fake_bottom -> <empty>','r_pop_fake_bottom',0,'p_r_pop_fake_bottom','parser.py',499),
  ('r_check_int -> <empty>','r_check_int',0,'p_r_check_int','parser.py',505),
  ('r_if_end -> <empty>','r_if_end',0,'p_r_if_end','parser.py',511),
  ('r_else_start -> <empty>','r_else_start',0,'p_r_else_start','parser.py',517),
  ('r_set_while -> <empty>','r_set_while',0,'p_r_set_while','parser.py',523),
  ('r_while_end -> <empty>','r_while_end',0,'p_r_while_end','parser.py',529),
  ('r_for_gen -> <empty>','r_for_gen',0,'p_r_for_gen','parser.py',535),
  ('r_for_end -> <empty>','r_for_end',0,'p_r_for_end','parser.py',541),
  ('r_save_param_func -> <empty>','r_save_param_func',0,'p_r_save_param_func','parser.py',547),
  ('r_save_vars -> <empty>','r_save_vars',0,'p_r_save_vars','parser.py',553),
  ('r_func_set -> <empty>','r_func_set',0,'p_r_func_set','parser.py',559),
  ('r_func_end -> <empty>','r_func_end',0,'p_r_func_end','parser.py',565),
  ('r_check_func -> <empty>','r_check_func',0,'p_r_check_func','parser.py',571),
  ('r_check_param -> <empty>','r_check_param',0,'p_r_check_param','parser.py',579),
  ('r_go_sub -> <empty>','r_go_sub',0,'p_r_go_sub','parser.py',586),
  ('r_goto_main -> <empty>','r_goto_main',0,'p_r_goto_main','parser.py',593),
  ('r_regresa -> <empty>','r_regresa',0,'p_r_regresa','parser.py',599),
  ('r_escribe -> <empty>','r_escribe',0,'p_r_escribe','parser.py',605),
  ('r_lee -> <empty>','r_lee',0,'p_r_lee','parser.py',611),
  ('r_print_constants -> <empty>','r_print_constants',0,'p_r_print_constants','parser.py',617),
]
