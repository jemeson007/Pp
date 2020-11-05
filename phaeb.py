import ast
import js
import jiphy
# import astring
import execjs

def phaeb(nyyt):
  p , j = 0, 3

  while( p < nyyt):
    print(p, end=' ')
    p, j = j, p + j

  pd = ast.NodeTransformer().visit(ast.parse('photon.py'))
  print(ast.NodeTransformer().visit(ast.parse('photon.py')))
  
  # node = execjs.get(execjs.runtime_names.Node)
  # node.eval('import {generate} from "astring"')
  # p = astring.generate(pd)
  # p = node.astring.generate(pd)
  # # node.eval('astring.generate(pd)')

  print(jiphy.to.javascript('print(3*12)')
  )

phaeb(33)