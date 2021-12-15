from django.db import models

class DisplayClass(models.Model):
    disp_id = models.AutoField('disp_id', primary_key=True)
    room_number = models.CharField(max_length=50)
    square = models.IntegerField(verbose_name='Square')
    def __str__(self):
        return f'{self.room_number}{self.square}'

class Computer(models.Model):
    comp_id = models.AutoField('comp_id', primary_key=True)
    cpu = models.CharField(max_length=80,verbose_name='CPU')
    graphic_card = models.CharField(max_length=80, verbose_name='Graphic Card')
    disp_id = models.ForeignKey('DisplayClass', models.DO_NOTHING, db_column='disp_id', verbose_name='Display Class')


    