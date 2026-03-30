# Hoja de Ejercicios: Cálculo II

## Integrales Impropias

**Descripción:** Extensión del concepto de integral definida para evaluar áreas en intervalos de longitud infinita (Tipo I) o funciones que presentan discontinuidades infinitas o asíntotas verticales dentro del intervalo de integración (Tipo II). Su resolución requiere el cálculo de límites. La convergencia sin cálculo directo se determina mediante criterios de comparación directa o comparación en el límite.

1. Determine si las siguientes integrales impropias son convergentes o divergentes. Evalúe las que sean convergentes:
    * a) $\int_{2}^{\infty}\frac{x+\sin x}{x^{2}-x}dx$
    * b) $\int_{1}^{3}\frac{x}{(x-3)^{3}}dx$
    * c) $\int_{0}^{1}\frac{\ln(x)}{\sqrt{x}}dx$
    * d) $\int_{-\infty}^{\infty}\frac{6x^{3}}{(x^{4}+1)^{2}}dx$
    * e) $\int_{3}^{\infty}\frac{1}{(x-2)^{3/2}}dx$
    * f) $\int_{-\infty}^{0}5^{t}dt$
    * g) $\int_{0}^{9}\frac{1}{\sqrt[3]{x-1}}dx$
    * h) $\int_{0}^{1}\frac{\sec^{2}(x)}{x\sqrt{x}}dx$
    * i) $\int_{0}^{\infty}\frac{\sqrt{x^{5}+3x^{3}+5x}}{x^{4}+x^{2}+1}dx$
    * j) $\int_{1}^{\infty}\frac{\cos(1/t)}{\sqrt{t}}dt$

2. Use el criterio de comparación para determinar si las siguientes integrales convergen o divergen:
    * a) $\int_{0}^{\infty}\frac{x}{x^{3}+1}dx$
    * b) $\int_{1}^{\infty}\frac{w^{2}+1}{w^{3}(\cos^{2}(w)+1)}dw$

3. Determine para qué valor de $C$ la integral $\int_{0}^{\infty}\left(\frac{x}{x^{2}+1}-\frac{C}{3x+1}\right)dx$ converge. Evalúe la integral para el valor de $C$ encontrado.

4. Determine si la integral $\int_{-\infty}^{1}\frac{e^{-\sqrt{1-x}}}{\sqrt{1-x}}dx$ es convergente o divergente. En caso de convergencia, calcule el valor numérico de la integral.

---

## Sucesiones

**Descripción:** Funciones cuyo dominio es el conjunto de los números naturales. El análisis se centra en el comportamiento de los términos a medida que $n \to \infty$ y en demostrar propiedades estructurales como el acotamiento y la monotonía.

**Recomendaciones para Inducción Matemática:**
1. **Caso base:** Verificar que la proposición se cumple para el primer valor del índice (usualmente $n=1$).
2. **Hipótesis inductiva:** Asumir explícitamente que la proposición es verdadera para un valor arbitrario $n=k$.
3. **Paso inductivo:** Demostrar que la proposición se cumple para $n=k+1$. Es estrictamente necesario manipular la expresión algebraica para forzar la aparición del término $k$ y sustituir ahí la hipótesis inductiva.

**Ejemplo de Inducción Matemática:**
Considere la sucesión definida por $a_{1}=2$ y $a_{n+1}=\frac{a_{n}+5}{3}$. Demuestre que $a_{n} < \frac{5}{2}$ para todo $n \in \mathbb{N}$.
* **Caso base ($n=1$):** $a_{1} = 2$. Como $2 < 2.5$, la proposición se cumple para $n=1$.
* **Hipótesis inductiva ($n=k$):** Asuma que $a_{k} < \frac{5}{2}$.
* **Paso inductivo ($n=k+1$):** Demostrar que $a_{k+1} < \frac{5}{2}$.
  Partiendo de la hipótesis inductiva:
  $a_{k} < \frac{5}{2}$
  Sumando 5 a ambos lados:
  $a_{k} + 5 < \frac{5}{2} + 5 = \frac{15}{2}$
  Dividiendo por 3 a ambos lados:
  $\frac{a_{k}+5}{3} < \frac{15}{6} = \frac{5}{2}$
  Por definición de la recurrencia, el lado izquierdo es $a_{k+1}$:
  $a_{k+1} < \frac{5}{2}$. La proposición queda demostrada para todo $n \in \mathbb{N}$.

1. Determine si las siguientes sucesiones convergen o divergen. Si convergen, encuentre el límite:
    * a) $a_{n}=\frac{(-1)^{n}+n}{(-1)^{n}-n}$
    * b) $a_{n}=\frac{n \sin(n)}{n^{2}+1}$
    * c) $a_{n}=\frac{n!}{n^{n}}$
    * d) $a_{k}=\frac{3+5k^{2}}{k^{2}+k}$
    * e) $a_{k}=\frac{3^{k+2}}{5^{k}}$
    * f) $a_{k}=\frac{e^{k}+e^{-k}}{e^{2k}-1}$
    * g) $a_{n}=\frac{\ln(n+2)}{\ln(1+4n)}$
    * h) $a_{n}=\frac{1+(-1)^{n}}{n^{2}}$

