import datajoint as dj
virus = dj.create_virtual_module('virus','common_virus')
mice = dj.create_virtual_module('mice','common_mice')
reso = dj.create_virtual_module('reso','pipeline_reso')
