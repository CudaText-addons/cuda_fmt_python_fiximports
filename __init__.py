from cudatext import ini_read
from cuda_fmt import get_config_filename, ed_filename
from .fiximports import FixImports

fmt = FixImports()

def do_fix_imports(text):

    fn = get_config_filename('Python Fix Imports')
    op_split = ini_read(fn, 'op', 'split_import_statements', '1')=='1'
    op_sort = ini_read(fn, 'op', 'sort_import_statements', '1')=='1'

    res, textout = fmt.sortImportGroups(
        ed_filename,
        text,
        splitImportStatements=op_split,
        sortImportStatements=op_sort)
    if res:
        if textout!=text:
            return textout
