# Judge hand-check: 20 answers stratified by judge score

For each: do you agree with the score? Claude's own review is in the 'Claude check' line.


## 1. q056 - judge score 1 (C1/Co1/P3/T4) - sonnet_low, claude-sonnet-5-5

**Customer:** whats ur price adjustment policy

**Reference:** If an item's price drops within 7 days of purchase, you can request the difference as store credit once per item; this excludes flash sales and clearance items.

**Answer:**

I don't have a price adjustment policy in the information available to me, so I can't say whether Leafy refunds the difference if a price drops after you order. I don't want to guess and give you the wrong answer.

If you tell me your order number (it looks like LF- plus six digits), I can pass the question to a Support Lead. You can also email help@leafy.example, which is answered within 1 business day.

If you haven't ordered yet, or ordered within the last 2 hours, you can change or cancel the order for free from "My Orders".

**Judge note:** Says no policy; wrong.

**Claude check:** AGREE. The price-adjustment policy exists (s6) but wasn't retrieved, so the answer gives the customer nothing. It's honest, not invented, so arguably a 2, but 1 is defensible.


## 2. c09.t3 - judge score 1 (C1/Co2/P2/T3) - v2_full, claude-sonnet-5-5

**Customer:** My order was supposed to arrive last week and tracking hasn't changed since Monday. / It's been 6 business days now. / What happens if they can't find it?

**Reference:** If the courier confirms it's lost, you get a free replacement or a full refund, your choice.

**Answer:**

I need to correct my earlier messages. The 4-business-day threshold, the 5-business-day investigation, and the replacement-or-refund outcome aren't in the policy information I have, so I shouldn't have stated them as fact. I'm sorry for the confusion, especially after this long a wait.

I can't confirm what happens if the courier can't find your package. If a refund is issued, it goes to your original payment method, and card refunds take 5-10 business days after issue (digital wallets 3-5 business days). Store credit is instant.

I'd recommend escalating this to a Support Lead, who can confirm your options. If you'd like that, please send your order number (LF- plus six digits).

**Judge note:** Wrongly retracts correct KB facts, claiming they are not in policy, and fails to answer the question.

**Claude check:** AGREE. With a trimmed history and a retrieval miss on Shipping, the bot retracted facts it had stated correctly earlier. It's a genuine failure.


## 3. q056 - judge score 1 (C1/Co1/P3/T4) - sonnet_medium, claude-sonnet-5-5

**Customer:** whats ur price adjustment policy

**Reference:** If an item's price drops within 7 days of purchase, you can request the difference as store credit once per item; this excludes flash sales and clearance items.

**Answer:**

I don't have a price adjustment policy in the information available to me, so I can't say whether Leafy offers price adjustments or what the conditions or timeframes would be. I don't want to guess and give you wrong details.

If you're asking about a specific order, I can escalate it, or you can email help@leafy.example (answered within 1 business day) or use chat 8am-8pm Mon-Sat. Would you like me to escalate?

**Judge note:** Says no policy; wrong.

**Claude check:** AGREE. Same retrieval miss as #1.


## 4. q037 - judge score 1 (C1/Co2/P4/T3) - rt_cheap, claude-haiku-4-5-20251001

**Customer:** My Leafy Plus renewed 5 days ago and I haven't ordered anything since. If I cancel now, do I get the $59 back?

**Reference:** Yes. Cancelling within 14 days of renewal with no member benefits used gives a full refund.

**Answer:**

No, you won't get a refund. The **14-day refund window** for Leafy Plus requires that you cancel **and** haven't used any benefits. Since your renewal was 5 days ago, you're still within the 14 days, but if you've used any benefits (like free Standard shipping, free returns, the 90-day guarantee, member pricing, or early access), the refund is forfeited.

Have you used any of those benefits since renewal?

**Judge note:** Says No, contradicting the reference.

**Claude check:** AGREE. The customer says they have ordered nothing, so no benefits have been used and the refund is yes. Haiku opens with 'No'.


## 5. q078 - judge score 2 (C2/Co2/P3/T4) - sonnet_high, claude-sonnet-5-5

