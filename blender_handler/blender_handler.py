import subprocess

def coord_template(template):
    if template == "1":
        return "0.4 0.4"
    elif template == "2":
        return "-0.4 0.4"
    elif template == "3":
        return "-0.4 -0.4"
    elif template == "4":
        return "0.4 -0.4"

class BlenderHandler:
    def __init__(self):
        pass

    def call(self, params):
        (template0, template1) = params
        coords = f"{coord_template(template0)} -0.8 {coord_template(template1)} 0.8".split()
        args = ["blender", "--background", "template.blend", "--python", "render.py", "--", "image.jpg", "norm.png", "depth.png"] + coords
        print(" ".join(args))
        subprocess.run(args, stdout=subprocess.PIPE)
