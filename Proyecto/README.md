# Proyecto Final
# Genómica Computacional 2021-
## Interacciones de la comunidad bacteriana asociada al Microbioma intestinal diferenciado por sexo.
### Integrantes

Luis Miguel MB (ebooshi - 315116663)

Daniel AG (daniel-acga 315124772)

Mirén HL (mjhl1999 - 315309452)

Mario AV (Mario-Avella - 419003296)

Vanessa CA (316105408)

Astrid AL (316115607)


### 1. Introducción
El metabarcoding aprovecha la determinación de primers “barcode” de taxa específicos (ej: subunidad 16S 
de rDNA en bacterias) que recuperan información de solo un grupo de organismos y llegar a determinar la
representación de estos en la comunidad. Esto presenta muchas ventajas ya que el desarrollo de
primers “barcode” para taxa de distinto nivel ha aumentado durante las últimas décadas
permitiendo que se lleven a cabo cada vez más estudios ecológicos y funcionales de este tipo.
(Ficetola et al, 2014).
La estandarización de los métodos de análisis de DNA ambiental por medio de la secuenciación de
amplicones(metabarcoding) se ha realizado de manera muy general al igual que otras ramas de la
bioinformática. Esto se debe al desarrollo constante de nuevos softwares que a menudo se
encuentran optimizados para un tipo de estudio o de datos. A partir del análisis de la calidad de las
secuencias crudas y del filtrado de estas mismas, se debe realizar un agrupamiento de los reads
que formen unidades taxonómicas operacionales (OTU’s) bajo un criterio de similitud para finalizar
con la determinación taxonómica, a menudo en contra de bases de datos especializadas para
determinados taxa. Es importante destacar que el nivel de umbral de identidad mínimo para asignar
la identidad taxonómica a un OTU’s es de 97% (Galhardo ​ et al ​., 2018)
El enfoque convencional para inferir una red de interacciones microbianas consistía en observar el
comportamiento de crecimiento en cultivos mixtos de muy pocos microorganismos. Actualmente los
programas diseñados para la construcción de redes de interacción a partir de datos de
secuenciación de alto rendimiento se apoyan de softwares de computo numérico para optimizar el
cálculo de las estimaciones temporales, en el caso de MetaMIS (Shaw et al., 2016) fue diseñado a
través de MATLAB R2015b. Las interacciones entre OTU’s se infieren por medio de la
implementación del modelo de Lotka-Volterra en tiempo discreto junto con métodos estadísticos
para manejar datos discretos altamente correlacionados (en este caso por regresión de mínimos
cuadrados parciales). A partir del valor obtenido mediante la estimación del modelo se predice qué
tipo de interacción se presenta.
El análisis topológico de este tipo de redes a partir de redes reales y aleatorias ha sido empleado
para hacer inferencias sobre el origen de este tipo de interacciones, en este proyecto se realizó por
medio de la pipeline NetAn (De Anda et al., 2018). A partir de las redes dirigidas calculadas por
MetaMIS, NetAn extrae propiedades clave como la densidad, los nodos con máximo grado de
entrada y salida y el coeficiente de agrupamiento, para posteriormente asumir a las redes como
aleatorias y calcular la modularidad y el número de comunidades que las integran (Blondel, 2018)
El tracto gastrointestinal humano alberga una población compleja y dinámica de microorganismos
que ejercen una influencia marcada sobre el huésped durante la homeostasis y la enfermedad.
Múltiples factores contribuyen al establecimiento de la microbiota intestinal humana durante la
infancia, considerándose la dieta como uno de los principales impulsores en la configuración de la
microbiota intestinal a lo largo de la vida (Danneskiold-Samsøe et al ​., 2019; Fan & Pedersen, 2021).
Es interesante notar que existen diferencias geográficas en cuanto al contenido y riqueza de la
microbiota (Yatsunenko ​ et al. 2012). A pesar de que el estudio de estas se ha extendido durante los
últimos años, la dificultad de colectar muestras bajo series temporales se ha presentado como un
obstáculo, el desarrollo de los métodos para la recopilación y el procesamiento de los datos ha
permitido conocer cada vez más sobre las características más generales y variables de estas
comunidades en diferentes poblaciones humanas. A medida que la composición del microbioma
cambia, también lo hace la composición de las proteínas bacterianas producidas en el intestino. En
los microbiomas de adultos, se ha encontrado una alta prevalencia de enzimas implicadas en la
fermentación, la metanogénesis y el metabolismo de la arginina, el glutamato, el aspartato y la
lisina. En cambio, en los microbiomas de los lactantes las enzimas dominantes están implicadas en
el metabolismo de la cisteína y en las vías de fermentación (Gerritsen ​ et al., ​ 2011).


