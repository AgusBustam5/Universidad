# Super-Guía de Preparación Avanzada: MAT1620 Cálculo II (Versión Extendida)

Esta guía ha sido expandida para incluir una mayor variedad de problemas de alta dificultad, extraídos de interrogaciones históricas, apuntes de ayudantías (2026) y problemas propuestos del libro Stewart.

---

## Temática 1: Sucesiones y Series de Potencias

### Subtema 10: Criterios de Convergencia Numérica
* **Ejercicio 1.1:** Determine si la serie $\sum_{n=10}^{\infty} \frac{\cos(n\pi)}{\sqrt{n}}$ es condicionalmente convergente, absolutamente convergente o divergente.
* **Ejercicio 1.2:** Sea $a_1=1$ y $a_{n+1} = \frac{2 - \arctan(n^2)}{\sqrt{n}} a_n$. Determine si $\sum_{n=1}^{\infty} a_n$ converge o no.
* **Ejercicio 1.3:** Analice la convergencia de $\sum \frac{(-1)^n}{\ln(n)}$ y determine si la convergencia es absoluta o condicional.
* **Ejercicio 1.4:** Aplique el criterio de la integral para determinar para qué valores de $p$ converge la serie $\sum_{n=2}^\infty \frac{1}{n(\ln n)^p}$.
* **Ejercicio 1.5:** Use el criterio de comparación al límite para analizar $\sum \frac{n^2 + 1}{n^4 + n^2 + 1}$.
* **[NUEVO] Ejercicio 1.6:** Determine la convergencia de la serie alternante $\sum_{n=1}^{\infty} \frac{(-1)^n \ln(n)}{n^2}$ y evalúe si la convergencia es absoluta usando el criterio de la integral.
* **[NUEVO] Ejercicio 1.7:** Sea la sucesión de Fibonacci $a_{n+1} = a_n + a_{n-1}$. Demuestre que $a_{n+1}/a_n \le 2$ y analice la serie $\sum_{n=1}^\infty \frac{a_n}{3^n}$.
* **[NUEVO] Ejercicio 1.8:** Determine si la serie $\sum_{n=5}^{\infty}\frac{(n^{3}+4)(n-2)}{(n-3)(n^{5}+1)}$ converge usando el criterio de comparación en el límite.

### Subtema 11: Radio e Intervalo de Convergencia
* **Ejercicio 1.11:** Si $k$ es un entero positivo, encuentre el radio de convergencia de la serie $\sum_{n=1}^{\infty} \frac{(n!)^k}{(kn)!} x^n$.
* **Ejercicio 1.12:** Encuentre el intervalo de convergencia de la serie $\sum_{n=1}^{\infty} \frac{(2x-1)^n}{5^n \sqrt{n}}$, analizando la convergencia en los extremos.
* **Ejercicio 1.13:** Determine el intervalo de convergencia de $\sum_{n=0}^{\infty} \frac{(-1)^n}{4^n \sqrt{n+1}}(x-3)^n$.
* **Ejercicio 1.14:** Halle el radio de convergencia de $\sum \frac{n^n}{n!} x^n$.
* **[NUEVO] Ejercicio 1.15:** Determine el radio y el intervalo de convergencia de $\sum_{n=0}^{\infty}(-1)^{n}\frac{x^{2n}}{(2n)!}$.
* **[NUEVO] Ejercicio 1.16:** Determine el intervalo de convergencia de $\sum_{n=1}^{\infty}(\frac{nx}{n+1})^{n}$ evaluando cuidadosamente el comportamiento mediante el criterio de la raíz.
* **[NUEVO] Ejercicio 1.17:** Encuentre el intervalo de convergencia de $\sum_{n=1}^{\infty} \frac{n(x-4)^n}{n^3 + 1}$.

### Subtema 12: Representación, Derivación e Integración
* **Ejercicio 1.21:** Exprese como serie de potencias la integral indefinida $\int x^2 \ln(1+x) dx$.
* **Ejercicio 1.22:** Exprese la función $f(x) = \frac{x+1}{x^3+1}$ como una suma de dos series de potencias centradas en $x=0$.
* **Ejercicio 1.23:** Utilice la representación en serie de $\frac{1}{x^2-x+1}$ para demostrar que $\pi = \frac{3\sqrt{3}}{4} \sum_{n=0}^{\infty} \frac{(-1)^n}{8^n} (\frac{2}{3n+1} + \frac{1}{3n+2})$.
* **Ejercicio 1.24:** Demuestre que $\int_0^x \frac{e^t - 1 - t}{t^2} dt > \frac{x}{2}$ para todo $x > 0$ mediante el uso de series de Taylor.
* **[NUEVO] Ejercicio 1.25:** Encuentre una representación como serie de potencias centrada en $x=0$ para $f(x)=\frac{3}{x^{2}-x-2}$ usando fracciones parciales.
* **[NUEVO] Ejercicio 1.26:** Considere la serie $S(x) = \sum_{n=0}^{\infty}\frac{(-1)^{n}}{2^{2n}(n!)^{2}}x^{2n}$. Muestre que satisface la ecuación diferencial $xS''(x)+S'(x)+xS(x)=0$.
* **[NUEVO] Ejercicio 1.27:** Exprese $f(x)=x \arctan(x^3)$ como serie de potencias e indique su radio de convergencia.

