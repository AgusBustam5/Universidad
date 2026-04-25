# Pauta Detallada - Subtema 10: Criterios de Convergencia Numérica

Este bloque se enfoca en el uso de los criterios de la serie alternante (Leibniz), la razón, la raíz, la integral y comparaciones para determinar el carácter de una serie.

---

### Ejercicio 1.1
**Enunciado:** Determine si la serie $\sum_{n=10}^{\infty} \frac{\cos(n\pi)}{\sqrt{n}}$ es condicionalmente convergente, absolutamente convergente o divergente.

**Resolución:**
1. **Simplificación:** Notamos que $\cos(n\pi) = (-1)^n$. La serie es $\sum_{n=10}^{\infty} \frac{(-1)^n}{\sqrt{n}}$.
2. **Convergencia Absoluta:** Estudiamos $\sum |a_n| = \sum \frac{1}{n^{1/2}}$. Esta es una $p$-serie con $p=1/2 \le 1$, por lo tanto, **diverge**. No hay convergencia absoluta.
3. **Criterio de Leibniz (Alternante):** Sea $b_n = \frac{1}{\sqrt{n}}$.
   - $b_n > 0$ para todo $n \ge 10$.
   - Es decreciente: $\sqrt{n+1} > \sqrt{n} \implies \frac{1}{\sqrt{n+1}} < \frac{1}{\sqrt{n}}$.
   - Límite: $\lim_{n \to \infty} \frac{1}{\sqrt{n}} = 0$.
**Conclusión:** La serie es **Condicionalmente Convergente**.

---

### Ejercicio 1.2
**Enunciado:** Sea $a_1=1$ y $a_{n+1} = \frac{2 - \arctan(n^2)}{\sqrt{n}} a_n$. Determine si $\sum a_n$ converge.

**Resolución:**
1. **Criterio de la Razón:** Calculamos $L = \lim_{n \to \infty} \frac{a_{n+1}}{a_n}$.
2. **Desarrollo:** $L = \lim_{n \to \infty} \frac{2 - \arctan(n^2)}{\sqrt{n}}$.
3. **Límite:** Como $\arctan(n^2) \to \pi/2$ y el denominador $\sqrt{n} \to \infty$:
   $L = \frac{2 - \pi/2}{\infty} = 0$.
**Conclusión:** Como $L = 0 < 1$, la serie **Converge Absolutamente**.

---

### Ejercicio 1.3
**Enunciado:** Analice la convergencia de $\sum_{n=2}^{\infty} \frac{(-1)^n}{\ln(n)}$ (Absoluta vs Condicional).

**Resolución:**
1. **Absoluta:** $\sum \frac{1}{\ln n}$. Por comparación directa: $\ln n < n \implies \frac{1}{\ln n} > \frac{1}{n}$. Como $\sum \frac{1}{n}$ diverge, la absoluta **diverge**.
2. **Alternante:** $b_n = \frac{1}{\ln n}$ es positiva, decreciente y tiende a 0. Cumple Leibniz.
**Conclusión:** **Condicionalmente Convergente**.

---

### Ejercicio 1.4
**Enunciado:** Determine para qué valores de $p$ converge la serie $\sum_{n=2}^\infty \frac{1}{n(\ln n)^p}$.

**Resolución:**
1. **Criterio de la Integral:** Sea $f(x) = \frac{1}{x(\ln x)^p}$, continua, positiva y decreciente en $[2, \infty)$.
2. **Integral:** $\int_{2}^{\infty} \frac{1}{x(\ln x)^p} dx$. Hacemos $u = \ln x, du = \frac{1}{x} dx$.
   $\int_{\ln 2}^{\infty} u^{-p} du$.
3. **Convergencia:** Esta integral converge si y solo si $p > 1$.
**Conclusión:** La serie converge si **$p > 1$** y diverge si $p \le 1$.

---

### Ejercicio 1.5
**Enunciado:** Analice $\sum \frac{n^2 + 1}{n^4 + n^2 + 1}$ usando comparación al límite.

**Resolución:**
1. **Elección de serie de prueba:** El término dominante es $\frac{n^2}{n^4} = \frac{1}{n^2}$. Sea $b_n = \frac{1}{n^2}$.
2. **Límite:** $\lim_{n \to \infty} \frac{a_n}{b_n} = \lim_{n \to \infty} \frac{(n^2+1)n^2}{n^4+n^2+1} = \lim_{n \to \infty} \frac{n^4+n^2}{n^4+n^2+1} = 1$.
3. **Conclusión:** Como el límite es $1 \in (0, \infty)$, $a_n$ se comporta como $\sum \frac{1}{n^2}$. Como esta es una $p$-serie con $p=2 > 1$, la serie **Converge**.

---

### Ejercicio 1.6
**Enunciado:** Analice $\sum_{n=1}^{\infty} \frac{(-1)^n \ln(n)}{n^2}$ (Convergencia absoluta).

**Resolución:**
1. **Valores absolutos:** $\sum \frac{\ln n}{n^2}$.
2. **Comparación:** $\ln n < \sqrt{n} \implies \frac{\ln n}{n^2} < \frac{n^{1/2}}{n^2} = \frac{1}{n^{3/2}}$.
3. **Resultado:** $\sum \frac{1}{n^{1.5}}$ converge ($p=1.5 > 1$).
**Conclusión:** La serie es **Absolutamente Convergente**.

---

### Ejercicio 1.7
**Enunciado:** Sea la sucesión de Fibonacci $a_1=a_2=1, a_{n+1}=a_n+a_{n-1}$. Analice $\sum_{n=1}^\infty \frac{a_n}{3^n}$.

**Resolución:**
1. **Criterio de la Razón:** Evaluamos $\frac{a_{n+1}/3^{n+1}}{a_n/3^n} = \frac{a_{n+1}}{3 a_n}$.
2. **Acotamiento:** Nos dan la pista $\frac{a_{n+1}}{a_n} \le 2$.
3. **Límite:** $\frac{a_{n+1}}{3 a_n} \le \frac{2}{3} < 1$.
**Conclusión:** Por el criterio de la razón, la serie **Converge**.

---

### Ejercicio 1.8
**Enunciado:** Analice $\sum_{n=5}^{\infty}\frac{(n^{3}+4)(n-2)}{(n-3)(n^{5}+1)}$.

**Resolución:**
1. **Comparación al Límite:** El grado del numerador es $n^4$ ($n^3 \cdot n$) y el del denominador es $n^6$ ($n \cdot n^5$).
2. **Serie de prueba:** $b_n = \frac{n^4}{n^6} = \frac{1}{n^2}$.
3. **Límite:** $\lim \frac{a_n}{b_n} = 1$. Como $\sum \frac{1}{n^2}$ converge, nuestra serie **Converge**.

# Pauta Detallada - Subtema 11: Radio e Intervalo de Convergencia

El procedimiento estándar para estos ejercicios consta de tres pasos:
1. Plantear el Criterio de la Razón o de la Raíz (con valor absoluto).
2. Forzar a que el límite sea menor a 1 para despejar $|x - c| < R$, hallando el Radio de Convergencia $R$.
3. Evaluar manualmente la convergencia en los extremos $x = c - R$ y $x = c + R$.

---

### Ejercicio 1.11
**Enunciado:** Si $k$ es un entero positivo, encuentre el radio de convergencia de la serie $\sum_{n=1}^{\infty} \frac{(n!)^k}{(kn)!} x^n$.

**Resolución:**
1. **Criterio de la Razón:** Evaluamos $L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$.
   $$L = \lim_{n \to \infty} \left| \frac{((n+1)!)^k x^{n+1}}{(k(n+1))!} \cdot \frac{(kn)!}{(n!)^k x^n} \right|$$
2. **Simplificación Factorial:** Notamos que $((n+1)!)^k = (n+1)^k (n!)^k$, y que $(kn+k)! = (kn+k)(kn+k-1)\dots(kn+1)(kn)!$.
   $$L = \lim_{n \to \infty} |x| \frac{(n+1)^k}{(kn+k)(kn+k-1)\dots(kn+1)}$$
3. **Cálculo del Límite:** El numerador es un polinomio de grado $k$ con coeficiente principal 1. El denominador es el producto de $k$ factores lineales, por lo que es un polinomio de grado $k$ con coeficiente principal $k^k$.
   $$L = |x| \frac{1}{k^k}$$
4. **Radio de Convergencia:** Forzamos $L < 1 \implies |x| \frac{1}{k^k} < 1 \implies |x| < k^k$.
**Conclusión:** El radio de convergencia es **$R = k^k$**.

---

### Ejercicio 1.12
**Enunciado:** Encuentre el intervalo de convergencia de $\sum_{n=1}^{\infty} \frac{(2x-1)^n}{5^n \sqrt{n}}$.

**Resolución:**
1. **Criterio de la Razón:**
   $$L = \lim_{n \to \infty} \left| \frac{(2x-1)^{n+1}}{5^{n+1}\sqrt{n+1}} \cdot \frac{5^n\sqrt{n}}{(2x-1)^n} \right| = \lim_{n \to \infty} \frac{|2x-1|}{5} \sqrt{\frac{n}{n+1}} = \frac{|2x-1|}{5}$$