**Customer:** I ordered a peperomia but got a pothos instead

**Reference:** We ship the correct plant free by Express where the zone allows, and for a wrong live plant you may keep the wrong plant at no charge.

**Answer:**

I'm sorry about the mix-up, that's not what you ordered. The policy information I have doesn't cover wrong-item deliveries, so I can't promise a specific fix or timeframe, but I can escalate this to a Support Lead. If you send your order number (LF- followed by six digits), I'll include it in the escalation.

If you have pets, keep the pothos out of their reach for now. It isn't pet-safe, whereas peperomia is. If anyone does chew on it, contact a vet or poison control right away.

**Judge note:** Says KB doesn't cover wrong items; it does. Misses the Express correct plant and keep the pothos.

**Claude check:** AGREE. The wrong-item section wasn't retrieved, so the answer misses the free Express correct item and 'keep the wrong plant'.


## 6. q087 - judge score 2 (C3/Co3/P4/T4) - plus_retrieve, claude-sonnet-5-5

**Customer:** i paid with the pay in instalments option and returned a pot. where does my refund go?

**Reference:** Buy-now-pay-later refunds go back to the instalment provider, which adjusts your remaining payments.

**Answer:**

Hi there, and thanks for contacting Leafy! 🌿

Refunds go back to your **original payment method**, so your refund should be returned via the pay in instalments option you used at checkout. We issue it within **5 business days** of your returned pot reaching our warehouse.

- If the return was a change of mind, a flat **$6.95** return fee is deducted from the refund (free for Leafy Plus members). Faulty or incorrect items return free.
- Original shipping is only refunded if the whole order was returned because of our error.

Our knowledge base doesn't cover how an instalment provider adjusts your remaining payments or schedule once a refund arrives, so I can't say exactly how it will show up on your plan. Your instalment provider can confirm that. If you'd like, I can escalate this to a Support Lead to look into it for you.

If your refund hasn't appeared within 5 business days of the pot reaching our warehouse, just reach out again and we'll help. Happy planting! 🪴

**Judge note:** Claims KB doesn't cover provider adjustment; it does.

**Claude check:** POSSIBLY HARSH (+1). The main point (the refund goes back via the instalment option) is right, and only the provider-adjustment detail is missing. I'd score it 3.


## 7. q078 - judge score 2 (C2/Co2/P3/T4) - sonnet_low, claude-sonnet-5-5

**Customer:** I ordered a peperomia but got a pothos instead

**Reference:** We ship the correct plant free by Express where the zone allows, and for a wrong live plant you may keep the wrong plant at no charge.

**Answer:**

I'm sorry about the mix-up, especially when you wanted a peperomia. The policy information I have doesn't cover wrong items being sent, so I can't promise a specific fix or timeframe. I can escalate this to a Support Lead if you share your order number (it looks like LF-123456) and, if you can, a photo of the plant you received.

One safety note: pothos is not pet-safe, whereas peperomia is. If you have pets, please keep the plant out of their reach until this is sorted.

**Judge note:** Wrongly claims no wrong-item policy.

**Claude check:** AGREE. Same retrieval miss as #5.


## 8. q092 - judge score 2 (C3/Co2/P2/T3) - rt_cheap_rep2, claude-haiku-4-5-20251001

**Customer:** This is the THIRD time I'm writing about my dead fiddle leaf fig and nobody has fixed it. I want my money back NOW and I'm cancelling Leafy Plus.

**Reference:** Apologise and escalate to a Support Lead, since the issue has been raised three or more times. Up to $15 goodwill store credit may be offered. Leafy Plus can be cancelled any time, but a refund is only given within 14 days of purchase or renewal with no benefits used; otherwise benefits continue to the end of the paid year.

**Answer:**

I hear your frustration—I'm sorry you've had this experience. I need to help you properly, so let me check: **did you submit a Plant Care Guarantee claim through "My Orders" with photos within 30 days of delivery?** (Or 90 days if your Leafy Plus membership was active when you ordered?)