![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Data/gut_microbiome_Donaldson2015.jpg)

Fig. 1. ​ ​Las familias de bacterias dominantes del intestino delgado y el colon reflejan diferencias fisiológicas a lo largo
del intestino. Los phyla bacterianos dominantes en el intestino son Bacteroidetes, Firmicutes, Actinobacteria,
Proteobacteria y Verrucomicrobia. Imagen proveniente de Donaldson et al. (2015).

### 2. Objetivos
a. Modelar la red de interacciones ecológicas de la comunidad bacteriana del
microbioma intestinal de un sujeto de cada sexo
b. Identificar motivos de interacción en las comunidades bacterianas del sistema
digestivo mediante el análisis de muestras de 16S rRNA.
c. Determinar la estructura de las redes asociadas con el origen de las interacciones
entre taxa bacterianos.

### 3.Hipótesis
Al modelar las interacciones entre la comunidad bacteriana de taxa más abundantes se observará
una dinámica de interacción estructuralmente similar en el sujeto mujer y en el hombre.

### 4. Método

![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Data/M%C3%A9todo%20-%20DiagFlujo.jpg)

Se utilizaron datos provenientes del artículo de Caropaso y colaboradores de 2011 con los que previamente se generaron
las tablas de abundancias crudas disponibles como datos de prueba de MetaMIS. Con ellos se
estudió a la microbiota intestinal (a partir de heces) de un hombre y una mujer sanos por 15 meses
y por 6 meses respectivamente. Usando la taxonomía de Greengenes, el número total de taxones
asignados a nivel Familia fue 92 para el hombre y de 69 para la mujer. Los dos conjuntos de datos
se comprobaron más a fondo mediante el programa de corrección del número de copias del gen
(Gregory-Carposo ​ et al. ​, 2011).
Tras construir las redes de interacción con el software MetaMIS para los 14 OTU’s más abundantes,
con los cuales se puedan realizar comparaciones a pesar de las diferencias metodológicas para
cada sujeto, se realizarán predicciones sobre el desarrollo de la comunidad y se buscarán
relaciones ecológicas tales como mutualismo, depredación o parasitismo, comensalismo y
amensalismo. También se evaluaron las proporciones de interacciones positivas y negativas al
modelar las redes con un mayor número de OTU 's en cada sujeto y se reportaron las redes
consenso generadas por MetaMIS a partir de todas las redes con distinto número de OTU’s en la
carpeta ​ outputs ​del repositorio.
A partir de la red de interacciones dirigidas, se correrá el script NetAn (De Anda ​ et al, ​, 2018) para
analizar esta red, obtener el porcentaje de interacciones asociadas a diferentes niveles
taxonómicos, identificar posibles motivos de interacciones específicas y evaluar varias
características topológicas como densidad, grado medio, concentradores, componentes
conectados, modularidad del coeficiente de agrupamiento asociado a las comunidades.

### 5. Resultados
Análisis de la red interacción por medio de MetaMIS

![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/MetaMis/Abundancia%20original%20y%20predecida_M.jpg)

Fig 2. Perfil de abundancia original y predecida en sujeto hombre (A)


![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/MetaMis/Abundancia%20original%20y%20predecida_F.jpg)

Fig. 3 Perfil de abundancia original y predecida en sujeto femenino (B)

A lo largo del tiempo se observa que los OTU ́s de las familias Lachnospiraceae y Bacteroidaceae,
tanto en la mujer como en el hombre son las más abundantes, formando parte del 80% de la
comunidad de la mujer y de más del 60% del total de la diversidad de la comunidad del hombre.
Esto era de esperarse porque en múltiples estudios (Segata ​ et al., 2013; Saxena ​ et al., 2016;
Kusada ​ et al., 2017) se han reportado estas dos familias como las más abundantes en el tracto
intestinal y rectal humano. Esto puede asociarse con la influencia de  Lachnospiraceae con un estado antiinflamatorio
y producción de células T reguladoras en el cuerpo humano (Scher et al., 2013). 
La mayoría de los taxones observados se encuentran también representados en ambas comunidades (10 de estos).
Las gráficas resultantes no muestran una diferencia entre la predicción y la abundancia real,
reflejada en el índice de Bray-Curtis, por lo que  propone que la diversidad de la microbiota es
estable considerando que la persona en cuestión no se encontraba en un ambiente totalmente
controlado..

