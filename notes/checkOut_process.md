#Checkout Process

1. Cart --> Checkout view
    ?
    - Login or Enter an Email (as Guest)
    - Shopping Address
    - Billing Info
        - Billing Address
        - Credit Card / Payment

2. Billing App/Component
    - Billing Profolie
        - User or Email (Guest Email)
        - Generate Payment Processor Token (Stripe or Braintee)

3. Order / Invoices Component
    - Connecting the Billing Profile
    - Shipping / Billing Address
    - Cart
    - Status -- Shipped? Cancelled?