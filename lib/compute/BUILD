load("@rules_python//python:defs.bzl", "py_import", "py_test")
load("@compute_requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_library(
    name="compute",
    srcs=[
        "__init__.py",
        "operators.py"
    ],
    deps=[
        requirement("lazy-object-proxy")
    ]
)

py_test(
    name="operators_tests",
    srcs=[
        "operators.py",
        "operators_tests.py"
    ],
    deps=[
        requirement("lazy-object-proxy"),
        requirement("pytest")
    ]
)