### Subtema 13: Series de Taylor y Maclaurin
* **Ejercicio 1.31:** Determine los tres primeros términos de Maclaurin de $f(x) = \ln(\frac{1+x}{1-x})$ y calcule una serie numérica a partir de ella.
* **Ejercicio 1.32:** Obtenga el desarrollo en serie de potencias para $f(x) = \frac{\ln(1+x^2)}{x}$.
* **Ejercicio 1.33:** Use la serie de Taylor de $\sin(x)$ para encontrar la serie de $f(x) = \frac{\sin(x)}{x}$.
* **Ejercicio 1.34:** Encuentre la serie de Taylor de $F(x) = \int_0^x \frac{\sin(t)}{t} dt$ centrada en $x=0$.
* **[NUEVO] Ejercicio 1.35:** Utilice series de potencias para aproximar $\int_{0}^{\pi} \frac{\sin(x)}{x} dx$ con un error máximo de 0.001. Determine cuántos términos son necesarios.
* **[NUEVO] Ejercicio 1.36:** Encuentre la serie de Maclaurin para $f(x) = x \cos(x^2 / 2)$ e identifique el valor de $f^{(15)}(0)$.
* **[NUEVO] Ejercicio 1.37:** Utilice el desarrollo de Taylor de orden 2 para aproximar el valor de $\sqrt{1.1}$.

---

## Temática 2: Geometría Analítica y Vectorial en $\mathbb{R}^3$

### Subtema 14: Sistemas Coordenados y Vectores
* **Ejercicio 2.1:** Demuestre que $\vec{v}_1 \times (\vec{v}_2 \times \vec{v}_3) + \vec{v}_2 \times (\vec{v}_3 \times \vec{v}_1) + \vec{v}_3 \times (\vec{v}_1 \times \vec{v}_2) = 0$.
* **Ejercicio 2.2:** Determine si existe un vector $\vec{v}$ tal que $\langle 2, -1, 2 \rangle \times \vec{v} = \langle 1, 3, 2 \rangle$.
* **Ejercicio 2.3:** Calcule el ángulo entre las rectas $L_1(t) = \langle 5, -1, 2 \rangle + t\langle 2, 3, 4 \rangle$ y $L_2(t) = \langle 5, -8, 0 \rangle + t\langle -1, 2, -1 \rangle$.
* **[NUEVO] Ejercicio 2.4:** Demuestre la Identidad de Lagrange: $||\vec{a}||^{2}||\vec{b}||^{2}=(\vec{a}\cdot \vec{b})^{2}+||\vec{a}\times \vec{b}||^{2}$.
* **[NUEVO] Ejercicio 2.5:** Considere el triángulo con vértices $A(4,2,0)$, $B(1,3,0)$, $C(1,1,3)$. Determine el vector que une el origen con el punto de intersección de las medianas (baricentro).
* **[NUEVO] Ejercicio 2.6:** Determine las coordenadas del punto de la esfera $x^2 + y^2 + z^2 = 4$ que está más cerca del plano $x+y+z=12$.

### Subtema 15: Producto Punto y Cruz
* **Ejercicio 2.11:** Si el ángulo entre $\vec{u}$ y $\vec{v}$ es $\pi/3$ con $|\vec{u}|=4$ y $|\vec{v}|=7$, calcule $|3\vec{u} - 5\vec{v}|$.
* **Ejercicio 2.12:** Demuestre que la distancia $d$ desde un punto $P$ a la recta $L$ (por $Q$ y $R$) es $d = \frac{|\vec{QR} \times \vec{QP}|}{|\vec{QR}|}$.
* **Ejercicio 2.13:** Calcule el área del paralelogramo definido por vectores posición dados.
* **[NUEVO] Ejercicio 2.14:** Encuentre el ángulo entre los vectores $\vec{u} = 3\hat{i} - 2\hat{j} + \hat{k}$ y $\vec{v} = -\hat{j} - 8\hat{k}$.
* **[NUEVO] Ejercicio 2.15:** Demuestre la identidad del producto escalar de dos productos cruzados: $(\vec{a}\times \vec{b})\cdot(\vec{c}\times \vec{d}) = (\vec{a}\cdot \vec{c})(\vec{b}\cdot \vec{d}) - (\vec{a}\cdot \vec{d})(\vec{b}\cdot \vec{c})$.
* **[NUEVO] Ejercicio 2.16:** Dados los puntos A(1,0,1), B(0,2,2) y C(3,3,0), encuentre el volumen del paralelepípedo sustentado por los vectores formados desde el origen hasta estos puntos.

