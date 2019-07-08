import os
from cudatext import ed, ini_read
from cuda_fmt import get_config_filename
from .fiximports import FixImports

def do_fix_imports(text):

    fn = get_config_filename('Python Fix Imports')
    section = 'op'
    op_split = ini_read(fn, section, 'split_import_statements', '1')=='1'
    op_sort = ini_read(fn, section, 'sort_import_statements', '1')=='1'
    
    res, textout = FixImports().sortImportGroups(
        ed.get_filename(), 
        text,
        splitImportStatements=op_split,
        sortImportStatements=op_sort)      
    if res:
        if textout!=text:
            return textout