![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/MetaMis/PCA_M.jpg)

Fig. 4 Análisis de Principales Componentes de los diferentes tipos de interacción en la red del hombre

![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/MetaMis/Abundancia%20original%20y%20predecida_F.jpg)

Fig.5 Análisis de Principales Componentes de los diferentes tipos de interacción en la red de la mujer

La interacción más fuerte dentro de la comunidad fue el parasitismo o depredación donde uno de
los OTUs se ve beneficiado a expensas de otro, los OTUs ejemplificado por la familia Neisseriaceae
y Prevotellaceae que se caracteriza por contener al género Prevotella, estos se alojan en la cavidad
bucal produciendo placa, halitosis, y enfermedad periodontal , fueron los que presentaron una
mayor cantidad de parasitismo o depredación, por el contrario, el OTU de la familia
Oxalobacteraceae tuvo menor interacción negativa. Otra de las interacciones más destacables
dentro de la comunidad fue la competencia, la cual se caracteriza porque los OTUs involucrados en
esta interacción biológica disputan por los mismos recursos del ambiente, en general el nivel de
competencia es relativamente similar en todos los OTUs, a excepción de de la familia
Neisseriaceae y, particularmente, la familia Clostridiales Family XI. Incertae Sedis pues no tuvo
ninguna interacción de competencia. La tercera interacción más importante fue la del mutualismo,
en este caso en OTU en cuestión se beneficia de la presencia de otros y viceversa puesto que se
pueden conferir ciertas ventajas ante otros organismos de la microbiota, uno de los OTUs que
resalta sobre los demás es el de Oxalobacteriaceae en el cual, de entre todas sus demás
interacciones, el mutualismo formó parte de más de la mitad de sus interacciones. El OTU
14,Micrococcaceae, parece contener la mayoría de las interacciones, por lo que se infiere que su
influencia es determinante para la construcción de la red.
A diferencia de la red del hombre, la interacción predominante parece ser el mutualismo,
reflejada con más fuerza en la familia Staphylococcaceae (OTU 11). Al igual que en la comunidad
del hombre, a pesar de no ser una familia tan abundante esta tiene una influencia relevante por sus
interacciones con el resto de los taxa. Cabe destacar que su baja abundancia puede ser un
indicador de la buena salud del hospedero, ya que esta se ha detectado en abundancias altas en
casos de cáncer colorrectal junto con otros taxa, por lo que su rol como mutualista fuerte puede
tener un efecto importante en la composición de la comunidad asociada a la enfermedad (Marques
et al. ​, 2016). La siguiente familia con interacciones más fuertes, Corynebacteriaceae, cuya
abundancia elevada ha sido confirmada por otros estudios como un indicador de una microbiota
intestinal sana en adultos de edad avanzada (45 - 70), por lo que, a pesar de no ser tan abundante
en la comunidad estudiada, la gran intensidad sus interacciones mutualistas con el resto de familias
pueden tener relación con esto (Spinner, 2015). Otra de las familias cuyas interacciones
mutualistas resaltan en el PCA de la mujer es la número 9, Lactobacillaceae. Se ha encontrado que
esta tiende a mantener relaciones metabólicas íntimas con otros taxa e incluso tiene un impacto
funcional en el hospedero. La abundancia de esta familia a menudo se ha relacionado con la dieta y
el buen funcionamiento del sistema digestivo (p. ej asimilación de carbohidratos y señalización de
factor de crecimiento de insulina), además de que su papel en las comunidades se ha relacionado
con el consumo de probióticos (Matos y Leullier, 2014)

![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/MetaMis/Red%20consenso_M.jpg)

Fig 6. Red de interacción a partir de los OTU’s más abundantes del sujeto hombre. Las flechas rojas indican
interacciones positivas y las azules negativas.

![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/MetaMis/Red%20consenso_F.jpg)

Fig 7.  Red de interacción a partir de los OTU’s más abundantes del sujeto mujer. Las flechas rojas indican
interacciones positivas y las azules negativas.

