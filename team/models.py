from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

@python_2_unicode_compatible
class Company_info(models.Model):
    company_Num = models.IntegerField(primary_key=True)
    company_Name = models.CharField(max_length=20, blank = False)
    company_Scale = models.CharField( max_length=20, blank = False)
    jobCode = models.IntegerField(default=0)

    def __str__(self):
        return self.company_Name

class Company_select(models.Model):
    comp_selNum	 = models.IntegerField(primary_key=True)
    mem_Num	= models.ForeignKey('Member_info', on_delete=models.CASCADE)
    company_Num	= models.ForeignKey('Company_info', on_delete=models.CASCADE)

class Interview_apply(models.Model):
    inter_apply_num	= models.IntegerField(primary_key=True)
    interv_sNum	= models.ForeignKey('Company_select', on_delete=models.CASCADE)
    comp_selNum	= models.ForeignKey('Interview_state', on_delete=models.CASCADE)
    emplo_fNum	= models.ForeignKey('Employee_form', on_delete=models.CASCADE)
    work = models.CharField(max_length=50, blank = False)

class Interview_state(models.Model):
    interv_sNum	= models.IntegerField(primary_key=True)
    intervS_info = models.CharField(max_length=50, blank = False)


class Employee_form(models.Model):
    emplo_fNum = models.IntegerField(primary_key=True)
    emploF_info	= models.CharField(max_length=50, blank = False)



### 현진
class Member_info(models.Model):
    mem_Num = models.IntegerField(primary_key=True)
    mem_ID = models.CharField(max_length=20, blank=False)
    mem_PW = models.CharField(max_length=20, blank=False)
    mem_Gender = models.CharField(max_length=2, blank=False)
    mem_Birth = models.CharField(max_length=10, blank=False)
    mem_HP = models.CharField(max_length=20)
    mem_Email = models.CharField(max_length=50, blank=False)
    mem_Add = models.CharField(max_length=200, blank=False)
    mem_Name = models.CharField(max_length=20, blank=False)
    mem_Rank = models.CharField(max_length=10)
    mem_DIV = models.CharField(max_length=10)

    def __str__(self):
        return self.mem_Name


class Self_introduction(models.Model):
    mem_Num = models.ForeignKey('Member_info', on_delete=models.CASCADE)
    self_intro_cont = models.CharField(max_length=2000, blank=False)
    portfolio_File = models.FileField()
    inter_occupation1 = models.CharField(max_length=20)
    inter_occupation2 = models.CharField(null = True, max_length=20)
    inter_occupation3 = models.CharField(null = True, max_length=20)

    def __str__(self):
        return self.self_intro_cont

class Mento_info(models.Model):
    mem_Num = models.ForeignKey('Member_info', on_delete=models.CASCADE)
    profile_Pic = models.ImageField(blank=False)
    mento_Career = models.CharField(max_length=2000, blank=False)
    mento_Proof_doc = models.FileField(blank=False)

class Occupation_type(models.Model):
    occ_Num = models.IntegerField(primary_key=True)
    occ_Name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.occ_Name

class Member_occupation(models.Model):
    mem_occ_Num = models.IntegerField(primary_key=True)
    mem_Num = models.ForeignKey('Member_info', on_delete=models.CASCADE)
    occ_Num = models.ForeignKey('Occupation_type', on_delete=models.CASCADE)



# 혜진

# 게시판 분류
class Board_C(models.Model):
    b_categ_num = models.IntegerField(primary_key=True)
    # board_c = models.ForeignKey('Board')
    b_categ_name = models.CharField(max_length = 20, blank = False)

    def __str__(self):
        return self.b_categ_name

# 게시판
class Board(models.Model):
    # b_num = models.IntegerField(primary_key=True)
    # board_c = models.ForeignKey('Board_C', null = True)
    board_c = models.ForeignKey('Board_C')
    b_categ_num = models.IntegerField(null=True, blank = True)
    owner = models.ForeignKey(User, null=True)
    b_title = models.CharField(max_length = 20, blank = False)
    b_contnet = models.CharField(max_length=500,blank = False)
    b_published_date = models.DateTimeField(blank=True, null=True)
    b_hit = models.IntegerField( default = 0)
    # b_parent_id = models.IntegerField(null=True, blank = True)
    # b_parent_id = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return self.b_title

