__author__ = 'ChengLyu'
# Build the built-in scores of career mappings into the database

from adviceapp.models import CategoryCorrelation
from adviceapp.models import Category


def set_category_scores(category1, category2, score):
    try:
        category_correlation = CategoryCorrelation.objects.get(category1=category1, category2=category2)
    except CategoryCorrelation.DoesNotExist:
        try:
            category_correlation = CategoryCorrelation.objects.get(category1=category2, category2=category1)
        except CategoryCorrelation.DoesNotExist:
            category_correlation = CategoryCorrelation(category1=category1, category2=category2)
    category_correlation.score = score
    category_correlation.save()


def build_category_scores():
    """
        Determine the scores between any two categories (Hardcoding currently)
    """

    industry_categories = ['Accounting', 'Broadcast & Media', 'Consulting', 'Energy',
                           'Education', 'Entertainment', 'Financial', 'Health Care',
                           'Internet & Software', 'Law & Legal', 'Manufacturing', 'Retail & Consumer',
                           'Social Enterprise', 'Others']

    career_fields = ['Accounting & Auditing', 'Advertising', 'Analyst', 'Business Development',
                     'Consulting', 'Customer Service', 'Computer Software', 'Design',
                     'Entrepreneur', 'Engineering', 'Human Resources', 'Marketing',
                     'Project Management', 'Public Relations', 'Research & Scientist', 'Sales',
                     'Others']

    categories = [Category(main=industry_categories[0], sub=career_fields[0]),
                  Category(main=industry_categories[1], sub=career_fields[11]),
                  Category(main=industry_categories[2], sub=career_fields[4]),
                  Category(main=industry_categories[3], sub=career_fields[2]),
                  Category(main=industry_categories[4], sub=career_fields[4]),
                  Category(main=industry_categories[5], sub=career_fields[13]),
                  Category(main=industry_categories[6], sub=career_fields[2]),
                  Category(main=industry_categories[7], sub=career_fields[5]),
                  Category(main=industry_categories[8], sub=career_fields[6]),
                  Category(main=industry_categories[9], sub=career_fields[5]),
                  Category(main=industry_categories[10], sub=career_fields[3]),
                  Category(main=industry_categories[11], sub=career_fields[15]),
                  Category(main=industry_categories[12], sub=career_fields[8]),
                  Category(main=industry_categories[13], sub=career_fields[16])]

    # Save the categories
    for category in categories:
        category.save()

    # Construct the scores
    set_category_scores(categories[0], categories[0], 0)
    set_category_scores(categories[0], categories[1], 10)
    set_category_scores(categories[0], categories[2], 5)
    set_category_scores(categories[0], categories[3], 10)
    set_category_scores(categories[0], categories[4], 10)
    set_category_scores(categories[0], categories[5], 10)
    set_category_scores(categories[0], categories[6], 0)
    set_category_scores(categories[0], categories[7], 10)
    set_category_scores(categories[0], categories[8], 10)
    set_category_scores(categories[0], categories[9], 10)
    set_category_scores(categories[0], categories[10], 5)
    set_category_scores(categories[0], categories[11], 5)
    set_category_scores(categories[0], categories[12], 5)
    set_category_scores(categories[0], categories[13], 15)

    set_category_scores(categories[1], categories[1], 0)
    set_category_scores(categories[1], categories[2], 5)
    set_category_scores(categories[1], categories[3], 10)
    set_category_scores(categories[1], categories[4], 5)
    set_category_scores(categories[1], categories[5], 0)
    set_category_scores(categories[1], categories[6], 10)
    set_category_scores(categories[1], categories[7], 10)
    set_category_scores(categories[1], categories[8], 5)
    set_category_scores(categories[1], categories[9], 10)
    set_category_scores(categories[1], categories[10], 10)
    set_category_scores(categories[1], categories[11], 5)
    set_category_scores(categories[1], categories[12], 5)
    set_category_scores(categories[1], categories[13], 15)

    set_category_scores(categories[2], categories[2], 0)
    set_category_scores(categories[2], categories[3], 5)
    set_category_scores(categories[2], categories[4], 5)
    set_category_scores(categories[2], categories[5], 10)
    set_category_scores(categories[2], categories[6], 5)
    set_category_scores(categories[2], categories[7], 10)
    set_category_scores(categories[2], categories[8], 5)
    set_category_scores(categories[2], categories[9], 10)
    set_category_scores(categories[2], categories[10], 0)
    set_category_scores(categories[2], categories[11], 5)
    set_category_scores(categories[2], categories[12], 5)
    set_category_scores(categories[2], categories[13], 15)

    set_category_scores(categories[3], categories[3], 0)
    set_category_scores(categories[3], categories[4], 10)
    set_category_scores(categories[3], categories[5], 10)
    set_category_scores(categories[3], categories[6], 5)
    set_category_scores(categories[3], categories[7], 10)
    set_category_scores(categories[3], categories[8], 5)
    set_category_scores(categories[3], categories[9], 5)
    set_category_scores(categories[3], categories[10], 0)
    set_category_scores(categories[3], categories[11], 5)
    set_category_scores(categories[3], categories[12], 10)
    set_category_scores(categories[3], categories[13], 15)

    set_category_scores(categories[4], categories[4], 0)
    set_category_scores(categories[4], categories[5], 10)
    set_category_scores(categories[4], categories[6], 10)
    set_category_scores(categories[4], categories[7], 10)
    set_category_scores(categories[4], categories[8], 5)
    set_category_scores(categories[4], categories[9], 10)
    set_category_scores(categories[4], categories[10], 10)
    set_category_scores(categories[4], categories[11], 10)
    set_category_scores(categories[4], categories[12], 5)
    set_category_scores(categories[4], categories[13], 15)

    set_category_scores(categories[5], categories[5], 0)
    set_category_scores(categories[5], categories[6], 5)
    set_category_scores(categories[5], categories[7], 10)
    set_category_scores(categories[5], categories[8], 5)
    set_category_scores(categories[5], categories[9], 10)
    set_category_scores(categories[5], categories[10], 10)
    set_category_scores(categories[5], categories[11], 5)
    set_category_scores(categories[5], categories[12], 10)
    set_category_scores(categories[5], categories[13], 15)

    set_category_scores(categories[6], categories[6], 0)
    set_category_scores(categories[6], categories[7], 10)
    set_category_scores(categories[6], categories[8], 5)
    set_category_scores(categories[6], categories[9], 5)
    set_category_scores(categories[6], categories[10], 5)
    set_category_scores(categories[6], categories[11], 5)
    set_category_scores(categories[6], categories[12], 5)
    set_category_scores(categories[6], categories[13], 15)

    set_category_scores(categories[7], categories[7], 0)
    set_category_scores(categories[7], categories[8], 5)
    set_category_scores(categories[7], categories[9], 5)
    set_category_scores(categories[7], categories[10], 10)
    set_category_scores(categories[7], categories[11], 10)
    set_category_scores(categories[7], categories[12], 5)
    set_category_scores(categories[7], categories[13], 15)

    set_category_scores(categories[8], categories[8], 0)
    set_category_scores(categories[8], categories[9], 10)
    set_category_scores(categories[8], categories[10], 10)
    set_category_scores(categories[8], categories[11], 5)
    set_category_scores(categories[8], categories[12], 5)
    set_category_scores(categories[8], categories[13], 15)

    set_category_scores(categories[9], categories[9], 0)
    set_category_scores(categories[9], categories[10], 5)
    set_category_scores(categories[9], categories[11], 10)
    set_category_scores(categories[9], categories[12], 5)
    set_category_scores(categories[9], categories[13], 15)

    set_category_scores(categories[10], categories[10], 0)
    set_category_scores(categories[10], categories[11], 5)
    set_category_scores(categories[10], categories[12], 5)
    set_category_scores(categories[10], categories[13], 15)

    set_category_scores(categories[11], categories[11], 0)
    set_category_scores(categories[11], categories[12], 5)
    set_category_scores(categories[11], categories[13], 15)

    set_category_scores(categories[12], categories[12], 0)
    set_category_scores(categories[12], categories[13], 15)

    set_category_scores(categories[13], categories[13], 0)