Al recuperar sólo las 30 interacciones más fuertes se observó en la red del hombre que a pesar de que
Micrococcaceae no está entre las familias más abundantes, es la familia que tiene más interacciones
fuertes con las otras, presentando 13 interacciones por lo que se infiere que tiene un papel como
organizadora a pesar de sólo presentarse en la red del hombre. Esta familia se ha encontrado en otros
estudios como un componente activo de la microbiota intestinal y fecal debido a su capacidad de
adaptarse a los diferentes taxa que pueden integrar a la comunidad, además de que se ha demostrado
que presentan una actividad antibacteriana considerable y una capacidad de resistencia a los antibióticos
(Peris-Bondia, 2011; Shaw ​ et al ​., 2011).
Al contrastar la red generada para la comunidad del hombre y de la mujer podemos observar que a
pesar de que no observamos a los mismos taxa como organizadores, se observa una proporción similar
de relaciones positivas y negativas. Cabe destacar que en nuestro estudio esto puede verse fuertemente
relacionado con la simplicidad del modelo elegido (sólo 14 OTU’s), ya que se ha reportado que la
exclusión de OTU’s raros en la construcción de redes puede tener un efecto importante en las
predicciones sobre el comportamiento de la comunidad​.
yt

![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/MetaMis/Interacciones%20por%20OTUs%20modelados.JPG)

Fig 8. Proporción de interacciones al modelar distinto número de OTU’s en cada red
NetAn. Se observa que aún aumentar el número de OTU’s considerados en el modelo, se mantiene una proporción


Para concluir el análisis de las redes de interacción que MetaMis nos proporciona se corrieron
ambas (masculina y femenina) con el script NetAn el cual permite ver estadísticas elementales
que nos brindan mayor comprensión sobre la dinámica y la información retratada por la
interacción en la comunidad.

Red ​ ​ Femenina

![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/NetAn/F%20gut/F_gut_EDGE_14_directed_network.png)

Fig 9. Red de interacción femenina filtrada por NetAn.

Random Analysis Results, Mean Measures:			runs(100) 
 - [/] order:	14 
 - [/] size:	30 
 - [u] diameter:	3.17 
 - [u] radius:	1.93 
 - [d] density:	0.1648351648351646 
 - [d] mean degree:	2.1428571428571406 
 - [d] clustering coefficient:	0.15575586768389907 
 - [/] maximum in degree:	4.55 
 - [/] maximum out degree:	4.67 
 - [d] hubs with max in degree:	1.65 
 - [d] hubs with max out degree:	1.6 
 - [u] modularity:	0.23909913055044274 
 - [u] coverage:	0.5956093245196693 
 - [u] performance:	0.7710989010989004 
 - [u] number of communities:	3.35 
 - [/] number of connected components:	1.14 
 - [d] number of strongly connected components:	3.96 
 - [u] number of cycles in cycle basis:	14.7 



- [u] undirected associated graph 
- [d] directed graph 
- [/] both undirected and directed 


![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/NetAn/F%20gut/F_gut_EDGE_14_distribution_indegree.png)
![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/NetAn/F%20gut/F_gut_EDGE_14_distribution_outdegree.png)


Fig 10. Estadísticas de outin degree de la gráfica femenina. La distribución indegree reflejan el número de conexiones
dirigidas hacia cada vértice y las del outdegree el número de interacciones que salen de cada vértice

La mayoría de los vértices de nuestra gráfica no interactúan con otras especies (dado que tenemos
11 vértices con out-degree 0) y 3 vértices con out-degree 7, 11 y 12 respectivamente.
De lo anterior podemos interpretar que 2 de los vértices que si interactúan presentan
comportamientos dominantes en la red, mientras que el tercero solo lo hace con la mitad.
De las estadísticas anteriores podemos notar que hay una especie en nuestra interacción que
muestra un comportamiento dominante con respecto al out-degree que la conecta con el resto de
los vértices (a saber hay un vértice que interactúa con 12 de los 14 que hay presentes en la red).
El ​ clustering coefficient ​en este análisis es bajo, nos indica la ausencia de algún nodo “acaparador”
en el que recaigan todas las interacciones, por lo que éstas están distribuidas.