2. Considere la sucesión $a_{k}=\frac{2k}{3k+1}$. Demuestre que la sucesión $a_{k}$ es convergente.

3. Ejercicios de demostración por Inducción Matemática:
    * a) Considere la sucesión definida por $a_{n+1}=\sqrt{2a_{n}}$ con $a_{1}=1$. Demuestre que la sucesión es monótona creciente y que $a_{n}\le2$ para todo $n\in\mathbb{N}$. Deduzca su límite.
    * b) Considere la sucesión recursiva definida por $a_{1}=5$ y $a_{n+1}=\frac{a_{n}+7}{2}$. Demuestre que $a_{n}<7$ y que $a_{n}$ es creciente. Demuestre que converge y calcule el límite.
    * c) Considere la sucesión dada por recurrencia $x_{n+1}=\frac{x_{n}^{2}+1}{x_{n}+2}$ con $x_{1}=\frac{1}{3}$. Pruebe que para todo $n\in\mathbb{N}$ se cumple $0<x_{n}<\frac{1}{2}$ y $x_{n}<x_{n+1}$. Demuestre que el límite existe y determínelo.
    * d) Demuestre que la sucesión definida por $a_{1}=1$ y $a_{k+1}=3-\frac{1}{a_{k}}$ es creciente y acotada superiormente por $3$. Deduzca que es convergente y determine su límite.
    * e) Considere la sucesión definida por $a_1 = \sqrt{2}$ y $a_{n+1} = \sqrt{2 + a_n}$. Demuestre por inducción que $a_n < 2$ para todo $n \in \mathbb{N}$ y que es estrictamente creciente. Calcule su límite.
    * f) Considere la sucesión definida por $y_1 = 3$ y $y_{n+1} = \frac{3(1+y_n)}{3+y_n}$. Demuestre por inducción que $y_n > \sqrt{3}$ para todo $n \in \mathbb{N}$ y que la sucesión es estrictamente decreciente. Encuentre el límite.

---

## Series Numéricas y Convergencia

**Descripción:** Suma de los términos de una sucesión infinita. El objetivo es determinar si la secuencia de sumas parciales converge a un valor finito o diverge.
* **Series Geométricas:** Estructuradas como $\sum_{n=0}^{\infty} ar^n$. Convergen estrictamente si la razón cumple $|r| < 1$, y su suma exacta se calcula mediante la fórmula $S = \frac{a}{1-r}$. Si $|r| \ge 1$, divergen.
* **Series Telescópicas:** Series cuya estructura algebraica permite que, al expandir las sumas parciales $S_k$, los términos intermedios se cancelen sistemáticamente. La suma de la serie se obtiene calculando el límite de los términos residuales cuando $k \to \infty$.

1. Estudie la convergencia de las siguientes series:
    * a) $\sum_{n=1}^{\infty}\frac{9n}{e^{-n}+n}$
    * b) $\sum_{n=1}^{\infty}\frac{e^{1/n}}{3n^{2}}$
    * c) $\sum_{n=1}^{\infty}\frac{2\sqrt{n}+\sin(n)}{3n^{2}-2n+1}$
    * d) $\sum_{n=1}^{\infty}\frac{n^{2}+n\cos(n)}{\sqrt{n^{8}-n+1}}$
    * e) $\sum_{n=1}^{\infty}\frac{3+2\cos(n)}{n^{3}-2n^{2}+7}$

2. Determine si las siguientes series son convergentes o divergentes. En caso de convergencia determine la suma si corresponde:
    * a) $\sum_{n=1}^{\infty}\frac{2^{n}}{n^{2}}$
    * b) $\sum_{n=1}^{\infty}\frac{\sqrt{2n^{2}+4n+1}}{n^{3}+9}$
    * c) $\sum_{n=0}^{\infty}\frac{2^{n}\sin^{2}(5n)}{4^{n}+\cos^{2}(n)}$
    * d) $\sum_{n=1}^{\infty}\frac{1+2^{n}}{3^{n}}$
    * e) $\sum_{n=1}^{\infty}\frac{e^{n}}{n^{2}}$
    * f) $\sum_{n=2}^{\infty}\frac{2}{n^{2}-1}$
    * g) $\sum_{k=1}^{\infty}\frac{1}{k(\ln(k))^{2}}$
    * h) $\sum_{k=1}^{\infty}\frac{9^{k}}{3+10^{k}}$
    * i) $\sum_{k=1}^{\infty}\frac{\sqrt[3]{k}}{\sqrt{k^{3}+4k+3}}$
    * j) $\sum_{n=1}^{\infty}\frac{1+2^{n}}{3^{n-1}}$
    * k) $\sum_{n=1}^{\infty}\frac{8^{n}}{5+11^{n}}$