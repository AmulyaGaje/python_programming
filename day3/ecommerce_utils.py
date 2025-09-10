def apply_discount(price,per):
    final=price-((per/100)*price)
    return final
def gst(price,gst_per=18):
    final=price+(0.18*price)
    return final
def generate_invoice(cart,per=10,gst_per=18):
    print("--------INVOICE---------")
    for i in cart.keys():
        print(i,"    :",cart[i])
    print("----------------")
    total=0
    for i in cart.values():
        total+=i
    print("Subtotal",total)
    print("After 10% discount: Rs",apply_discount(total,10))
    print("Ater 18% GST :Rs",gst(total))
    print("-----------------------------------------")
    print("TRhank you for shopping with us!!")