El valor ​ density ​(0.164...) nos indica que la red no es robusta contra perturbaciones, ya que al ser
un valor bajo nos indica la ausencia de clados o nodos altamente conectados (entre más cercano a
1 más densa y por ende más estable la red es).
Interpretando el valor de modularidad ​(0.2390...) que sugiere una preferencia por interacciones
competitivas dentro del mismo sistema (entre más cercano a 1 mayor es la estabilidad en la red y
entre más cercano a 0 significa que más elementos de la red interactúan entre sí).
Red ​ ​ Masculina

![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/NetAn/M%20gut/M_gut_EDGE_14_directed_network.png)

Fig 11. Red de interacción masculina filtrada por NetAn.

Random Analysis Results, Mean Measures:			runs(100) 
 - [/] order:	14 
 - [/] size:	30 
 - [u] diameter:	3.28 
 - [u] radius:	1.93 
 - [d] density:	0.1648351648351646 
 - [d] mean degree:	2.1428571428571406 
 - [d] clustering coefficient:	0.1533276633536706 
 - [/] maximum in degree:	4.59 
 - [/] maximum out degree:	4.73 
- [d] hubs with max in degree:	1.77 
 - [d] hubs with max out degree:	1.56 
 - [u] modularity:	0.23874454027679082 
 - [u] coverage:	0.6077017051913604 
 - [u] performance:	0.7683516483516479 
 - [u] number of communities:	3.25 
 - [/] number of connected components:	1.12 
 - [d] number of strongly connected components:	4.49 
 - [u] number of cycles in cycle basis:	14.85 


- [u] undirected associated graph 
- [d] directed graph 
- [/] both undirected and directed 


