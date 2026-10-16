# Legacy parcellations

Parcellation files that osl-ephys shipped before version 3, kept under their
original names so that older analyses can be reproduced. They are variants of
atlases that exist in [`parcellation/`](..) in a maintained form, and are not
documented or updated beyond this note:

| File | What it is |
| --- | --- |
| dk_full.nii.gz | Desikan-Killiany with 68 cortical and 14 subcortical parcels at 8 mm |
| giles_39_binary.nii.gz | A binarised version of the Giles 39-parcel parcellation at 8 mm |
| fmri_d100_parcellation_with_PCC_tighterMay15_v2_6mm_exclusive.nii.gz | The Giles 39-parcel parcellation at 6 mm with non-overlapping parcels |
| fmri_d100_parcellation_with_PCC_reduced_2mm.nii.gz | An earlier 39-parcel version of the Giles parcellation at 2 mm |
| WTA_fMRI_parcellation_ds2mm.nii.gz, WTA_fMRI_parcellation_ds8mm.nii.gz | Winner-takes-all label volumes of the Giles 38-parcel parcellation at 2 mm and 8 mm |

New analyses should use the files in `parcellation/`.
