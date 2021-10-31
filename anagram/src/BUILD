load("@rules_python//python:defs.bzl", "py_binary")

package(default_visibility = ["//visibility:public"])

py_binary(
    name="anagram",
    srcs=glob(["*.py"]),
    deps=[
        "@libraries//utils:utils"
    ]
)
