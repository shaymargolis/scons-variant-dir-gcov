# Coverage Merging for SCons VariantDir

This repository provides a technique to merge coverage files generated from SCons builds that use `variantDir`. By using this method, you can combine multiple coverage reports into a single unified file. This allows for easier tracking and analysis of test coverage in projects that build with SCons, where each variant directory might generate its own separate coverage file.

## Why Use This?

When building a project with SCons, especially when using `variantDir` for different build configurations, coverage files may be generated in different locations. This can lead to multiple coverage files being created for a single set of tests, making it difficult to get an overall view of your code's coverage.

By using this technique, you can merge those separate coverage files into a single file, allowing you to view the complete coverage for your project.

## How to Use This Technique

### 1. Compile Your Project
To begin, compile your project using SCons.

```bash
scons
```

### 2. Run Your Tests

Once compiled, run the tests for your project. If you have multiple test binaries across different variants, you can run them sequentially.

```bash
./build/a/test && ./build/b/test && ./build/c/test
```

### 3. Generate Coverage Report

After running the tests, generate the initial coverage reports. You can use gcovr to generate a JSON file of the coverage data.

```bash
gcovr --json --exclude-unreachable-branches --print-summary -o coverage.json
```

### 4. Merge Coverage Files

If you have coverage files from multiple variantDir builds, you can merge them into one file using the provided Python script fix_variant_dir.py.

```bash
python fix_variant_dir.py coverage.json coverage.out.json
```

This will create a single merged coverage file (coverage.out.json), which contains the combined coverage data from all the variants.

### 5. Generate HTML Report

Finally, you can generate an HTML report of your merged coverage data using gcovr.

```bash
gcovr --add-tracefile coverage.out.json --html-details --exclude-unreachable-branches --print-summary -o coverage.html
```

Now you have a single HTML report that represents the coverage for all your variants, making it easier to analyze the overall coverage of your project.
