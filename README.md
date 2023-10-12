# VecParser
Parser for Vec.g4 using ANTLR library

## Sample Parse Tree
Input: R[i][j] += A[i][k]*B[k][j]- (A[i][k]*B[k][j]>thres[j])*A[i][k]*B[k][j]*dis[j];<br>
Parse Tree: (parse (block (stmt (assignment (var R [ (expr (var i)) ] [ (expr (var j)) ])   (assignop +=)   (expr (expr (expr (var A [ (expr (var i)) ] [ (expr (var k)) ])) * (expr (var B [ (expr (var k)) ] [ (expr (var j)) ]))) -   (expr (expr (expr (expr ( (expr (expr (expr (var A [ (expr (var i)) ] [ (expr (var k)) ])) * (expr (var B [ (expr (var k)) ] [ (expr (var j)) ]))) > (expr (var thres [ (expr (var j)) ]))) )) * (expr (var A [ (expr (var i)) ] [ (expr (var k)) ]))) * (expr (var B [ (expr (var k)) ] [ (expr (var j)) ]))) * (expr (var dis [ (expr (var j)) ]))))) ;)) \<EOF\>)

## Installation

```bash
pip install -r requirements.txt
```

## Command to create parse trees

```bash
python Driver.py input.txt
```

## Steps to generate parser files
### Installation
```bash
pip install antlr4-tools
```
### Command
```bash
antlr4 -Dlanguage=Python3 Vec.g4 -o parse
```

### Reference
https://github.com/antlr/antlr4/blob/master/doc/python-target.md