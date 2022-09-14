

f = open("index.html", "w")
f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre.min.css">
<link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre-exp.min.css">
<link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre-icons.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    """)

f.close()
f = open("index.html", "a")
def __init__(title):
    c = "<title>"+title+"</title></head><body>"
    f.write(c)
def dom_add(class_, content):
    c = "<div class='"+class_+"'>"+str(content)+"</div>"
    f.write(c)