### Subtema 16: Ecuaciones de Rectas y Planos
* **Ejercicio 2.21:** Encuentre la ecuación del plano que pasa por $(-1, 2, 1)$ y contiene a la recta de intersección de $x+y-z=2$ y $2x-y+3z=1$.
* **Ejercicio 2.22:** Encuentre la ecuación paramétrica de la recta $L$ intersección de $\Pi_1: x+y-3z=0$ y $\Pi_2: -x+2y+2z=1$.
* **Ejercicio 2.23:** Determine la ecuación del plano perpendicular a los planos $2x-y+5z=28$ y $x+3y-z=7$, cuya intersección es $(-1, 5, 7)$.
* **[NUEVO] Ejercicio 2.24:** Halle la ecuación del plano que contiene a la recta de intersección de los planos $2x-y+z=4$ y $x+4y-z=-3$, y que es paralelo a la recta $x-2y+3z=1, 2x+y-z=6$.
* **[NUEVO] Ejercicio 2.25:** Determine la ecuación del plano que es perpendicular a la recta dada por la intersección de los planos $3x-2y+z=7$ y $x+y+2z=5$, y que pasa por el punto (1, -1, 0).
* **[NUEVO] Ejercicio 2.26:** Encuentre la distancia mínima entre las rectas alabeadas $L_1(t) = \langle 1,0,-1 \rangle + t\langle 2,1,0 \rangle$ y $L_2(s) = \langle 0,2,2 \rangle + s\langle 1,-1,1 \rangle$.

---

## Temática 3: Funciones de Varias Variables

### Subtema 17: Dominio de Funciones
* **Ejercicio 3.1:** Determine y grafique el dominio de $f(x,y) = \frac{\ln(x-1) + \sqrt{y-x} + \ln(4-y)}{x^2+2x+1}$.
* **Ejercicio 3.2:** Determine el dominio de $f(x,y) = \sqrt{\frac{x-y}{1-x^2-y^2}}$.
* **Ejercicio 3.3:** Determine el dominio de $f(x,y) = \sqrt{9-x-y^2}$.
* **[NUEVO] Ejercicio 3.4:** Determine y grafique el dominio de $f(x,y) = \sqrt{1-x^{2}} - \sqrt{1-y^{2}}$.
* **[NUEVO] Ejercicio 3.5:** Determine el dominio de $g(x,y) = \ln(9-x^{2}-9y^{2})$ y descríbalo analítica y geométricamente.
* **[NUEVO] Ejercicio 3.6:** Bosqueje el dominio de $h(x,y) = \arcsin(x+y) + \sqrt{x y}$.

### Subtema 18: Gráficas y Curvas de Nivel
* **Ejercicio 3.11:** Grafique la curva de nivel $f(x,y) = -2$ para la función $f(x,y) = \frac{x^2+y^2}{y-4}$.
* **Ejercicio 3.12:** Bosqueje las curvas de nivel para $k=0, 3, 4$ de la función $f(x,y) = \sqrt{9-x-y^2}$.
* **Ejercicio 3.13:** Describa y grafique las curvas de nivel de $g(x,y) = y^2 - 2x^2$ para distintos valores de $k$.
* **[NUEVO] Ejercicio 3.14:** Encuentre el ángulo agudo entre las curvas de nivel $y=x^{1/2}$ e $y=x^{1/3}$ en el punto de intersección (1, 1).
* **[NUEVO] Ejercicio 3.15:** Clasifique la superficie dada por la ecuación $4x^2 - y^2 + z^2 - 8x + 2y + 4 = 0$ completando cuadrados.
* **[NUEVO] Ejercicio 3.16:** Dibuje un mapa de contorno para la función $f(x,y) = e^{-x^2-y^2}$ indicando los valores máximos de las curvas.

