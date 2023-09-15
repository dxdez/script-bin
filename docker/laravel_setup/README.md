## Laravel Setup

This is a basic setup for a laravel project which utilizes docker compose to split a laravel application into three seperate containers: one container for the php service/application, one container for the nginx service and one container for the mysql database. The docker file includes the details for setting up the PHP service.


### Running Commands for php artisan

Because artisan and composer are not running on the local machine and instead running within containers, you will need to make use of docker compose to execute a command. A typical command will look something like this:
```
docker-compose exec <nameofcontainer> <command>
```
An additional note is that the full path of the working directory needs to be included when running artisan since the container will not be able to locate it otherwise. Refer to the below examples of common commands to understand the general use-case of the artisan commands within a container:


#### Create a Controller
```
docker-compose exec app php /var/www/artisan make:controller ItemController
```

#### Create a Model
```
docker-compose exec app php /var/www/artisan make:model Item
```
