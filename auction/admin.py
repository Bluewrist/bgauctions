from django.contrib import admin
from.models import *
# Register your models here.
admin.site.site_header = "BG Auctions Admindashboard"
admin.site.register(Product)
admin.site.register(Product_img)
admin.site.register(Bidder)
admin.site.register(Bidds)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Auction_details)
admin.site.register(Registration)
admin.site.register(Onsale)