2. **Búsqueda del Radio:**
   Exigimos $\frac{|2x-1|}{5} < 1 \implies |2x-1| < 5$.
   Despejamos el centro: $2|x - 1/2| < 5 \implies |x - 1/2| < 5/2$. El radio es $R = 5/2$.
   Desigualdad: $-5 < 2x - 1 < 5 \implies -4 < 2x < 6 \implies -2 < x < 3$.
3. **Análisis de Extremos:**
   - **En $x = 3$:** Reemplazamos en la serie original: $\sum \frac{(2(3)-1)^n}{5^n \sqrt{n}} = \sum \frac{5^n}{5^n \sqrt{n}} = \sum \frac{1}{\sqrt{n}}$. Es una $p$-serie con $p = 1/2 \le 1$, por lo tanto **Diverge**.
   - **En $x = -2$:** Reemplazamos: $\sum \frac{(2(-2)-1)^n}{5^n \sqrt{n}} = \sum \frac{(-5)^n}{5^n \sqrt{n}} = \sum \frac{(-1)^n}{\sqrt{n}}$. Es una serie alternante que cumple Leibniz, por lo tanto **Converge**.
**Conclusión:** El intervalo de convergencia es **$[-2, 3)$**.

---

### Ejercicio 1.13
**Enunciado:** Determine el intervalo de convergencia de $\sum_{n=0}^{\infty} \frac{(-1)^n}{4^n \sqrt{n+1}}(x-3)^n$.

**Resolución:**
1. **Criterio de la Razón:**
   $$L = \lim_{n \to \infty} \left| \frac{(-1)^{n+1} (x-3)^{n+1}}{4^{n+1}\sqrt{n+2}} \cdot \frac{4^n\sqrt{n+1}}{(-1)^n (x-3)^n} \right| = \lim_{n \to \infty} \frac{|x-3|}{4} \sqrt{\frac{n+1}{n+2}} = \frac{|x-3|}{4}$$
2. **Búsqueda del Radio:**
   Exigimos $\frac{|x-3|}{4} < 1 \implies |x-3| < 4$. El radio es $R = 4$.
   Desigualdad: $-4 < x - 3 < 4 \implies -1 < x < 7$.
3. **Análisis de Extremos:**
   - **En $x = 7$:** $\sum \frac{(-1)^n}{4^n \sqrt{n+1}} (4)^n = \sum \frac{(-1)^n}{\sqrt{n+1}}$. Converge por Criterio de Leibniz.
   - **En $x = -1$:** $\sum \frac{(-1)^n}{4^n \sqrt{n+1}} (-4)^n = \sum \frac{(-1)^n (-1)^n 4^n}{4^n \sqrt{n+1}} = \sum \frac{1}{\sqrt{n+1}}$. Diverge por comparación al límite con $\frac{1}{\sqrt{n}}$ ($p$-serie, $p=1/2$).
**Conclusión:** El intervalo de convergencia es **$(-1, 7]$**.

---

### Ejercicio 1.14
**Enunciado:** Halle el radio de convergencia de $\sum_{n=1}^{\infty} \frac{n^n}{n!} x^n$.

**Resolución:**
1. **Criterio de la Razón:**
   $$L = \lim_{n \to \infty} \left| \frac{(n+1)^{n+1} x^{n+1}}{(n+1)!} \cdot \frac{n!}{n^n x^n} \right|$$
2. **Simplificación Estratégica:**
   Separamos $(n+1)^{n+1} = (n+1)(n+1)^n$ y $(n+1)! = (n+1)n!$.
   $$L = \lim_{n \to \infty} |x| \frac{(n+1)(n+1)^n n!}{(n+1)n! n^n} = \lim_{n \to \infty} |x| \left( \frac{n+1}{n} \right)^n = \lim_{n \to \infty} |x| \left( 1 + \frac{1}{n} \right)^n$$
3. **Cálculo del Límite:**
   Reconocemos el límite fundamental del número $e$: $\lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n = e$.
   $$L = |x|e$$
4. **Radio de Convergencia:**
   Forzamos $L < 1 \implies |x|e < 1 \implies |x| < \frac{1}{e}$.
**Conclusión:** El radio de convergencia es **$R = \frac{1}{e}$**.

---

### Ejercicio 1.15
**Enunciado:** Determine el intervalo de convergencia de $\sum_{n=0}^{\infty}(-1)^{n}\frac{x^{2n}}{(2n)!}$.

**Resolución:**
1. **Criterio de la Razón:**
   $$L = \lim_{n \to \infty} \left| \frac{x^{2(n+1)}}{(2(n+1))!} \cdot \frac{(2n)!}{x^{2n}} \right| = \lim_{n \to \infty} \left| \frac{x^{2n+2}}{(2n+2)!} \cdot \frac{(2n)!}{x^{2n}} \right|$$
2. **Simplificación:**
   $(2n+2)! = (2n+2)(2n+1)(2n)!$.
   $$L = \lim_{n \to \infty} \frac{|x|^2}{(2n+2)(2n+1)}$$
3. **Cálculo del Límite:**
   Dado que el denominador crece hacia infinito y el numerador es un número finito (sin importar el valor de $x$):
   $$L = 0$$
4. **Conclusión:** Como $L = 0 < 1$ sin importar qué número real sea $x$, la serie converge para todo $x$.
**Conclusión:** El radio es **$R = \infty$** y el intervalo es **$(-\infty, \infty)$**. *(Nota: Esta es la serie de Maclaurin de $\cos(x)$).*

---

### Ejercicio 1.16
**Enunciado:** Determine el intervalo de convergencia de $\sum_{n=1}^{\infty}\left(\frac{nx}{n+1}\right)^{n}$.

**Resolución:**
1. **Identificación del método:** Como todo el término está elevado a $n$, el **Criterio de la Raíz** es el más directo.
   $$L = \lim_{n \to \infty} \sqrt[n]{|a_n|} = \lim_{n \to \infty} \sqrt[n]{\left|\frac{nx}{n+1}\right|^n} = \lim_{n \to \infty} \left| \frac{n}{n+1} x \right|$$
2. **Cálculo del Límite:**
   $$L = |x| \lim_{n \to \infty} \frac{n}{n+1} = |x| \cdot 1 = |x|$$
3. **Búsqueda del Radio:**
   Exigimos $L < 1 \implies |x| < 1$. El radio es $R = 1$. Intervalo preliminar: $-1 < x < 1$.
4. **Análisis de Extremos:**
   - **En $x = 1$:** $\sum \left(\frac{n}{n+1}\right)^n$. Calculamos el límite del término general: 
     $\lim_{n \to \infty} \left(\frac{n}{n+1}\right)^n = \lim_{n \to \infty} \frac{1}{(1+1/n)^n} = \frac{1}{e}$. Como el límite no es 0, la serie Diverge por el Test de la Divergencia.
   - **En $x = -1$:** $\sum (-1)^n \left(\frac{n}{n+1}\right)^n$. El término general no tiende a cero. Diverge.
**Conclusión:** El intervalo de convergencia es **$(-1, 1)$**.

# Pauta Detallada - Subtema 12: Representación, Derivación e Integración de Series

La clave en estos ejercicios es partir de la serie geométrica fundamental:
$$\frac{1}{1-u} = \sum_{n=0}^{\infty} u^n, \quad \text{para } |u| < 1$$
Y aplicar operaciones de cálculo para obtener nuevas series.

---

### Ejercicio 1.21
**Enunciado:** Exprese como serie de potencias la integral indefinida $\int x^2 \ln(1+x) dx$.

**Resolución:**
1. **Serie de la base:** Sabemos que $\frac{d}{dx} \ln(1+x) = \frac{1}{1+x}$. Usando la serie geométrica con $u = -x$:
   $$\frac{1}{1+x} = \sum_{n=0}^{\infty} (-1)^n x^n, \quad |x| < 1$$
2. **Integración para obtener ln:**
   $$\ln(1+x) = \int \left( \sum_{n=0}^{\infty} (-1)^n x^n \right) dx = \sum_{n=0}^{\infty} \frac{(-1)^n x^{n+1}}{n+1} + C$$
   Como $\ln(1+0) = 0$, entonces $C=0$. Reindexando (sea $m = n+1$): $\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^n}{n}$.
3. **Multiplicación por $x^2$:**
   $$x^2 \ln(1+x) = x^2 \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^n}{n} = \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^{n+2}}{n}$$
4. **Integral final:**
   $$\int x^2 \ln(1+x) dx = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n} \int x^{n+2} dx = C + \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^{n+3}}{n(n+3)}$$
**Conclusión:** La representación es $C + \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^{n+3}}{n(n+3)}$.

---

### Ejercicio 1.22
**Enunciado:** Exprese $f(x) = \frac{x+1}{x^3+1}$ como una suma de dos series de potencias centradas en $x=0$.

**Resolución:**
1. **Descomposición:** Separamos el numerador: $f(x) = \frac{x}{x^3+1} + \frac{1}{x^3+1}$.
2. **Serie base:** Usamos $\frac{1}{1+u} = \sum_{n=0}^{\infty} (-1)^n u^n$ con $u = x^3$:
   $$\frac{1}{x^3+1} = \sum_{n=0}^{\infty} (-1)^n (x^3)^n = \sum_{n=0}^{\infty} (-1)^n x^{3n}$$
