from django.contrib import admin
from.models import Book,Category,Student,OrderItem,Order,Cart
# Register your models here.

class bookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'is_publisher', 'created_at')
    list_display_links = ('id','title')
    list_filter = ('author','created_at')
    list_editable = ('is_publisher',)
    search_fields = ('title','author')

admin.site.register(Book, bookAdmin)
admin.site.register(Category)
admin.site.register(Student)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Cart)