![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/NetAn/M%20gut/M_gut_EDGE_14_distribution_indegree.png)
![alt text](https://github.com/ebooshi/Gen-mica-Computacional/blob/master/Proyecto/Outputs/NetAn/M%20gut/M_gut_EDGE_14_distribution_outdegree.png)

Fig 12. Estadísticas del outin degree de la gráfica masculina. La distribución indegree reflejan el número 
de conexiones dirigidas hacia cada vértice y las del outdegree el número de interacciones que salen de cada vértice

Para el caso de la red de interacciones en el tracto masculino se tiene un comportamiento distinto,
10 de los 14 vértices no poseen aristas dirigidas hacía ninguna otra familia, mientras que hay 4 que
poseen 2, 4, 11 y 13 aristas dirigidas respectivamente.

De nueva cuenta, hay una especie que tiene un comportamiento dominante en la red ya que esta
está conectada con 13 de los 14 vértices. Una familia con un comportamiento menos agresivo
conectada a 11 de los 14 vértices y 2 pequeñas familias conectadas a 2 de los 14 vértices y 4 de
los 14 vértices respectivamente (estas últimas dos familias tienen un comportamiento menos
prominente).
El valor del coeficiente de agrupamiento (​ clustering coefficient) ​se asocia con redes que presentan
un mayor número de focos nodales o taxa organizadores, por lo que las perturbaciones de estos
pueden tener un efecto desequilibrador en la comunidad. En el caso de red de las dos redes este
valor bajo denota que los taxa previamente considerados como determinantes en la red pueden no
tener un efecto tan fuerte.
A partir del análisis realizado por NetAn mediante la reconstrucción de redes aleatorias no dirigidas
podemos observar que la modularidad (o el grado en el que los bordes se distribuyen dentro, en
lugar de entre distintos conjuntos de nodos) asignado para ambas comunidades tuvo un valor
positivo, el cual a menudo se asocia con interacciones restringidas a ciertos grupos de la
comunidad.
Como se puede observar las estadísticas de la red aleatoria generada tanto para la muestra del
tracto masculino como femenino presentan en los mismos comportamientos y más aún valores
similares en los coeficientes y estadísticos.
El valor similar de las métricas entre ambas redes es congruente con resultados previamente
reportados sobre una correlación significativa que presentan estas medidas topológicas entre sí
(particularmente aquellas sobre la centralidad) y entre redes de interacción de comunidades del
mismo origen, sin embargo esto no refleja que dos métricas tienen propiedades idénticas y aún
puedan divergir en diferentes modelos.

### 6. Conclusiones
De la información recopilada y procesada de ambas muestras intestinales pudimos observar
variación entre ellas, probablemente debido a un número limitado de elementos y tiempos distintos
de muestreo (15 meses para la muestra masculina y 6 meses para la muestra femenina), 
así como el bajo control sobre el tratamiento de los individuos analizados(hábitos alimenticios, 
lugares frecuentados, hábitos de higiene etc.), a pesar de esto, los datos proporcionados
mostraron proporciones similares en la cantidad de OTUs de las principales familias que se han 
reportado como parte de nuestro tracto digestivo, por lo que las diferencias marcadas probablemente 
sean por la falta de control en la toma de los datos. 

La dinámica de interacción y estadísticas observadas tanto por ​ MetaMis ​y ​ NetAn
nos brindaron una perspectiva mucho más completa para poder compararlas.
Por lo que los resultados del análisis de ambas comunidades bacterianas nos permite afirmar que
se presenta una dinámica de interacción estructuralmente similar en el sujeto mujer y en el hombre.
Los datos proporcionados de los grupo de mujeres y hombres mostraron proporciones similares en
familias que se han reportado anteriormente como parte de nuestro tracto digestivo, por lo que las
diferencias marcadas entre las familias probablemente sean por la falta de control en la toma de los
datos y la diferencia de tiempo.

El software de MetaMIS proporcionó los datos de una red de interacciones en la microbiota intestinal; 
dicha red, en conjunto con el script de NetAn, nos brinda información de mayor comprensión acerca de la 
dinámica en las comunidades, con el fin de hacer un análisis biológico de las interacciones en el microbioma. 
Los resultados de los análisis computacionales y estadísticos demostraron que la estructura de las interacciones
es similar tanto en el hombre como en la mujer, a pesar que hubo diferencias en la cantidad de OTUs registrados 
y la diversidad de familias a las que estos pertenecen.
Se registró una proporción importante de mutualismo dada por familias indicadoras de microbiota. Se mostró la 
importancia de algunos OTUS con baja abundancia pero con papeles importantes en las interacciones con otros OTU,
esto reafirma las utilidades de MetaMis al proporcionar las predicciones de interacciones.


### 7. Referencias
Blondel, V. D., Guillaume, J. -L., Lambiotte, R., & Lefebvre, E. (2008). Fast unfolding of communities in
large networks. ​ Journal of Statistical Mechanics Theory and Experiment, 2008 ​(10), 1–12.
Caporaso, J. G., Lauber, C. L., Costello, E. K., Berg-Lyons, D., Gonzalez, A., Stombaugh, J., Knights, D.,
Gajer, P., Ravel, J., Fierer, N., Gordon, J. I., & Knight, R. (2011). Moving pictures of the human
microbiome. ​ Genome biology ​, ​ 12 ​(5), R50. httpsdoi.org10.1186gb-2011-12-5-r
Danneskiold-Samsøe, N. B., Dias de Freitas Queiroz Barros, H., Santos, R., Bicas, J. L., Cazarin, C. B.
B., Madsen, L., Kristiansen, K., Pastore, G. M., Brix, S., & Maróstica Júnior, M. R. (2019).
Interplay between food and gut microbiota in health and disease. In ​ Food Research International
(Vol. 115, pp. 23–31). Elsevier Ltd. ​httpsdoi.org10.1016j.foodres.2018.07.
Donaldson, G. P., Lee, S. M., & Mazmanian, S. K. (2015). Gut biogeography of the bacterial microbiota.
In ​ Nature Reviews Microbiology (Vol. 14, Issue 1, pp. 20–32). Nature Publishing Group.
httpsdoi.org10.1038nrmicro
Fan, Y., & Pedersen, O. (2021). Gut microbiota in human metabolic health and disease. In ​ Nature
Reviews Microbiology (Vol. 19, Issue 1, pp. 55–71). Nature Research.
httpsdoi.org10.1038s41579-020-0433-
Ficetola, G. F., Pansu, J., Bonin, A., Coissac, E., Giguet-Covex, C., De Barba, M., ... Taberlet, P. (2014).
Replication levels, false presences and the estimation of the presenceabsence from eDNA
metabarcoding data. Molecular Ecology Resources, 15(3), 543–556.
doi10.11111755-0998.
Galhardo, M., Foneca, N., Egeter, B., Paupério, J., Ferreira, S., Oxelfelt, F., ... & Beja, P. (2018).
Deliverable 4.5 (D4. 5) Protocol for the processing of DNA sequence data generated by next-gen
platforms, EnMetaGen project (Grant Agreement No 668981).
Gerritsen, J., Smidt, H., Rijkers, G. T., & de Vos, W. M. (2011). Intestinal microbiota in human health
and disease the impact of probiotics. ​ Genes & nutrition ​, ​ 6 ​(3), 209–240.
httpsdoi.org10.1007s12263-011-0229-
Huttenhower, C., Gevers, D., Knight, R., Abubucker, S., Badger, J. H., Chinwalla, A. T., Creasy, H. H.,
Earl, A. M., Fitzgerald, M. G., Fulton, R. S., Giglio, M. G., Hallsworth-Pepin, K., Lobos, E. A.,
Madupu, R., Magrini, V., Martin, J. C., Mitreva, M., Muzny, D. M., Sodergren, E. J., ... White,
O. (2012). Structure, function and diversity of the healthy human microbiome. ​ Nature ​,
486 ​(7402), 207–214. ​httpsdoi.org10.1038nature
Kusada, H., Kameyama, K., Meng, X. Y., Kamagata, Y., & Tamaki, H. (2017). Fusimonas intestini gen.
nov., sp. nov., a novel intestinal bacterium of the family Lachnospiraceae associated with
diabetes in mice. ​ Scientific reports ​, ​ 7 ​(1), 1-9.
Matos, R. C., & Leulier, F. (2014). Lactobacilli-Host mutualism learning on the fly. Microbial cell
factories, 13(1), 1-8.
Peris-Bondia, F., Latorre, A., Artacho, A., Moya, A., & D'Auria, G. (2011). The active human gut
microbiota differs from the total microbiota. PloS one, 6(7), e22448.
Saxena, R., & Sharma, V. K. (2016). A Metagenomic Insight into the Human Microbiome Its
Implications in Health and Disease. In ​ Medical and Health Genomics (pp. 107–119). Elsevier
Inc. ​httpsdoi.org10.1016B978-0-12-420196-5.00009-
Scher, J. U., Sczesnak, A., Longman, R. S., Segata, N., Ubeda, C., Bielski, C., Rostron, T., Cerundolo, V.,
Pamer, E. G., Abramson, S. B., Huttenhower, C., & Littman, D. R. (2013). Expansion of
intestinal Prevotella copri correlates with enhanced susceptibility to arthritis. ​ eLife ​, ​ 2 ​, e01202.
httpsdoi.org10.7554eLife.
Segata, N., Boernigen, D., Tickle, T. L., Morgan, X. C., Garrett, W. S., & Huttenhower, C. (2013).
Computational meta'omics for microbial community studies. ​ Molecular systems biology ​, ​ 9 ​, 666.
httpsdoi.org10.1038msb.2013.
Spinler, J. K. (2015). Corynebacteriaceae. In ​ Encyclopedia of Metagenomics (pp. 112–119). Springer US.
httpsdoi.org10.1007978-1-4899-7475-4_
Yatsunenko, T., Rey, F. E., Manary, M. J., Trehan, I., Dominguez-Bello, M. G., Contreras, M., Magris,
M., Hidalgo, G., Baldassano, R. N., Anokhin, A. P., Heath, A. C., Warner, B., Reeder, J.,
Kuczynski, J., Caporaso, J. G., Lozupone, C. A., Lauber, C., Clemente, J. C., Knights, D., ...
Gordon, J. I. (2012). Human gut microbiome viewed across age and geography. In ​ Nature (Vol.
486, Issue 7402, pp. 222–227). Nature Publishing Group. ​httpsdoi.org10.1038nature

#### Referencias Software
Shaw, G. T. W., Pao, Y. Y., & Wang, D. (2016). MetaMIS A metagenomic microbial interaction
simulator based on microbial community profiles. ​ BMC Bioinformatics ​, ​ 17 ​(1), 488.
httpsdoi.org10.1186s12859-016-1359-
De Anda, V., Zapata-Peñasco, I., Blaz, J., Poot-Hernández, A. C., Contreras-Moreira, B.,
González-Laffitte, M., Gámez-Tamariz, N., Hernández-Rosales, M., Eguiarte, L. E., & Souza, V.
(2018). Understanding the Mechanisms Behind the Response to Environmental Perturbation in
Microbial Mats A Metagenomic-Network Based Approach. ​ Frontiers in microbiology ​, ​ 9 ​, 2606.
httpsdoi.org10.3389fmicb.2018.
httpsgithub.comvaldeandaNetAn
