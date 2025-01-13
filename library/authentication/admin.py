from django.contrib import admin

from book.models import Book
from author.models import Author
from order.models import Order
from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'role')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'count', 'get_authors') 
    list_filter = ('id', 'name', 'authors') 
    search_fields = ('id', 'name', 'authors__name')
    list_editable = ('name', 'description')
    list_per_page = 20
    
    def get_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])
    get_authors.short_description = 'Authors'

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'count')
        }),
    )


class BookInline(admin.TabularInline):
    model = Book.authors.through  
    extra = 1 

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'get_books')
    list_filter = ('name', 'books')
    search_fields = ('name',)
    list_editable = ('surname', 'patronymic')
    list_per_page = 20
    def get_books(self, obj):
        return ", ".join([book.name for book in obj.books.all()])
    get_books.short_description = 'Books'

    def get_books(self, obj):
        return ", ".join([book.name for book in obj.books.all()])
    get_books.short_description = 'Books'
    inlines = [BookInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'surname', 'patronymic')
        }),
        ('Books', {
            'fields': ('books',) 
        }),
    )
    filter_horizontal = ('books',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'created_at', 'end_at')
    list_filter = ('book', 'user', 'created_at', 'end_at')
    search_fields = ('book', 'user', 'created_at', 'end_at')
    list_editable = ('end_at',)
    
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Order, OrderAdmin)
