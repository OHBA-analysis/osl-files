# OHBA Software Library (OSL) Files

Data files used by the OHBA Software Library (OSL): brain parcellations, MNI152
templates and masks, cortical surfaces, MEG scanner layouts and Workbench
scenes.

## Layout

| Directory | Contents |
| --- | --- |
| `parcellation/` | Volumetric brain parcellations (AAL, Desikan-Killiany, Giles, Glasser, Schaefer). Labels, MNI coordinates and pictures for each one are in [docs/parcellations](docs/parcellations). |
| `mask/` | MNI152 brain masks at several resolutions |
| `surface/32k_fs_LR/` | Cortical surface meshes for plotting |
| `surface/mni152/` | Pre-extracted MNI152 skull and scalp surfaces, for use with RHINO when no subject MRI is available |
| `scanner/` | MEG scanner layouts and channel names (CTF-275, Neuromag-306) |
| `scene/` | HCP Workbench scene files |

## Where they are cached

| Platform | Location |
| --- | --- |
| macOS | `~/Library/Caches/osl-files/` |
| Linux and WSL | `$XDG_CACHE_HOME/osl-files/`, falling back to `~/.cache/osl-files/` |
| Windows | `%LOCALAPPDATA%\osl-files\Cache\` |

Set the `OSL_DATA` environment variable to cache them somewhere else, for
example on a cluster where your home directory has a quota, or to point a whole
group at one read-only copy.

Each download is checked against a checksum, so a file is only fetched once and
a truncated or corrupted one is caught rather than passed on to the analysis.

To fetch everything up front, for a machine that will later be offline, run the
download command of whichever package you use somewhere with network access and
copy the cache across.

## Packages that use these files

| Package | Download command |
| --- | --- |
| [osl-dynamics](https://github.com/OHBA-analysis/osl-dynamics) | `osl-dynamics-download-data` |

## Adding or changing files

Add, change or remove the file here and open a pull request. That is the whole
procedure: `registry.txt` lists every data file with its SHA-256 checksum, and
is regenerated automatically on every push to `main` by
[the Registry workflow](.github/workflows/registry.yml). The packages download
that registry at runtime, so a change here reaches users on their next run
without any package needing to be released.

The checksum is also what refreshes a cache. Change a file's contents and its
checksum changes, so anyone holding the old copy downloads the new one; leave
it alone and nobody re-downloads anything.

Renaming or moving a file is the one thing to be careful with, since already
released packages ask for files by path. Prefer adding a new file under a new
name, and remove the old one only once no supported release still fetches it.
