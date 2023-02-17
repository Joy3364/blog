## install nginx  
```
sudo install nginx 
```
## edit /etc/nginx/nginx.conf
```
# http server 
http {
    ...
    server {
        listen      ip:port; #不加ip则监听全部ip
        listen      [::]:port ipv6only=on; #同时监听ipv4与ipv6的唯一方法

        location    your_url {  #
            root real_path;  # root匹配的是location的上一层目录 
        }
    }
}

# uwsgi 代理
http {
    ...
    server {
                                
        listen      ip:port; #不加ip则监听全部ip
        listen      [::]:port ipv6only=on; #同时监听ipv4与ipv6的唯一方法

        location    your_url {  
            uwsgi_pass      unix:///home/loner/www/MainWebsite/uwsgi/uwsgi.sock; # ip:port
            include          /etc/nginx/uwsgi_params; 

        }
    }
}
```
## read nginx log
```
default        /var/log/nginx/access.log
specify        access_log    log_path  #每个server可指定一个
```
## nginx cmd
```
service nginx restart/stop/start/staus
```

