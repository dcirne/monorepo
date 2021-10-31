load("@rules_python//python:defs.bzl", "py_binary")
load("@calculator_requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_binary(
    name="calculator",
    srcs=["calculator.py"],
    deps=[
        "@library//compute:compute",
        requirement("termcolor")
    ]
)

