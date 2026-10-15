# Test recordings

Short M/EEG files for testing osl-ephys and osl-dynamics: one per scanner
type, each with the geometry of a real recording and a synthetic signal.

## What is real and what is not

Kept from a real recording: the channel set and names, the sensor
positions and orientations, the fiducials, the HPI coil positions and
frequencies, the EEG electrode positions, the CTF compensation matrices,
and a headshape thinned to at most 100 points with nothing on the face or
below the fiducials.

Everything else is synthetic. Every data channel was overwritten with
simulated signal: a few dipoles projected through a sphere-model forward
solution computed from the real sensor geometry, 1/f sensor noise, a
blink and a heartbeat leaking into the channels, synthetic EOG/ECG/EMG
where the scanner records them, one deliberately bad channel per channel
type, one bad segment and a set of events. Dates, names, free-text fields
and the HPI measurement data were removed. None of the participant's
time series is in these files.

## Ground truth

- Events: codes and onsets in seconds `{1: [2.0, 6.0, 10.0, 14.0, 18.0], 2: [4.0, 8.0, 12.0, 16.0]}` on the first stim channel, or as `event_<code>` annotations where there is no stim channel (read back from BrainVision as `Comment/event_<code>`).
- Bad segment: all MEG/EEG channels scaled by 8 between 10.0 s and 11.0 s.
- Bad channel: the first channel of each type (mag, grad, eeg) carries 20 times the noise of the others and is not marked in `info['bads']`.
- Blinks at [1.3, 5.1, 9.4, 13.7, 17.2] s on the EOG channels, leaking into the frontal channels; heartbeat at 1.1 Hz on the ECG channel.

## Files

| File | Size | Length | Channels | Head geometry |
| --- | --- | --- | --- | --- |
| `elekta/rest-raw.fif` | 6.3 MB | 20 s at 250 Hz | 1 ecg, 1 emg, 2 eog, 204 grad, 102 mag, 1 stim | 3 fiducials, 4 HPI, 0 EEG, 100 headshape |
| `ctf/headshape.pos` | 8 kB |  | 100 headshape points + 3 fiducials (CTF .pos) |  |
| `ctf/rest-raw.fif` | 7.4 MB | 20 s at 250 Hz | 64 eeg, 273 mag, 28 ref_meg, 1 stim | 3 fiducials, 0 HPI, 64 EEG, 0 headshape |
| `opm/task-raw.fif` | 3.9 MB | 20 s at 250 Hz | 192 mag, 2 stim | 3 fiducials, 0 HPI, 0 EEG, 100 headshape |
| `eeg/rest-dig.fif` | 3 kB |  | montage for rest.vhdr (mne.channels.read_dig_fif) | 3 fiducials, 62 EEG |
| `eeg/rest.vhdr/.vmrk/.eeg` | 3.7 MB | 60 s at 250 Hz | 62 eeg | 0 fiducials, 0 EEG, 0 headshape |

Total: 21.4 MB.

## Sources and terms

| Dataset | Source recording | Terms |
| --- | --- | --- |
| `elekta` | Elekta/MEGIN VectorView (306 channels), resting state, University of Oxford | TO CONFIRM |
| `ctf` | CTF-275 with 64 EEG channels, resting state, University of Nottingham | TO CONFIRM |
| `opm` | QuSpin triaxial OPM array (64 sensors), task, University of Nottingham | TO CONFIRM |
| `eeg` | Brain Products actiCAP 62 channels with a Brainstorm localiser, resting state | TO CONFIRM |

## How they were made

The scripts that build these files are kept outside this repository
(OHBA-internal `make_osl_test_data`: one script per dataset and the
shared steps in `common.py`). Each script takes the private source
recording as an argument, so the files are reproducible and the
anonymisation is code. `readme.py` regenerates this file from the
built files and the ground-truth constants.