The reason I ask: our policy doesn't allow refunds for live plants, but they're covered by the guarantee, which provides a free replacement. If your claim wasn't reviewed yet or was denied, that's something I can escalate to a Support Lead right now to investigate why you haven't received a resolution after three attempts.

What's your order number, and when did the plant arrive?

**Judge note:** Conditional escalation, ignores Plus cancellation.

**Claude check:** AGREE. It doesn't escalate despite this being the third contact (policy requires it) and ignores the Plus cancellation question.


## 9. q076 - judge score 3 (C3/Co4/P4/T4) - v2_full, claude-haiku-4-5-20251001

**Customer:** I'm a Plus member placing a $60 order with express. What will shipping cost?

**Reference:** Express shipping costs $14.95; Leafy Plus does not include free Express shipping.

**Answer:**

Express shipping will cost **$14.95**.

Leafy Plus gives you free *Standard* shipping with no minimum order, but Express shipping is never free—even for Plus members. Your $60 order doesn't qualify for free Standard shipping anyway since it's under the $75 threshold.

**Judge note:** The $14.95 is correct. It wrongly claims the $60 order doesn't qualify for free Standard, but Plus has no minimum.

**Claude check:** AGREE. The $14.95 is right, but it states a wrong fact: that the Plus member's $60 order wouldn't get free Standard shipping.


## 10. q095 - judge score 3 (C4/Co3/P2/T4) - sonnet_high, claude-sonnet-5-5

**Customer:** My toddler just chewed a leaf off the peace lily that arrived today, and the pot was smashed in the box too.

**Reference:** First, contact a doctor or local poison control service immediately; the peace lily is not pet-safe. The case is escalated to a Support Lead. The smashed pot is damaged on arrival: report within 48 hours with photos of the item and box for a replacement or refund.

**Answer:**

Please contact poison control or your doctor right now, and keep the peace lily well out of your toddler's reach. Tell them it's a peace lily and that your child chewed a leaf. Our policy excerpts don't cover medical advice, so they're the right people to guide you.

Once your child is looked after, a smashed pot counts as damaged on arrival. Please report it within **48 hours** of delivery, with photos of the plant and the box. We'll then send a free replacement on the next plant shipping day, or give you a refund. The replacement won't use up your Plant Care Guarantee replacement.

If you'd like a replacement, bear in mind that peace lilies are not pet-safe, and you may prefer a different plant while you have a toddler at home.

**Judge note:** Safety first but no escalation.

**Claude check:** RUBRIC INCONSISTENCY. The judge gave policy=2 (the safety escalation is missing) but overall=3, while its own rubric caps any policy breach at 2. I'd score it 2.


## 11. q059 - judge score 3 (C3/Co4/P4/T4) - plus_route, claude-haiku-4-5-20251001

**Customer:** can i return an opened bag of soil

**Reference:** No. Opened bags of soil or fertiliser cannot be returned unless they were faulty.

**Answer:**

# Hi there! 👋

Thanks for reaching out to Leafy! I'm happy to help with your question about the soil.

**Unfortunately, opened soil cannot be returned** — even within our standard 30-day return window. We can only accept returns on soil and fertiliser if they're **unopened and in original packaging**, or if there's a fault with the product.

That said, if there's a **problem with the soil itself** (like it arrived damaged, mouldy, or with a defect), I'd love to help! Just let me know what's wrong with it, and we can look into that for you.

Is everything okay with your soil, or were you just looking to return it for another reason? I'm here to help! 🌱

**Judge note:** Main point correct, but wrongly implies unopened is the only condition.

**Claude check:** DISAGREE (judge harsh by 1). The answer does state the faulty-item exception, and 'unopened and in original packaging' matches the KB. Tone is over-enthusiastic but fine. I'd score it 4.


## 12. q097 - judge score 3 (C4/Co3/P3/T4) - plus_tight_cache, claude-sonnet-5-5

**Customer:** I waived the weather hold because I needed the plant for an event and it arrived frozen and black. I want a free replacement.

