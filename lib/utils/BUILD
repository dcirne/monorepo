load("@rules_python//python:defs.bzl", "py_import")
load("@rules_python//python:defs.bzl", "py_test")
load("@compute_requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_library(
    name="utils",
    srcs=[
        "__init__.py",
        "string_utils.py"
    ]
)

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
