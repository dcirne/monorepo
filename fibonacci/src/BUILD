# Loads Python rules to specify build details
load("@io_bazel_rules_scala//scala:scala.bzl", "scala_binary")

# Sets the scope of the library as publicly visible
# There are other options where it can be made private or
# limited visibility scope
package(default_visibility = ["//visibility:public"])

# Defines the binary, its contents, and how it uses other targets (dependencies)
# Note that the external dependency uses the `@library` label defined in the
# `WORKSPACE` file. This is necessary because the project uses an external dependency.
#
# In Scala, it is necessary to specify the class that implements the `main` method
# to use as an entry point (`main_class`).
scala_binary(
    name="fibonacci",
    srcs=[
        "fibonacci.scala"
    ],
    main_class="Fibonacci",
    deps=[
        "@library//fibonator:fibonator"
    ]
)
