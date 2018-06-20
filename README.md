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

**nginx配置**

	user root;
	worker_processes 4;
	
	error_log /var/log/nginx/error.log;
	pid /var/run/nginx.pid;
	
	events {
	        worker_connections  1024;
	}
	
	
	http {
	        log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
	                                          '$status $body_bytes_sent "$http_referer" '
	                                          '"$http_user_agent" "$http_x_forwarded_for"';
	
	        access_log  /var/log/nginx/access.log  main;
	
	        sendfile            on;
	        tcp_nopush          on;
	        tcp_nodelay         on;
	        keepalive_timeout   65;
	        #types_hash_max_size 2048;
	
	        include             /etc/nginx/mime.types;
	        default_type        application/octet-stream;
	
	        upstream django {
	                # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
	                server 127.0.0.1:8000;       # for a web port socket (we'll use this first)
	        }
	        server {
	                listen      80;
	
	                #server_name ;
	                charset     utf-8;
	
	
	                # max upload size
	                client_max_body_size 75M;     # adjust to taste
	
	                location /static {
	                        alias  /mypro/AuthAndSignIn/mystatic;     # your Django project's static files - amend as required
	                }
	
	                # Finally, send all non-media requests to the Django server.
	                location / {
	                        uwsgi_pass  django;
	                        include     uwsgi_params; # the uwsgi_params file you installed
	                }
	        }
	}