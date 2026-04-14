#本文件可以实现不同参数的生成，用户可以根据提示输入参数值，程序会调用接口生成文本并输出结果
from function import get_parameters, generate
#示例
if __name__ == "__main__":
    prompt = input("请输入 prompt：")
    params = get_parameters()
    response = generate(prompt, params)
    print(response)