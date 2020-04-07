from selenium.webdriver.common.by import By


class WishListLocators:

    featured_section = (By.CSS_SELECTOR, '#content .product-thumb.transition .caption h4 a')
    wish_list_link = (By.CSS_SELECTOR, '#wishlist-total .fa-heart')
    wish_list_button = (By.CSS_SELECTOR, '.btn-group [data-original-title="Add to Wish List"]')
    wish_list_product_name = (By.CSS_SELECTOR, '.table-bordered.table-hover .text-left > a')
    delete_wish_list_position_button = (By.CSS_SELECTOR, '[data-original-title="Remove"] .fa-times')
    my_wish_list_breadcrumb = (By.CSS_SELECTOR, '.breadcrumb li:nth-child(3)')