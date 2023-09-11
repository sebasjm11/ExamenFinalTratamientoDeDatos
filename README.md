

## EXAMEN FINAL OPCIÓN B
Este es el proyecto/examen final para la materia Tratamiento de Datos de la Maestría en Ciberseguridad de la Universidad Internacional del Ecuador.

Autor: Walter Sebastián Jara Morillo

*lA PÁGINA EN LA CUÁL SE REALIZÓ LA CONSULTA ES LA SIGUIENTE(https://www.camisetasfutboleses.com/)*

<h1 align="center"> CAMISETAS FUTBOL ESPAÑOL</h1>
<p align="center"> Logo de la página</p>
<p align="center"><img src="https://www.camisetasfutboleses.com/image/catalog/camisetasfutboleses/untitled%20folder/picture13627358327771-1.jpg"/></p> 

## Tabla de contenidos:
---

- [Antecendentes](#antecendentes)
- [Herramientas](#herramientas)
- [Resultados](#resultados)
- [Dificultades](#dificultades)


## Antecedentes
En el presente proyecto proporciona una interfaz web simple para acceder a datos relacionados con camisetas del Real Madrid almacenados en una base de datos MongoDB. En esta se busca guardar su el nombre de las camisetas con el año del que son con su descripción. Todo esto mediante el programa realizado en Phycharm con las respectivas librerías para ejecución de un código que contaba con varias clases. 

### Herramientas & Proceso

![HerramientasExcalidraw](https://github.com/sebasjm11/ExamenFinalTratamientoDeDatos/assets/45462923/df831343-7b57-4c52-8e0d-ae3b42578a90)


![Flask](https://github.com/sebasjm11/ExamenFinalTratamientoDeDatos/assets/45462923/21d0dce6-1d67-4870-9a4a-88907b1fb4c1)


### Resultados
---
Como resultados se obtuvo los datos de la página mencionada realizando la búsqueda desde la barra "Buscar" y colocando "Real Madrid Retro" y automatizando que dé clicks por si solos, además de en un dropdownlist colocar que presente 25 camisetas y no solo 16 en la página, una vez filtrado lo requerido se extrajo los datos como la descripción de cada una de las camisetas de "Real Madrid Retro" las cuáles presentaban la descripción de la camiseta, su precio oferta, precio normal y el descuento que se presentaba en ese momento. Para luego almacenarlas en la base de datos en MongoDB, en una colección.

## Dificultades encontradas
---
Cómo dificultades principales se obtuvo lo que es el tipo de datos que presentaba cada una de las camisetas, ya que ciertas no contaban con el descuento, entonces eso obtenía un error al ejecutar. Así que se añadió un try y un exception para que no presente el inconveniente. Adicional, ciertos datos al tener tipos y clases diferentes se tendía a una confusión directamente en el código html. Finalmente el apartado de Flask fue complicado encontrar la manera correcta de realizarlo, especialmente desde pycharm para luego presentarlo en el navegador.