3. **Segunda serie:** Multiplicamos la anterior por $x$:
   $$\frac{x}{x^3+1} = x \sum_{n=0}^{\infty} (-1)^n x^{3n} = \sum_{n=0}^{\infty} (-1)^n x^{3n+1}$$
4. **Suma final:**
   $$f(x) = \sum_{n=0}^{\infty} (-1)^n x^{3n} + \sum_{n=0}^{\infty} (-1)^n x^{3n+1}$$
**Conclusión:** El radio de convergencia es $R=1$ (de $|x^3|<1$).

---

### Ejercicio 1.25 (Pauta MAT1620-2026)
**Enunciado:** Encuentre una representación como serie de potencias centrada en $x=0$ para $f(x)=\frac{3}{x^{2}-x-2}$ usando fracciones parciales.

**Resolución:**
1. **Factorización y Fracciones Parciales:**
   $x^2-x-2 = (x-2)(x+1)$.
   $$\frac{3}{(x-2)(x+1)} = \frac{A}{x-2} + \frac{B}{x+1} \implies 3 = A(x+1) + B(x-2)$$
   - Si $x=-1 \implies 3 = -3B \implies B = -1$.
   - Si $x=2 \implies 3 = 3A \implies A = 1$.
   $$f(x) = \frac{1}{x-2} - \frac{1}{x+1}$$
2. **Ajuste a forma geométrica:**
   - $\frac{1}{x-2} = \frac{1}{-2(1 - x/2)} = -\frac{1}{2} \sum_{n=0}^{\infty} \left(\frac{x}{2}\right)^n = \sum_{n=0}^{\infty} -\frac{1}{2^{n+1}} x^n$
   - $\frac{1}{x+1} = \sum_{n=0}^{\infty} (-1)^n x^n$
3. **Resta de series:**
   $$f(x) = \sum_{n=0}^{\infty} \left( -\frac{1}{2^{n+1}} - (-1)^n \right) x^n$$
**Conclusión:** Converge para $|x| < 1$ (la intersección de $|x/2|<1$ y $|x|<1$).

---

### Ejercicio 1.26
**Enunciado:** Sea $S(x) = \sum_{n=0}^{\infty}\frac{(-1)^{n}}{2^{2n}(n!)^{2}}x^{2n}$. Muestre que satisface $xS''(x)+S'(x)+xS(x)=0$.

**Resolución:**
1. **Derivada primera $S'(x)$:**
   $$S'(x) = \sum_{n=1}^{\infty} \frac{(-1)^n 2n}{2^{2n}(n!)^2} x^{2n-1}$$
2. **Derivada segunda $S''(x)$:**
   $$S''(x) = \sum_{n=1}^{\infty} \frac{(-1)^n 2n(2n-1)}{2^{2n}(n!)^2} x^{2n-2}$$
3. **Sustitución en la ED:**
   $xS''(x) + S'(x) = \sum_{n=1}^{\infty} \frac{(-1)^n [2n(2n-1) + 2n]}{2^{2n}(n!)^2} x^{2n-1} = \sum_{n=1}^{\infty} \frac{(-1)^n (2n)^2}{2^{2n}(n!)^2} x^{2n-1}$
   Usando $(2n)^2 = 4n^2$ y $2^{2n} = 4 \cdot 2^{2n-2}$ y $(n!)^2 = n^2 ((n-1)!)^2$:
   $xS''(x) + S'(x) = \sum_{n=1}^{\infty} \frac{(-1)^n}{2^{2n-2}((n-1)!)^2} x^{2n-1}$
4. **Comparación con $-xS(x)$:**
   $-xS(x) = -\sum_{k=0}^{\infty} \frac{(-1)^k}{2^{2k}(k!)^2} x^{2k+1}$. Si hacemos $n = k+1$:
   $-xS(x) = \sum_{n=1}^{\infty} \frac{(-1) (-1)^{n-1}}{2^{2n-2}((n-1)!)^2} x^{2n-1} = \sum_{n=1}^{\infty} \frac{(-1)^n}{2^{2n-2}((n-1)!)^2} x^{2n-1}$
**Conclusión:** Ambos lados son iguales. La serie satisface la ecuación diferencial.

# Pauta Detallada - Subtema 13: Series de Taylor y Maclaurin

La estrategia principal en la universidad NO es calcular derivadas infinitas a mano (usando la fórmula $c_n = \frac{f^{(n)}(a)}{n!}$), sino utilizar las **Series de Maclaurin Conocidas** y aplicar sustituciones o álgebra básica.

**Series Fundamentales a Memorizar:**
* $e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$
* $\sin(x) = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$
* $\cos(x) = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$
* $\ln(1+x) = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$

---

### Ejercicio 1.31 (I2 2023-1)
**Enunciado:** Determine los tres primeros términos no nulos de la serie de Maclaurin de $f(x) = \ln\left(\frac{1+x}{1-x}\right)$ y utilícelos para deducir a qué valor converge la suma $2(\frac{3}{4}) + \frac{2}{3}(\frac{3}{4})^3 + \frac{2}{5}(\frac{3}{4})^5 + \dots$

**Resolución:**
1.  **Propiedades de Logaritmos:**
    $f(x) = \ln(1+x) - \ln(1-x)$
2.  **Series Conocidas:**
    Sabemos que:
    $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \frac{x^5}{5} - \dots$
    Para $\ln(1-x)$, evaluamos la misma serie en $(-x)$:
    $\ln(1-x) = (-x) - \frac{(-x)^2}{2} + \frac{(-x)^3}{3} - \frac{(-x)^4}{4} + \dots = -x - \frac{x^2}{2} - \frac{x^3}{3} - \frac{x^4}{4} - \dots$
3.  **Resta de Series:**
    Restamos término a término: $\ln(1+x) - \ln(1-x)$
    $= \left(x - \frac{x^2}{2} + \frac{x^3}{3} - \dots\right) - \left(-x - \frac{x^2}{2} - \frac{x^3}{3} - \dots\right)$
    Los términos con potencias pares se cancelan ($-\frac{x^2}{2} - (-\frac{x^2}{2}) = 0$), y los impares se duplican:
    $f(x) = 2x + \frac{2}{3}x^3 + \frac{2}{5}x^5 + \dots$
    *(Estos son los tres primeros términos no nulos).*
4.  **Cálculo de la Suma Numérica:**
    La serie numérica entregada es exactamente $f(x)$ evaluada en $x = \frac{3}{4}$.
    Evaluamos en la función original:
    $f(3/4) = \ln\left(\frac{1 + 3/4}{1 - 3/4}\right) = \ln\left(\frac{7/4}{1/4}\right) = \ln(7)$
**Conclusión:** La serie es $2x + \frac{2}{3}x^3 + \frac{2}{5}x^5 + \dots$ y la suma numérica converge exactamente a **$\ln(7)$**.

---

### Ejercicio 1.32 (I2 2023-TAV)
**Enunciado:** Obtenga el desarrollo en serie de potencias para $f(x) = \frac{\ln(1+x^2)}{x}$.

**Resolución:**
1.  **Serie Base:** Partimos del desarrollo de Maclaurin de $\ln(1+u)$:
    $\ln(1+u) = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{u^n}{n}$
2.  **Sustitución:** Sea $u = x^2$:
    $\ln(1+x^2) = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{(x^2)^n}{n} = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^{2n}}{n}$
3.  **División Algebraica:** Dividimos por $x$ (con $x \neq 0$):
    $f(x) = \frac{1}{x} \sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^{2n}}{n} = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^{2n-1}}{n}$
**Conclusión:** El desarrollo en serie es **$\sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^{2n-1}}{n}$**.

---

### Ejercicio 1.35 (Nivel Ayudantía MAT1620)
**Enunciado:** Utilice series de potencias para representar la integral $\int_0^x \frac{\sin(t)}{t} dt$.

**Resolución:**
1.  **Serie Base del Seno:**
    $\sin(t) = \sum_{n=0}^{\infty} (-1)^n \frac{t^{2n+1}}{(2n+1)!}$
2.  **División por t:**
    $\frac{\sin(t)}{t} = \sum_{n=0}^{\infty} (-1)^n \frac{t^{2n}}{(2n+1)!}$
3.  **Integración término a término:**
    $\int_0^x \frac{\sin(t)}{t} dt = \int_0^x \left( \sum_{n=0}^{\infty} (-1)^n \frac{t^{2n}}{(2n+1)!} \right) dt$
    Intercambiamos suma con integral (válido en el intervalo de convergencia):
    $= \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} \int_0^x t^{2n} dt = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} \left[ \frac{t^{2n+1}}{2n+1} \right]_0^x$
    $= \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!(2n+1)}$
**Conclusión:** La integral (conocida como función Sine Integral $Si(x)$) se representa como **$\sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!(2n+1)} x^{2n+1}$**.

---

### Ejercicio 1.36 (Desafío de Identificación de Coeficientes)
**Enunciado:** Encuentre la serie de Maclaurin para $f(x) = x \cos(x^2 / 2)$. A partir de su resultado, determine el valor de la 13° derivada evaluada en cero: $f^{(13)}(0)$.

