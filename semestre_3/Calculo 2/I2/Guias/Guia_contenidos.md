# 📘 GUÍA DE ESTUDIO TEÓRICA MAT1620: CÁLCULO II (EDICIÓN APLICADA)

Este documento es un tratado analítico de los teoremas de Cálculo II. Su objetivo es dotar al estudiante del criterio matemático para saber exactamente **cuándo** utilizar una herramienta, **por qué** funciona y **cómo** se aplica rigurosamente en escenarios teóricos y prácticos.

---

## 1. SUCESIONES Y SERIES: EL CONTROL DEL INFINITO

### 1.1 Criterio de la Razón (Teorema de D'Alembert)
* **Anatomía Teórica:** Extrae el "factor de contracción" asintótico de la serie evaluando $\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = L$.
* **Contexto de Utilización:** Se debe utilizar **obligatoriamente** cuando el término general $a_n$ contiene factoriales ($n!$) o la mezcla de factoriales con constantes exponenciales ($c^n$). Nunca debe usarse en funciones puramente racionales (polinomios) o logarítmicas, ya que arrojarán un límite $L=1$, dejando el caso en un punto ciego analítico.
* **Mecánica de Aplicación Analítica:**
  1. Construir la fracción de recurrencia $\left| \frac{a_{n+1}}{a_n} \right|$.
  2. Expandir los términos factoriales algebraicamente (ej. $(n+1)! = (n+1)n!$) para forzar la cancelación masiva con el denominador.
  3. Agrupar las potencias de igual base y aplicar propiedades de límites.
  4. Si $L < 1$, se decreta convergencia absoluta por dominancia de contracción. Si $L > 1$, divergencia.

### 1.2 Criterio de la Raíz (Teorema de Cauchy)
* **Anatomía Teórica:** Asume una estructura exponencial subyacente $a_n \approx L^n$. El operador límite-raíz $\lim_{n \to \infty} \sqrt[n]{|a_n|} = L$ actúa como un escalpelo que aísla la base asintótica.
* **Contexto de Utilización:** Es la herramienta exclusiva y definitiva cuando **todo el término general** (o su gran mayoría) se encuentra elevado a potencias que dependen de $n$ (como $n$, $n^2$, o funciones compuestas de $n$). Usar el criterio de la razón aquí resultaría en un álgebra insoluble.
* **Mecánica de Aplicación Analítica:**
  1. Aplicar la raíz $n$-ésima a todo el valor absoluto del término general.
  2. Simplificar los exponentes multiplicando las potencias (ej. $(f(n))^{n^2/n} = (f(n))^n$).
  3. Resolver el límite resultante, que a menudo desembocará en la definición de Euler $\lim (1 + x/n)^n = e^x$. Evaluar $L$ contra 1.

### 1.3 Criterio de Leibniz para Series Alternantes
* **Anatomía Teórica:** Garantiza que una oscilación que se atenúa asintóticamente hacia cero atrapará forzosamente el límite en un punto escalar finito.
* **Contexto de Utilización:** Se aplica siempre que aparezca un alternador de signos explícito $(-1)^n$ o $\cos(n\pi)$ y se necesite clasificar la convergencia como *condicional* (cuando el valor absoluto diverge, como en la serie armónica alternada). Es mandatorio usarlo al probar la convergencia en los extremos cerrados de un intervalo de convergencia.
* **Mecánica de Aplicación Analítica:**
  1. Separar el alternador $(-1)^n$ y aislar la sucesión estrictamente positiva $b_n$.
  2. Demostrar monotonía decreciente: algebraicamente verificando que $b_{n+1} \le b_n$, o derivando la función continua asociada $f(x)$ y demostrando que $f'(x) < 0$ para $x$ suficientemente grande.
  3. Demostrar analíticamente que $\lim_{n \to \infty} b_n = 0$.

