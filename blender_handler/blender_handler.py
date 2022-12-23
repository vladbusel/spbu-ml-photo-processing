import subprocess

def coord_template(template):
    if template == "1":
        return "0 0 0.8 0 0 -0.3"
    elif template == "2":
        return "-0.7 0 0.5 0.7 0 0.5"
    elif template == "3":
        return "0.7 0 0.5 -0.7 0 0.5"
    elif template == "4":
        return "0 0 -0.3 0 0 0.8"

class BlenderHandler:
    def __init__(self):
        pass

    def call(self, params):
        template = params
        coords = f"{coord_template(template[0])}".split()
        args = ["blender", "--background", "template.blend", "--python", "render.py", "--", "image.jpg", "norm.png", "depth.png"] + coords
        print(" ".join(args))
        subprocess.run(args, stdout=subprocess.PIPE)
