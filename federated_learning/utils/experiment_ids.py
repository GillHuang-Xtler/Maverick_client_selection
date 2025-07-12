def generate_experiment_ids(start_idx, num_exp):
    log_files = []
    results_files = []
    models_folders = []
    worker_selections_files = []

    for i in range(num_exp):
        idx = str(start_idx + i)

        log_files.append("logs/" + idx + ".log")
        results_files.append(idx + "_results.csv")
        models_folders.append(idx + "_models")
        worker_selections_files.append(idx + "_workers_selected.csv")

    return log_files, results_files, models_folders, worker_selections_files
