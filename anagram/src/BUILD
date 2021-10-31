load("@rules_python//python:defs.bzl", "py_binary")
load("@anagram_requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_binary(
    name="anagram",
    srcs=glob(["*.py"]),
    deps=[
        "@library//utils:utils",
        requirement("termcolor")
    ]
)
