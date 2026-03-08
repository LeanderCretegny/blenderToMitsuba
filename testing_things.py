import mitsuba as mi
mi.set_variant('cuda_ad_rgb')

import mitsuba.parser as p
# load with parser
parser_res = p.parse_file(p.ParserConfig('cuda_ad_rgb'), filename='simple_xml.xml')
for n in parser_res.nodes:
    print(f'node {n}')
    print(f' node file index: {n.file_index}')
    print(f' node properties: {n.props}')
    print(f' node type: {n.type}')