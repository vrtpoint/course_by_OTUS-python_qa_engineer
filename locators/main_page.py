from selenium.webdriver.common.by import By


class MainPage:


        class HeaderSection:
            currency_dropdown_link = (By.CSS_SELECTOR, '#form-currency')
            currency_EUR_button = (By.CSS_SELECTOR, 'button[name="EUR"]')
            currency_GBP_button = (By.CSS_SELECTOR, 'button[name="GBP"]')
            currency_USD_button = (By.CSS_SELECTOR, 'button[name="USD"]')
            phone_number_link = (By.CSS_SELECTOR, '.list-inline .fa-phone')
            my_account_link = (By.CSS_SELECTOR, '#top-links .dropdown .fa-user')
            register_link = (By.CSS_SELECTOR, 'a[href="https://localhost/index.php?route=account/register"]')
            login_link = (By.CSS_SELECTOR, 'a[href="https://localhost/index.php?route=account/login"]')
            email_address_field = (By.CSS_SELECTOR, '#input-email')
            password_field = (By.CSS_SELECTOR, '#input-password')
            login_button = (By.CSS_SELECTOR, 'input[type="submit"]')
            logout_button = (By.CSS_SELECTOR, '#top-links .dropdown-menu-right li:nth-child(5) a')
            wish_list_link = (By.CSS_SELECTOR, '#wishlist-total .fa-heart')
            shopping_cart_link = (By.CSS_SELECTOR, 'a[title="Shopping Cart"]')
            checkout_link = (By.CSS_SELECTOR, 'a[title="Checkout"]')
            logo_name = (By.CSS_SELECTOR, '#logo>h1 a')
            desktops_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(1) [data-toggle="dropdown"]')
            pc_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(1) ul li:nth-child(1) a')
            mac_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(1) ul li:nth-child(2) a')
            show_all_desktops_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(1) a.see-all')
            laptops_and_notebooks_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(2) [data-toggle="dropdown"]')
            macs_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(2) ul li:nth-child(1) a')
            windows_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(2) ul li:nth-child(2) a')
            show_all_laptops_and_notebooks_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(2) a.see-all')
            components_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(3) [data-toggle="dropdown"]')
            mice_and_trackballs_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(3) ul li:nth-child(1) a')
            monitors_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(3) ul li:nth-child(2)')
            printers = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(3) ul li:nth-child(3)')
            scanners = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(3) ul li:nth-child(4)')
            web_cameras = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(3) ul li:nth-child(5)')
            show_all_components_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(3) [data-toggle="dropdown"]')
            tablets_label = (By.CSS_SELECTOR, '#menu > .collapse ul.navbar-nav > li:nth-child(4) a')
            software_label = (By.CSS_SELECTOR, '#menu > .collapse ul.navbar-nav > li:nth-child(5) a')
            phones_and_PDAs_label = (By.CSS_SELECTOR, '#menu > .collapse ul.navbar-nav > li:nth-child(6) a')
            cameras_label = (By.CSS_SELECTOR, '#menu > .collapse ul.navbar-nav > li:nth-child(7) a')
            mp3_players_label = (By.CSS_SELECTOR, '#menu > .collapse li:nth-child(8) [data-toggle="dropdown"]')


        class SearchingSection:

            searching_field = (By.CSS_SELECTOR, 'input[class="form-control input-lg"]')
            searching_button = (By.CSS_SELECTOR, '.input-group-btn .btn-lg')
            shopping_cart_button = (By.CSS_SELECTOR, '#cart-total')


        class MainSection:

            slide_section = (By.CSS_SELECTOR, '#slideshow0')
            active_slide = (By.CSS_SELECTOR, '#slideshow0 > .swiper-wrapper .swiper-slide-duplicate.swiper-slide-active img')
            duplicate_slide = (By.CSS_SELECTOR, '#slideshow0 > .swiper-wrapper .swiper-slide-prev.swiper-slide-duplicate-next img')
            left_side_arrow_link = (By.CSS_SELECTOR, '.swiper-button-prev')
            right_side_arrow_link = (By.CSS_SELECTOR, '.swiper-button-next')
            featured_section = (By.CSS_SELECTOR, '#content .product-thumb.transition .caption h4 a')
            wish_list_button = (By.CSS_SELECTOR, '.btn-group [data-original-title="Add to Wish List"]')
            wish_list_product_name = (By.CSS_SELECTOR, '.table-bordered.table-hover .text-left > a')
            shopping_cart_product_name = (By.CSS_SELECTOR, '.table-bordered .text-left > a')
            add_to_cart_button = (By.CSS_SELECTOR, '#content i.fa-shopping-cart')
            carousel_section = (By.CSS_SELECTOR, '#carousel0 .swiper-slide.text-center')


        class InnerSection:

            account_breadcrumb = (By.CSS_SELECTOR, '#account-account > ul li:nth-child(2)')
            logout_breadcrumb = (By.CSS_SELECTOR, '.breadcrumb li:nth-child(3)')
            my_wish_list_breadcrumb = (By.CSS_SELECTOR, '.breadcrumb li:nth-child(3)')
            delete_wish_list_position_button = (By.CSS_SELECTOR, '[data-original-title="Remove"] .fa-times')
            delete_shopping_cart_position_button = (By.CSS_SELECTOR, '.btn.btn-danger .fa-times-circle')
            shopping_cart_info = (By.CSS_SELECTOR, '#content h1')