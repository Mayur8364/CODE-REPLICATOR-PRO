import os
import csv
from fpdf import FPDF

class Replicator:
    def __init__(self, template_path):
        self.template_path = template_path

    def read_template(self):
        with open(self.template_path, 'r') as f:
            return f.read()

    def save_as_python(self, content, filename, output_folder='.'):
        path = os.path.join(output_folder, filename)
        with open(path, 'w') as f:
            f.write(content)

    def save_as_pdf(self, content, filename, output_folder='.'):
        path = os.path.join(output_folder, filename.replace('.py', '.pdf'))
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in content.split('\n'):
            pdf.cell(200, 10, txt=line, ln=True)
        pdf.output(path)

    def generate_custom(self, name, roll, output_format):
        content = self.read_template()
        content = content.replace("Ganesh Wagh", name)
        content = content.replace("133", roll)

        filename = f"{roll}_{name.replace(' ', '_')}.py"
        if output_format == "Python File (.py)":
            self.save_as_python(content, filename)
        else:
            self.save_as_pdf(content, filename)

    def generate_from_csv(self, csv_path, output_folder, output_format):
        content = self.read_template()

        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                roll = row['Roll']

                custom_content = content.replace("Ganesh Wagh", name)
                custom_content = custom_content.replace("133", roll)

                filename = f"{roll}_{name.replace(' ', '_')}.py"
                
                if output_format == "Python File (.py)":
                    self.save_as_python(custom_content, filename, output_folder)
                else:
                    self.save_as_pdf(custom_content, filename, output_folder)
