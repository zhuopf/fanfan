# coding:utf-8

"""
请从键盘获得每位同学的每项考核成绩.并格式化输出每位同学的单项得分和总分
"""

# 输入张三的成绩
print("-----请输入张三的统计数字----")
zhangsan_subjectscore = int(input("张三的专业成绩: "))
zhangsan_moralityscore = int(input("张三的思想品德分数: "))
zhangsan_sportsscore = int(input("张三的体育成绩: "))
zhangsan_instructorscore = int(input("张三的辅导员评分: "))
zhangsan_classscore = int(input("张三的班级评分: "))
# 输入李四的成绩
print("-----请输入李四的统计数字----")
lisi_subjectscore = int(input("李四的专业成绩: "))
lisi_moralityscore = int(input("李四的思想品德分数: "))
lisi_sportsscore = int(input("李四的体育成绩: "))
lisi_instructorscore = int(input("李四的辅导员评分: "))
lisi_classscore = int(input("李四的班级评分: "))
# 输入王二的成绩
print("-----请输入王二的统计数字----")
wanger_subjectscore = int(input("王二的专业成绩: "))
wanger_moralityscore = int(input("王二的思想品德分数: "))
wanger_sportsscore = int(input("王二的体育成绩: "))
wanger_instructorscore = int(input("王二的辅导员评分: "))
wanger_classscore = int(input("王二的班级评分: "))

print("----------")
# 计算张三的总分
zhangsan_score = float(zhangsan_subjectscore * 0.3 +
                       zhangsan_moralityscore * 0.2 +
                       zhangsan_sportsscore * 0.2 +
                       zhangsan_instructorscore * 0.15 +
                       zhangsan_classscore * 0.15)
# 计算李四的总分
lisi_score = float(lisi_subjectscore * 0.3 + lisi_moralityscore * 0.2 +
                   lisi_sportsscore * 0.2 + lisi_instructorscore * 0.15 +
                   lisi_classscore * 0.15)
# 计算王二的总分
wanger_score = float(wanger_subjectscore * 0.3 + wanger_moralityscore * 0.2 +
                     wanger_sportsscore * 0.2 + wanger_instructorscore * 0.15 +
                     wanger_classscore * 0.15)

# 输出张三的所有成绩
print("张三的专业成绩是 %d 分, 思想品德成绩是 %d 分, 体育成绩是 %d 分, 辅导员评分是 %d 分, 班级评分是 %d 分,张三的总分是 %f 分" %
      (zhangsan_subjectscore, zhangsan_moralityscore, zhangsan_sportsscore,
       zhangsan_instructorscore, zhangsan_classscore, zhangsan_score))
# 输出李四的所有成绩
print("李四的专业成绩是 %d 分, 思想品德成绩是 %d 分, 体育成绩是 %d 分, 辅导员评分是 %d 分, 班级评分是 %d 分, 李四的总分是 %f 分" %
      (lisi_subjectscore, lisi_moralityscore, lisi_sportsscore,
       lisi_instructorscore, lisi_classscore, lisi_score))
# 输出王二的所有成绩
print("王二的专业成绩是 %d 分, 思想品德成绩是 %d 分, 体育成绩是 %d 分, 辅导员评分是 %d , 班级评分是 %d 分, 李四的总分是 %f 分" %
      (wanger_subjectscore, wanger_moralityscore, wanger_sportsscore,
       wanger_instructorscore, wanger_classscore, wanger_score))

print("按照评分规则，总分高的评选为三好学生! 恭喜!")