"""Extract from a log file speeds and compute average speed and batch time."""
from __future__ import print_function
import sys
import os
import yaml


def main():
    """Main function."""
    # Get input parameters
    models_dir = sys.argv[1]
    model_name = sys.argv[2]
    model_file = sys.argv[3]

    if not model_file.endswith('.xml'):
        model_file = model_file + '.xml'

    # print("models_dir={}, model_name={}, model_file={}".format(models_dir, model_name, model_file))
    #
    models_list = '/opt/intel/openvino/deployment_tools/tools/model_downloader/list_topologies.yml'
    # models_list = '/home/serebrya/.dlbs/openvino/list_topologies.yml'
    with open(models_list, 'r') as stream:
        try:
            models = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            exit(1)

    #
    models = models['topologies']
    for model in models:
        if model['name'] != model_name:
            continue
        for file_info in model['files']:
            if file_info['name'] == model_file:
                print(os.path.join(models_dir, model['output'], model_file))
                exit(0)


if __name__ == '__main__':
    main()
