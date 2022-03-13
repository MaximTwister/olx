from faker import Faker

from olx.models import (
    Advertisement,
    AdvCategory,
    AdvSubCategory,
    Account,
)
from olx.utils.constants import (
    FIRST_NAME_INDEX,
    CATEGORIES_SUBCATEGORIES,
    ADV_TEMPLATES,
)


def create_accounts(accounts_amount=10):
    fake = Faker()
    nicknames = set()
    for _ in range(accounts_amount):
        name = fake.name().split()[FIRST_NAME_INDEX]
        nicknames.add(name)
    accounts = [Account(nickname=name) for name in nicknames]
    Account.objects.bulk_create(accounts)


def create_categories():
    for category, subcategories in CATEGORIES_SUBCATEGORIES.items():
        cat = AdvCategory(title=category)
        subcats = [AdvSubCategory(title=subcat, category=cat) for subcat in subcategories]
        cat.save()
        AdvSubCategory.objects.bulk_create(subcats)


def create_advertisement():
    accounts = Account.objects.all()
    cat = AdvCategory.objects.get(title="Clothes-Shoes")
    subcat = cat.subcategories.get(title="Men")
    for acc in accounts:
        ads = [Advertisement(**adv_templ) for adv_templ in ADV_TEMPLATES]
        for ad in ads:
            ad.account = acc
            ad.subcategory = subcat
        Advertisement.objects.bulk_create(ads)


def main():
    print("Create Accounts")
    create_accounts()
    print("Create Categories and Subcategories")
    create_categories()
    print("Create Advertisements")
    create_advertisement()


main()
