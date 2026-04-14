from function import save_results, run_experiments
#本文件是实验的主入口，负责加载实验配置，运行实验，并保存结果,实验参数保存在data/exp.json中，结果保存到data/results.json中
if __name__ == "__main__":    
    results = run_experiments(filepath=r"data\exp.json")
    save_results(results, "data/results.json")

    print("实验完成")
