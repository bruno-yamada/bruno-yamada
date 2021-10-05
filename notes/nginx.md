# NGINX

sudo nginx -t # Check syntax
sudo systemctl status nginx # nginx current status
sudo systemctl reload nginx # Reload nginx
sudo systemctl restart nginx  # Restart nginx

## Static files
```
server {
    listen 80;
    server_name example.com;

    root /path/to/website;
    # root /www/data/ for example

    # If there's no 'root' inside, it will look for /www/data/index.html
    location / {
    }

    # If there's no 'root' inside, it will look for /www/data/images/index.html
    location /images/ {
    }

    # Since there's 'root' inside, it will look for /www/media/videos/index.html
    location /videos/ {
        root /www/media;
    }
}
```

## Redirect (HTTP 301)

```
server {
    # Redirect www.example.com to example.com
    listen 80;
    server_name www.example.com;
    return 301 http://example.com$request_uri;
}
```

## reverse proxy
```
server {
  listen 80;
  server_name example.com;
  
  location / {
    proxy_pass http://0.0.0.0:3000;
    # where 0.0.0.0:3000 is your Node.js Server bound on 0.0.0.0 listing on port 3000
  }
}

# Basic + (upstream)

upstream node_js {
  server 0.0.0.0:3000;
  # where 0.0.0.0:3000 is your Node.js Server bound on 0.0.0.0 listing on port 3000
}

server {
  listen 80;
  server_name example.com;
  
  location / {
    proxy_pass http://node_js;
  }
}
```
## Load balancing
```
upstream node_js {
  server 0.0.0.0:3000;
  server 0.0.0.0:4000;
  server 127.155.142.421;
}
```