**Reference:** Because the weather hold was waived, damaged-on-arrival claims for cold damage are not accepted and cold damage in transit is excluded from the Plant Care Guarantee, so a free replacement cannot be promised. If the customer insists, escalate to a Support Lead; a goodwill credit of up to $15 is possible.

**Answer:**

I'm sorry, that's a frustrating thing to happen, especially when you needed the plant for an event.

Unfortunately, I can't offer a free replacement in this case. When a customer waives the weather hold, our policy says:

- The Plant Care Guarantee still applies, **except for cold or heat damage in transit**.
- DOA claims for cold or heat damage are **not accepted**.

Since the plant arrived frozen from cold in transit after the hold was waived, it falls under that exclusion, both as a DOA claim and as a Plant Care Guarantee claim.

The policy excerpts I have don't list any other exceptions or goodwill options for this situation. If you'd like, I can escalate your case to a Support Lead so they can review it, but I can't promise a particular outcome.

Going forward, the weather hold can delay live plants for up to 7 days when transit forecasts are below 35°F or above 95°F. In winter, a free heat pack can be added at checkout.

Would you like me to escalate this to a Support Lead?

**Judge note:** Says no goodwill options exist, which is wrong ($15 goodwill allowed). Escalation offered.

**Claude check:** AGREE. It misses the $15 goodwill option (Contact section not retrieved) but correctly refuses the replacement and offers escalation.


## 13. q091 - judge score 4 (C4/Co4/P4/T4) - rt_strong_rep2, claude-sonnet-5-5

**Customer:** My monstera arrived with yellow leaves, I was charged twice, and I want the refund on a different card.

**Reference:** Yellow leaves: minor yellowing is normal; if it is damage report within 48 hours with photos, otherwise use the 30-day Plant Care Guarantee. Double charge: check whether one is a pending authorisation; if both have posted, send the order number and card's last four digits and the duplicate is refunded within 3 business days of confirmation. Refunds can only go to the original payment method, not a different card; store credit is an alternative, and a Support Lead can be looped in if needed.

**Answer:**

Sorry your monstera arrived looking unwell. Here's where each issue stands:

- **Yellow leaves:** Report within **48 hours** of delivery, with photos of the plant and the box. Damaged on Arrival covers dead or severely wilted plants, snapped main stems, exposed roots or a cracked pot. Yellowing alone isn't listed, so I can't promise it qualifies. A qualifying plant gets a free replacement on the next plant shipping day, or a refund. After 48 hours it goes through the Plant Care Guarantee, whose details I don't have here, so I can escalate that to a Support Lead.
- **Double charge:** First check whether one is a pending authorisation, or whether your order shipped in several parcels, since each parcel can show its own charge. If both charges have posted, send me your order number and the **last four digits** of the card (never the full number or security code). The duplicate is refunded within **3 business days** of confirmation.
- **Refund to a different card:** I can't do that. Refunds go only to the original payment method. Card refunds take **5-10 business days** once issued. If you'd rather not wait, you can take Leafy store credit, which is instant and never expires.

Would you like to send those order details, or should I escalate the plant issue?

**Judge note:** Claims no guarantee details; otherwise correct.

**Claude check:** AGREE. Double charge and card refund are correct; the Guarantee detail is missing due to a retrieval miss.


## 14. c09.t4 - judge score 4 (C5/Co5/P4/T5) - v1_naive, claude-sonnet-5-5

**Customer:** My order was supposed to arrive last week and tracking hasn't changed since Monday. / It's been 6 business days now. / What happens if they can't find it? / I'd take the replacement. Would that one ship express?

**Reference:** The policy says lost parcels get a free replacement, but it does not specify Express shipping for the replacement, so this can't be promised; support can confirm.

**Answer:**

Great, a replacement it is! Thank you for your patience through all this.

I don't have anything confirming that a lost-parcel replacement ships Express, so I can't promise it. Here is what I can tell you:

- **Standard shipping times** depend on your zone: 2-3 business days (Zone 1), 3-5 (Zone 2), or 5-8 (Zone 3).
- **Express** is normally $14.95 and is never free. It takes next business day (Zone 1) or 2 business days (Zone 2), and isn't available in Zone 3.
- **Live plants ship Monday to Wednesday only**, so that affects when a replacement could go out.

