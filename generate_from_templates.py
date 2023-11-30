from datetime import datetime

from jinja2 import Environment, FileSystemLoader


TEMPLATES_DIR = 'templates'
TEMPLATES = {
    'Day00.scala.txt': 'src/main/scala/Advent{year}/',
    'Day00.txt.txt': 'src/main/resources/Advent{year}/',
    'Day00Suite.scala.txt': 'src/test/scala/Advent{year}/',
    'day_00.py.txt': 'src/main/python/Advent{year}/',
    'test_day_00.py.txt': 'src/test/python/Advent{year}/',
}

if __name__ == '__main__':
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    day_number = input('Two digit day number (like 01): ')
    year = datetime.now().year

    template_vars = {
        'DAY_NUMBER': day_number,
        'YEAR': year,
    }

    for template_file, path in TEMPLATES.items():
        template = env.get_template(template_file)
        rendered = template.render(template_vars)
        output_path = path.format(year=year).replace('.txt', '') + template_file.replace('00', day_number)
        with open(output_path, 'w') as f:
            f.write(rendered)
            print(f'Wrote {output_path}.')
