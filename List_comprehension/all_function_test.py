podLabels = {
    "name": "esm",
    "test": True,
    "version": 1.15,
    "package": "base",
    "catalog": 1.8
}

name = "Kubernetes IO"

matchLabels = {
    "name": "esm",
    "version": 1.15,
    "package": "base"
}

my_list = []

if all([label in podLabels and matchLabels[label] == podLabels[label] for label in matchLabels]):
    my_list.append(name)
    
print(my_list)