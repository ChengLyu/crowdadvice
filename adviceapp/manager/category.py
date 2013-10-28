from adviceapp.models import Category
from adviceapp.helper import move_to_last

def get_category_mapping():
    """Get a dict of all main category to available sub category
    """
    
    cat_dict = {}
    for cat in Category.objects.all():
        if not cat.main in cat_dict:
            cat_dict[cat.main] = []
        
        cat_dict[cat.main].append(cat.sub)

    return cat_dict


def get_industry_choices():
    """Get a list of tuple for all industries used be choices in model or form
    """
    
    industries = set()
    for cat in Category.objects.all():
        industries.add(cat.main)
    
    industries_list = list(industries)
    industries_list.sort()
    
    move_to_last(industries_list, "Other")

    return [(c, c) for c in industries_list]


def get_field_choices():
    """Get a list of tuple for all fields used be choices in model or form
    """
    
    fields = set()
    for cat in Category.objects.all():
        fields.add(cat.sub)

    fields_list = list(fields)
    fields_list.sort()
    
    move_to_last(fields_list, "Other")
    
    return [(c, c) for c in fields_list]
