# Loads Scala rules to specify build details
load("@io_bazel_rules_scala//scala:scala.bzl", "scala_library", "scala_test")

# Sets the scope of the library as publicly visible
# There are other options where it can be made private or
# limited visibility scope
package(default_visibility = ["//visibility:public"])

# Defines the library, its contents, and how it can be used by
# other targets
scala_library(
    name="fibonator",
    srcs=[
        "src/monorepo/fibonator/fibonator.scala"
    ]
)

# Defines the unit tests and their dependencies
scala_test(
    name="fibonator_test",
    srcs=[
        "src/test/monorepo/fibonator/fibonator_test.scala"
    ],
    deps=[
        ":fibonator"
    ]
)
