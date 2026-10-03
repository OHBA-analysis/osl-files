# Parcellations

The parcellation files themselves are in [`parcellation/`](../../parcellation).
They are downloaded on demand by the OSL packages, so you do not need to fetch
them by hand.

## Available Parcellations

### Desikan-Killiany parcellations

- [atlas-DK_nparc-68_space-MNI_res-8x8x8.nii.gz](dk68.md)
- [atlas-DK_nparc-54_space-MNI_res-8x8x8.nii.gz](dk54.md)

### Giles parcellations

- [atlas-Giles_nparc-42_space-MNI_res-8x8x8.nii.gz](giles42.md)
- [atlas-Giles_nparc-39_space-MNI_res-8x8x8.nii.gz](giles39.md)
- [atlas-Giles_nparc-38_space-MNI_res-8x8x8.nii.gz](giles38.md)

### Schaefer parcellations

- [atlas-Schaefer_nparc-100_space-MNI_res-8x8x8.nii.gz](schaefer100.md)
- [atlas-Schaefer_nparc-100_space-MNI_res-5x5x5.nii.gz](schaefer100.md)

### AAL parcellations

- [atlas-AAL_nparc-116_space-MNI_res-8x8x8.nii.gz](aal116.md)
- [atlas-AAL_nparc-78_space-MNI_res-8x8x8.nii.gz](aal78.md)
- [atlas-AAL_nparc-24_space-MNI_res-8x8x8.nii.gz](aal24.md)

## Old Naming

Note, the parcellation files in osl-dynamics have been renamed:

| New name | Old name |
| --- | --- |
| atlas-DK_nparc-68_space-MNI_res-8x8x8.nii.gz | dk_cortical.nii.gz |
| atlas-Giles_nparc-42_space-MNI_res-8x8x8.nii.gz | fmri_d100_parcellation_with_3PCC_ips_reduced_2mm_ss5mm_ds8mm_adj.nii.gz |
| atlas-Giles_nparc-39_space-MNI_res-8x8x8.nii.gz | fmri_d100_parcellation_with_PCC_tighterMay15_v2_8mm.nii.gz |
| atlas-Giles_nparc-38_space-MNI_res-8x8x8.nii.gz | fmri_d100_parcellation_with_PCC_reduced_2mm_ss5mm_ds8mm.nii.gz |
| atlas-AAL_nparc-78_space-MNI_res-8x8x8.nii.gz | aal_cortical_merged_8mm_stacked.nii.gz |

## MNI Coordinates

The parcellations provided are in MNI space.

Obtaining the MNI coordinates of each parcel center, using osl-dynamics:

```python
from osl_dynamics.meeg.parcellation import Parcellation

filename = 'atlas-Giles_nparc-42_space-MNI_res-8x8x8.nii.gz'
parc = Parcellation(filename)
mni_coords = parc.roi_centers()
```
