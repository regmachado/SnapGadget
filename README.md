# About

Tools to read, write and manipulate Gadget-2 snapshots, using the [UNSIO](https://projets.lam.fr/projects/unsio/wiki/PythonReadDataNew) python wrapper.

# Requirements

* pip3 install python-unsio
* pip3 install python-unsiotools

# Usage

- Print information about a snapshot

```
python3 snapinfo.py input
```

- Copy a snapshot

```
python3 snapcopy.py input output
```

- Rotate a snapshot

```
python3 snaprotate.py input output 0 0 0
```

- Join two snapshots

```
python3 snapjoin.py inputA inputB output 0 0 0  0 0 0
```

- Shift snapshot to COM

```
python3 snapcom.py input output all
```

- Shift snapshot to COD

```
python3 snapcod.py input output all
```

- Empty example

```
python3 snapmanip.py input output
```


# Comments

These programs expect snapshots in the Gadget-2 format, i.e. including some combination of the particle types: gas, halo, disk, bulge, stars. Typically useful for non-cosmological simulations of isolated galaxies or clusters. The UNSIO library itself is not written in python, so it is quite fast at loading large files.
