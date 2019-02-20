# Problem-Judger
## 介绍
基于django的在线选择题判题系统， 目前还在进一步开发当中。
## 功能
实现选择题在线评判并且设置admin页面可以将题目上传到数据库。
## 部署
你需要安装python3， django2.0， mysql 在配置文件中配置好后，迁移数据库， 直接在根目录下运行run.sh文件即可。
数据库配置：
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '你的mysql数据库名称',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
    }
}
```
mysql中新建数据库
```
#mysql
create database problem_judger;
```

数据库迁移使用以下命令（根目录）：
```
#python3
python3 manage.py makemigrations
python manage.py migrate
```