**Resolución:**
1.  **Construcción de la Serie:**
    Sabemos que $\cos(u) = \sum_{n=0}^{\infty} (-1)^n \frac{u^{2n}}{(2n)!}$. Evaluamos en $u = x^2/2$:
    $\cos(x^2/2) = \sum_{n=0}^{\infty} (-1)^n \frac{(x^2/2)^{2n}}{(2n)!} = \sum_{n=0}^{\infty} (-1)^n \frac{x^{4n}}{2^{2n} (2n)!}$
2.  **Multiplicación por x:**
    $f(x) = x \sum_{n=0}^{\infty} (-1)^n \frac{x^{4n}}{2^{2n} (2n)!} = \sum_{n=0}^{\infty} (-1)^n \frac{x^{4n+1}}{2^{2n} (2n)!}$
3.  **Identificación del Coeficiente de Taylor:**
    El teorema de Taylor establece que el coeficiente que acompaña a $x^k$ en la serie es $\frac{f^{(k)}(0)}{k!}$.
    Queremos encontrar $f^{(13)}(0)$, así que nos interesa el término donde el exponente de $x$ es 13.
    Igualamos los exponentes: $4n + 1 = 13 \implies 4n = 12 \implies n = 3$.
4.  **Cálculo de la derivada:**
    El coeficiente para $n=3$ es $\frac{(-1)^3}{2^{2(3)} (2(3))!} = \frac{-1}{2^6 \cdot 6!} = \frac{-1}{64 \cdot 720}$.
    Igualando a la fórmula de Taylor:
    $\frac{f^{(13)}(0)}{13!} = \frac{-1}{64 \cdot 720} \implies f^{(13)}(0) = -\frac{13!}{64 \cdot 720}$
**Conclusión:** El valor de la derivada es **$f^{(13)}(0) = -\frac{13!}{46080}$**. *(Nota: Si nos hubieran pedido $f^{(12)}(0)$, el valor sería 0, ya que $4n+1 = 12$ no tiene solución entera, indicando que ese término no existe en la serie).*

# Pauta Detallada - Subtema 14: Sistemas Coordenados y Vectores

En esta sección, los ejercicios evalúan tu comprensión geométrica y algebraica de los vectores, especialmente las propiedades que relacionan la ortogonalidad (producto punto) y los vectores normales (producto cruz).

---

### Ejercicio 2.2 (I2 2023-TAV)
**Enunciado:** Determine si existe un vector $\vec{v}$ tal que $\langle 2, -1, 2 \rangle \times \vec{v} = \langle 1, 3, 2 \rangle$.

**Resolución:**
1. **Análisis de Propiedades del Producto Cruz:**
   Por definición geométrica, el producto cruz de dos vectores $\vec{a} \times \vec{b} = \vec{c}$ genera un nuevo vector $\vec{c}$ que es simultáneamente **ortogonal** (perpendicular) tanto a $\vec{a}$ como a $\vec{b}$.
   Esto implica que el producto punto entre el resultado y cualquiera de los vectores originales debe ser cero:
   $\vec{a} \cdot (\vec{a} \times \vec{v}) = 0$
2. **Identificación de Vectores:**
   Sean $\vec{a} = \langle 2, -1, 2 \rangle$ y $\vec{c} = \langle 1, 3, 2 \rangle$.
   La ecuación planteada nos dice que $\vec{a} \times \vec{v} = \vec{c}$.
3. **Verificación de Ortogonalidad:**
   Si la ecuación fuera cierta, obligatoriamente se debe cumplir que $\vec{a} \cdot \vec{c} = 0$. Calculemos este producto punto:
   $\vec{a} \cdot \vec{c} = (2)(1) + (-1)(3) + (2)(2)$
   $\vec{a} \cdot \vec{c} = 2 - 3 + 4 = 3$
4. **Conclusión:**
   Como el producto punto es $3 \neq 0$, el vector $\langle 1, 3, 2 \rangle$ NO es ortogonal a $\langle 2, -1, 2 \rangle$. Por lo tanto, por las propiedades fundamentales del espacio en $\mathbb{R}^3$, **NO existe** tal vector $\vec{v}$.

---

### Ejercicio 2.4 (Identidad de Lagrange - Ayudantía 2026)
**Enunciado:** Demuestre la Identidad de Lagrange para vectores en $\mathbb{R}^3$: 
$||\vec{a}||^2 ||\vec{b}||^2 = (\vec{a} \cdot \vec{b})^2 + ||\vec{a} \times \vec{b}||^2$

**Resolución:**
1. **Definiciones Geométricas Fundamentales:**
   Sabemos que las magnitudes del producto punto y producto cruz se relacionan directamente con el ángulo $\theta$ entre los vectores:
   - Producto Punto: $\vec{a} \cdot \vec{b} = ||\vec{a}|| ||\vec{b}|| \cos(\theta)$
   - Magnitud del Producto Cruz: $||\vec{a} \times \vec{b}|| = ||\vec{a}|| ||\vec{b}|| \sin(\theta)$
2. **Sustitución en el lado derecho de la identidad:**
   Tomamos el término $(\vec{a} \cdot \vec{b})^2 + ||\vec{a} \times \vec{b}||^2$ y reemplazamos:
   $= (||\vec{a}|| ||\vec{b}|| \cos(\theta))^2 + (||\vec{a}|| ||\vec{b}|| \sin(\theta))^2$
   $= ||\vec{a}||^2 ||\vec{b}||^2 \cos^2(\theta) + ||\vec{a}||^2 ||\vec{b}||^2 \sin^2(\theta)$
3. **Factorización e Identidad Trigonométrica:**
   Factorizamos el término común $||\vec{a}||^2 ||\vec{b}||^2$:
   $= ||\vec{a}||^2 ||\vec{b}||^2 \left( \cos^2(\theta) + \sin^2(\theta) \right)$
   Por la identidad trigonométrica fundamental, $\cos^2(\theta) + \sin^2(\theta) = 1$.
   $= ||\vec{a}||^2 ||\vec{b}||^2 (1)$
   $= ||\vec{a}||^2 ||\vec{b}||^2$
4. **Conclusión:**
   Hemos llegado exactamente al lado izquierdo de la ecuación, quedando **demostrada** la Identidad de Lagrange.

---

### Ejercicio 2.5 (Centroide Vectorial - Ayudantía 2026)
**Enunciado:** Considere el triángulo con vértices $A(4,2,0)$, $B(1,3,0)$, $C(1,1,3)$. Determine el vector de posición del punto de intersección de las medianas (baricentro).

**Resolución:**
1. **Fórmula del Baricentro Vectorial:**
   El baricentro o centroide $G$ de un triángulo cuyos vértices tienen vectores de posición $\vec{r}_A$, $\vec{r}_B$, y $\vec{r}_C$ se calcula como el promedio de estos vectores:
   $\vec{r}_G = \frac{1}{3} (\vec{r}_A + \vec{r}_B + \vec{r}_C)$
2. **Sustitución de Coordenadas:**
   $\vec{r}_G = \frac{1}{3} \left( \langle 4, 2, 0 \rangle + \langle 1, 3, 0 \rangle + \langle 1, 1, 3 \rangle \right)$
3. **Suma de Componentes:**
   Sumamos componente a componente:
   - $x: 4 + 1 + 1 = 6$
   - $y: 2 + 3 + 1 = 6$
   - $z: 0 + 0 + 3 = 3$
   $\vec{r}_G = \frac{1}{3} \langle 6, 6, 3 \rangle$
4. **Conclusión:**
   Multiplicando por el escalar, el vector de posición del baricentro es **$\langle 2, 2, 1 \rangle$**.

---

### Ejercicio 2.6 (Distancia Esfera-Plano)
**Enunciado:** Determine las coordenadas del punto de la esfera $x^2 + y^2 + z^2 = 4$ que está más cerca del plano $x+y+z=12$.

**Resolución:**
1. **Análisis Geométrico:**
   La esfera está centrada en el origen $(0,0,0)$ y tiene radio $R = \sqrt{4} = 2$.
   El plano tiene como vector normal $\vec{n} = \langle 1, 1, 1 \rangle$.
   El punto de la esfera más cercano al plano será el punto de intersección entre la esfera y una recta que pase por el centro de la esfera y sea *perpendicular* al plano (es decir, paralela a $\vec{n}$).
2. **Ecuación de la Recta Normal:**
   La recta pasa por el origen $(0,0,0)$ con dirección $\vec{n} = \langle 1, 1, 1 \rangle$:
   $\vec{r}(t) = \langle 0,0,0 \rangle + t\langle 1,1,1 \rangle = \langle t, t, t \rangle$
   Esto nos da las ecuaciones paramétricas: $x=t$, $y=t$, $z=t$.
3. **Intersección con la Esfera:**
   Reemplazamos la recta en la ecuación de la esfera:
   $(t)^2 + (t)^2 + (t)^2 = 4 \implies 3t^2 = 4 \implies t^2 = \frac{4}{3} \implies t = \pm \frac{2}{\sqrt{3}}$
   Esto nos da dos puntos candidatos (los "polos" de la esfera relativos al plano):
   $P_1 = \left( \frac{2}{\sqrt{3}}, \frac{2}{\sqrt{3}}, \frac{2}{\sqrt{3}} \right)$ y $P_2 = \left( -\frac{2}{\sqrt{3}}, -\frac{2}{\sqrt{3}}, -\frac{2}{\sqrt{3}} \right)$
