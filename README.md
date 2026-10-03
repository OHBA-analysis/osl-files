# OHBA Software Library (OSL) Files

Data files used by the OHBA Software Library (OSL): brain parcellations, MNI152
templates and masks, cortical surfaces, MEG scanner layouts and Workbench
scenes.

## Layout

| Directory | Contents |
| --- | --- |
| `parcellation/` | Volumetric brain parcellations (AAL, Desikan-Killiany, Giles, Schaefer). Labels, MNI coordinates and pictures for each one are in [docs/parcellations](docs/parcellations). |
| `mask/` | MNI152 brain masks at several resolutions, and cortical surface meshes for plotting |
| `mni152_surfaces/` | Pre-extracted MNI152 skull and scalp surfaces, for use with RHINO when no subject MRI is available |
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

| Package | Checksum registry | Download command |
| --- | --- | --- |
| [osl-dynamics](https://github.com/OHBA-analysis/osl-dynamics) | `osl_dynamics/files/registry.txt` | `osl-dynamics-download-data` |

## Adding or changing files

Files are fetched from `main` and checked against a checksum recorded in the
package that fetches them, so a file's path *and* its contents are both part of
the interface:

1. Add or change the file here and open a pull request.
2. Regenerate the checksum registry in each package that fetches it (see the
   table above) and release that package.

Editing a file in place, renaming it or moving it breaks every already-released
version of the packages that fetch it, because the checksum they recorded no
longer matches. Prefer adding a new file under a new name, and remove the old
one only once no supported release still fetches it.
