# Loads Python rules to specify build details
load("@rules_python//python:defs.bzl", "py_binary")

# Loads the command to install requirements listed in requirements.txt
load("@anagram_requirements//:requirements.bzl", "requirement")

# Sets the scope of the library as publicly visible
# There are other options where it can be made private or
# limited visibility scope
package(default_visibility = ["//visibility:public"])

# Defines the binary, its contents, and how it uses other targets (dependencies)
# Note that the external dependency uses the `@library` label defined in the
# `WORKSPACE` file. This is necessary because the project uses an external dependency.
# It also installs the required package `termcolor` that in requirements.txt.
#
# Rather than specifying the source code files one-by-one, `glob` was used with a 
# predicate to include all matching files.
py_binary(
    name="anagram",
    srcs=glob(["*.py"]),
    deps=[
        "@library//utils:utils",
        requirement("termcolor")
    ]
)
