# sign-web-demo

**demo大概功能：**   

- 实现一个登录页面，需要去数据库进行验证

- 登录完成之后用户进行签到，用户当日已签到不能重复签到  

- 测试并发能达到2000+

**环境**

	CentOS7.2   4CPU、4G
	python环境：python3.6.0
	
	安装配置nginx服务
	启动nginx服务
	
	pip3 install -r requirements.txt  ----安装依赖pip包

	用uwsgi启动
	uwsgi uwsgi.ini