# Loads Python rules to specify build details
load("@rules_python//python:defs.bzl", "py_import")
load("@rules_python//python:defs.bzl", "py_test")

# Loads the command to install requirements listed in requirements.txt
load("@compute_requirements//:requirements.bzl", "requirement")

# Sets the scope of the library as publicly visible
# There are other options where it can be made private or
# limited visibility scope
package(default_visibility = ["//visibility:public"])

# Defines the library, its contents, and how it can be used by
# other targets
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

# Defines the unit tests and their dependencies
py_test(
    name="operators_test",
    srcs=[
        "operators_test.py"
    ],
	main="operators_test.py",
    deps=[
        ":compute",
        requirement("pytest")
    ]
)
