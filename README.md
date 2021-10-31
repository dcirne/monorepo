# Monorepo Reference Implementation

## Build and Run the Docker Image

```bash
docker build --rm . -t monorepo:<x.y.z>
```

```bash
docker run --rm -it -v $(pwd):/workspace monorepo:<x.y.z> /bin/bash
```


## Build and Run the Projects

```bash
cd anagram

bazel build //src:anagram
```


## Dependency Graph

```bash
bazel query --notool_deps --noimplicit_deps "deps(//src:anagram)" --output graph
```


## Additional Reading

- [Bazel](https://bazel.build)
- [Bazel - Working with External Dependencies](https://docs.bazel.build/versions/main/external.html)
- [Bazel Rules - Python](https://github.com/bazelbuild/rules_python)
- [How We Used Bazel to Streamline Our AI Development](https://www.spotdraft.com//engineering-blog/how-we-used-bazel-to-streamline-our-ai-development?utm_source=pocket_mylist)
- [You too can love the MonoRepo](https://medium.com/@Jakeherringbone/you-too-can-love-the-monorepo-d95d1d6fcebe)
- [What is Bazel – Tutorial, Examples, and Advantages](https://semaphoreci.com/blog/bazel-build-tutorial-examples?utm_source=pocket_mylist)
