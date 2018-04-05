grade={}
homepage=input('欢迎光临学生成绩信息管理系统！按任意键继续\n')
while homepage:
    menu=('1.录入','2.查询','3.修改','4.删除','5.总览','6.退出')
    for feature in menu:
        print(feature)
    number=('1','2','3','4','5','6')
    order=input('请输入您想要操作的序号：')
    if order in number:
        num=int(order)
        while num==1:
            name=input('请输入学生姓名：')
            sorce=float(input('请输入学生成绩：'))
            grade[name]=sorce
            exit=input('录入成功！按y继续录入，按任意键返回主菜单\n')
            if exit=='y':
                continue
            else:
                print('欢迎回到主菜单')
                break
        while num==2:
            name=input('请输入您要查询的学生姓名：')
            if name in grade:
                print('%s的成绩为：%.2f'%(name,grade[name]))
                exit=input('查询成功！按y继续查询，按任意键返回主菜单\n')
                if exit=='y':
                    continue
                else:
                    print('欢迎回到主菜单')
                    break
            else:
                print('查无此人，请重新输入')
                exit2=input('按y继续查询，按任意键返回主菜单\n')
                if exit2=='y':
                    continue
                else:
                    print('欢迎回到主菜单')
                    break
        while num==3:
            name=input('请输入您要修改成绩的学生姓名：')
            if name in grade:
                sorce=float(input('请输入新的成绩：'))
                grade[name]=sorce
                print('修改成功！')
                exit=input('按y继续修改，按任意键返回主菜单\n')
                if exit=='y':
                    continue
                else:
                    print('欢迎回到主菜单')
                    break
            else:
                print('查无此人，请重新输入')
                exit2=input('按y继续修改，按任意键返回主菜单\n')
                if exit2=='y':
                    continue
                else:
                    print('欢迎回到主菜单')
                    break
        while num==4:
            name=input('请输入您要删除信息的学生姓名：')
            if name in grade:
                grade.pop(name)
                print('删除成功！')
                exit=input('按y继续删除，按任意键返回主菜单\n')
                if exit=='y':
                    continue
                else:
                    print('欢迎回到主菜单')
                    break
            else:
                print('查无此人，请重新输入')
                exit2=input('按y继续删除，按任意键返回主菜单\n')
                if exit2=='y':
                    continue
                else:
                    print('欢迎回到主菜单')
                    break
        while num==5:
            print(grade)
            exit=input('查询成功！按任意键返回主菜单\n')
            if exit:
                break
        if num==6:
            print('感谢您的使用，再见！')
            break
    elif order not in number:
        print('输入有误，请输入序号1~6')
        continue