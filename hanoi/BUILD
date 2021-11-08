# Sets the scope of the library as publicly visible
# There are other options where it can be made private or
# limited visibility scope
package(default_visibility = ["//visibility:public"])

# Defines the binary, its contents, and how it uses other targets (dependencies)
# Note that the there are no external dependencies here. The only dependency refers 
# to a library in a nested directory. 
#
# Custom command line parameters were specified in `copts`
cc_binary(
    name="tower_of_hanoi",
    srcs=[
        "main.cpp"
    ],
    deps=[
        "//lib:hanoi_solver"
    ],
    copts=[
        "-Ilib",
		"--std=c++17"
    ]
)
