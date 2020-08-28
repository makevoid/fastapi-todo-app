from env import APP_ENV, TEMPLATES
import mako.lookup
import haml

lookup = mako.lookup.TemplateLookup(["views"], preprocessor=haml.preprocessor)

def lookup_template(template_name):
    template = TEMPLATES.get(template_name)
    cache_template = template and APP_ENV != "development"
    if cache_template: return template
    template = lookup.get_template(f'{template_name}.haml')
    TEMPLATES[template_name] = template
    return template

def render(template_name, **args):
    template = lookup_template(template_name)
    return template.render(**args)
