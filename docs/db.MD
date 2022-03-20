`docker exec -it jobsche_db_1 sh`             
`mysql -u root -p`            
-> Enter Password: password            
`USE jobsche;`             
`SHOW TABLES;`         

##### Migration
1. flask db init (one time)        
2. flask db migrate (requires review and edit)          
3. flask db upgrade