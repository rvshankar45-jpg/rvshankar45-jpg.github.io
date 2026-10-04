# Misroute examples (Laya at the configured threshold): cheap answer vs strong answer


## complex_to_cheap (3 total, first 5)


### q075 [complex] Laya P(complex)=0.468

**Customer:** Sending a plant to my sister as a gift. will she see what I paid, and can I add a message?

**Cheap model** (quality 5, $0.0016):

Great question! Here's what happens with gift orders:

**Price:** No—prices are never printed on gift packing slips, so your sister won't see what you paid.

**Message:** Yes! You can add a free printed gift note with up to 200 characters, so you can include a personal message with the plant.

Just make sure to select the gift option when placing your order on the website or app.

**Strong model** (quality 5, $0.0037):

No, she won't see what you paid. Prices are never printed on gift packing slips. You can also add a free printed gift note of up to 200 characters to your order.


### q076 [complex] Laya P(complex)=0.295

**Customer:** I'm a Plus member placing a $60 order with express. What will shipping cost?

**Cheap model** (quality 3, $0.0015):

Express shipping will cost **$14.95**.

Leafy Plus gives you free *Standard* shipping with no minimum order, but Express shipping is never free—even for Plus members. Your $60 order doesn't qualify for free Standard shipping anyway since it's under the $75 threshold.

**Strong model** (quality 5, $0.0050):

Express shipping is **$14.95** for your order. Express is never free, including for Leafy Plus members, so your membership doesn't reduce that cost. The Plus free shipping benefit applies only to Standard shipping.

Express delivery is next business day in Zone 1 and 2 business days in Zone 2. It isn't available for Zone 3 addresses (over 1,000 miles from the nearest greenhouse, or remote and island addresses).

If your order includes an XL plant (usually over 4 ft), it adds a $20 handling fee and ships Standard only.


### q085 [complex] Laya P(complex)=0.490

**Customer:** I want to delete my account but I'm on the plant club. what happens to that?

**Cheap model** (quality 3, $0.0020):

When you delete your account, your Plant Club subscription will be **cancelled automatically**. 

Here's what you need to know:

- Account deletion takes up to **30 days** to complete.
- Any Plant Club box that's already been charged (typically on the 25th of the previous month) will still be sent to you during that 30-day window, even though the subscription is cancelled.
- You can delete your account anytime from "Account" > "Privacy" — there's no cancellation fee or minimum term.

If you'd prefer to cancel just the Plant Club subscription *before* deleting your full account, you can skip that from "Account" > "Subscriptions" anytime, and it takes effect before the 25th if you do it before that date.

Is there anything else I can help with?

**Strong model** (quality 3, $0.0082):

Deleting your account cancels your Plant Club subscription, but deletion can take up to 30 days to complete. The policy doesn't say exactly when the cancellation takes effect within that window, so I'd cancel the subscription yourself first under "Account" > "Subscriptions". Plant Club is charged on the 25th for the following month's box, so cancelling before October 25 stops the November box from being billed.

Cancelling has no fee, but a box that's already been billed isn't refunded and still ships. If you've been billed for October's box, expect it to arrive in the first full week of October.

You can start the deletion under "Account" > "Privacy". You can also download your data there first if you want a copy.


## simple_to_strong (45 total, first 5)


### q003 [simple] Laya P(complex)=0.554

**Customer:** Do you ship internationally?

**Cheap model** (quality 4, $0.0013):

No, we don't ship internationally. Leafy ships within the US only.

If you're outside the US, I'd recommend checking if there's a local plant retailer in your area. Is there anything else I can help with?

**Strong model** (quality 5, $0.0036):

No, we don't offer international shipping. Leafy ships only within our domestic delivery zones, and live plants can't be sent to PO boxes. If you have an address in mind, I can go over the delivery times that would apply to it.


### q005 [simple] Laya P(complex)=0.593

**Customer:** How long does the plant care guarantee last?

**Cheap model** (quality 5, $0.0010):

The Plant Care Guarantee lasts **30 days** from delivery for all customers, or **90 days** if you're a Leafy Plus member (on plants ordered while your membership is active).

**Strong model** (quality 5, $0.0033):

Every live plant has a **30-day guarantee** from the delivery date. Leafy Plus members get **90 days** on plants ordered while their membership is active.

To make a claim, go to "My Orders" within that window and upload at least two photos (the whole plant and a close-up). A Plant Care Specialist will review it within 2 business days.


### q006 [simple] Laya P(complex)=0.553

**Customer:** Can I pay with cash?

**Cheap model** (quality 5, $0.0016):

No, Leafy doesn't accept cash payments. We accept:

- Credit and debit cards
- Digital wallets at checkout
- Leafy gift cards

Buy-now-pay-later is also available for orders between $50–$1,000. You can place your order on our website or app using any of these methods.

**Strong model** (quality 5, $0.0040):

No, we don't accept cash (or cheques or bank transfers). You can pay with credit or debit cards, digital wallets at checkout, or Leafy gift cards. Buy-now-pay-later is also available on orders of $50–$1,000.


### q008 [simple] Laya P(complex)=0.582

**Customer:** when r u open for chat

**Cheap model** (quality 5, $0.0015):

Hi! Our **chat support is open 8am–8pm Monday to Saturday** (your local time).

If you need help outside those hours, you can email us at **help@leafy.example** and we'll reply within 1 business day. 

What can I help with?

**Strong model** (quality 5, $0.0044):

Our chat is open **8am–8pm, Monday to Saturday**, in your local time. If you'd like to talk to a Plant Care Specialist, their chat hours are **9am–5pm, Monday to Friday**.

You can also email help@leafy.example any time and expect a reply within 1 business day. We don't offer phone support.


### q009 [simple] Laya P(complex)=0.555

**Customer:** do u have a phone number i can call

**Cheap model** (quality 5, $0.0017):

We don't have phone support, I'm afraid. Here's how to reach us instead:

- **Chat:** 8am–8pm Mon–Sat (your local time)
- **Email:** help@leafy.example (answered within 1 business day)
- **Plant Care Specialists:** chat 9am–5pm Mon–Fri for plant advice

What can I help you with today?

**Strong model** (quality 5, $0.0045):

We don't offer phone support, but there are other ways to reach us:

- **Chat:** 8am-8pm Mon-Sat (your local time)
- **Email:** help@leafy.example, answered within 1 business day
- **Plant Care Specialists:** chat only, 9am-5pm Mon-Fri (your local time)

Is there something I can help you with right now?
