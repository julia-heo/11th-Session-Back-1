from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):   # 각 모델들의 직렬화 역질렬화를 연결
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    # id = serializers.IntegerField(read_only = True)
    # title = serializers.CharField(required = False, allow_blank = True, max_length = 100)
    # code = serializers.CharField(style = {'base_template':'textarea.html'})     # textarea는 기본적으로 제공하는 text를 위한 ~~..오
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default = 'python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default = 'friendly')

    # 코드 때문..
    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)            # 'title'에 새로 들어오는 데이터가 없으면 이미 가지고 있는 instance.title를 사용함 (즉, 기존 데이터 유지)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance