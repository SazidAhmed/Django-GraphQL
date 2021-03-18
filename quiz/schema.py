import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes, Category, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id","title","category")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question","answer_text")

#To Query Data
class Query(graphene.ObjectType):

    # quiz = graphene.String()
    # def resolve_quiz(root, info):
    #     return f"this is the first question"
    

    # all_quizzes = DjangoListField(QuizzesType)
    # all_quizzes = graphene.List(QuizzesType)
    # def resolve_all_quizzes(root, info):
        # return Quizzes.objects.filter(id=1)


    # all_quizzes = graphene.List(QuizzesType)
    # all_questions = graphene.List(QuestionType)
    # def resolve_all_quizzes(root, info):
    #     return Quizzes.objects.all()
    # def resolve_all_questions(root, info):
    #     return Question.objects.all()


    # all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())
    # def resolve_all_quizzes(root, info, id):
    #     return Quizzes.objects.get(pk=id)

    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)

# Mutation

#Create data
class CategoryMutation(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryMutation(category=category)

#Update data
# class CategoryMutation(graphene.Mutation):

#     class Arguments:
#         id = graphene.ID()
#         name = graphene.String(required=True)
        
#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info, name, id):
#         category = Category.objects.get(id=id)
#         category.name = name
#         category.save()
#         return CategoryMutation(category=category)

#Delete data
# class CategoryMutation(graphene.Mutation):

#     class Arguments:
#         id = graphene.ID()
        
#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info, id):
#         category = Category.objects.get(id=id)
#         category.delete()

class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