# 후기 게시판
class Review(models.Model):
    mrapply_Num = models.ForeignKey('Mrapply', on_delete=models.CASCADE)
    r_num = models.IntegerField(primary_key=True)
    mrapply_Num = models.IntegerField(null = True, blank = True)
    mr_title = models.CharField("멘티이름", max_length = 20, null = True, blank = False)
    mto_name = models.CharField("멘토이름", max_length = 20, null = True, blank = False)
    r_score = models.IntegerField("조회수", null = True, blank = True, default=0) # 조회 수
    r_content = models.CharField("내용", max_length=500, null = True, blank = False)
    r_image = models.ImageField(null = True)
    r_like = models.IntegerField("좋아요 수", null = True, blank = True, default = 0)
    r_date = models.DateTimeField("작성날짜",  null = True, auto_now_add=True)

    def __str__(self):
        return self.mr_title


# # 혜리
# # 멘토링찜하기
# class Mr_Wish(models.Model):
#     mr_wish_num = models.IntegerField(primary_key=True)
#     mem_Num = models.ForeignKey('Member_info', on_delete = models.CASCADE) # FK
#     mtr_num = models.ForeignKey('Mtr_info', on_delete = models.CASCADE) # FK


# # 기업찜하기
# class Biz_Wish(models.Model):
#     # 기업 외래키 설정
#     biz_wish_num = models.IntegerField(primary_key=True)
#     mem_Num = models.ForeignKey('Company_info', on_delete = models.CASCADE) # FK
#     mem_Num = models.ForeignKey('Member_info', on_delete = models.CASCADE) # FK


# # 멘토링신청정보
# class Mrapply(models.Model):
#     mrapply_num = models.IntegerField(primary_key=True)
#     mr_wish_num = models.ForeignKey('Mr_Wish', on_delete = models.CASCADE) # FK
#     mrapply_start = models.DateTimeField(auto_now_add=True)
#     mrapply_con = models.IntegerField(blank = False)
#     mr_pay_method = models.CharField(max_length=10, null=False)
#     mr_credit_com = models.CharField(max_length=10, null=False)
#     mr_credit_num = models.IntegerField(blank = False)
#     mr_apporve_num = models.IntegerField(blank = False)
#     mr_approve_date = models.DateTimeField(auto_now_add=True)
#     mr_depositless_name = models.CharField(max_length=10, null=False)
#     mr_depositless_date = models.DateTimeField(auto_now_add=True)
#     mr_depositless_bank = models.CharField(max_length=10, null=False)
#     mr_deposit_date = models.DateTimeField(auto_now_add=True)
#     mr_payamount =  models.IntegerField(blank = False)

#     def __str__(self):
#         return self.mr_pay_method


# # 멘토링신청정보 상태
# class Mrapply_State(models.Model):
#     mrapply_con = models.IntegerField(primary_key=True)
#     mrapply_name = models.CharField(max_length=10, null=False)


# # 면접수수료결제정보
# class Inter(models.Model):
#     # 면접신청번호 외래키 설정
#     inter_num = models.IntegerField(primary_key=True)
#     inter_apply_num = models.ForeignKey('Interview_apply', on_delete = models.CASCADE) #FK
#     inter_pay_method = models.CharField(max_length=10, null=False)
#     inter_credit_com = models.CharField(max_length=10, null=False)
#     inter_credit_num = models.IntegerField(blank = False)
#     inter_apporve_num = models.IntegerField(blank = False)
#     inter_approve_date = models.DateTimeField(auto_now_add=True)
#     inter_depositless_name = models.CharField(max_length=10, null=False)
#     inter_depositless_date = models.DateTimeField(auto_now_add=True)
#     inter_depositless_bank = models.CharField(max_length=10, null=False)
#     inter_deposit_date = models.DateTimeField(auto_now_add=True)
#     inter_payamount =  models.IntegerField(blank = False)

