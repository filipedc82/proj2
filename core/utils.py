from products import models as pmodels

def createTestProduct(product_no = ""):
    """
    Create a Test Product with
    :param product_no:
    :return product:
    """

    p = pmodels.Product()
    if product_no == "":
       p.product_no = "Guide" + str(pmodels.Product.objects.count())
    else:
        p.product_no = product_no
    p.save()
    # if standard_alias_no == "":
    #     pa = createTestAlias(p, "Guide"+str(p.id)+"std")
    # else:
    #     pa= createTestAlias(p, standard_alias_no)
    #
    # p.standard_alias = pa
    p.product_group = "VG"
    p.oem = "MAK"
    p.engine = "M32"
    p.save()
    return p

def createTestAlias(product = "", product_no = ""):
    pa = pmodels.ProductAlias()
    if product == "":
        pa.product = createTestProduct()
    else:
        pa.product = product
    pa.vendor = "Vendor"+str(pmodels.ProductAlias.objects.count())
    if product_no == "":
        pa.product_no = pa.vendor+ "Guide"+str(pa.product_id)
    else:
        pa.product_no = product_no
    pa.save()
    return pa

def createTestDrawing(product_alias = ""):
    d = pmodels.Drawing()
    if product_alias == "":
        d.product_alias = createTestAlias()
    else:
        d.product_alias = product_alias

    d.drawing_no = "Drwg" + str(pmodels.Drawing.objects.count())
    d.status = "A"
    d.save()
    return d