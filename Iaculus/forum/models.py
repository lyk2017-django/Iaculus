"""
                             . .  ,  ,
                              |` \/ \/ \,',
                              ;          ` \/\,.
                             :               ` \,/
                             |                  /
                             ;                 :
                            :                  ;
                            |      ,---.      /
                           :     ,'     `,-._ \
                           ;    (   o    \   `'
                         _:      .      ,'  o ;
                        /,.`      `.__,'`-.__,
                        \_  _               \
                       ,'  / `,          `.,'
                 ___,'`-._ \_/ `,._        ;
              __;_,'      `-.`-'./ `--.____)
           ,-'           _,--\^-'
         ,:_____      ,-'     \
        (,'     `--.  \;-._    ;
        :    Y      `-/    `,  :
        :    :       :     /_;'
        :    :       |    :
         \    \      :    :
          `-._ `-.__, \    `.
             \   \  `. \     `.
           ,-;    \---)_\ ,','/
           \_ `---'--'" ,'^-;'
           (_`     ---'" ,-')
           / `--.__,. ,-'    \
           )-.__,-- ||___,--' `-.
          /._______,|__________,'\
          `--.____,'|_________,-'


"""


from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Topic(models.Model):
    title = models.CharField(max_length=200)
    forum = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(blank=True, default=False)

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic)
    body = models.TextField()