#     def __str__(self):
#         return self.inter_pay_method

# 혜리
# 멘토링찜하기
class Mr_Wish(models.Model):
    mr_wish_num = models.IntegerField(primary_key=True)
    mem_Num = models.ForeignKey('Member_info', on_delete = models.CASCADE) # FK
    mtr_num = models.ForeignKey('Mtr_info', on_delete = models.CASCADE) # FK, 180514 수정


# 기업찜하기(혜영이가 해 놓음)
# class Biz_Wish(models.Model):
    # biz_wish_num = models.IntegerField(primary_key=True)
    # 기업 외래키 설정
    # mem_Num = models.ForeignKey('Company_info', on_delete = models.CASCADE) # FK
    # mem_Num = models.ForeignKey('Member_info', on_delete = models.CASCADE) # FK


# 멘토링신청정보
class Mrapply(models.Model):
    mrapply_num = models.IntegerField(primary_key=True)
    mr_wish_num = models.ForeignKey('Mr_Wish', on_delete = models.CASCADE) # FK
    mrapply_start = models.DateTimeField(auto_now_add=True)
    mrapply_con = models.IntegerField(blank = False)
    mr_pay_method = models.CharField(max_length=10, null=False)
    mr_credit_com = models.CharField(max_length=10, null=True)
    mr_credit_num = models.IntegerField(null=True)
    mr_apporve_num = models.IntegerField(null=True)
    mr_approve_date = models.DateTimeField(auto_now_add=True)
    mr_depositless_name = models.CharField(max_length=10, null=True)
    mr_depositless_date = models.DateTimeField(auto_now_add=True)
    mr_depositless_bank = models.CharField(max_length=10, null=True)
    mr_deposit_date = models.DateTimeField(auto_now_add=True)
    mr_payamount =  models.IntegerField(blank = False)

    def __str__(self):
        return self.mr_pay_method


# 멘토링신청정보 상태
class Mrapply_State(models.Model):
    mrapply_con = models.IntegerField(primary_key=True)
    mrapply_name = models.CharField(max_length=10, null=False)


# 면접수수료결제정보
class Inter(models.Model):
    inter_num = models.IntegerField(primary_key=True)
    # 면접신청번호 외래키 설정
    inter_apply_num = models.ForeignKey('Interview_apply', on_delete = models.CASCADE) # FK
    inter_pay_method = models.CharField(max_length=10, null=False)
    inter_credit_com = models.CharField(max_length=10, null=True)
    inter_credit_num = models.IntegerField(null=True)
    inter_apporve_num = models.IntegerField(null=True)
    inter_approve_date = models.DateTimeField(auto_now_add=True)
    inter_depositless_name = models.CharField(max_length=10, null=True)
    inter_depositless_date = models.DateTimeField(auto_now_add=True)
    inter_depositless_bank = models.CharField(max_length=10, null=True)
    inter_deposit_date = models.DateTimeField(auto_now_add=True)
    inter_payamount =  models.IntegerField(blank = False)

    def __str__(self):
        return self.inter_pay_method


# 지선
class Mtr_info(models.Model):
    mtr_num = models.IntegerField(primary_key=True)
    mem_Num = models.ForeignKey('Mento_info', on_delete=models.CASCADE)
    field = models.CharField(max_length=500,blank=True, null=True)
    theme =  models.CharField(max_length=100, blank=True, null=True)
    amount = models.IntegerField(blank = False)
    mtr_content =  models.CharField(max_length=500, blank=True, null=True)
    fixed_people = models.IntegerField(blank = False)

    def __str__(self):
        return self.theme

class Mtr_daily_report(models.Model):
    mtr_daily_num = models.IntegerField(primary_key=True)
    mrapply_num = models.ForeignKey('Mrapply', on_delete=models.CASCADE)
    mtr_lesson = models.CharField(max_length=500, blank=True, null=True)
    mtr_date = models.DateField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장
    mtr_answer = models.CharField(max_length=500, blank=True, null=True)
    mtr_content = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.mtr_content