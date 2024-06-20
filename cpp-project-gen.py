import os

def create_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)

def create_cpp_project_structure(project_name):
    # Define the folder structure
    folders = [
        f"{project_name}/include/{project_name}",
        f"{project_name}/src",
        f"{project_name}/tests",
        f"{project_name}/third_party",
        f"{project_name}/build",
        f"{project_name}/docs"
    ]

    # Create the folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Define the content for CMakeLists.txt
    cmake_content = f"""cmake_minimum_required(VERSION 3.10)
project({project_name} VERSION 1.0)

# Specify C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add include directory
include_directories(include)

# Add executable
add_executable({project_name} src/main.cpp src/example.cpp)

# Add library (if you have one)
add_library(example src/example.cpp)
target_include_directories(example PUBLIC include)

# Link library to executable
target_link_libraries({project_name} example)

# Add tests
enable_testing()
add_subdirectory(tests)
"""

    # Define the content for tests/CMakeLists.txt
    tests_cmake_content = """add_executable(runTests test_example.cpp)
target_link_libraries(runTests gtest gtest_main)
add_test(NAME ExampleTest COMMAND runTests)
"""

    # Define the content for main.cpp
    main_cpp_content = """#include <iostream>
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
"""

    # Define the content for example.h
    example_h_content = f"""#ifndef {project_name.upper()}_EXAMPLE_H
#define {project_name.upper()}_EXAMPLE_H

void exampleFunction();

#endif // {project_name.upper()}_EXAMPLE_H
"""

    # Define the content for example.cpp
    example_cpp_content = f"""#include "{project_name}/example.h"
#include <iostream>

void exampleFunction() {{
    std::cout << "This is an example function." << std::endl;
}}
"""

    # Define the content for test_example.cpp
    test_example_content = """#include <gtest/gtest.h>

TEST(ExampleTest, BasicAssertions) {
    // Expect two strings to be equal.
    EXPECT_EQ("hello", "hello");
    // Expect equality.
    EXPECT_EQ(7 * 6, 42);
}
"""

    # Define the content for README.md
    readme_content = f"""# {project_name}
This is the {project_name} project.
"""

    # Create files with the defined content
    create_file(f"{project_name}/CMakeLists.txt", cmake_content)
    create_file(f"{project_name}/tests/CMakeLists.txt", tests_cmake_content)
    create_file(f"{project_name}/src/main.cpp", main_cpp_content)
    create_file(f"{project_name}/include/{project_name}/example.h", example_h_content)
    create_file(f"{project_name}/src/example.cpp", example_cpp_content)
    create_file(f"{project_name}/tests/test_example.cpp", test_example_content)
    create_file(f"{project_name}/README.md", readme_content)

    print(f"C++ project '{project_name}' structure generated successfully.")

# Prompt the user for a project name
project_name = input("Enter the project name: ")
create_cpp_project_structure(project_name)
