# TrabajoDocker
Realizar una investigación sobre microservicios y docker-compose.  Adicional realizar un microservicio ejemplo que sea implementado con docker-compose.

En esta practica se desarrolla un trabajo enfocado en la arquitectura de microservicios el objetivo principal es comprender cómo funcionan los microservicios en entornos distribuidos, cómo se comunican entre sí y cómo Docker facilita su despliegue y ejecución utilizando la herramienta Docker Compose creamos la aplicacion que estara distribuida por secciones donde cada uno conlleva el requerimeinto que se pide para la practica en este caso los datos para la conexion con msql como mi base de datos

<img width="302" height="181" alt="image" src="https://github.com/user-attachments/assets/d417d1b4-b2ee-42f8-9bab-c401f82b9f87" />

luego de crearmos asi tambien la base de datos en mysql donde tendremos la tabla y los usuarios que creamos 

<img width="362" height="184" alt="image" src="https://github.com/user-attachments/assets/377b04e6-9897-45cf-83b7-307a9793ef6c" />

Construimos la imagen en docker , dockerFile y verificamos la conexión que este realizado correctamete  para ello se entra al local host que nos creamos y verifiamos la conexion con ello 

<img width="345" height="110" alt="image" src="https://github.com/user-attachments/assets/2b543da8-651f-43fa-9346-19e7276d44ee" />

Verificamos la conexion este correcto 

<img width="630" height="207" alt="image" src="https://github.com/user-attachments/assets/478d3e56-b027-4239-bc47-23b36206c882" />

verificamos la base de datos creada 

<img width="317" height="166" alt="image" src="https://github.com/user-attachments/assets/935839a2-6677-4ff1-a785-692458164d39" />

Una vez realizado estos pasos lo que tenemos que hacer es la conexion y comunicacion con la base de datos donde vamos a crear las tablas en cuestion 
1 accedemos al directorio del proyecto 
2 levantamos los contenedores con docker compose up
3 accedemos al contenedor mysql docker exec -it microserviciousu-db-1 mysql -u root -p
4 Dentro del contenedor, se creó la base y la tabla usuarios 


<img width="603" height="256" alt="image" src="https://github.com/user-attachments/assets/b8868730-449d-422f-b8e7-01723542c199" />



5 Finalmente, se probó el microservicio en el navegador y Funciona correctamente. 

<img width="423" height="57" alt="image" src="https://github.com/user-attachments/assets/d7c1058a-a480-4e88-b42a-e66cecf3903c" />

El sistema funcionó correctamente.

El contenedor Flask (API) se conectó de forma exitosa con el contenedor MySQL, demostrando la independencia y comunicación entre servicios.


verificamos las tablas creadas dentro del archivo msql

<img width="614" height="259" alt="image" src="https://github.com/user-attachments/assets/fcd70f14-a39a-4450-9445-ce1c80527b72" />

y hacemos un pequeño cambio en los usuarios agregamos correo electronico para verificar que su funcionamiento este ejecutanose de forma correcta incluyendo edit.

<img width="474" height="194" alt="image" src="https://github.com/user-attachments/assets/d956c76a-7db5-4c98-9b14-866464bb3173" />

y verificamos que la imagen docker creada este trabajando de forma correcta 

<img width="1086" height="397" alt="image" src="https://github.com/user-attachments/assets/74aaddf7-35d6-4857-9030-ad3013509b25" />



