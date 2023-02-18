# Protein distribution

## Intro

Proteins are large biological molecules consisting of amino acids. In general, the genetic code specifies 20 standard amino acids. This assignment is based on the systematic exploration of the distribution of certain amino acids in proteins’ structures.

3-letter codes of the 20 standard amino acids:

`ALA ARG ASN ASP CYS GLU GLN GLY HIS ILE LEU LYS MET PHE PRO SER THR TRP TYR VAL`

## Your task

Implement a program invoked like:

`program_name configuration_file output_file`

Command line always contains configuration file name and it can contain output file name. If the output file name is not listed, standard output should be used.

Both the configuration file and the data files are row-oriented.
Data file structure

One file describes one protein and contains information about all its amino acids and their spatial coordinates (x, y, z – discrete values). Each row begins with the 3-letter amino acid code and continues with the spatial coordinates for that amino acid.

Keep in mind: coordinates can also be negative numbers, space between strings on one line can be one or more whitespaces.

**Note**: This is a simplification of a real PDB file describing protein structures.

### Configuration file structure

```text
R-neighborhood .. is an integer
Pattern ......... is a sequence of one or more amino acids separated by one or more whitespaces
protein_1 ....... is the name of the first data file
...
protein_N ....... is the name of the N-th data file
```

## Histogram

The R-neighborhood represents the neighborhood of a certain amino acid at a distance less than or equal to R. The R-neighborhood of an amino acid with coordinates `[x,y,z]` is defined as points with all coordinates in the range `[x-R..x+R, y-R..y+R , z-R..z+R]`.

A histogram is constructed for each point in discrete 3D space in which an amino acid from the set of specified proteins is located. For each point, we calculate the number of amino acid types - specified in pattern - in its R-neighborhood. Let these numbers be (in order according to the specified pattern) `[c1..cn]`. Then the record corresponding to the values `[c1..cn]` is incremented. The resulting histogram is created by gradually incrementing the records according to the R-neighborhood of all points corresponding to the amino acids of all input proteins.

## Output

The output format is *row-oriented*, one line is in the form and sorted lexicographically, i.e:

```text
[0 0 0 1]: xxx
[0 0 0 2]: xxx
...
[0 0 1 0]: xxx
[0 0 1 2]: xxx
...
[0 0 2 1]: xxx
```

Only non-zero occurrences are included in the output.
Example

Configuration file:

```text
6000
ARG LYS
simple.pdb
```

Data file (simple.pdb):

```text
ARG 14872 -18107 30327
LYS 16112 -17325 26790
HIS 17615 -20594 25563
ILE 18797 -24042 26472
ARG 21860 -24523 24296
ARG 24156 -21734 23132
GLY 27393 -22378 21345
HIS 29225 -19697 19391
ALA 32741 -18808 18304
```

Output:

```text
[1 0]: 1
[1 1]: 2
[2 0]: 3
[2 1]: 1
[3 0]: 1
```

One of the data files used in tests: `data.pdb`

## Assumptions and efficiency requirements

The discrete 3D space where all the amino acids are located is large, think on the order of 100000^3. It is therefore not possible to store in memory a map with data for every point in this space.

Space filling with amino acids is very sparse. Assume tens to small hundreds of amino acids (occupied points in space). Therefore, choose a suitable data representation so that the necessary operations are as efficient as possible.

It is certainly not efficient to search every point of the entire space for each amino acid, nor to go through all other amino acids entered.

You may find it useful to observe that for each amino acid in each dimension there are sufficiently few other amino acids in the range of R-neighborhoods (i.e., in the subspace [x-R..x+R, *, *]) that one can already search sequentially.
Configuration and data file syntax checking requirements

The primary evaluation criterion is functional correctness and efficiency on correctly entered data. The program must be stable (i.e. not perform any undefined operations, have unhandled exceptions, exit uncontrollably, etc.) on any (i.e. arbitrarily corrupted) data.

In order to achieve the full number of points, a check of the syntax of the configuration and data files is necessary, if it is violated, the program writes (to the output file or to the standard output, according to the parameters of the command line) the string "error" and ends (with a return code of 0). Consider a syntax violation other than a valid 3-letter amino acid code, a different number of coordinates, non-numeric characters at coordinate positions, etc.

If any data file specified in the configuration file cannot be opened (e.g. because it does not exist), it is not considered an error, simply skip the file. Being not able to open configuration file is an error.
