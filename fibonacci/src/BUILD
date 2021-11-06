load("@io_bazel_rules_scala//scala:scala.bzl", "scala_binary")

package(default_visibility = ["//visibility:public"])

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
