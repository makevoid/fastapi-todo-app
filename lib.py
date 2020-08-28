import mako.lookup
import haml

lookup = mako.lookup.TemplateLookup(["views"], preprocessor=haml.preprocessor)

TEMPLATES = {}

def lookup_template(template_name):
    template = TEMPLATES.get(template_name)
    if template: return template
    template = lookup.get_template(f'{template_name}.haml')
    TEMPLATES[template_name] = template
    return template

def render(template_name, **args):
    template = lookup_template(template_name)
    return template.render(**args)
