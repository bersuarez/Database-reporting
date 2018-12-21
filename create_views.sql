create view question1 as select '"'||articles.title||'"' as title, count(*) as views
     from articles, log 
     WHERE log.path = CONCAT('/article/', articles.slug) 
     group by articles.title 
     order by views desc
     limit 3;

create view question2 as select authors.name as author, count (*) as views 
     from articles, authors, log 
     where authors.id::text=articles.author::text 
     and log.path like '%'||articles.slug||'%' 
     group by authors.name 
     order by views desc;


create view question3 as select to_char(to_date(tabla1.fecha::text,'YYYY-MM-DD'),'Mon DD YYYY'), round(100.0*tabla1.errores/tabla2.totales,1)||'%' as porcentajes
     from (select time::date as fecha, count(*) as errores
         from log where status!='200 OK'
         group by time::date)
         as tabla1
     join (select log.time::date as fecha, count (*) as totales
         from log group by log.time::date)
         as tabla2
     on tabla1.fecha=tabla2.fecha where 100.0*tabla1.errores/tabla2.totales>1;