# API_Automated_Testing
This is the simple framework for API testing and easy for test engineers..
采用的是python自带的unittest框架，简单易懂，采用json格式的文件执行数据驱动，更适合测试工程师测试使用。

## 结构
- common  存放通用方法
- report  存放测试结果
- test_case 存放测试用例
- test_data 存放测试数据
- RunTestCase 运行需要运行的命令

### 细节描述
1. request方法封装在method里
2. 使用HTTPRunner生成的report，方法在Common里
3. header及其相关参数封装在common_func里
4. 测试用例放在Test_case里，根据api分类，提示unittest的执行是以test/Test开头，数字，大写字母，小写字符的顺序执行，切记命名顺序
5. 测试数据放在Test_data里，每个用例使用一个json文件，主要存放的是api的body数据，便于修改和前期的测试
6. 需要执行的case，放在Run_test_case里，执行完成后生成报告