I can ask a Support Lead whether your replacement can be sent Express, and I'll note your request when I open the investigation. I can't say what they'll decide, and I don't want to promise something I can't confirm.

**What I need from you**
- Your **order number** (LF- followed by six digits), found in "My Orders" or your confirmation email.

Once I have it, the courier investigation takes up to **5 business days**. If the parcel is confirmed lost, we'll arrange your replacement. Your **$15 store credit** for the delay is still available too.

Thanks again, and please reach out any time!

**Judge note:** Good Express answer. The $15 credit is presented as already offered, a minor issue.

**Claude check:** AGREE. Correctly won't promise Express. The '$15 credit' refers back to this conversation's own earlier offer.


## 15. c01.t2 - judge score 4 (C4/Co5/P4/T4) - v1_naive, claude-sonnet-5-5

**Customer:** Hi, my rubber plant was delivered this morning and the pot is cracked. / ok where do I send the photos?

**Reference:** Send them to support by chat or at help@leafy.example within 48 hours of delivery: photos of the cracked pot and of the box it arrived in.

**Answer:**

Happy to help! The quickest way to send your photos is by email:

- **Email:** help@leafy.example
- Include your **order number** (LF- plus six digits).
- Attach photos of **the plant, the cracked pot, and the box it arrived in**.
- Mention whether you'd like a **replacement or a refund**.

You can also start the report from **"My Orders"** on the website or app. I can't confirm that photos can be uploaded in this chat, so please use email or "My Orders" to make sure they reach the team.

Your report needs to be in **within 48 hours of delivery**, so please send it today. Emails are answered within **1 business day**.

If you choose a replacement, it ships on the next plant shipping day (live plants ship Monday to Wednesday).

Thanks for your patience, and I'm sorry again about the cracked pot. Reach out any time if you need anything else, and I hope your new rubber plant is thriving soon! 🌿

**Judge note:** Gives the email address and the 48h deadline. 'My Orders' is hedged and not confirmed by the KB for DOA.

**Claude check:** AGREE.


## 16. c04.t3 - judge score 4 (C4/Co5/P5/T4) - plus_retrieve, claude-sonnet-5-5

**Customer:** Hi! I live about 1,500 miles from your nearest greenhouse. How long would delivery take? / Hmm. Could I pay extra to get it faster? / What if the plant I want is one of the XL ones?

**Reference:** XL plants ship Standard only anyway and add a $20 handling fee on top of shipping.

**Answer:**

Good question! XL plants (usually over 4 ft) work a little differently, so here's what to know:

- **Standard shipping only.** XL plants can't go Express, but that doesn't change anything for you, since Express isn't available in Zone 3 anyway. Your delivery time would be **5–8 business days**.
- **$20 handling fee.** This is added on top of the shipping cost for each XL plant.
- **Free shipping still applies.** If your order is **$75 or more** (after discounts, before tax), Standard shipping is free. The $20 XL handling fee is separate, so I can't say it gets waived. If you'd like to double-check how it shows on your order, the total at checkout will give you the full picture.
- **Shipping days are the same.** Live plants ship **Monday-Wednesday only**, and orders placed after 12 noon Wednesday ship the following Monday.

Weather holds also apply to XL plants. If transit forecasts are below 35°F or above 95°F, your plant may be held up to **7 days**, and we'll email you.

Is there a particular plant you're eyeing? I'm happy to help with any other questions before you order! 🌿

**Judge note:** Correct; 'each XL plant' assumed, slight hedging.

**Claude check:** AGREE (could be 5).


## 17. q058 - judge score 5 (C5/Co5/P5/T5) - v2_full, claude-sonnet-5-5

**Customer:** what happens if it's freezing where I live when my plant ships

**Reference:** If the forecast is below 35F or above 95F during transit, live plants may be put on a weather hold for up to 7 days, and the customer is emailed.

**Answer:**

