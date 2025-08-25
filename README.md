Generador de Contraseñas en Python 

Este proyecto implementa un generador de contraseñas seguras utilizando 
Python. 
El usuario puede decidir:

• La longitud de la contraseña 

• Si incluir números 

• Si incluir letras mayúsculas 

• (Siempre incluye símbolos para más seguridad) 

Concepto del Proyecto 

El objetivo es crear una aplicación simple pero robusta que permita generar 
contraseñas seguras para el uso diario. 
La seguridad de las contraseñas es fundamental en la informática, y este 
programa aprovecha librerías estándar de Python para garantizar aleatoriedad 
y variedad de caracteres. 

Librerías utilizadas 
1. secrets 
o Es una librería estándar de Python enfocada en la generación de 
valores aleatorios seguros para criptografía. 
o Se utiliza para evitar que las contraseñas puedan ser predecibles, 
lo cual sí puede ocurrir si se usa random. 
o En este proyecto, secrets.choice() selecciona caracteres al azar 
de forma segura. 
2. string 
o También es parte de la librería estándar de Python. 
o Permite acceder a conjuntos predefinidos de caracteres como: 
▪ string.ascii_lowercase → letras minúsculas 
▪ string.ascii_uppercase → letras mayúsculas 
▪ string.digits → números 
▪ string.punctuation → símbolos 
o Gracias a esta librería se evita tener que escribir manualmente 
todos los caracteres posibles. 
Estructura del Programa 
1. Definición de la función generar_contrasena 
o Recibe como parámetros: longitud, si usar números y si usar 
mayúsculas. 
o Construye un conjunto de caracteres posibles según lo que el 
usuario decida. 
o Genera la contraseña seleccionando caracteres aleatorios con 
secrets.choice(). 
2. Función main 
o Muestra el título del programa. 
o Pregunta al usuario la longitud y sus preferencias (números y 
mayúsculas). 
o Llama a la función generar_contrasena y muestra el resultado. 
3. Control de ejecución con if __name__ == "__main__": 
o Esto asegura que el programa se ejecute solo cuando se corre 
directamente, no cuando se importa en otro archivo.
