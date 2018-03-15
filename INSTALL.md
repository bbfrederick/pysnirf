Prerequisites
-------------

The processing programs in capcalc require the following to be installed first:

* Python 2.x or 3.x
* numpy
* h5py

Installation
------------

Once you have installed the prerequisites, cd into the package directory, and type the following:
```bash
python setup.py install
```
to install all of the tools in the package.  You should be able to run them from the command line
then (after rehashing).

Updating
--------

If you've previously installed pysnirf and want to update, cd into the package directory and do a git pull first:
```bash
git pull
python setup.py install
```


Usage
------------

Execute any of the commands to run capcalc on the sample data:

```bash
# run rapidtide2 to perform dynamic global signal regression (dGSR) on an fMRI file[1]:
snirftest

```

References
----------
1) Erdoğan S, Tong Y, Hocke L, Lindsey K, Frederick B (2016). Correcting
	resting state fMRI-BOLD signals for blood arrival time enhances
	functional connectivity analysis. Front. Hum. Neurosci., 28 June 2016
	| http://dx.doi.org/10.3389/fnhum.2016.00311
