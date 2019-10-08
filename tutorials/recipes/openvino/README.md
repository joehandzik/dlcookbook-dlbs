# OpenVINO benchmarks recipes.

> Work in progress.
For more details, read this [file](../../../docker/openvino/19.09/README.md).


## Models
Batch sizes different from those defined here may not work. Copy-past one of these configurations to the config [file](./config.json).

#### Example configuration 1
```
"exp.model": "resnet-50-int8-tf-0001",
"openvino.model": "FP32/resnet-50-int8-tf-0001",
"exp.replica_batch": 1,
``` 
Batch size 2 error: `[ ERROR ] Failed to infer shapes for Reshape layer (resnet_v1_50/pool5/Reshape) with error: Invalid reshape mask (dim attribute): number of elements in input: [2,2048,7,7] and output: [1,2048,49,1] mismatch`.

#### Example configuration 2
```
"exp.model": "vehicle-license-plate-detection-barrier-0106",
"openvino.model": "FP16/vehicle-license-plate-detection-barrier-0106.xml",
"exp.replica_batch": 1,
``` 
Batch size 2 error: `[ ERROR ] Number of priors must match number of confidence predictions.`.


#### Eample configuration 3
```
"exp.model": "semantic-segmentation-adas-0001",
"openvino.model": "FP32/semantic-segmentation-adas-0001.xml",
"exp.replica_batch": 2,
```
Batch size 2 works OK.