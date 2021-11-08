# Loads Python rules to specify build details
load("@rules_python//python:defs.bzl", "py_import")
load("@rules_python//python:defs.bzl", "py_test")

# Loads the command to install requirements listed in requirements.txt
load("@utils_requirements//:requirements.bzl", "requirement")

# Sets the scope of the library as publicly visible
# There are other options where it can be made private or
# limited visibility scope
package(default_visibility = ["//visibility:public"])

# Defines the library, its contents, and how it can be used by
# other targets
py_library(
    name="utils",
    srcs=[
        "__init__.py",
        "string_utils.py"
    ]
)

# Defines the unit tests and their dependencies
py_test(
    name="utils_test",
    srcs=[
        "utils_test.py"
    ],
    deps=[
        ":utils",
        requirement("pytest")
    ]
)
