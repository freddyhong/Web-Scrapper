def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("Job,Company,Location,Link\n")

    for job in jobs:
        file.write(
            f"{job['name']},{job['company']},{job['location']},{job['link']}\n")

    file.close()
