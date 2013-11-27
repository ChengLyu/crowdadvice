from adviceapp.models import Category
from adviceapp.helper import move_to_last

def get_category_mapping():
    """Get a dict of all main(industry) category to available sub(career field) category
    """
    
    cat_dict = {}
    for cat in Category.objects.all():
        if not cat.industry in cat_dict:
            cat_dict[cat.industry] = []
        
        cat_dict[cat.industry].append(cat.career_field)

    return cat_dict


def get_industry_choices():
    """Get a list of tuple for all industries to be choices in model or form
    """
    
    industries = set()
    for cat in Category.objects.all():
        industries.add(cat.industry)
    
    industries_list = list(industries)
    industries_list.sort()
    
    move_to_last(industries_list, "Other")

    return [(c, c) for c in industries_list]


def get_field_choices():
    """Get a list of tuple for all career fields used be choices in model or form
    """
    
    fields = set()
    for cat in Category.objects.all():
        fields.add(cat.career_field)

    fields_list = list(fields)
    fields_list.sort()
    
    move_to_last(fields_list, "Other")
    
    return [(c, c) for c in fields_list]
