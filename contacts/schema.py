import graphene
from graphene_django import DjangoObjectType
from .models import Contacts


class ContactsType(DjangoObjectType):
    class Meta:
        model = Contacts
        fields = ("id", "name", "email", "phone")

class Query(graphene.ObjectType):

    all_contacts = graphene.List(ContactsType)
    def resolve_all_contacts(root, info):
        try:
            return Contacts.objects.all()
        except Contacts.DoesNotExist:
            return None

    details_contact = graphene.Field(ContactsType, id=graphene.Int())
    def resolve_details_contact(root, info, id):
        try:
            return Contacts.objects.get(pk=id)
        except Contacts.DoesNotExist:
            return None

    search_contact = graphene.Field(ContactsType, name=graphene.String())
    def resolve_search_contact(root, info, name):
        try:
            return Contacts.objects.get(name=name)
        except Contacts.DoesNotExist:
            return None

#Create data
class ContactCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        
    contact = graphene.Field(ContactsType)

    @classmethod
    def mutate(cls, root, info, name, email, phone):
        contact = Contacts(name=name, email=email, phone=phone)
        contact.save()
        return ContactCreate(contact=contact)

#Update data
class ContactUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        
    contact = graphene.Field(ContactsType)

    @classmethod
    def mutate(cls, root, info, id, name, email, phone):
        try:
            contact = Contacts.objects.get(id=id)
            contact.name = name
            contact.email = email
            contact.phone = phone
            contact.save()
            return ContactUpdate(contact=contact)
        except Contacts.DoesNotExist:
            return None

#Delete data
class ContactDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        
    contact = graphene.Field(ContactsType)

    @classmethod
    def mutate(cls, root, info, id):
        try:
            contact = Contacts.objects.get(id=id)
            contact.delete()
            return None
        except Contacts.DoesNotExist:
            return None

class Mutation(graphene.ObjectType):
    create_contact = ContactCreate.Field()
    update_contact = ContactUpdate.Field()
    delete_contact = ContactDelete.Field()

# schema = graphene.Schema(query=Query, mutation=Mutation)