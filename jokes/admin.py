from django.contrib import admin

from .models import Category, Joke, JokeVote, Tag
from common.admin import DjangoJokesAdmin


@admin.register(Category)
class CategoryAdmin(DjangoJokesAdmin):
    model = Category
    list_display = ['category', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return ()

@admin.register(Joke)
class JokeAdmin(DjangoJokesAdmin):
    model = Joke

    # Form Attributes
    autocomplete_fields = ['tags', 'user']
    radio_fields = { 'category': admin.HORIZONTAL}

    # List Attributes
    list_display = ['question', 'created', 'updated']
    search_fields = ['question', 'answer']
    ordering = ['-updated']
    list_filter = ['updated', 'category', 'tags']
    date_hierarchy = 'updated'

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated', 'vote_summary')
        return ()

    def vote_summary(self, obj):
        return f'{obj.num_votes} votes. Rating: {obj.rating}.'


@admin.register(Tag)
class TagAdmin(DjangoJokesAdmin):
    model = Tag
    list_display = ['tag', 'created', 'updated']
    search_fields = ['tag']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return ()

@admin.register(JokeVote)
class JokeVoteAdmin(DjangoJokesAdmin):
    model = JokeVote
    list_display = ['joke', 'user', 'vote']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created', 'updated')
        return ()
