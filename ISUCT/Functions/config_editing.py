def edit_config_file(config_file):
    with open(config_file) as config:
        return config.readlines()