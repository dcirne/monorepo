# Sets the scope of the library as publicly visible
# There are other options where it can be made private or
# limited visibility scope
package(default_visibility = ["//visibility:public"])

# Defines the library, its contents, and how it can be used by
# other targets
#
# Custom command line parameters were specified in `copts`
cc_library(
    name="hanoi_solver",
    srcs=[
        "hanoi_solver.hpp"
    ],
    copts=[
        "-Ilib",
        "--std=c++17"
    ]
)

