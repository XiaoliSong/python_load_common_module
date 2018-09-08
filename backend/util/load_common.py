'''
当前文件所在路径./backend/util/load_common.py
或者./cms/util/load_common.py
'''

import sys
import os

# 公共项目的绝对路径
COMMON_PROJECT_PATH = os.path.join(os.path.dirname(__file__), '../../common')

# 公共模块的依赖模块，如果依赖的包没有在公共模块的包出现，可以不添加
dependent_modules = ['const.app']

# 公共模块，应该具体到文件模块，而不是包，如需要引入const.redis不能填util
common_modules = [
    'const.redis',
    'const.db',
]


def delete_package(module_name):
    '''删除模块以上的包
    如module_name=util.const.redis，则从sys.modules删除util.const,util
    '''
    parent_packages = module_name.split('.')[0:-1]
    while len(parent_packages) > 0:
        parent_package = '.'.join(parent_packages)
        if parent_package in sys.modules:
            del sys.modules[parent_package]
            parent_packages = parent_packages[0:-1]
        else:
            break


def load_module(module_name):
    '''引入模块
    '''
    import_str = '__import__("' + module_name + '")'
    eval(import_str)


# 先加载公共模块的依赖模块
for dependent_module in dependent_modules:
    load_module(dependent_module)

# 删除已经加载的公共模块及其上面的包
for common_module in common_modules:
    if common_module in sys.modules:
        del common_module
    delete_package(common_module)

# 设置优先检索公共项目COMMON_PROJECT_PATH
sys.path.insert(0, COMMON_PROJECT_PATH)

# 导入公共模块common_modules
for common_module in common_modules:
    load_module(common_module)

# 恢复优先检索当前文件夹
sys.path.pop(0)

# 删除公共模块上面的包
for common_module in common_modules:
    delete_package(common_module)

# 重新加载当前模块所在包，避免报错
if 'util' in sys.modules:
    del sys.modules['util']
    import util
else:
    import util
