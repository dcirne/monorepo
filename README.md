# Monorepo Reference Implementation

This is a reference implementation of a monorepo using an open-source high-level building language and tool, [Bazel](https://bazel.build), to manage and support efficient builds, runs, tests, artifact generation, multiple programming languages, and more. Bazel is multi-platform, multi-language, reliable, scalable, and extensible. It was originally created by Google it is used to manage their own monorepo.

The two key configuration files are `WORKSPACE` and `BUILD`. Each project has their own `WORKSPACE` file that specifies the characteristics and dependencies of that project, plus one or more `BUILD` files that can be located within that project (directory hierarchy), a separate project in a different directory, another repository, or in the internet (third-party, outside dependency).

It is important to understand the fundamental concepts in Bazel: Workspaces, Packages, Targets, and Labels. You can read more in the lexicon of [Concepts and Terminology](https://docs.bazel.build/versions/4.2.1/build-ref.html). When reading or writing the configuration files we want to pay special attention to the definitions of binaries and libraries.

A binary specifies the project you want to build, including dependencies and other parameters. A library specifies a framework or a package to be used by a binary. A binary may have zero, one, or many libraries.


## Python Projects

There are two Python projects in this monorepo: `anagram` and `calculator`. They are independent from each other, and they both depend on another project `lib`, which provides reusable packages (libraries) for them.

With Bazel it is possible to specify the dependencies and generate builds that only include the necessary files and assets. For example, the `calculator` project includes the `compute` library and also a third-party dependencies. The `calculator` project depends directly only on the `termcolor` package. The `compute` library depends on `lazy-object-proxy` and `pytest`. With Bazel we can specify all that in a very elegant way. Each binary or library only needs to specify what they depend on, in this case `calculator` is not aware of the dependencies `compute` has. They are self contained.


## Bazel in Action

You can choose to install Bazel on your computer, but if you want to jump straight into the action, there is a convenient Docker image that will get you there faster.

Go to the root directory of the monorepo and build the Docker image with:

```bash
docker build --rm . -t monorepo:<x.y.z>
```

Where `<x.y.z>` is a the semantic version of the image, like `0.0.1`. Feel free to use other versioning scheme or label. This image will be build on your machine only. There will be no impact on others. On my machine I build using the following command:

```bash
docker build --rm . -t monorepo:1.0.0
```

Once the image is build, run the image to access the shell, and mount the root of the monorepo to the image's `/workspace` directory:

```bash
docker run --rm -it -v $(pwd):/workspace monorepo:<x.y.z> /bin/bash
```

Again, `<x.y.z>` is the same label you used to build the image. In my case:

```bash
docker run --rm -it -v $(pwd):/workspace monorepo:1.0.0 /bin/bash
```


## Building and Running the First Project

Now that you have running container with Bazel, let's build and run the first project: _anagram_. In the Docker shell, switch to the `anagram` directory:

```bash
cd /workspace/anagram
```

Build the Bazel project:

```bash
bazel build //src:anagram
```

Understanding what is going on with the command above, we break it down into the following parts:

- `build` -> Command to build the project
- `//` -> The directory in which the `WORKSPACE` file is located (project root)
- `src` -> Relative path from the root directory
- `:` -> Separator between the relative path and the target name
- `anagram` - Target to be built (specified in the BUILD file)

After the build is complete you will see a few new directories:

- `bazel-anagram`
- `bazel-bin`
- `bazel-out`
- `bazel-testlogs`

Those are symbolic links to temporary directories. Anything beginning with `bazel-` is ignored by `git` and the directories themselves can be cleaned with `bazel clean`.

Now it is time to run the project:

```bash
bazel run //src:anagram
```

Alternatively, you can run the project with (it is self-contained):

```bash
./bazel-bin/src/anagram
```


## The Second Project

Straight to the point. Switch to the `calculator` directory, build, and run:

```bash
cd /workspace/calculator
bazel build //src:calculator
bazel run //src:calculator
```


## Testing

The _anagram_ and _calculator_ projects are bare-bones and lack unit tests. Instead, we will run tests on the libraries those projects depend on. Switch to the `lib` directory:

```bash
cd /workspace/lib
```

And run the tests for the `compute` library:

```bash
bazel test //compute:operators_test
```


## Dependency Graph

It would be nice to visualize a graph with all the dependencies of our projects. And with Bazel we can do just that using the `query` command.

We can see the dependencies in text format:

```bash
bazel query --notool_deps --noimplicit_deps "deps(//src:calculator)"
```

Or we can see if a nice graphical format.

```bash
bazel query --notool_deps --noimplicit_deps "deps(//src:calculator)" --output graph
```

If you do not have `graphviz` installed on your computer, copy the output of the command above and paste it to [Sketchviz](https://sketchviz.com/new) to see the result. It is a pretty picture.


## Additional Reading

- [Bazel](https://bazel.build)
- [Bazel - Working with External Dependencies](https://docs.bazel.build/versions/main/external.html)
- [Bazel Rules - Python](https://github.com/bazelbuild/rules_python)
- [Bazel - Command-Line Reference](https://docs.bazel.build/versions/main/command-line-reference.html)
- [Python Rules](https://docs.bazel.build/versions/main/be/python.html)
- [A User's Guide to Bazel](https://docs.bazel.build/versions/main/guide.html)
- [How We Used Bazel to Streamline Our AI Development](https://www.spotdraft.com//engineering-blog/how-we-used-bazel-to-streamline-our-ai-development?utm_source=pocket_mylist)
- [You too can love the MonoRepo](https://medium.com/@Jakeherringbone/you-too-can-love-the-monorepo-d95d1d6fcebe)
- [What is Bazel – Tutorial, Examples, and Advantages](https://semaphoreci.com/blog/bazel-build-tutorial-examples?utm_source=pocket_mylist)