### 1.4 Teorema de Taylor y el Resto de Lagrange
* **Anatomía Teórica:** Fuerza a un polinomio de grado infinito a compartir la topología y curvatura de una función trascendente en un punto $a$, igualando todas sus derivadas sucesivas.
* **Contexto de Utilización:** Se utiliza para integrar funciones que carecen de antiderivada elemental (como $\int \sin(x^2)dx$ o $\int e^{-x^2}dx$), para resolver límites indeterminados complejos sin utilizar L'Hôpital, y para estimaciones numéricas exactas que exigen un control riguroso de error.
* **Mecánica de Aplicación Analítica:**
  1. **Para representar/integrar:** Partir de una serie de Maclaurin conocida, inyectar el nuevo argumento por composición (ej. reemplazar $x$ por $x^2$), multiplicar por coeficientes externos y luego operar término a término (integrar o derivar la serie de potencias).
  2. **Para Acotar el Error (Resto de Lagrange):** Dada la fórmula $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$, se asume un escenario catastrófico. Se encuentra la cota superior $M$ máxima que puede tomar la derivada $(n+1)$-ésima en todo el intervalo entre el centro $a$ y el punto de evaluación $x$. Se inyecta $M$ en la fórmula para decretar que el error *jamás* superará ese valor absoluto.

### 1.5 Estrategias Analíticas para Representación Funcional e Integración mediante Series
* **Anatomía Teórica:** El Teorema de Representación establece que, estrictamente dentro de su radio de convergencia absoluto, una serie de potencias posee convergencia uniforme. Esta topología garantiza que la sumatoria infinita se comporte analíticamente como un polinomio, permitiendo que operadores lineales como el diferencial ($d/dx$) y la integral ($\int$) penetren la sumatoria y actúen término a término sin alterar la igualdad topológica.
* **Contexto de Utilización:** Obligatorio al enfrentar integrales carentes de primitivas elementales (ej. $\int e^{-x^2} dx$, $\int \frac{\sin x}{x} dx$) o al exigir el desarrollo en serie de funciones racionales compuestas, donde derivar $n$ veces para construir el polinomio de Taylor mediante la definición general sería algebraicamente extenuante e inviable.
* **Consejos y Mecánica de Aplicación Analítica:**
  1. **El Enmascaramiento Geométrico (Piedra Rosetta):** La serie geométrica fundamental es $\frac{1}{1-u} = \sum_{n=0}^{\infty} u^n$. Si te enfrentas a una función racional $f(x) = \frac{C}{A \pm Bx^k}$, el objetivo analítico es forzar el denominador a la estructura geométrica base. Factoriza la constante $A$ del denominador para obligar la aparición de un "1": obteniendo $\frac{C/A}{1 - (\mp \frac{B}{A}x^k)}$. Luego, inyecta la sustitución $u = \mp\frac{B}{A}x^k$ en la sumatoria original.
  2. **Integración Término a Término para "Integrales Imposibles":** El algoritmo infalible exige: (a) Aísla la función trascendente interna (ej. $\cos(x^2)$). (b) Evalúa la composición de variable $u = x^2$ dentro de su serie de Maclaurin notable ya conocida. (c) Ingresa cualquier factor externo que multiplicaba o dividía (ej. multiplicar por $x^3$) distribuyéndolo algebraicamente *dentro* de la sumatoria. (d) Al colapsar todo en una única potencia $x^m$, aplica el operador integral a $x^m$ transformándolo en $\frac{x^{m+1}}{m+1}$.
  3. **Derivación como Operador Inverso:** Ante funciones cuyo denominador exhibe multiplicidad (ej. $\frac{1}{(1-x)^2}$ o $\frac{x}{(1+x^2)^2}$), el Teorema de Taylor directo no es la ruta óptima. Observa la arquitectura topológica: la primera función es exactamente la derivada de $\frac{1}{1-x}$. Por consiguiente, toma la serie geométrica original $\sum x^n$, aplica el operador derivada en su interior para obtener $\sum n x^{n-1}$, y habrás reconstruido la serie buscada evadiendo operaciones extremas.
  4. **Descomposición por Fracciones Parciales:** Para funciones racionales irreducibles de grado superior (ej. $\frac{x+1}{x^2-3x+2}$), aplica sistemáticamente la expansión en fracciones parciales. Posteriormente, aplica el "Enmascaramiento Geométrico" (Paso 1) de forma completamente independiente a cada fracción simple obtenida. En el paso conclusivo, unifica ambas series agrupando algebraicamente el coeficiente general de $x^n$.

---

## 2. GEOMETRÍA EN $\mathbb{R}^3$: LA ESTRUCTURA ESPACIAL

