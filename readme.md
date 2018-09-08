# Python不同项目加载公共模块

## 解决的问题

主要解决：Python中多个项目依赖公共项目的模块，引入公共模块的麻烦。

## 示例
backend和cms依赖于公共项目common，需要对backend和cms的util.load_common进行修改
* COMMON_PROJECT_PATH - 公共项目的绝对路径
* dependent_modules - 公共模块的依赖模块
* common_modules - 公共模块

然后backend和cms就可以像引入本项目的模块一样引入公共模块的项目了（使用 from package import module而不是import package.module）

