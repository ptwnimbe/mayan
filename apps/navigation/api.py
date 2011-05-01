import copy

object_navigation = {}
multi_object_navigation = {}
menu_links = []
model_list_columns = {}
sidebar_templates = {}


def register_multi_item_links(src, links, menu_name=None):
    if menu_name in multi_object_navigation:
        if hasattr(src, '__iter__'):
            for one_src in src:
                if one_src in object_navigation[menu_name]:
                    multi_object_navigation[menu_name][one_src]['links'].extend(links)
                else:
                    multi_object_navigation[menu_name][one_src] = {'links': copy.copy(links)}
        else:
            if src in multi_object_navigation[menu_name]:
                multi_object_navigation[menu_name][src]['links'].extend(links)
            else:
                multi_object_navigation[menu_name][src] = {'links': links}
    else:
        multi_object_navigation[menu_name] = {}
        if hasattr(src, '__iter__'):
            for one_src in src:
                multi_object_navigation[menu_name][one_src] = {'links': links}
        else:
            multi_object_navigation[menu_name] = {src: {'links': links}}


def register_links(src, links, menu_name=None):
    if menu_name in object_navigation:
        if hasattr(src, '__iter__'):
            for one_src in src:
                if one_src in object_navigation[menu_name]:
                    object_navigation[menu_name][one_src]['links'].extend(links)
                else:
                    object_navigation[menu_name][one_src] = {'links': copy.copy(links)}
        else:
            if src in object_navigation[menu_name]:
                object_navigation[menu_name][src]['links'].extend(links)
            else:
                object_navigation[menu_name][src] = {'links': links}
    else:
        object_navigation[menu_name] = {}
        if hasattr(src, '__iter__'):
            for one_src in src:
                object_navigation[menu_name][one_src] = {'links': links}
        else:
            object_navigation[menu_name] = {src: {'links': links}}


def register_menu(links):
    for link in links:
        menu_links.append(link)

    menu_links.sort(lambda x, y: 1 if x > y else -1, lambda x: x['position'] if 'position' in x else 1)


def register_model_list_columns(model, columns):
    if model in model_list_columns:
        model_list_columns[model].extend(columns)
    else:
        model_list_columns[model] = copy.copy(columns)


def register_sidebar_template(source_list, template_name):
    for source in source_list:
        if source in sidebar_templates:
            sidebar_templates[source].append(template_name)
        else:
            sidebar_templates[source] = [template_name]