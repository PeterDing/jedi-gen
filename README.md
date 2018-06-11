# deoplete-jedi Cache Generator

jedi-gen is a cache generator for deoplete-jedi.

deoplete-jedi will take long time to load information for some large packages, e.g. `numpy`, `tensorflow`.
At sometime, the procession can be fail, cause jedi has a timeout.

So, We can manually generate the information file for deoplete-jedi.

## Usage

### Install

First, we need to install jedi-gen at our python environment.
If you use `virtualenv`, you must be at the virtual environment.

```shell
git clone https://github.com/zchee/deoplete-jedi
cd deoplete-jedi
python setup.py install
```

### Use it

Now, we can generate the information file for any models we needed.

```shell
jedi-gen tensorflow > /path/to/tensorflow.json
```

Or, giving output path.

```shell
jedi-gen tensorflow -o /path/to/tensorflow.json
```

For macos, deoplete-jedi cache directory is `~/.cache/deoplete/jedi`.
Enjoying the completion server, after you move the cache file to the directory.

If you only need to generate a sub-model cache information file, you can do as following:

```shell
jedi-gen tensorflow.nn. -o /path/to/tensorflow.nn.json
```

**Warning**: there is `tensorflow.nn.`, not `tensorflow.nn`