4. **Elección del Punto Más Cercano:**
   El plano $x+y+z=12$ está en el "primer octante" (valores positivos).
   El punto $P_1$ tiene coordenadas positivas, acercándose al plano. Evaluemos la distancia (o simplemente notemos que al sustituir en la ecuación del plano, $P_1$ da un valor positivo más cercano a 12).
   Sustituyendo $P_1$ en $x+y+z$: $\frac{6}{\sqrt{3}} = 2\sqrt{3} \approx 3.46$.
   Sustituyendo $P_2$ en $x+y+z$: $-2\sqrt{3} \approx -3.46$.
   Claramente $P_1$ está "avanzando" hacia el plano de valor 12.
**Conclusión:** El punto de la esfera más cercano al plano es **$\left( \frac{2}{\sqrt{3}}, \frac{2}{\sqrt{3}}, \frac{2}{\sqrt{3}} \right)$**.

# Pauta Detallada - Subtema 15: Producto Punto y Cruz

El Producto Punto ($\vec{u} \cdot \vec{v}$) nos da un número y mide la "alineación" de los vectores. El Producto Cruz ($\vec{u} \times \vec{v}$) nos da un vector perpendicular y mide la "ortogonalidad" y el área.

---

### Ejercicio 2.11 (I2 2023-1)
**Enunciado:** Sean $\vec{u}, \vec{v}$ vectores tales que el ángulo entre ellos es $\pi/3$, con $||\vec{u}||=4$ y $||\vec{v}||=7$. Calcule los valores de:
a) $\vec{u} \cdot \vec{v}$
b) $||\vec{u} \times \vec{v}||$
c) $||3\vec{u} - 5\vec{v}||$

**Resolución:**
1. **Cálculo del Producto Punto:**
   Usamos la definición geométrica: $\vec{u} \cdot \vec{v} = ||\vec{u}|| \, ||\vec{v}|| \cos(\theta)$
   $\vec{u} \cdot \vec{v} = (4)(7) \cos(\pi/3) = 28 \cdot (1/2) = 14$
2. **Cálculo de la Magnitud del Producto Cruz:**
   Usamos la definición: $||\vec{u} \times \vec{v}|| = ||\vec{u}|| \, ||\vec{v}|| \sin(\theta)$
   $||\vec{u} \times \vec{v}|| = (4)(7) \sin(\pi/3) = 28 \cdot (\sqrt{3}/2) = 14\sqrt{3}$
3. **Cálculo de la Magnitud de la Combinación Lineal:**
   Para calcular la norma de una resta, elevamos al cuadrado y usamos propiedades del producto punto:
   $||3\vec{u} - 5\vec{v}||^2 = (3\vec{u} - 5\vec{v}) \cdot (3\vec{u} - 5\vec{v})$
   $= 9(\vec{u} \cdot \vec{u}) - 15(\vec{u} \cdot \vec{v}) - 15(\vec{v} \cdot \vec{u}) + 25(\vec{v} \cdot \vec{v})$
   $= 9||\vec{u}||^2 - 30(\vec{u} \cdot \vec{v}) + 25||\vec{v}||^2$
   Sustituimos los valores conocidos:
   $= 9(4^2) - 30(14) + 25(7^2)$
   $= 9(16) - 420 + 25(49) = 144 - 420 + 1225 = 949$
**Conclusión:** Los resultados son: a) **14**, b) **$14\sqrt{3}$**, c) **$\sqrt{949}$**.

---

### Ejercicio 2.12 (Pauta I2 2025-2)
**Enunciado:** Demuestre que el área del triángulo formado por los puntos $P, Q, R$ es $\frac{1}{2} ||\vec{QR} \times \vec{QP}||$. Utilice esto para demostrar que la distancia $d$ de un punto $P$ a la recta $L$ que pasa por $Q$ y $R$ es $d = \frac{||\vec{QR} \times \vec{QP}||}{||\vec{QR}||}$.

**Resolución:**
1. **Área del Triángulo:**
   Sabemos que $||\vec{a} \times \vec{b}||$ es igual al área del paralelogramo formado por los vectores. Un triángulo formado por tres puntos es exactamente la mitad de dicho paralelogramo.
   $A_{triangulo} = \frac{1}{2} A_{paralelogramo} = \frac{1}{2} ||\vec{QR} \times \vec{QP}||$
2. **Distancia Punto-Recta (Altura):**
   Geométricamente, el área de un triángulo también es $\frac{1}{2} \cdot \text{base} \cdot \text{altura}$.
   En este caso, la base es la longitud del segmento sobre la recta: $||\vec{QR}||$.
   La altura del triángulo desde el vértice $P$ es exactamente la distancia $d$ que buscamos.
   $A_{triangulo} = \frac{1}{2} \cdot ||\vec{QR}|| \cdot d$
3. **Igualación y Despeje:**
   $\frac{1}{2} ||\vec{QR} \times \vec{QP}|| = \frac{1}{2} ||\vec{QR}|| \cdot d$
   Simplificamos el factor $1/2$ y despejamos $d$:
   $d = \frac{||\vec{QR} \times \vec{QP}||}{||\vec{QR}||}$
**Conclusión:** Queda demostrada la fórmula de distancia mediante el uso de áreas vectoriales.

---

### Ejercicio 2.15 (Ayudantía 6 - Identidad del Producto Escalar)
**Enunciado:** Demuestre la identidad: $(\vec{a} \times \vec{b}) \cdot (\vec{c} \times \vec{d}) = (\vec{a} \cdot \vec{c})(\vec{b} \cdot \vec{d}) - (\vec{a} \cdot \vec{d})(\vec{b} \cdot \vec{c})$.

**Resolución:**
1. **Propiedad del Producto Mixto:**
   Sea $\vec{u} = \vec{a} \times \vec{b}$. La expresión es $\vec{u} \cdot (\vec{c} \times \vec{d})$.
   Por propiedad cíclica del producto triple escalar: $\vec{u} \cdot (\vec{c} \times \vec{d}) = \vec{d} \cdot (\vec{u} \times \vec{c})$.
2. **Sustitución y Triple Producto Vectorial:**
   Reemplazamos $\vec{u}$: $= \vec{d} \cdot ((\vec{a} \times \vec{b}) \times \vec{c})$.
   Usamos la regla BAC-CAB para el producto triple vectorial $(\vec{a} \times \vec{b}) \times \vec{c} = -\vec{c} \times (\vec{a} \times \vec{b}) = -[ \vec{a}(\vec{c} \cdot \vec{b}) - \vec{b}(\vec{c} \cdot \vec{a}) ]$.
   Reordenando: $= \vec{b}(\vec{a} \cdot \vec{c}) - \vec{a}(\vec{b} \cdot \vec{c})$.
3. **Distribución del Producto Punto final:**
   Multiplicamos por $\vec{d}$ usando producto punto:
   $= \vec{d} \cdot [ \vec{b}(\vec{a} \cdot \vec{c}) - \vec{a}(\vec{b} \cdot \vec{c}) ]$
   $= (\vec{d} \cdot \vec{b})(\vec{a} \cdot \vec{c}) - (\vec{d} \cdot \vec{a})(\vec{b} \cdot \vec{c})$
4. **Reordenamiento:**
   $= (\vec{a} \cdot \vec{c})(\vec{b} \cdot \vec{d}) - (\vec{a} \cdot \vec{d})(\vec{b} \cdot \vec{c})$
**Conclusión:** La identidad queda demostrada. Esta fórmula es útil para calcular productos de áreas orientadas en física y geometría avanzada.

# Pauta Detallada - Subtema 16: Ecuaciones de Rectas y Planos

**Conceptos Clave:**
* Para definir una **Recta ($L$)** necesitas: Un punto por el que pase ($P_0$) y un vector director ($\vec{v}$). 
  Ecuación Vectorial: $\vec{r}(t) = \vec{P_0} + t\vec{v}$
* Para definir un **Plano ($\Pi$)** necesitas: Un punto contenido en él ($P_0$) y un vector normal ($\vec{n}$) que sea perpendicular a todo el plano. 
  Ecuación Escalar: $A(x-x_0) + B(y-y_0) + C(z-z_0) = 0$

---

### Ejercicio 2.21 (Basado en I2 2023-1)
**Enunciado:** Encuentre la ecuación del plano $\Pi$ que pasa por el punto $P(-1, 2, 1)$ y que contiene a la recta $L$ dada por la intersección de los planos $\Pi_1: x+y-z=2$ y $\Pi_2: 2x-y+3z=1$.

**Resolución:**
1. **Hallar la dirección de la recta de intersección ($L$):**
   La recta $L$ está contenida en $\Pi_1$ y $\Pi_2$, por lo que su vector director $\vec{v}$ debe ser ortogonal a los vectores normales de ambos planos.
   $\vec{n}_1 = \langle 1, 1, -1 \rangle$
   $\vec{n}_2 = \langle 2, -1, 3 \rangle$
   $\vec{v} = \vec{n}_1 \times \vec{n}_2 = \langle (3-1), (-2-3), (-1-2) \rangle = \langle 2, -5, -3 \rangle$.
