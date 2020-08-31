import subprocess

# To remove images
raw_input = subprocess.check_output(["docker", "images", "-a"])

raw_string = str(raw_input).split("\\n")
rows = [row.split(" ") for row in raw_string]

filtered = [list(filter(lambda item: len(item)>0, row)) for row in rows]

images = [row[2] for row in filtered[1:len(filtered)-1]]

for image in images:
    subprocess.run(["docker", "rmi", image, "--force"])

# To remove volumes
raw_input = subprocess.check_output(["docker", "volume", "ls"])

raw_string = str(raw_input).split("\\n")
rows = [row.split(" ") for row in raw_string]

filtered = [list(filter(lambda item: len(item)>0, row)) for row in rows]

volumes = [row[1] for row in filtered[1:len(filtered)-1]]

for volume in volumes:
    subprocess.run(["docker", "volume", "rm",  volume])

# Prune everything
subprocess.run(["docker", "system", "prune", "--force"])
