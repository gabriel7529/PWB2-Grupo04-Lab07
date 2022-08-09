<div align="center">
<table>
<theader>
<tr>
<td><img src="https://github.com/elopezqu/Lab2_Team3K/blob/main/epis.png" alt="EPIS" style="width:50%; height:auto"/></td>
<th>
<span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
<span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
<span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
</th>
<td><img src="https://github.com/elopezqu/Lab2_Team3K/blob/main/abet.png" alt="ABET" style="width:50%; height:auto"/></td>
</tr>
</theader>
<tbody>
<tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
<tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
</tbody>
</table>
</div>
<div align="center">
<h3>INFORME DE LABORATORIO</h3>
</div>
<table>
<theader>
<tr><th colspan="6" bgcolor="red">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRACTICA:</td><td colspan="5"> DJANGO - REST</td></tr>
<tr><td>NÚMERO DE PRÁCTICA:</td><td>Practica de Laboratorio 07</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td></tr>
<tr><td>FECHA DE PRESENTACIÓN:</td><td>09/08/2022</td><td>HORA DE PRESENTACIÓN:</td><td colspan="3">11:30 p.m.</td></tr>
<tr><td>INTEGRANTES:</td><td colspan="3">- Edson Joel López Quispe<br>- Gabriel Steven Machicao Quispe<br>- Fernando Coyla Alvarez</td><td>NOTA:</td><td>...</td></tr>
<tr><td>DOCENTE:</td><td colspan="5">Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</td></tr>
</tbody>
</table>
<table>
<theader>
<tr><th>SOLUCIÓN Y RESULTADOS</th></tr>
</theader>
<tbody>
<tr><td>I. SOLUCIÓN DE EJERCICIOS/PROBLEMAS:
<p>...</p>
<h2><strong>Creación del cliente (GET)</strong></h2>
<h3>1. Creación de la vista </h3>
La vista se crea en el archivo <em>views.py</em> en la ruta Apps/Aplicación1<br>
<img src="imagenes_cliente/views.png"><br>
La vista se escribe en forma de función, basicamente renderiza el archivo index.html, que se procedera a crear posteriormente
<h3>2. Creación de la ruta de la vista</h3>
Se crea el archivo <em>urls.py</em> en la ruta Apps/Aplicación1 y se escribe los siguiente<br>
<img src="imagenes_cliente/urls.png"><br>
Este código le asigna una ruta a la vista previamente creada.
Posteriormente se edita el archivo <em>urls.py</em> de Proyecto<br>
<img src="imagenes_cliente/urls2.png">
<h3>3. Creación del archivo<em>index.html</em></h3>
Para esto se crea una carpeta <em>templates</em> en la ruta Apps/Aplicación1<br>
<h3>4. Creación de la petición Ajax </h3>
<img src="imagenes_cliente/html.png"><br>
A travéz del método Get se le hace la petición al url que dejo el Rest y se imprime en consola en forma de Array<br>
<img src="imagenes_cliente/consola.png"><br>
Se agrega contenido al html<br>
<img src="imagenes_cliente/body.png"><br>
Asi se veria la parte del cliente<br>
<img src="imagenes_cliente/cli.png"><br>
  </td></tr>
</tbody>
</table>

<table>
<theader>
  <tr><td>RETROALIMENTACIÓN GENERAL</td><br><tr>
</theader>
<tbody>
  <tr><td><p>...</p></td></tr>
</tbody>
</table>

<table>
<theader>
<tr><td>REFERENCIAS Y BIBLIOGRAFÍA</td><tr>
</theader>
<tbody>
<tr><td>...</tr></td>
</tbody>
</table>