2. **Hallar un punto cualquiera de la recta ($L$):**
   Fijamos arbitrariamente $z = 0$ en el sistema de planos:
   $x + y = 2$
   $2x - y = 1$
   Sumando ambas ecuaciones: $3x = 3 \implies x = 1$. Reemplazando en la primera: $1 + y = 2 \implies y = 1$.
   El punto $Q(1, 1, 0)$ pertenece a la recta.
3. **Construir el vector normal del plano buscado ($\Pi$):**
   El plano $\Pi$ contiene al vector director $\vec{v}$ y al vector formado por los puntos $P$ y $Q$.
   $\vec{PQ} = Q - P = \langle 1 - (-1), 1 - 2, 0 - 1 \rangle = \langle 2, -1, -1 \rangle$.
   El vector normal será perpendicular a ambos:
   $\vec{n} = \vec{v} \times \vec{PQ} = \langle 2, -5, -3 \rangle \times \langle 2, -1, -1 \rangle$
   $= \langle 5 - 3, -6 - (-2), -2 - (-10) \rangle = \langle 2, -4, 8 \rangle$.
   *Nota simplificadora:* Podemos usar un vector paralelo más pequeño dividiendo por 2: $\vec{n}_{optimo} = \langle 1, -2, 4 \rangle$.
4. **Ecuación del plano ($\Pi$):**
   Usamos $\vec{n}_{optimo}$ y el punto $P(-1, 2, 1)$:
   $1(x + 1) - 2(y - 2) + 4(z - 1) = 0$
   $x + 1 - 2y + 4 + 4z - 4 = 0$
**Conclusión:** La ecuación general del plano es **$x - 2y + 4z + 1 = 0$**.

---

### Ejercicio 2.22 (Pauta Oficial I2 2022-TAV)
**Enunciado:** Encuentre una ecuación paramétrica de la recta $L$ que corresponde a la intersección de los planos $\Pi_1: x+y-3z=0$ y $\Pi_2: -x+2y+2z=1$.

**Resolución (Método Algebraico de la Pauta):**
En lugar del producto cruz, la pauta oficial propone parametrizar directamente resolviendo el sistema de ecuaciones.
1. **Despejar una variable en común:**
   De $\Pi_1$: $x = -y + 3z$   (Eq. 1)
   De $\Pi_2$: $x = 2y + 2z - 1$  (Eq. 2)
2. **Igualar y parametrizar:**
   Igualando (1) y (2):
   $-y + 3z = 2y + 2z - 1$
   Despejando $z$ en función de $y$:
   $z = 3y - 1$
3. **Expresar la otra variable en función del parámetro:**
   Sustituimos $z$ en la Eq. 1:
   $x = -y + 3(3y - 1) = -y + 9y - 3 = 8y - 3$
4. **Armar las ecuaciones paramétricas:**
   Definimos la variable libre $y$ como nuestro parámetro $t$ ($y = t$).
   $x = 8t - 3$
   $y = t$
   $z = 3t - 1$
**Conclusión:** La ecuación paramétrica es **$L: \{(8t-3, t, 3t-1) \mid t \in \mathbb{R}\}$**.

---

### Ejercicio 2.23 (Pauta Oficial I2 2025-1)
**Enunciado:** Determine la ecuación del plano que es perpendicular a los planos $2x-y+5z=28$ y $x+3y-z=7$, y cuya intersección con ellos es el punto $(-1, 5, 7)$.

**Resolución:**
1. **Identificación de Vectores Normales:**
   Extraemos los vectores normales de los planos dados:
   $\vec{n}_1 = \langle 2, -1, 5 \rangle$
   $\vec{n}_2 = \langle 1, 3, -1 \rangle$
