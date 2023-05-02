from django.db import models

class Posting(models.Model):
    title = models.CharField('Title', max_length=50, blank=True) 
		#필드이름 =    문자열로구성('admin에서 표현되는 방식', 최대글자수, 빈상태허용)
    upload_time = models.DateTimeField(unique=True)
		#필드이름 =          날짜시간으로구성( 필드값중복X )
    content = models.TextField('Content')
		#필드이름 =        문자열로구성('admin에서 표현되는 방식')

    def __str__(self):        
		#__str__ : 해당 클래스로 만들어진 객체 출력할 때 문자열로 설명하기 위한 함수
							#models.py의 class가 admin페이지에서 어떻게 출력될지를 정의
        return self.title