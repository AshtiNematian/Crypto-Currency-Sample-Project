from cart.models import Cart, Coupon


class CartHelper:

    def __init__(self, user):
        self.user = user
        self.cart_base_total_amount = 0
        self.cart_final_total_amount = 0
        self.coupon_discount_amount = 0
        self.delivery_cost = 0
        self.cart_items = []
        self.discounts = {}
        self.checkout_details = {'products': [], 'total': [], 'amount': []}

    def prepare_cart_for_checkout(self):
        self.cart_items = Cart.objects.filter(user=self.user)

        if not self.cart_items:
            return False

        self.calculate_cart_base_total_amount()
        self.get_coupon_discounts()
        self.get_total_amount_after_discounts()
        self.prepare_checkout_details()

        return self.checkout_details

    def calculate_cart_base_total_amount(self):
        for cart_item in self.cart_items:
            self.cart_base_total_amount += cart_item.item.price

    def get_coupon_discounts(self):
        coupon_helper = CouponHelper(cart_total_amount=self.cart_base_total_amount)
        self.discounts['coupons'] = coupon_helper.get_coupon_discounts()

    def get_total_amount_after_discounts(self):

        self.cart_final_total_amount = self.cart_base_total_amount - self.coupon_discount_amount

        return self.cart_final_total_amount

    def prepare_checkout_details(self):
        for cart_item in self.cart_items:
            self.checkout_details['products'].append({
                                                      'product_id': cart_item.item.id,
                                                      'membership_type': cart_item.item.membership_type,
                                                      'unit_price': cart_item.item.price})

        self.checkout_details['total'].append({'total_price': self.cart_base_total_amount,
                                               'total_discount':
                                                   self.coupon_discount_amount})

        self.checkout_details['amount'].append({'total_amount': self.cart_final_total_amount,
                                                'delivery_cost': self.delivery_cost})


class CouponHelper:

    def __init__(self, cart_total_amount):
        self.cart_total_amount = cart_total_amount
        self.available_discounts = []

    def get_coupon_discounts(self):
        coupon_discounts = Coupon.objects.filter(minimum_cart_amount__lte=self.cart_total_amount)

        for coupon_discount in coupon_discounts:
            discount = AvailableDiscount(discount_type='Rate',
                                         min_purchased_items=0,
                                         amount={'rate': coupon_discount.discount_rate,
                                                 'amount': None})
            self.available_discounts.append(discount)

        return self.available_discounts


class AvailableDiscount:

    def __init__(self, discount_type, min_purchased_items, amount):
        self.discount_type = discount_type
        self.amount = amount
        self.min_purchased_items = min_purchased_items
