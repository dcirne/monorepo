# Loads Python rules to specify build details
load("@rules_python//python:defs.bzl", "py_binary")

# Loads the command to install requirements listed in requirements.txt
load("@calculator_requirements//:requirements.bzl", "requirement")

# Sets the scope of the library as publicly visible
# There are other options where it can be made private or
# limited visibility scope
package(default_visibility = ["//visibility:public"])

# Defines the binary, its contents, and how it uses other targets (dependencies)
# Note that the external dependency uses the `@library` label defined in the
# `WORKSPACE` file. This is necessary because the project uses an external dependency.
# It also installs the required package `termcolor` that in requirements.txt.
py_binary(
    name="calculator",
    srcs=["calc.py"],
    main="calc.py",
    deps=[
        "@library//compute:compute",
        requirement("termcolor")
    ]
)

