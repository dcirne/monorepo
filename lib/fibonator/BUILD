load("@io_bazel_rules_scala//scala:scala.bzl", "scala_library", "scala_test")

package(default_visibility = ["//visibility:public"])

scala_library(
    name="fibonator",
    srcs=[
        "src/monorepo/fibonator/fibonator.scala"
    ]
)

scala_test(
    name="fibonator_test",
    srcs=[
        "src/test/monorepo/fibonator/fibonator_test.scala"
    ],
    deps=[
        ":fibonator"
    ]
)