2. **Vector Normal del Plano Buscado:**
   Si nuestro plano es perpendicular a los dos planos dados, su vector normal $\vec{n}$ debe ser simultáneamente perpendicular a $\vec{n}_1$ y $\vec{n}_2$. Por lo tanto, usamos el producto cruz:
   $\vec{n} = \vec{n}_1 \times \vec{n}_2 = | \begin{matrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & -1 & 5 \\ 1 & 3 & -1 \end{matrix} |$
   $\vec{n} = \hat{i}(1 - 15) - \hat{j}(-2 - 5) + \hat{k}(6 - (-1))$
   $\vec{n} = \langle -14, 7, 7 \rangle$
   *Podemos simplificar dividiendo por 7 para facilitar los cálculos:*
   $\vec{n}_{optimo} = \langle -2, 1, 1 \rangle$.
3. **Planteamiento de la Ecuación:**
   El enunciado nos dice explícitamente que el plano pasa por el punto $(-1, 5, 7)$.
   Usamos la ecuación punto-normal:
   $-2(x - (-1)) + 1(y - 5) + 1(z - 7) = 0$
   $-2(x + 1) + y - 5 + z - 7 = 0$
   $-2x - 2 + y - 5 + z - 7 = 0$
   $-2x + y + z - 14 = 0$
**Conclusión:** La ecuación del plano es **$-2x + y + z = 14$** (o multiplicando por -1: $2x - y - z = -14$).

# Pauta Detallada - Subtema 17: Dominios de Funciones

El dominio de una función $f(x,y)$ es el conjunto de todos los puntos $(x,y) \in \mathbb{R}^2$ para los cuales la expresión de la función está bien definida matemáticamente.

**Restricciones clave a considerar:**
1.  **Raíces de índice par:** El argumento debe ser $\ge 0$.
2.  **Logaritmos:** El argumento debe ser estrictamente $> 0$.
3.  **Denominadores:** Deben ser distintos de $0$.
4.  **Funciones trigonométricas inversas:** $\arcsin(u)$ y $\arccos(u)$ requieren $-1 \le u \le 1$.

---

### Ejercicio 3.1 (I2 2023-1)
**Enunciado:** Determine y grafique el dominio de la función:
$$f(x,y) = \frac{\ln(x-1) + \sqrt{y-x} + \ln(4-y)}{x^2+2x+1}$$

**Resolución:**
Para que la función exista, todas sus partes deben estar definidas simultáneamente. Establecemos el sistema de inecuaciones:

1.  **Por el primer logaritmo:** $x - 1 > 0 \implies x > 1$.
2.  **Por la raíz cuadrada:** $y - x \ge 0 \implies y \ge x$.
3.  **Por el segundo logaritmo:** $4 - y > 0 \implies y < 4$.
4.  **Por el denominador:** $x^2 + 2x + 1 \neq 0 \implies (x+1)^2 \neq 0 \implies x \neq -1$.

**Análisis de la intersección:**
* De (1) y (4): Como $x > 1$, la restricción $x \neq -1$ ya se cumple automáticamente.
* De (2) y (3): Los puntos deben estar sobre la recta $y=x$ y por debajo de la recta horizontal $y=4$.

**Descripción formal:**
$Dom(f) = \{ (x,y) \in \mathbb{R}^2 : x > 1, \, y \ge x, \, y < 4 \}$.

**Geometría de la región:** Es un triángulo en el primer cuadrante delimitado por las rectas $x=1$ (punteada), $y=4$ (punteada) e $y=x$ (sólida).

---

### Ejercicio 3.2 (Pauta I2 2025-2)
**Enunciado:** Determine el dominio de $f(x,y) = \sqrt{\frac{x-y}{1-x^2-y^2}}$.

**Resolución:**
Para que la raíz cuadrada esté definida, el cociente debe ser mayor o igual a cero:
$$\frac{x-y}{1-x^2-y^2} \ge 0$$
Además, el denominador no puede ser cero: $x^2 + y^2 \neq 1$.

Este problema se resuelve analizando dos casos (donde el signo del cociente es positivo o cero):

**Caso 1: Numerador $\ge 0$ y Denominador $> 0$**
* $x - y \ge 0 \implies y \le x$ (Región bajo la diagonal principal).
* $1 - x^2 - y^2 > 0 \implies x^2 + y^2 < 1$ (Interior del círculo unitario).

**Caso 2: Numerador $\le 0$ y Denominador $< 0$**
* $x - y \le 0 \implies y \ge x$ (Región sobre la diagonal principal).
* $1 - x^2 - y^2 < 0 \implies x^2 + y^2 > 1$ (Exterior del círculo unitario).

**Conclusión:** El dominio es la unión de la sección del círculo unitario que está bajo la recta $y=x$, junto con la región exterior al círculo que está sobre la recta $y=x$.

---

### Ejercicio 3.4 (Ayudantía 6 - 2026)
**Enunciado:** Determine y grafique el dominio de $f(x,y) = \sqrt{1-x^2} - \sqrt{1-y^2}$.

**Resolución:**
1.  **Restricción 1 (primera raíz):** $1 - x^2 \ge 0 \implies x^2 \le 1 \implies |x| \le 1$. Analíticamente: $-1 \le x \le 1$.
2.  **Restricción 2 (segunda raíz):** $1 - y^2 \ge 0 \implies y^2 \le 1 \implies |y| \le 1$. Analíticamente: $-1 \le y \le 1$.

**Análisis Geométrico:**
El dominio es la intersección de una franja vertical entre $x=-1$ y $x=1$, con una franja horizontal entre $y=-1$ e $y=1$.
**Conclusión:** El dominio es el **cuadrado sólido** centrado en el origen con vértices en $(1,1), (-1,1), (-1,-1)$ y $(1,-1)$.
$Dom(f) = \{ (x,y) \in \mathbb{R}^2 : -1 \le x \le 1, \, -1 \le y \le 1 \}$.

# Pauta Detallada - Subtema 18: Gráficas y Curvas de Nivel

**Concepto Clave:**
Las **curvas de nivel** de una función $f(x,y)$ son el conjunto de puntos $(x,y)$ que satisfacen la ecuación $f(x,y) = k$, donde $k$ es una constante (perteneciente al recorrido de $f$). Representan "cortes horizontales" de la superficie $z = f(x,y)$.

---

### Ejercicio 3.11 (I2 2023-1)
**Enunciado:** Grafique la curva de nivel $f(x,y) = -2$ para la función $f(x,y) = \frac{x^2+y^2}{y-4}$.

**Resolución:**
1.  **Planteamiento de la ecuación de nivel:**
    Igualamos la función al valor $k = -2$:
    $$\frac{x^2+y^2}{y-4} = -2$$
2.  **Manipulación Algebraica:**
    Multiplicamos por el denominador (notando que $y \neq 4$):
    $$x^2 + y^2 = -2(y - 4)$$
    $$x^2 + y^2 = -2y + 8$$
    $$x^2 + y^2 + 2y = 8$$
3.  **Completación de Cuadrados:**
    Para identificar la figura geométrica en el plano $xy$, completamos el cuadrado para la variable $y$:
    $$x^2 + (y^2 + 2y + 1) = 8 + 1$$
    $$x^2 + (y+1)^2 = 9$$
4.  **Identificación Geométrica:**
    La ecuación $x^2 + (y+1)^2 = 3^2$ corresponde a una **circunferencia** con centro en $(0, -1)$ y radio $R = 3$.
**Conclusión:** La curva de nivel $k = -2$ es una circunferencia de radio 3 centrada en $(0, -1)$.

---

### Ejercicio 3.12 (I2 2023-2)
**Enunciado:** Para la función $f(x,y) = \sqrt{9 - x - y^2}$, bosqueje las curvas de nivel para $k=0$ y $k=3$.

**Resolución:**
1.  **Para $k = 0$:**
    $$\sqrt{9 - x - y^2} = 0 \implies 9 - x - y^2 = 0 \implies x = 9 - y^2$$
    Esta es una **parábola** que abre hacia la izquierda, con vértice en $(9, 0)$ y cortes en el eje $y$ en $(0, 3)$ y $(0, -3)$.
2.  **Para $k = 3$:**
    $$\sqrt{9 - x - y^2} = 3 \implies 9 - x - y^2 = 9 \implies -x - y^2 = 0 \implies x = -y^2$$
    Esta es una **parábola** con vértice en el origen $(0,0)$ que abre hacia la izquierda.
**Conclusión:** El mapa de contorno muestra una familia de parábolas que se desplazan hacia la izquierda a medida que $k$ aumenta.

---

### Ejercicio 3.15 (Ayudantía 6 - 2026)
**Enunciado:** Identifique la superficie dada por la ecuación $4x^2 - y^2 + z^2 - 8x + 2y + 4 = 0$.

**Resolución:**
1.  **Agrupación de términos:**
    $$(4x^2 - 8x) - (y^2 - 2y) + z^2 = -4$$
2.  **Completación de cuadrados:**
    $$4(x^2 - 2x + 1) - (y^2 - 2y + 1) + z^2 = -4 + 4(1) - (1)$$
    $$4(x-1)^2 - (y-1)^2 + z^2 = -1$$
3.  **Forma Canónica:**
    Multiplicamos por $-1$ para obtener un valor positivo en el lado derecho:
    $$(y-1)^2 - 4(x-1)^2 - z^2 = 1$$
    $$\frac{(y-1)^2}{1^2} - \frac{(x-1)^2}{(1/2)^2} - \frac{z^2}{1^2} = 1$$
4.  **Identificación:**
    Esta ecuación tiene la forma $\frac{y^2}{b^2} - \frac{x^2}{a^2} - \frac{z^2}{c^2} = 1$. Presenta dos signos negativos, lo cual corresponde a un **Hiperboloide de dos hojas** que se abre a lo largo del eje $y$ (variable con signo positivo).
**Conclusión:** La superficie es un hiperboloide de dos hojas centrado en $(1, 1, 0)$.

# Pauta Detallada - Subtema 19: Límites de Funciones

Para resolver límites en $\mathbb{R}^2$, seguimos este orden lógico:
1.  **Sustitución directa:** Si la función es continua y no hay indeterminación, el límite es simplemente el valor evaluado.
2.  **Prueba de trayectorias (No existencia):** Si sospechas que el límite no existe, intenta acercarte por $y = mx$, $y = ax^2$, etc. Si obtienes dos resultados distintos, el límite no existe.
3.  **Coordenadas Polares / Acotamiento:** Si sospechas que el límite existe (usualmente es 0), usa $x = r \cos \theta, y = r \sin \theta$. Si el resultado depende de $\theta$, el límite no existe.

---

### Ejercicio 3.21 (I2 2022-TAV)
**Enunciado:** Demuestre que no existe $\lim_{(x,y) \rightarrow (0,0)} \frac{x^2y^2}{x^3+y^3}$.

**Resolución:**
1.  **Trayectoria 1 (Recta $y = x$):**
    $\lim_{x \to 0} \frac{x^2(x)^2}{x^3+x^3} = \lim_{x \to 0} \frac{x^4}{2x^3} = \lim_{x \to 0} \frac{x}{2} = 0$.
2.  **Trayectoria 2 (Curva $y = -xe^x$):**
    Esta trayectoria se elige porque "anula" el denominador más rápido que el numerador.
    Sustituimos $y = -xe^x$:
    $L = \lim_{x \to 0} \frac{x^2(-xe^x)^2}{x^3 + (-xe^x)^3} = \lim_{x \to 0} \frac{x^4 e^{2x}}{x^3(1 - e^{3x})}$
    $= \lim_{x \to 0} e^{2x} \cdot \frac{x}{1 - e^{3x}}$
    Aplicando L'Hôpital al segundo factor: $\lim_{x \to 0} \frac{1}{-3e^{3x}} = -1/3$.
    $L = 1 \cdot (-1/3) = -1/3$.
**Conclusión:** Como $0 \neq -1/3$, el límite **no existe**.

---

### Ejercicio 3.22 (I2 2023-2)
**Enunciado:** Estudie el límite $\lim_{(x,y) \rightarrow (0,0)} \frac{x^3y^4}{x^4+y^4}$.

**Resolución:**
Cuando el grado del numerador (7) es mucho mayor al del denominador (4), es probable que el límite sea 0. Usamos **Coordenadas Polares**:
1.  **Sustitución:** $x = r \cos \theta, y = r \sin \theta$.
    $\lim_{r \to 0} \frac{(r \cos \theta)^3 (r \sin \theta)^4}{(r \cos \theta)^4 + (r \sin \theta)^4} = \lim_{r \to 0} \frac{r^7 \cos^3 \theta \sin^4 \theta}{r^4 (\cos^4 \theta + \sin^4 \theta)}$
2.  **Simplificación:**
    $= \lim_{r \to 0} r^3 \cdot \frac{\cos^3 \theta \sin^4 \theta}{\cos^4 \theta + \sin^4 \theta}$
3.  **Análisis de acotamiento:**
    La fracción $\frac{\cos^3 \theta \sin^4 \theta}{\cos^4 \theta + \sin^4 \theta}$ es una función que solo depende de $\theta$. Como el denominador $\cos^4 \theta + \sin^4 \theta$ nunca es cero en el círculo unitario, la fracción está **acotada**.
    Como $r^3 \to 0$ y está multiplicado por algo acotado:
    $0 \cdot (\text{acotado}) = 0$.
**Conclusión:** El límite **existe y es igual a 0**.

---

### Ejercicio 3.23 (I2 2024-TAV)
**Enunciado:** Determine si existe $\lim_{(x,y) \rightarrow (0,0)} \frac{x^4y^4}{(x^2+y^4)^3}$.

**Resolución:**
Notamos que los exponentes en el denominador son $x^2$ y $y^4$. Para "equilibrarlos", probamos la trayectoria $x = y^2$.
1.  **Trayectoria 1 (Eje $x$, $y=0$):**
    $\lim_{x \to 0} \frac{0}{(x^2+0)^3} = 0$.
2.  **Trayectoria 2 (Parábola $x = y^2$):**
    $\lim_{y \to 0} \frac{(y^2)^4 y^4}{((y^2)^2 + y^4)^3} = \lim_{y \to 0} \frac{y^8 y^4}{(y^4 + y^4)^3}$
    $= \lim_{y \to 0} \frac{y^{12}}{(2y^4)^3} = \lim_{y \to 0} \frac{y^{12}}{8y^{12}} = \frac{1}{8}$.
**Conclusión:** Como $0 \neq 1/8$, el límite **no existe**.

---

### Ejercicio 3.24 (Pauta I2 2024-2)
**Enunciado:** Analice el límite $\lim_{(x,y) \rightarrow (0,0)} \frac{y^2 \sin^2(x)}{x^4+y^4}$.

**Resolución:**
1.  **Trayectoria 1 (Eje $x$, $y=0$):** El límite es 0.
2.  **Trayectoria 2 (Recta $y = x$):**
    $\lim_{x \to 0} \frac{x^2 \sin^2(x)}{x^4 + x^4} = \lim_{x \to 0} \frac{x^2 \sin^2(x)}{2x^4} = \lim_{x \to 0} \frac{1}{2} \left( \frac{\sin x}{x} \right)^2$
    Sabemos que $\lim_{x \to 0} \frac{\sin x}{x} = 1$.
    Por lo tanto, el límite es $1/2 \cdot (1)^2 = 1/2$.
**Conclusión:** Como los límites por distintas trayectorias son diferentes ($0$ y $1/2$), el límite **no existe**.

# Pauta Detallada - Subtema 21: Derivadas Parciales y Regla de la Cadena

**Conceptos Clave:**
1.  **Definición por límite:** $f_x(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0+h, y_0) - f(x_0, y_0)}{h}$. Se usa obligatoriamente en puntos conflictivos (como el origen) donde las reglas de derivación fallan.
2.  **Regla de la Cadena:** Si $w = f(u,v)$ y a su vez $u = g(x,y)$, $v = h(x,y)$, entonces para derivar $w$ respecto a $x$ se ramifica: $w_x = f_u \cdot u_x + f_v \cdot v_x$.
3.  **Gradiente ($\nabla f$):** Es el vector formado por las primeras derivadas parciales $\langle f_x, f_y, f_z \rangle$. Siempre apunta en la dirección de máximo crecimiento de la función.

