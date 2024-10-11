# 准备工作
如果需要在生成完evosuite的生成用例后使用脚本中的mvn test执行，请在项目的pom.xml中添加：
```

<dependency>
    <groupId>org.evosuite</groupId>
    <artifactId>evosuite-standalone-runtime</artifactId>
    <version>1.0.6</version> <!-- 确保版本与使用的 EvoSuite 工具版本一致 -->
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.junit.vintage</groupId>
    <artifactId>junit-vintage-engine</artifactId>
    <version>5.11.0</version>
    <scope>test</scope>
</dependency>

<plugin>
    <groupId>org.evosuite.plugins</groupId>
    <artifactId>evosuite-maven-plugin</artifactId>
    <version>1.0.6</version>
    <executions>
        <execution>
            <goals>
                <goal>generate</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```
如果只是需要evosuite生成测试用例，而不需要使用mvn test执行的话，上述过程可跳过。

# 实现功能
输入类名，方法名和文件路径，生成evosuite生成的测试用例并使用mvn test执行

# 使用方法
```
python script.py <class_name> <method_name> <project_path> <test_path>
```
参数解释:
1.<class_name>:类的全类名
2.<method_name>:方法名
3.<project_path>:项目的绝对路径
4.<test_path>:生成测试用例的存放路径
例如：
```
python script.py net.hydromatic.morel.compile.NameGenerator inc /home/final-test/morel /home/final-test/morel/src/test/java
python script.py org.jsoup.HttpStatusException HttpStatusException /home/final-test/jsoup /home/final-test/jsoup/test/java
python script.py org.apache.commons.cli.ParseException wrap /home/final-test/commons-cli /home/final-test/commons-cli/test/java
```

# 其他说明
jdk版本：jdk11。
目前datafaker仓库不支持(jdk17+)。
对于某些method，evosuite生成测试用例时会报错导致无法生成，比如binance中的很多方法；而且有时指定的方法并没有被生成在测试用例里，可能是它工具的问题。

