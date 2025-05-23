import kagglehub

path = kagglehub.dataset_download("himanshuwagh/spotify-million")

print("Path to dataset files:", path)
with open("dataset_path.txt", "wt") as f:
    f.write(path)





