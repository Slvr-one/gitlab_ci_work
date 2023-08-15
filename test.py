import subprocess
import logging

def create_resource_group(resource_group_name, location):
    try:
        subprocess.run(['az', 'group', 'create', '--name', resource_group_name, '--location', location], check=True)
        print(f"Resource group '{resource_group_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        msg = print(f"Error creating resource group: {e}")
        logging.critical(msg)

def deploy_arm_template(resource_group_name, template_file, parameters_file):
    try:
        # subprocess.Popen()
        subprocess.run(['az', 'deployment', 'group', 'create', '--resource-group', resource_group_name,
                        '--template-file', template_file, '--parameters', parameters_file], check=True)
        print("ARM template deployment completed successfully.")
    except subprocess.CalledProcessError as e:
        msg = print(f"Error deploying ARM template: {e}")
        logging.critical(msg)

def main():
    resource_group_name = 'my-resource-group'
    location = 'East US'
    template_file = 'azuredeploy.json'
    parameters_file = 'azuredeploy.parameters.json'

    create_resource_group(resource_group_name, location)
    deploy_arm_template(resource_group_name, template_file, parameters_file)

if __name__ == "__main__":
    main()
