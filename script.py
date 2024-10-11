import os
import subprocess
import sys

def run_command(command):
    """执行shell命令并输出结果到控制台"""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode())
    if stderr:
        print(stderr.decode())

def generate_tests(class_name, method_name, project_path,test_path):
    # 保存当前脚本所在目录
    original_dir = os.getcwd()

    # 步骤1: 在项目路径下执行 Maven 命令获取依赖类路径
    # os.chdir(project_path)
    # print(f"进入项目目录: {project_path}")
    # mvn_command = "mvn dependency:build-classpath -DincludeScope=test -q -Dmdep.outputFile=classpath.txt"
    # print(f"执行命令: {mvn_command}")
    # run_command(mvn_command)
    
    # 步骤2: 读取 classpath.txt 中的依赖并保存到 dependency 变量
    # with open("classpath.txt", "r") as f:
    #     dependency = f.read().strip()
    
    # print(f"获取到的依赖: {dependency}")

    # 步骤3: 回到当前脚本所在目录，然后生成EvoSuite测试用例
    os.chdir(original_dir)
    print(f"切换回脚本所在目录: {original_dir}")
    evosuite_command = (
        f"java --add-opens java.base/java.util=ALL-UNNAMED "
        f"-jar ./evosuite-1.2.0.jar "
        f"-class {class_name} "
        f"-Dtarget_method={method_name} "
        f"-projectCP {project_path}/target/classes "
        f"-Dtest_dir={test_path} "
        f"-Dalgorithm=STANDARD_GA -generateSuite"
    )
    
    print(f"执行EvoSuite命令生成测试用例: {evosuite_command}")
    run_command(evosuite_command)

    # 步骤4: 在项目路径下，执行mvn test
    os.chdir(project_path)
    test_name = class_name.split(".")[-1]
    mvn_test_command = f"mvn test -Dcheckstyle.skip=true -Dtest={test_name}_ESTest* -Drat.skip=true"
    print(f"执行测试: {mvn_test_command}")
    run_command(mvn_test_command)

if __name__ == "__main__":    
    if len(sys.argv) != 5:
        print("使用方法: python script.py <类名> <方法名> <项目路径> <测试路径>")
        sys.exit(1)

    class_name = sys.argv[1]
    method_name = sys.argv[2]
    project_path = sys.argv[3]
    test_path = sys.argv[4]

    generate_tests(class_name, method_name, project_path, test_path)