### 2.1 Producto Punto y Proyecciones
* **Contexto de Utilización:** Se utiliza para dictaminar ortogonalidad, calcular ángulos entre vectores o planos, y aislar componentes vectoriales (cuánto de la fuerza A actúa en la dirección de B).
* **Mecánica de Aplicación Analítica:** Se calcula la suma del producto de las componentes. Si $\vec{a} \cdot \vec{b} = 0$, los elementos son matemáticamente ortogonales. Para ángulos, se despeja $\theta = \arccos(\frac{\vec{a} \cdot \vec{b}}{||\vec{a}|| ||\vec{b}||})$.

### 2.2 Producto Cruz y Planos
* **Contexto de Utilización:** Fundamental e insustituible cuando se necesita generar un vector que sea perpendicular a un sistema 2D completo. Es el núcleo para construir las ecuaciones de cualquier plano o calcular áreas espaciales.
* **Mecánica de Aplicación Analítica:** 1. Extraer dos vectores linealmente independientes que "vivan" en el plano.
  2. Ejecutar el determinante matricial (Producto Cruz) para obtener el Vector Normal $\vec{n} = \langle A, B, C \rangle$.
  3. Inyectar este vector en la ecuación del plano $A(x-x_0) + B(y-y_0) + C(z-z_0) = 0$.

### 2.3 Teorema del Producto Mixto (Distancias Alabeadas)
* **Contexto de Utilización:** Se aplica obligatoriamente cuando se pide la distancia mínima absoluta entre dos rectas alabeadas (rectas 3D que no son paralelas ni se intersecan).
* **Mecánica de Aplicación Analítica:**
  1. Identificar un punto de anclaje y el vector director de cada recta ($\vec{v}_1, \vec{v}_2$).
  2. Cruzar ambos directores para definir el piso topológico: $\vec{n} = \vec{v}_1 \times \vec{v}_2$. La magnitud de este vector es el "Área basal".
  3. Construir el vector de conexión de puntos $\vec{P_1P_2}$.
  4. Realizar el producto punto entre la conexión y la normal para obtener el "Volumen". La división de Volumen sobre Área arroja algebraicamente la distancia mínima.

---

## 3. FUNCIONES DE VARIAS VARIABLES: TOPOLOGÍA DEL LÍMITE

### 3.1 Teorema de los Límites por Trayectorias (No Existencia)
* **Anatomía Teórica:** Postula que si un límite topológico existe en $\mathbb{R}^n$, debe converger invariablemente al mismo valor escalar sin importar el sendero unidimensional a través del cual el límite se evalúe.
* **Contexto de Utilización:** Es el primer ataque ante un límite de la forma $0/0$ en $\mathbb{R}^2$. Especialmente indicado cuando las potencias algebraicas del numerador y del denominador presentan grados divergentes que no pueden simplificarse factorizando.
* **Mecánica de Aplicación Analítica:**
  1. Evaluar el límite acercándose por los ejes coordenados ($x=0$ y luego $y=0$) o por la familia de rectas $y = mx$. Si arroja un valor (generalmente 0), se establece la "cota a romper".
  2. **Análisis de Asimetría (La clave):** Mirar los exponentes sumados en el denominador (ej. $x^4 + y^2$).
  3. Plantear una trayectoria de curva polinomial $y = x^k$ (o $x = y^k$) diseñada estrictamente para igualar y homogeneizar esos exponentes en el denominador (en el ejemplo, forzamos $y = x^2$ para que $y^2 = x^4$).
  4. Evaluar el límite por esta curva. Si el álgebra se simplifica y arroja un valor escalar distinto al paso 1, se concluye la ruptura topológica y la no existencia del límite.

