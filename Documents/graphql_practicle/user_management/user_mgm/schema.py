from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
import graphene
from user_mgm.helper import encrypt_data, decrypt_data


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "password", "first_name", "email")

    username = graphene.String(
        resolver=lambda my_obj, resolve_obj: decrypt_data(my_obj.username)
    )
    first_name = graphene.String(
        resolver=lambda my_obj, resolve_obj: decrypt_data(my_obj.first_name)
    )
    email = graphene.String(
        resolver=lambda my_obj, resolve_obj: decrypt_data(my_obj.email)
    )
    id = graphene.ID()


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        return User.objects.all()


class UserMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        password = graphene.String()
        email = graphene.String()
        username = graphene.String()

    first_name = graphene.String()
    password = graphene.String()
    email = graphene.String()
    username = graphene.String()

    @classmethod
    def mutate(cls, root, info, first_name, password, email, username):
        user = User(
            first_name=encrypt_data(first_name),
            email=encrypt_data(email),
            username=encrypt_data(username),
        )
        user.set_password(password)
        user.save()


class UpdateUserMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        password = graphene.String()
        email = graphene.String()
        username = graphene.String()
        id = graphene.Int()

    first_name = graphene.String()
    password = graphene.String()
    email = graphene.String()
    username = graphene.String()
    id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, first_name, password, email, username, id):
        user = User.objects.get(id=id)
        print("--------------->>>>>>>>>>user: ", user)
        user.first_name = encrypt_data(first_name)
        user.password = encrypt_data(password)
        user.email = encrypt_data(email)
        user.username = encrypt_data(username)
        if user and password:
            user.set_password(password)
        user.save()


class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id):
        user = User.objects.get(id=id)
        #########Delete##############
        print("--------------->>>>>>>>>>user delete: ", user)
        user.delete()


class Mutation(graphene.ObjectType):
    # keywords that will be used to do the mutation in the frontend
    create_user = UserMutation.Field()
    update_user = UpdateUserMutation.Field()  # new
    delete_user = DeleteUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
