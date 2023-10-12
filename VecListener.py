# Generated from Vec.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .VecParser import VecParser
else:
    from VecParser import VecParser

# This class defines a complete listener for a parse tree produced by VecParser.
class VecListener(ParseTreeListener):

    # Enter a parse tree produced by VecParser#blockParse.
    def enterBlockParse(self, ctx:VecParser.BlockParseContext):
        pass

    # Exit a parse tree produced by VecParser#blockParse.
    def exitBlockParse(self, ctx:VecParser.BlockParseContext):
        pass


    # Enter a parse tree produced by VecParser#forParse.
    def enterForParse(self, ctx:VecParser.ForParseContext):
        pass

    # Exit a parse tree produced by VecParser#forParse.
    def exitForParse(self, ctx:VecParser.ForParseContext):
        pass


    # Enter a parse tree produced by VecParser#block.
    def enterBlock(self, ctx:VecParser.BlockContext):
        pass

    # Exit a parse tree produced by VecParser#block.
    def exitBlock(self, ctx:VecParser.BlockContext):
        pass


    # Enter a parse tree produced by VecParser#assignStatement.
    def enterAssignStatement(self, ctx:VecParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by VecParser#assignStatement.
    def exitAssignStatement(self, ctx:VecParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by VecParser#ifStatement.
    def enterIfStatement(self, ctx:VecParser.IfStatementContext):
        pass

    # Exit a parse tree produced by VecParser#ifStatement.
    def exitIfStatement(self, ctx:VecParser.IfStatementContext):
        pass


    # Enter a parse tree produced by VecParser#forStatement.
    def enterForStatement(self, ctx:VecParser.ForStatementContext):
        pass

    # Exit a parse tree produced by VecParser#forStatement.
    def exitForStatement(self, ctx:VecParser.ForStatementContext):
        pass


    # Enter a parse tree produced by VecParser#simdDoubleFmaddStatement.
    def enterSimdDoubleFmaddStatement(self, ctx:VecParser.SimdDoubleFmaddStatementContext):
        pass

    # Exit a parse tree produced by VecParser#simdDoubleFmaddStatement.
    def exitSimdDoubleFmaddStatement(self, ctx:VecParser.SimdDoubleFmaddStatementContext):
        pass


    # Enter a parse tree produced by VecParser#matmulKernel8x16Statement.
    def enterMatmulKernel8x16Statement(self, ctx:VecParser.MatmulKernel8x16StatementContext):
        pass

    # Exit a parse tree produced by VecParser#matmulKernel8x16Statement.
    def exitMatmulKernel8x16Statement(self, ctx:VecParser.MatmulKernel8x16StatementContext):
        pass


    # Enter a parse tree produced by VecParser#matmulKernel2x8Statement.
    def enterMatmulKernel2x8Statement(self, ctx:VecParser.MatmulKernel2x8StatementContext):
        pass

    # Exit a parse tree produced by VecParser#matmulKernel2x8Statement.
    def exitMatmulKernel2x8Statement(self, ctx:VecParser.MatmulKernel2x8StatementContext):
        pass


    # Enter a parse tree produced by VecParser#matmulKernel1D2x8Statement.
    def enterMatmulKernel1D2x8Statement(self, ctx:VecParser.MatmulKernel1D2x8StatementContext):
        pass

    # Exit a parse tree produced by VecParser#matmulKernel1D2x8Statement.
    def exitMatmulKernel1D2x8Statement(self, ctx:VecParser.MatmulKernel1D2x8StatementContext):
        pass


    # Enter a parse tree produced by VecParser#gotoKernel8x8Statement.
    def enterGotoKernel8x8Statement(self, ctx:VecParser.GotoKernel8x8StatementContext):
        pass

    # Exit a parse tree produced by VecParser#gotoKernel8x8Statement.
    def exitGotoKernel8x8Statement(self, ctx:VecParser.GotoKernel8x8StatementContext):
        pass


    # Enter a parse tree produced by VecParser#convKernelStatement.
    def enterConvKernelStatement(self, ctx:VecParser.ConvKernelStatementContext):
        pass

    # Exit a parse tree produced by VecParser#convKernelStatement.
    def exitConvKernelStatement(self, ctx:VecParser.ConvKernelStatementContext):
        pass


    # Enter a parse tree produced by VecParser#declarativeLoopStatement.
    def enterDeclarativeLoopStatement(self, ctx:VecParser.DeclarativeLoopStatementContext):
        pass

    # Exit a parse tree produced by VecParser#declarativeLoopStatement.
    def exitDeclarativeLoopStatement(self, ctx:VecParser.DeclarativeLoopStatementContext):
        pass


    # Enter a parse tree produced by VecParser#ifStmt.
    def enterIfStmt(self, ctx:VecParser.IfStmtContext):
        pass

    # Exit a parse tree produced by VecParser#ifStmt.
    def exitIfStmt(self, ctx:VecParser.IfStmtContext):
        pass


    # Enter a parse tree produced by VecParser#forStmt.
    def enterForStmt(self, ctx:VecParser.ForStmtContext):
        pass

    # Exit a parse tree produced by VecParser#forStmt.
    def exitForStmt(self, ctx:VecParser.ForStmtContext):
        pass


    # Enter a parse tree produced by VecParser#equalAssn.
    def enterEqualAssn(self, ctx:VecParser.EqualAssnContext):
        pass

    # Exit a parse tree produced by VecParser#equalAssn.
    def exitEqualAssn(self, ctx:VecParser.EqualAssnContext):
        pass


    # Enter a parse tree produced by VecParser#unaryAssnFront.
    def enterUnaryAssnFront(self, ctx:VecParser.UnaryAssnFrontContext):
        pass

    # Exit a parse tree produced by VecParser#unaryAssnFront.
    def exitUnaryAssnFront(self, ctx:VecParser.UnaryAssnFrontContext):
        pass


    # Enter a parse tree produced by VecParser#unaryAssnBack.
    def enterUnaryAssnBack(self, ctx:VecParser.UnaryAssnBackContext):
        pass

    # Exit a parse tree produced by VecParser#unaryAssnBack.
    def exitUnaryAssnBack(self, ctx:VecParser.UnaryAssnBackContext):
        pass


    # Enter a parse tree produced by VecParser#simdDoubleFmadd.
    def enterSimdDoubleFmadd(self, ctx:VecParser.SimdDoubleFmaddContext):
        pass

    # Exit a parse tree produced by VecParser#simdDoubleFmadd.
    def exitSimdDoubleFmadd(self, ctx:VecParser.SimdDoubleFmaddContext):
        pass


    # Enter a parse tree produced by VecParser#matmulKernel8x16.
    def enterMatmulKernel8x16(self, ctx:VecParser.MatmulKernel8x16Context):
        pass

    # Exit a parse tree produced by VecParser#matmulKernel8x16.
    def exitMatmulKernel8x16(self, ctx:VecParser.MatmulKernel8x16Context):
        pass


    # Enter a parse tree produced by VecParser#matmulKernel2x8.
    def enterMatmulKernel2x8(self, ctx:VecParser.MatmulKernel2x8Context):
        pass

    # Exit a parse tree produced by VecParser#matmulKernel2x8.
    def exitMatmulKernel2x8(self, ctx:VecParser.MatmulKernel2x8Context):
        pass


    # Enter a parse tree produced by VecParser#gotoKernel8x8.
    def enterGotoKernel8x8(self, ctx:VecParser.GotoKernel8x8Context):
        pass

    # Exit a parse tree produced by VecParser#gotoKernel8x8.
    def exitGotoKernel8x8(self, ctx:VecParser.GotoKernel8x8Context):
        pass


    # Enter a parse tree produced by VecParser#convKernel.
    def enterConvKernel(self, ctx:VecParser.ConvKernelContext):
        pass

    # Exit a parse tree produced by VecParser#convKernel.
    def exitConvKernel(self, ctx:VecParser.ConvKernelContext):
        pass


    # Enter a parse tree produced by VecParser#declarativeLoop.
    def enterDeclarativeLoop(self, ctx:VecParser.DeclarativeLoopContext):
        pass

    # Exit a parse tree produced by VecParser#declarativeLoop.
    def exitDeclarativeLoop(self, ctx:VecParser.DeclarativeLoopContext):
        pass


    # Enter a parse tree produced by VecParser#matmulKernel1D2x8.
    def enterMatmulKernel1D2x8(self, ctx:VecParser.MatmulKernel1D2x8Context):
        pass

    # Exit a parse tree produced by VecParser#matmulKernel1D2x8.
    def exitMatmulKernel1D2x8(self, ctx:VecParser.MatmulKernel1D2x8Context):
        pass


    # Enter a parse tree produced by VecParser#varExpr.
    def enterVarExpr(self, ctx:VecParser.VarExprContext):
        pass

    # Exit a parse tree produced by VecParser#varExpr.
    def exitVarExpr(self, ctx:VecParser.VarExprContext):
        pass


    # Enter a parse tree produced by VecParser#atomExpr.
    def enterAtomExpr(self, ctx:VecParser.AtomExprContext):
        pass

    # Exit a parse tree produced by VecParser#atomExpr.
    def exitAtomExpr(self, ctx:VecParser.AtomExprContext):
        pass


    # Enter a parse tree produced by VecParser#relationalExpr.
    def enterRelationalExpr(self, ctx:VecParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by VecParser#relationalExpr.
    def exitRelationalExpr(self, ctx:VecParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by VecParser#parenExpr.
    def enterParenExpr(self, ctx:VecParser.ParenExprContext):
        pass

    # Exit a parse tree produced by VecParser#parenExpr.
    def exitParenExpr(self, ctx:VecParser.ParenExprContext):
        pass


    # Enter a parse tree produced by VecParser#andExpr.
    def enterAndExpr(self, ctx:VecParser.AndExprContext):
        pass

    # Exit a parse tree produced by VecParser#andExpr.
    def exitAndExpr(self, ctx:VecParser.AndExprContext):
        pass


    # Enter a parse tree produced by VecParser#arrayVar.
    def enterArrayVar(self, ctx:VecParser.ArrayVarContext):
        pass

    # Exit a parse tree produced by VecParser#arrayVar.
    def exitArrayVar(self, ctx:VecParser.ArrayVarContext):
        pass


    # Enter a parse tree produced by VecParser#idVar.
    def enterIdVar(self, ctx:VecParser.IdVarContext):
        pass

    # Exit a parse tree produced by VecParser#idVar.
    def exitIdVar(self, ctx:VecParser.IdVarContext):
        pass


    # Enter a parse tree produced by VecParser#binop.
    def enterBinop(self, ctx:VecParser.BinopContext):
        pass

    # Exit a parse tree produced by VecParser#binop.
    def exitBinop(self, ctx:VecParser.BinopContext):
        pass


    # Enter a parse tree produced by VecParser#assignop.
    def enterAssignop(self, ctx:VecParser.AssignopContext):
        pass

    # Exit a parse tree produced by VecParser#assignop.
    def exitAssignop(self, ctx:VecParser.AssignopContext):
        pass


    # Enter a parse tree produced by VecParser#intAtom.
    def enterIntAtom(self, ctx:VecParser.IntAtomContext):
        pass

    # Exit a parse tree produced by VecParser#intAtom.
    def exitIntAtom(self, ctx:VecParser.IntAtomContext):
        pass



del VecParser