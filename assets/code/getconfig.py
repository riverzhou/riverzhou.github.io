#!/usr/bin/env python3ss

import json

url = 'themes=prism-okaidia&languages=markup+css+clike+javascript+arduino+bash+basic+c+csharp+cpp+diff+django+excel-formula+fortran+git+go+http+ini+java+json+kotlin+latex+liquid+llvm+lua+makefile+markdown+markup-templating+matlab+mongodb+nasm+nginx+objectivec+pascal+perl+php+plsql+properties+python+rest+ruby+scss+sql+swift+typescript+verilog+vhdl+vim+visual-basic+wasm+wiki+xml-doc+yaml&plugins=line-numbers+show-language+toolbar'

desc = {} 
for stage in url.split('&'):
    item, package = stage.split('=')
    desc[item] = []
    for feature in package.split('+'):
        desc[item].append(feature)

filename = 'config.json'
with open(filename,'w',encoding='utf-8') as f:
    f.write(json.dumps(desc,indent=4))