---

### Ejercicio 4.1 (I2 2023-2)
**Enunciado:** Sea $f(x,y) = \sqrt[3]{x^3+y^3}$. Determine, en caso de que exista, $f_x(0,0)$ mediante la definición de derivada parcial.

**Resolución:**
1.  **Planteamiento de la definición:**
    La derivada parcial respecto a $x$ en el origen se define como:
    $$f_x(0,0) = \lim_{h \to 0} \frac{f(0+h, 0) - f(0,0)}{h} = \lim_{h \to 0} \frac{f(h, 0) - f(0,0)}{h}$$
2.  **Evaluación de la función:**
    * $f(0,0) = \sqrt[3]{0^3+0^3} = 0$.
    * $f(h,0) = \sqrt[3]{h^3+0^3} = \sqrt[3]{h^3} = h$.
3.  **Cálculo del límite:**
    $$f_x(0,0) = \lim_{h \to 0} \frac{h - 0}{h} = \lim_{h \to 0} \frac{h}{h} = \lim_{h \to 0} 1 = 1$$
**Conclusión:** La derivada parcial $f_x(0,0)$ **existe y es igual a 1**. *(Nota: Si derivas usando la regla de la cadena directamente, te quedará un cero en el denominador, lo cual es un error conceptual común).*

---

### Ejercicio 4.3 (I2 2022-TAV)
**Enunciado:** Si $w = f\left(\frac{y-x}{xy}, \frac{z-y}{yz}\right)$, donde $f$ es diferenciable, demuestre que $x^2 \frac{\partial w}{\partial x} + y^2 \frac{\partial w}{\partial y} + z^2 \frac{\partial w}{\partial z} = 0$.

**Resolución:**
1.  **Cambio de variables:**
    Definimos variables intermedias para facilitar la regla de la cadena:
    $u = \frac{y-x}{xy} = \frac{1}{x} - \frac{1}{y}$
    $v = \frac{z-y}{yz} = \frac{1}{y} - \frac{1}{z}$
    Así, $w = f(u, v)$.
2.  **Cálculo de derivadas parciales (Regla de la Cadena):**
    * Para $x$: $w_x = f_u \cdot u_x + f_v \cdot v_x$
        $u_x = -\frac{1}{x^2}$ ; $v_x = 0$ $\implies w_x = -f_u \frac{1}{x^2}$
    * Para $y$: $w_y = f_u \cdot u_y + f_v \cdot v_y$
        $u_y = \frac{1}{y^2}$ ; $v_y = -\frac{1}{y^2}$ $\implies w_y = f_u \frac{1}{y^2} - f_v \frac{1}{y^2}$
    * Para $z$: $w_z = f_u \cdot u_z + f_v \cdot v_z$
        $u_z = 0$ ; $v_z = \frac{1}{z^2}$ $\implies w_z = f_v \frac{1}{z^2}$
3.  **Sustitución en la ecuación pedida:**
    Reemplazamos en la expresión $x^2 w_x + y^2 w_y + z^2 w_z$:
    $= x^2 \left(-f_u \frac{1}{x^2}\right) + y^2 \left(\frac{f_u - f_v}{y^2}\right) + z^2 \left(f_v \frac{1}{z^2}\right)$
    Simplificamos los coeficientes:
    $= -f_u + (f_u - f_v) + f_v$
    $= -f_u + f_u - f_v + f_v = 0$
**Conclusión:** La igualdad matemática queda **demostrada**.

---

### Ejercicio 4.5 (I2 2024-TAV)
**Enunciado:** Calcule la dirección en la cual se produce el mayor crecimiento de la temperatura $T(x,y,z) = x^2 + 2y^2 + 2z^2$ en el punto $(1,1,1)$.

**Resolución:**
1.  **Fundamento teórico:**
    La dirección de máximo crecimiento está dada por el vector unitario que apunta en la misma dirección que el **vector gradiente** $\nabla T$ evaluado en el punto.
2.  **Cálculo del Gradiente:**
    $\nabla T = \left\langle \frac{\partial T}{\partial x}, \frac{\partial T}{\partial y}, \frac{\partial T}{\partial z} \right\rangle$
    $\nabla T = \langle 2x, 4y, 4z \rangle$
3.  **Evaluación en el punto $(1,1,1)$:**
    $\nabla T(1,1,1) = \langle 2(1), 4(1), 4(1) \rangle = \langle 2, 4, 4 \rangle$
4.  **Normalización del vector (Dirección):**
    Calculamos la magnitud (norma) del gradiente:
    $||\nabla T|| = \sqrt{2^2 + 4^2 + 4^2} = \sqrt{4 + 16 + 16} = \sqrt{36} = 6$.
    La dirección es el vector unitario $\hat{u} = \frac{\nabla T}{||\nabla T||}$:
    $\hat{u} = \left\langle \frac{2}{6}, \frac{4}{6}, \frac{4}{6} \right\rangle = \left\langle \frac{1}{3}, \frac{2}{3}, \frac{2}{3} \right\rangle$
**Conclusión:** La dirección de máximo crecimiento es **$\left\langle \frac{1}{3}, \frac{2}{3}, \frac{2}{3} \right\rangle$**.

---

### Ejercicio 4.8 (Pauta I2 2023-2)
**Enunciado:** Sea $f(x,y) = \frac{e^{-x^2/y}}{\sqrt{y}}$. Determine para qué valor de $c \in \mathbb{R}$ se cumple que $f_y + c f_{xx} = 0$.

**Resolución:**
Para facilitar las derivadas, reescribimos $f(x,y) = y^{-1/2} e^{-x^2/y}$.

1.  **Derivadas respecto a $x$ (manteniendo $y$ constante):**
    $f_x = y^{-1/2} e^{-x^2/y} \cdot \left(\frac{-2x}{y}\right) = -2x y^{-3/2} e^{-x^2/y}$.
    Para $f_{xx}$, aplicamos regla del producto sobre $x$:
    $f_{xx} = \frac{\partial}{\partial x} \left[ -2x \left(y^{-3/2} e^{-x^2/y}\right) \right]$
    $f_{xx} = -2 \left(y^{-3/2} e^{-x^2/y}\right) - 2x \left[ y^{-3/2} e^{-x^2/y} \left(\frac{-2x}{y}\right) \right]$
    $f_{xx} = -2y^{-3/2} e^{-x^2/y} + 4x^2 y^{-5/2} e^{-x^2/y}$.

2.  **Derivada respecto a $y$ (regla del producto):**
    $f_y = \left( -\frac{1}{2}y^{-3/2} \right) e^{-x^2/y} + y^{-1/2} e^{-x^2/y} \left( \frac{x^2}{y^2} \right)$
    $f_y = -\frac{1}{2}y^{-3/2} e^{-x^2/y} + x^2 y^{-5/2} e^{-x^2/y}$.

3.  **Sustitución en la ecuación térmica:**
    $f_y + c f_{xx} = 0$
    Sustituimos y factorizamos el término común $e^{-x^2/y}$:
    $e^{-x^2/y} \left[ \left(-\frac{1}{2}y^{-3/2} + x^2 y^{-5/2}\right) + c\left(-2y^{-3/2} + 4x^2 y^{-5/2}\right) \right] = 0$
    
    Como la exponencial nunca es cero, lo que está entre corchetes debe anularse. Agrupamos por potencias de $y$:
    $y^{-3/2} \left(-\frac{1}{2} - 2c\right) + x^2 y^{-5/2} \left(1 + 4c\right) = 0$
    
    Para que esta igualdad se cumpla para todo $x,y$, los coeficientes deben ser simultáneamente cero:
    $1 + 4c = 0 \implies 4c = -1 \implies c = -\frac{1}{4}$
    Y verificamos en el otro: $-\frac{1}{2} - 2\left(-\frac{1}{4}\right) = -\frac{1}{2} + \frac{1}{2} = 0$.
**Conclusión:** El valor constante es **$c = -\frac{1}{4}$**.