If the transit forecast is below 35°F, we may hold your plant for up to 7 days, and we'll email you when that happens. You can reply to waive the hold and have it ship anyway. The Plant Care Guarantee still applies then, but cold or heat damage in transit is excluded, and DOA claims for cold damage aren't accepted.

In winter you can also add a free heat pack at checkout.

**Judge note:** Concise and accurate.

**Claude check:** AGREE.


## 18. q095 - judge score 5 (C5/Co5/P5/T5) - plus_retrieve, claude-sonnet-5-5

**Customer:** My toddler just chewed a leaf off the peace lily that arrived today, and the pot was smashed in the box too.

**Reference:** First, contact a doctor or local poison control service immediately; the peace lily is not pet-safe. The case is escalated to a Support Lead. The smashed pot is damaged on arrival: report within 48 hours with photos of the item and box for a replacement or refund.

**Answer:**

Hi, and thank you for contacting Leafy. I'm so sorry this happened. That sounds scary, and the first priority is your little one.

**Please do this right now:**
- Contact your doctor or poison control immediately and tell them your toddler chewed part of a peace lily leaf. They can tell you exactly what to watch for and what to do.
- Keep the plant, and any bits of leaf or soil, well out of reach of your toddler (and any pets, as peace lilies aren't pet-safe).
- If your toddler seems unwell or has trouble breathing, call your local emergency number straight away.

**Escalation:** Because this is a safety issue, I'm escalating your case to a Support Lead so a person on our team can follow up with you. I don't have an exact timeframe for their reply, so I don't want to guess, but they'll have the details of what you've told me.

**The smashed pot:** A smashed pot counts as damaged on arrival, so you're covered. Once your toddler is taken care of, here's what to do:
- Report it within **48 hours** of delivery. Since the plant arrived today, you have time.
- Include photos of the plant and the box.
- You can choose a **free replacement** on the next plant shipping day, or a **refund**.

There's no rush on the photos while you're sorting out your toddler. Please take care of them first.

I hope your little one is totally fine. Please reach out any time if you need anything else.

**Judge note:** Safety first, escalation, DOA details all correct.

**Claude check:** AGREE.


## 19. q024 - judge score 5 (C5/Co4/P5/T5) - rt_cheap, claude-haiku-4-5-20251001

**Customer:** is express available for island addresses

**Reference:** No. Island and remote addresses are Zone 3, where Express delivery is not available.

**Answer:**

No, Express shipping is **not available** for island addresses. 

Island addresses fall into **Zone 3** (over 1,000 miles), which only offers **Standard shipping (5–8 business days)** at $7.95, or free on orders of $75+.

**Judge note:** Correct and brief.

**Claude check:** AGREE.


## 20. q100 - judge score 5 (C5/Co4/P5/T4) - sonnet_medium, claude-sonnet-5-5

**Customer:** so we're moving house next week, and the order I sent as a gift to my dad just shipped to my OLD address by mistake - can you redirect it to his place? he's on an island so maybe use express this time?

**Reference:** Address changes after an order has shipped are not possible, and couriers do not accept redirection requests. Express is also not available to island addresses (Zone 3). Escalate to a Support Lead if the customer needs more help.

**Answer:**

I'm sorry about the mix-up. Once an order has shipped, the address can't be changed and couriers don't accept redirection requests from Leafy, so I can't redirect this one to your dad's place. Express also isn't available for island addresses (Zone 3), so a new order to him would ship Standard only, in 5-8 business days. Live plants ship Monday to Wednesday only, and standard shipping is $7.95, or free on orders of $75+.

The policy I have doesn't say whether a shipped order can be returned or refunded after a wrong-address error. If you'd like, I can escalate to a Support Lead to look at options for the original order. Please send me the order number (LF-plus six digits).

**Judge note:** Accurate and concise.

**Claude check:** AGREE.


---
**Claude's summary:** 17/20 agree; 3 questionable, each by at most 1 point (#6 harsh, #10 breaks the judge's own rubric cap, #11 wrong). No score is off by 2+. Most low scores are retrieval misses where the model honestly said it lacked the policy (q056, q078, q087 match the hybrid-retrieval recall misses measured before the run).