### 3.2 Teorema de Acotamiento (El Sándwich)
* **Anatomía Teórica:** Obliga a una función de comportamiento caótico a converger si su envoltura topológica (cota superior e inferior) colapsa hacia un valor idéntico en el punto de acumulación.
* **Contexto de Utilización:** Se utiliza cuando se sospecha firmemente que el límite **SÍ** existe (generalmente es 0), lo cual suele ocurrir cuando el grado absoluto del numerador es marcadamente superior al del denominador, o cuando la expresión involucra entidades trigonométricas acotadas por naturaleza ($\sin$, $\cos$, $\arctan$).
* **Mecánica de Aplicación Analítica:**
  1. Identificar el "agente caótico" y establecer su frontera topológica estricta. (ej. $|\sin(1/xy)| \le 1$, o la fracción espacial $\frac{x^2}{x^2+y^2} \le 1$).
  2. Multiplicar toda la inecuación por el término algebraico restante de la función (ej. si la función era $r^3 \frac{\cos^2\theta}{\dots}$, aislar el $r^3$).
  3. Aplicar el límite cuando la variable independiente tiende a 0. Como $0 \le |f(x,y)| \le (\text{Término que tiende a 0}) \times 1$, la función original es empujada irrefutablemente a 0.

---

## 4. CÁLCULO DIFERENCIAL MULTIVARIABLE

### 4.1 El Vector Gradiente ($\nabla f$) y Derivada Direccional
* **Anatomía Teórica:** El gradiente es la matriz jacobiana de una función escalar. Contiene toda la información del cambio local.
* **Contexto de Utilización:** Se requiere para calcular tasas de cambio en senderos no paralelos a los ejes (derivada direccional), para encontrar la senda de máxima pendiente (o descenso) en problemas físicos (termometría, topografía), y para dictaminar la normal geométrica a cualquier superficie.
* **Mecánica de Aplicación Analítica:**
  1. Calcular el gradiente construyendo el vector de derivadas parciales: $\nabla f = \langle f_x, f_y, f_z \rangle$.
  2. **Para tasas de cambio diagonales:** Definir el vector dirección dado y normalizarlo obligatoriamente (convertirlo en un vector unitario $\vec{u}$). Ejecutar el producto punto $D_{\vec{u}}f = \nabla f \cdot \vec{u}$.
  3. **Para máxima pendiente:** La dirección de máximo ascenso es exactamente el vector $\nabla f$. Su magnitud $||\nabla f||$ es el valor escalar de la máxima tasa de cambio.

### 4.2 Diferenciabilidad y Planos Tangentes
* **Anatomía Teórica:** Una superficie diferenciable puede ser suplantada localmente por su Plano Tangente de Taylor sin errores de primer orden. Debido a que el gradiente es un invariante topológicamente normal a las curvas de nivel, actúa como armazón del plano.
* **Contexto de Utilización:** Obligatorio para parametrizar la "cubierta lineal" de una superficie 3D en un punto específico, o para calcular la recta normal que atraviesa la superficie de forma perpendicular.
* **Mecánica de Aplicación Analítica:**
  1. Convertir la ecuación de la superficie en una función de nivel implícita $F(x,y,z) = 0$ (pasando todos los términos a un lado de la ecuación).
  2. Obtener el gradiente $\nabla F$ y evaluarlo en el punto $(x_0, y_0, z_0)$ para "congelar" la normal escalar $\vec{n} = \langle A, B, C \rangle$.
  3. Construir analíticamente el plano: $A(x-x_0) + B(y-y_0) + C(z-z_0) = 0$.

### 4.3 La Regla de la Cadena Multivariable
* **Anatomía Teórica:** Basada en el Principio de Superposición del Diferencial, decreta que el cambio total de una variable dependiente se compone de la sumatoria lineal de los cambios parciales propagados a través de todas las rutas intermedias conectadas.
* **Contexto de Utilización:** Se usa para medir derivadas sobre cinemática de curvas (un punto móvil $x(t), y(t)$ barriendo un campo escalar), ecuaciones en derivadas parciales (EDP), o cambios de sistemas de coordenadas (polares a cartesianas). Es vital para derivar sin inyectar masivamente variables.
* **Mecánica de Aplicación Analítica:**
  1. Construir un árbol o grafo dirigido para trazar rutas desde la variable superior (ej. $w$) hasta la variable objetivo inferior (ej. $t$).
  2. Por cada camino viable, plantear la multiplicación de los diferenciales (ej. un camino que pasa por $x$ es $\frac{\partial w}{\partial x} \frac{dx}{dt}$).
  3. Sumar algebraicamente todos los productos de todos los caminos. Evaluar las funciones internas de ser necesario para dejar el resultado en los términos solicitados.