### Subtema 19: Límites de Funciones
* **Ejercicio 3.21:** Demuestre que no existe $\lim_{(x,y) \rightarrow (0,0)} \frac{x^2y^2}{x^3+y^3}$ usando las trayectorias $y=x$ e $y = -xe^x$.
* **Ejercicio 3.22:** Estudie el límite $\lim_{(x,y) \rightarrow (0,0)} \frac{x^3y^4}{x^4+y^4}$.
* **Ejercicio 3.23:** Determine si existe $\lim_{(x,y) \rightarrow (0,0)} \frac{x^4y^4}{(x^2+y^4)^3}$ evaluando por la trayectoria $x=y^2$.
* **[NUEVO] Ejercicio 3.24:** Calcule el límite $\lim_{(x,y) \rightarrow (0,0)} \frac{y^2 \sin^2(x)}{x^4+y^4}$ acercándose por la trayectoria $y=x$ y concluya si existe.
* **[NUEVO] Ejercicio 3.25:** Utilice el Teorema del Sándwich para calcular $\lim_{(x,y)\rightarrow(0,0)} (x^2+y^2)\ln(x^2+y^2)$.
* **[NUEVO] Ejercicio 3.26:** Analice la existencia del límite $\lim_{(x,y)\rightarrow(0,0)} \frac{\sqrt{x}y^3}{x+y^6}$ probando con la trayectoria $x = y^6$.

### Subtema 20: Continuidad
* **Ejercicio 3.31:** Determine los valores de $a \in \mathbb{R}$ para que $f(x,y) = \frac{x^a}{x^2+y^2}$ sea continua en $(0,0)$.
* **Ejercicio 3.32:** Demuestre que $f(x,y) = \frac{x^2y+xy^2}{x^2+y^2}$ es continua en $(0,0)$ definiendo $f(0,0)=0$.
* **Ejercicio 3.33:** Determine el conjunto de puntos donde $g(x,y) = \frac{xy}{e^{x^2+y^2}-1}$ es continua.
* **[NUEVO] Ejercicio 3.34:** Analice la continuidad de la función $f(x,y) = \frac{\cos(y)\sin(x)}{x}$ si $x \neq 0$ y $\cos(y)$ si $x = 0$ en el punto $(0,0)$.
* **[NUEVO] Ejercicio 3.35:** Si $f(x,y) = \frac{x^3 + y^3}{x^2 + y^2}$ para $(x,y)\neq(0,0)$, ¿cómo debe definirse $f(0,0)$ para que la función sea continua en todo $\mathbb{R}^2$?
* **[NUEVO] Ejercicio 3.36:** Demuestre que la función $h(x,y) = \ln(1+x^2+y^2)$ es continua en todo el plano.

---

## Temática 4: Cálculo Diferencial Multivariable

### Subtema 21: Derivadas Parciales y Regla de la Cadena
* **Ejercicio 4.1:** Sea $f(x,y) = \sqrt[3]{x^3+y^3}$. Determine $f_x(0,0)$ mediante la definición de límite.
* **Ejercicio 4.2:** Verifique que $u = \frac{x^2y^2}{x+y}$ satisface $x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = 3u$.
* **Ejercicio 4.3:** Si $w = f(\frac{y-x}{xy}, \frac{z-y}{yz})$, demuestre que $x^2 \frac{\partial w}{\partial x} + y^2 \frac{\partial w}{\partial y} + z^2 \frac{\partial w}{\partial z} = 0$.
* **Ejercicio 4.4:** Encuentre el plano tangente a la superficie $x^3z + x^2y^2 + \sin(yz) + 3 = 0$ en $(-1, 0, 3)$.
* **Ejercicio 4.5:** Calcule la dirección de máximo crecimiento de $T(x,y,z) = x^2 + 2y^2 + 2z^2$ en $(1,1,1)$.
* **[NUEVO] Ejercicio 4.6:** Encuentre y clasifique los puntos críticos (máximo, mínimo, punto silla) de la función $f(x,y)=xy(2x+4y+1)$.
* **[NUEVO] Ejercicio 4.7:** Considere la curva $C$ obtenida de intersecar el plano $x+y+z=1$ con el cilindro $x^2+y^2=1$. Determine los puntos sobre $C$ más cercanos y más lejanos al origen usando Multiplicadores de Lagrange.
* **[NUEVO] Ejercicio 4.8:** Sea $f(x,y) = \frac{e^{-x^2/y}}{\sqrt{y}}$. Determine el valor de la constante $c \in \mathbb{R}$ para que se cumpla la ecuación de calor térmica $f_y + c f_{xx} = 0$.