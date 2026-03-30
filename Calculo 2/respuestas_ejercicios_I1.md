# Solucionario Detallado: Cálculo II

## Integrales Impropias

**1. Convergencia de integrales impropias:**

* **a) $\int_{2}^{\infty}\frac{x+\sin x}{x^{2}-x}dx$**
  Por propiedades trigonométricas, $-1 \le \sin x \le 1$. Sumando $x$: $x-1 \le x+\sin x$.
  Para $x \ge 2$, se cumple $x^2 \ge 2x > x$, implicando $x^2-x > 0$.
  Al dividir la desigualdad por $x^2-x$ (término positivo), la relación se mantiene:
  $\frac{x+\sin x}{x^{2}-x} \ge \frac{x-1}{x^2-x}$.
  Factorizando el denominador: $\frac{x-1}{x(x-1)} = \frac{1}{x}$.
  Se analiza la integral de la cota inferior: $\int_{2}^{\infty}\frac{1}{x}dx = \lim_{b \to \infty} [\ln|x|]_{2}^{b} = \lim_{b \to \infty} (\ln b - \ln 2) = \infty$.
  Como la integral de la función menor diverge, la integral evaluada diverge por el Criterio de Comparación Directa.

* **b) $\int_{1}^{3}\frac{x}{(x-3)^{3}}dx$**
  Existe una discontinuidad infinita en $x=3$. Se plantea el límite: $\lim_{b\rightarrow3^{-}}\int_{1}^{b}\frac{x}{(x-3)^{3}}dx$.
  Sustitución: $u = x-3 \implies x = u+3 \implies dx = du$.
  Integral indefinida: $\int\frac{u+3}{u^{3}}du = \int(u^{-2}+3u^{-3})du = -u^{-1}-\frac{3}{2}u^{-2} = -\frac{1}{x-3}-\frac{3}{2(x-3)^{2}}$.
  Evaluación del límite:
  $\lim_{b\rightarrow3^{-}}\left(-\frac{1}{b-3}-\frac{3}{2(b-3)^{2}}\right) - \left(-\frac{1}{1-3}-\frac{3}{2(1-3)^{2}}\right)$.
  $\lim_{b\rightarrow3^{-}}\left(\frac{-2(b-3)-3}{2(b-3)^{2}}\right) = \lim_{b\rightarrow3^{-}}\left(\frac{-2b+3}{2(b-3)^{2}}\right)$.
  El numerador tiende a $-3$ y el denominador a $0^+$. El cociente tiende a $-\infty$. La integral diverge.

* **c) $\int_{0}^{1}\frac{\ln(x)}{\sqrt{x}}dx$**
  Discontinuidad infinita en $x=0$. Límite: $\lim_{t\rightarrow0^{+}}\int_{t}^{1}x^{-1/2}\ln(x)dx$.
  Integración por partes: $u = \ln(x) \implies du = \frac{1}{x}dx$; $dv = x^{-1/2}dx \implies v = 2x^{1/2}$.
  $\int x^{-1/2}\ln(x)dx = 2x^{1/2}\ln(x) - \int 2x^{1/2} \cdot \frac{1}{x}dx = 2\sqrt{x}\ln(x) - 2\int x^{-1/2}dx = 2\sqrt{x}\ln(x) - 4\sqrt{x}$.
  Evaluación: $\lim_{t\rightarrow0^{+}}\left[2\sqrt{1}\ln(1) - 4\sqrt{1} - (2\sqrt{t}\ln(t) - 4\sqrt{t})\right] = -4 - 2\lim_{t\rightarrow0^{+}}\sqrt{t}\ln(t) + 4(0)$.
  Resolución de la indeterminación $0 \cdot (-\infty)$ mediante L'Hôpital:
  $\lim_{t\rightarrow0^{+}}\frac{\ln(t)}{t^{-1/2}} \xrightarrow{L'H} \lim_{t\rightarrow0^{+}}\frac{1/t}{-(1/2)t^{-3/2}} = \lim_{t\rightarrow0^{+}}-2t^{1/2} = 0$.
  Sustituyendo el límite: $-4 - 2(0) = -4$. Converge a $-4$.

* **d) $\int_{-\infty}^{\infty}\frac{6x^{3}}{(x^{4}+1)^{2}}dx$**
  Se divide el intervalo en $x=0$: $\lim_{a\rightarrow-\infty}\int_{a}^{0}\frac{6x^{3}}{(x^{4}+1)^{2}}dx + \lim_{b\rightarrow\infty}\int_{0}^{b}\frac{6x^{3}}{(x^{4}+1)^{2}}dx$.
  Sustitución: $u = x^{4}+1 \implies du = 4x^{3}dx \implies \frac{3}{2}du = 6x^{3}dx$.
  Integral indefinida: $\int\frac{3/2}{u^{2}}du = -\frac{3}{2}u^{-1} = -\frac{3}{2(x^{4}+1)}$.
  Límite izquierdo: $\lim_{a\rightarrow-\infty}\left(-\frac{3}{2(0+1)} - \left(-\frac{3}{2(a^{4}+1)}\right)\right) = -\frac{3}{2} - 0 = -\frac{3}{2}$.
  Límite derecho: $\lim_{b\rightarrow\infty}\left(-\frac{3}{2(b^{4}+1)} - \left(-\frac{3}{2(0+1)}\right)\right) = 0 + \frac{3}{2} = \frac{3}{2}$.
  Suma: $-\frac{3}{2} + \frac{3}{2} = 0$. Converge a $0$.

* **e) $\int_{3}^{\infty}\frac{1}{(x-2)^{3/2}}dx$**
  Límite asintótico: $\lim_{b\rightarrow\infty}\int_{3}^{b}(x-2)^{-3/2}dx$.
  Antiderivada: $\frac{(x-2)^{-1/2}}{-1/2} = -2(x-2)^{-1/2} = \frac{-2}{\sqrt{x-2}}$.
  Evaluación: $\lim_{b\rightarrow\infty}\left(\frac{-2}{\sqrt{b-2}} - \frac{-2}{\sqrt{3-2}}\right)$.
  Como $\lim_{b\rightarrow\infty}\frac{-2}{\sqrt{b-2}} = 0$, el resultado es $0 - (-2) = 2$. Converge a $2$.

* **f) $\int_{-\infty}^{0}5^{t}dt$**
  Límite asintótico: $\lim_{a\rightarrow-\infty}\int_{a}^{0}5^{t}dt$.
  Antiderivada: $\frac{5^{t}}{\ln(5)}$.
  Evaluación: $\lim_{a\rightarrow-\infty}\left(\frac{5^{0}}{\ln(5)} - \frac{5^{a}}{\ln(5)}\right)$.
  Como $5 > 1$, $\lim_{a\rightarrow-\infty}5^{a} = 0$.
  Resultado: $\frac{1}{\ln(5)} - 0 = \frac{1}{\ln(5)}$. Converge a $\frac{1}{\ln(5)}$.

* **g) $\int_{0}^{9}\frac{1}{\sqrt[3]{x-1}}dx$**
  Discontinuidad infinita en $x=1$. Se separa en dos integrales: $\lim_{a\rightarrow1^{-}}\int_{0}^{a}(x-1)^{-1/3}dx + \lim_{b\rightarrow1^{+}}\int_{b}^{9}(x-1)^{-1/3}dx$.
  Antiderivada: $\frac{(x-1)^{2/3}}{2/3} = \frac{3}{2}(x-1)^{2/3}$.
  Primer límite: $\lim_{a\rightarrow1^{-}}\left(\frac{3}{2}(a-1)^{2/3} - \frac{3}{2}(0-1)^{2/3}\right) = 0 - \frac{3}{2}(-1)^{2/3} = -\frac{3}{2}$.
  Segundo límite: $\lim_{b\rightarrow1^{+}}\left(\frac{3}{2}(9-1)^{2/3} - \frac{3}{2}(b-1)^{2/3}\right) = \frac{3}{2}(8)^{2/3} - 0 = \frac{3}{2}(4) = 6$.
  Suma total: $-\frac{3}{2} + 6 = \frac{9}{2}$. Converge a $\frac{9}{2}$.

* **h) $\int_{0}^{1}\frac{\sec^{2}(x)}{x\sqrt{x}}dx$**
  En el intervalo $(0,1]$, la función $\cos(x)$ decrece desde $1$ hasta $\cos(1) > 0$.
  Por lo tanto, $0 < \cos(x) \le 1 \implies \sec(x) \ge 1 \implies \sec^{2}(x) \ge 1$.
  Multiplicando por $x^{-3/2}$ (positivo en el dominio): $\frac{\sec^{2}(x)}{x^{3/2}} \ge \frac{1}{x^{3/2}}$.
  La integral $\int_{0}^{1}x^{-3/2}dx = \lim_{t\to0^+}\left[-2x^{-1/2}\right]_t^1 = -2 - \lim_{t\to0^+}\frac{-2}{\sqrt{t}} = \infty$.
  Diverge por ser $p$-integral con $p = 3/2 \ge 1$.
  Por Criterio de Comparación Directa, la integral original diverge.

* **i) $\int_{0}^{\infty}\frac{\sqrt{x^{5}+3x^{3}+5x}}{x^{4}+x^{2}+1}dx$**
  El integrando es continuo en $[0,\infty)$. El comportamiento asintótico determina la convergencia en infinito.
  Término dominante del numerador: $\sqrt{x^5} = x^{5/2}$.
  Término dominante del denominador: $x^4$.
  Razón dominante: $b(x) = \frac{x^{5/2}}{x^4} = \frac{1}{x^{3/2}}$.
  Se aplica Criterio de Comparación en el Límite:
  $\lim_{x\rightarrow\infty}\frac{a(x)}{b(x)} = \lim_{x\rightarrow\infty}\frac{\sqrt{x^{5}+3x^{3}+5x}}{x^{4}+x^{2}+1} \cdot \frac{x^{3/2}}{1} = \lim_{x\rightarrow\infty}\frac{\sqrt{x^3(x^{5}+3x^{3}+5x)}}{x^{4}+x^{2}+1} = \lim_{x\rightarrow\infty}\frac{\sqrt{x^8+3x^6+5x^4}}{x^4+x^2+1}$.
  Dividiendo numerador y denominador por $x^4 = \sqrt{x^8}$:
  $\lim_{x\rightarrow\infty}\frac{\sqrt{1+3/x^2+5/x^4}}{1+1/x^2+1/x^4} = \frac{\sqrt{1+0+0}}{1+0+0} = 1$.
  Como $0 < 1 < \infty$, ambas integrales comparten convergencia. La integral $\int_{1}^{\infty}x^{-3/2}dx$ converge ($p = 3/2 > 1$). La integral evaluada converge.

* **j) $\int_{1}^{\infty}\frac{\cos(1/t)}{\sqrt{t}}dt$**
  Para $t \in [1,\infty)$, el argumento $1/t \in (0,1]$.
  En $(0,1]$, la función $\cos(x)$ es decreciente y positiva, alcanzando su mínimo en $x=1$.
  Por lo tanto, $\cos(1/t) \ge \cos(1) > 0$.
  Dividiendo por $\sqrt{t}$: $\frac{\cos(1/t)}{\sqrt{t}} \ge \frac{\cos(1)}{t^{1/2}}$.
  La integral $\int_{1}^{\infty}t^{-1/2}dt = \lim_{b\to\infty}[2t^{1/2}]_1^b = \infty$. Diverge ($p = 1/2 \le 1$).
  Por Comparación Directa, la integral diverge.

**2. Criterio de comparación:**

* **a) $\int_{0}^{\infty}\frac{x}{x^{3}+1}dx$**
  Se divide la integral en $[0,1]$ (propia, finita) y $[1,\infty)$ (impropia).
  Para $x \ge 1$: $x^3 + 1 > x^3 > 0$.
  Invirtiendo y multiplicando por $x$: $\frac{x}{x^3+1} < \frac{x}{x^3} = \frac{1}{x^2}$.
  La integral $\int_{1}^{\infty}x^{-2}dx$ converge ($p=2>1$).
  Por Comparación Directa, la integral original converge.

* **b) $\int_{1}^{\infty}\frac{w^{2}+1}{w^{3}(\cos^{2}(w)+1)}dw$**
  Acotamiento del numerador: $w^2+1 > w^2$.
  Acotamiento del denominador trigonométrico: $-1 \le \cos(w) \le 1 \implies 0 \le \cos^2(w) \le 1 \implies 1 \le \cos^2(w)+1 \le 2$.
  Sustituyendo el máximo valor en el denominador minimiza la fracción: $\frac{1}{\cos^2(w)+1} \ge \frac{1}{2}$.
  Construcción de la desigualdad combinada: $\frac{w^2+1}{w^3(\cos^2(w)+1)} > \frac{w^2}{w^3(2)} = \frac{1}{2w}$.
  La integral $\int_{1}^{\infty}\frac{1}{2w}dw = \frac{1}{2}\lim_{b\to\infty}[\ln|w|]_1^b = \infty$.
  Por Comparación Directa, la integral diverge.

**3. Determinación de $C$ en $\int_{0}^{\infty}\left(\frac{x}{x^{2}+1}-\frac{C}{3x+1}\right)dx$**
Desarrollo de la integral indefinida:
$\int\frac{x}{x^{2}+1}dx = \frac{1}{2}\ln(x^{2}+1)$.
$\int\frac{C}{3x+1}dx = \frac{C}{3}\ln(3x+1)$.
Evaluación del límite de integración superior:
$\lim_{t\rightarrow\infty}\left[\frac{1}{2}\ln(t^{2}+1) - \frac{C}{3}\ln(3t+1) - (0 - 0)\right]$.
Aplicación de propiedades logarítmicas:
$\lim_{t\rightarrow\infty}\left[\ln((t^{2}+1)^{1/2}) - \ln((3t+1)^{C/3})\right] = \lim_{t\rightarrow\infty}\ln\left(\frac{(t^{2}+1)^{1/2}}{(3t+1)^{C/3}}\right)$.
Para que el logaritmo converja a un número real, el argumento debe tender a una constante positiva. Esto exige que los polinomios del numerador y denominador posean el mismo grado asintótico.
Grado asintótico del numerador: $(t^2)^{1/2} = t^1$.
Grado asintótico del denominador: $(t^1)^{C/3} = t^{C/3}$.
Igualación de grados: $1 = \frac{C}{3} \implies C = 3$.
Cálculo del valor numérico sustituyendo $C=3$:
$\lim_{t\rightarrow\infty}\ln\left(\frac{\sqrt{t^{2}+1}}{3t+1}\right) = \ln\left(\lim_{t\rightarrow\infty}\frac{\sqrt{1+1/t^2}}{3+1/t}\right) = \ln\left(\frac{1}{3}\right)$.
Convergencia garantizada solo para $C=3$, convergiendo a $\ln(1/3)$.

**4. $\int_{-\infty}^{1}\frac{e^{-\sqrt{1-x}}}{\sqrt{1-x}}dx$**
Se define el límite doble: $\lim_{a\rightarrow-\infty}\int_{a}^{0}\frac{e^{-\sqrt{1-x}}}{\sqrt{1-x}}dx + \lim_{b\rightarrow1^{-}}\int_{0}^{b}\frac{e^{-\sqrt{1-x}}}{\sqrt{1-x}}dx$.
Sustitución en integral indefinida: $u = -\sqrt{1-x} \implies du = \frac{1}{2\sqrt{1-x}}dx \implies 2du = \frac{1}{\sqrt{1-x}}dx$.
$\int e^u(2du) = 2e^u = 2e^{-\sqrt{1-x}}$.
Evaluación del límite inferior:
$\lim_{a\rightarrow-\infty}\left(2e^{-\sqrt{1-0}} - 2e^{-\sqrt{1-a}}\right) = 2e^{-1} - 2\lim_{a\rightarrow-\infty}e^{-\sqrt{1-a}} = 2e^{-1} - 2(0) = 2e^{-1}$.
Evaluación del límite superior:
$\lim_{b\rightarrow1^{-}}\left(2e^{-\sqrt{1-b}} - 2e^{-\sqrt{1-0}}\right) = 2e^0 - 2e^{-1} = 2 - 2e^{-1}$.
Suma de los fragmentos: $2e^{-1} + 2 - 2e^{-1} = 2$.
La integral converge exactamente a $2$.

---

## Sucesiones

**1. Convergencia y cálculo de límites:**

* **a) $a_{n}=\frac{(-1)^{n}+n}{(-1)^{n}-n}$**
  Extracción de factor común $n$: $\lim_{n\rightarrow\infty}\frac{n(\frac{(-1)^n}{n}+1)}{n(\frac{(-1)^n}{n}-1)} = \lim_{n\rightarrow\infty}\frac{\frac{(-1)^n}{n}+1}{\frac{(-1)^n}{n}-1}$.
  Teorema del sándwich para el término oscilante: $-\frac{1}{n} \le \frac{(-1)^n}{n} \le \frac{1}{n}$. Como $\lim \pm\frac{1}{n} = 0$, $\lim \frac{(-1)^n}{n} = 0$.
  Sustitución: $\frac{0+1}{0-1} = -1$. Converge a $-1$.

* **b) $a_{n}=\frac{n \sin(n)}{n^{2}+1}$**
  Acotamiento fundamental del seno: $|\sin(n)| \le 1$.
  Valor absoluto de la sucesión: $|a_n| = \left|\frac{n \sin(n)}{n^2+1}\right| \le \frac{n(1)}{n^2+1}$.
  Límite de la cota: $\lim_{n\rightarrow\infty}\frac{n}{n^2+1} = \lim_{n\rightarrow\infty}\frac{1/n}{1+1/n^2} = \frac{0}{1+0} = 0$.
  Dado que $0 \le |a_n| \le 0$ asintóticamente, $\lim_{n\rightarrow\infty}a_n = 0$. Converge a $0$.

* **c) $a_{n}=\frac{n!}{n^{n}}$**
  Desarrollo de los productos: $a_n = \frac{1 \cdot 2 \cdot 3 \cdots n}{n \cdot n \cdot n \cdots n} = \left(\frac{1}{n}\right)\left(\frac{2}{n}\right)\cdots\left(\frac{n}{n}\right)$.
  Cada factor $\frac{k}{n} \le 1$ para $1 \le k \le n$.
  Agrupación de la desigualdad: $0 \le a_n \le \left(\frac{1}{n}\right)(1)(1)\cdots(1) = \frac{1}{n}$.
  Límite de las cotas: $\lim_{n\rightarrow\infty}0 = 0$ y $\lim_{n\rightarrow\infty}\frac{1}{n} = 0$.
  Por Teorema del Sándwich, converge a $0$.

* **d) $a_{k}=\frac{3+5k^{2}}{k^{2}+k}$**
  División algebraica por $k^2$ (término de mayor grado del denominador):
  $\lim_{k\rightarrow\infty}\frac{\frac{3}{k^2}+\frac{5k^2}{k^2}}{\frac{k^2}{k^2}+\frac{k}{k^2}} = \lim_{k\rightarrow\infty}\frac{\frac{3}{k^2}+5}{1+\frac{1}{k}}$.
  Evaluación: $\frac{0+5}{1+0} = 5$. Converge a $5$.

* **e) $a_{k}=\frac{3^{k+2}}{5^{k}}$**
  Aplicación de propiedades de potencias: $a_k = \frac{3^k \cdot 3^2}{5^k} = 9\left(\frac{3}{5}\right)^k$.
  Sucesión geométrica con razón $r = 3/5$. Dado que $|r| < 1$, $\lim_{k\rightarrow\infty}r^k = 0$.
  Evaluación: $9(0) = 0$. Converge a $0$.

* **f) $a_{k}=\frac{e^{k}+e^{-k}}{e^{2k}-1}$**
  Factorización forzada extrayendo $e^{2k}$ (término dominante del denominador):
  $\lim_{k\rightarrow\infty}\frac{e^{2k}(e^{-k}+e^{-3k})}{e^{2k}(1-e^{-2k})} = \lim_{k\rightarrow\infty}\frac{e^{-k}+e^{-3k}}{1-e^{-2k}}$.
  Dado que $\lim_{k\rightarrow\infty}e^{-ck} = 0$ para $c>0$.
  Evaluación: $\frac{0+0}{1-0} = 0$. Converge a $0$.

* **g) $a_{n}=\frac{\ln(n+2)}{\ln(1+4n)}$**
  Transición a variable continua $x \in [1, \infty)$ para aplicar regla de L'Hôpital. Límite forma $\infty/\infty$.
  $\lim_{x\rightarrow\infty}\frac{\frac{d}{dx}\ln(x+2)}{\frac{d}{dx}\ln(1+4x)} = \lim_{x\rightarrow\infty}\frac{\frac{1}{x+2}}{\frac{4}{1+4x}} = \lim_{x\rightarrow\infty}\frac{1+4x}{4x+8}$.
  Segunda aplicación de L'Hôpital o división por $x$: $\lim_{x\rightarrow\infty}\frac{4}{4} = 1$. Converge a $1$.

* **h) $a_{n}=\frac{1+(-1)^{n}}{n^{2}}$**
  Acotamiento del oscilador: $-1 \le (-1)^n \le 1$. Sumando 1: $0 \le 1+(-1)^n \le 2$.
  División por término estrictamente positivo: $0 \le \frac{1+(-1)^n}{n^2} \le \frac{2}{n^2}$.
  Límites: $\lim_{n\rightarrow\infty}\frac{2}{n^2} = 0$. Por Sándwich, converge a $0$.

**2. Convergencia de $a_{k}=\frac{2k}{3k+1}$:**
Demostración directa por cálculo de límite. División por variable $k$:
$\lim_{k\rightarrow\infty}\frac{2k/k}{3k/k+1/k} = \lim_{k\rightarrow\infty}\frac{2}{3+1/k}$.
Sustitución del comportamiento asintótico $1/k \to 0$: $\frac{2}{3+0} = \frac{2}{3}$. Converge a $2/3$.

**3. Demostraciones por Inducción Matemática:**

* **a) $a_{n+1}=\sqrt{2a_{n}}$ con $a_{1}=1$**
  **Acotamiento ($P(n): a_n \le 2$):**
  * Caso base ($n=1$): $a_1 = 1 \le 2$. Se cumple.
  * HI: Asumir verdadero $a_k \le 2$.
  * Tesis: Demostrar $a_{k+1} \le 2$.
  * Demostración: Partiendo de HI $a_k \le 2$. Multiplicando por 2: $2a_k \le 4$. Aplicando raíz cuadrada (preserva monotonía): $\sqrt{2a_k} \le \sqrt{4} \implies a_{k+1} \le 2$.
  **Monotonía ($Q(n): a_n \le a_{n+1}$):**
  * Caso base ($n=1$): $a_1 = 1$. $a_2 = \sqrt{2(1)} = \sqrt{2} \approx 1.41$. $1 \le 1.41$. Se cumple.
  * HI: Asumir verdadero $a_k \le a_{k+1}$.
  * Tesis: Demostrar $a_{k+1} \le a_{k+2}$.
  * Demostración: Partiendo de HI $a_k \le a_{k+1}$. Multiplicando por 2: $2a_k \le 2a_{k+1}$. Aplicando raíz cuadrada: $\sqrt{2a_k} \le \sqrt{2a_{k+1}} \implies a_{k+1} \le a_{k+2}$. Sucesión monótona creciente.
  **Límite:** Por el Teorema de Convergencia Monótona, existe un límite finito $L$.
  Transición al límite en la recurrencia: $\lim a_{n+1} = \sqrt{2 \lim a_n} \implies L = \sqrt{2L}$.
  Resolución: $L^2 = 2L \implies L(L-2) = 0$. $L=0$ o $L=2$. Como $a_n$ crece desde $1$, $L \ne 0$. Converge a $2$.

* **b) $a_{n+1}=\frac{a_{n}+7}{2}$ con $a_{1}=5$**
  **Acotamiento ($P(n): a_n < 7$):**
  * Caso base: $a_1 = 5 < 7$. Se cumple.
  * HI: Asumir $a_k < 7$.
  * Demostración $P(k+1)$: Sumando 7 a HI: $a_k + 7 < 14$. Dividiendo por 2: $\frac{a_k+7}{2} < 7 \implies a_{k+1} < 7$.
  **Monotonía ($Q(n): a_n < a_{n+1}$):**
  * Planteamiento analítico de la diferencia: $a_{k+1} - a_k = \frac{a_k+7}{2} - a_k = \frac{a_k+7-2a_k}{2} = \frac{7-a_k}{2}$.
  * Utilizando el acotamiento demostrado, sabemos que $a_k < 7$, por lo tanto $7-a_k > 0$.
  * Consecuencia: $a_{k+1} - a_k > 0 \implies a_{k+1} > a_k$. Sucesión monótona creciente.
  **Límite:** Convergencia garantizada.
  Ecuación de límite: $L = \frac{L+7}{2} \implies 2L = L+7 \implies L = 7$. Converge a $7$.

* **c) $x_{n+1}=\frac{x_{n}^{2}+1}{x_{n}+2}$ con $x_{1}=\frac{1}{3}$**
  **Acotamiento ($P(n): x_n < \frac{1}{2}$):**
  * Caso base: $x_1 = 1/3 < 1/2$. Positividad es evidente al ser cociente de positivos.
  * HI: Asumir $0 < x_k < 1/2$.
  * Demostración $P(k+1)$: Se debe demostrar $\frac{x_k^2+1}{x_k+2} < \frac{1}{2}$. Como $x_k > 0$, el denominador es positivo. Multiplicando en cruz: $2(x_k^2+1) < x_k+2 \iff 2x_k^2+2 < x_k+2 \iff 2x_k^2 - x_k < 0 \iff x_k(2x_k - 1) < 0$.
  Dado que $x_k > 0$, la inecuación exige $2x_k - 1 < 0 \implies x_k < 1/2$. Esto es exactamente la HI. Los pasos son reversibles, confirmando $x_{k+1} < 1/2$.
  **Monotonía ($Q(n): x_n < x_{n+1}$):**
  * Diferencia algebraica: $x_{k+1} - x_k = \frac{x_k^2+1}{x_k+2} - x_k = \frac{x_k^2+1-x_k(x_k+2)}{x_k+2} = \frac{x_k^2+1-x_k^2-2x_k}{x_k+2} = \frac{1-2x_k}{x_k+2}$.
  * Análisis de signo: El denominador $x_k+2 > 0$. El numerador $1-2x_k > 0$ ya que demostramos $x_k < 1/2$. Por ende, la fracción es positiva y $x_{k+1} > x_k$. Creciente.
  **Límite:** Existe $L$.
  Ecuación: $L = \frac{L^2+1}{L+2} \implies L(L+2) = L^2+1 \implies L^2+2L = L^2+1 \implies 2L = 1 \implies L = 1/2$. Converge a $1/2$.

* **d) $a_{k+1}=3-\frac{1}{a_{k}}$ con $a_{1}=1$**
  **Acotamiento ($P(n): a_n \le 3$):**
  * Caso base: $a_1 = 1 \le 3$.
  * HI: Asumir $a_k \le 3$. (Se asume también positividad inicial por estructura, lo que es necesario para invertir la inecuación).
  * Demostración: Invirtiendo HI: $\frac{1}{a_k} \ge \frac{1}{3}$. Multiplicando por -1: $-\frac{1}{a_k} \le -\frac{1}{3}$. Sumando 3: $3 - \frac{1}{a_k} \le 3 - \frac{1}{3}$. Evaluando: $a_{k+1} \le 8/3 \le 3$. Se cumple.
  **Monotonía ($Q(n): a_n \le a_{n+1}$):**
  * Caso base: $a_2 = 3 - 1/1 = 2$. $1 \le 2$. Se cumple.
  * HI: Asumir $a_k \le a_{k+1}$.
  * Demostración: Invirtiendo: $\frac{1}{a_k} \ge \frac{1}{a_{k+1}}$. Multiplicando por -1: $-\frac{1}{a_k} \le -\frac{1}{a_{k+1}}$. Sumando 3: $3 - \frac{1}{a_k} \le 3 - \frac{1}{a_{k+1}} \implies a_{k+1} \le a_{k+2}$. Creciente.
  **Límite:** Existe $L$.
  Ecuación: $L = 3 - 1/L \implies L^2 = 3L - 1 \implies L^2 - 3L + 1 = 0$.
  Fórmula cuadrática: $L = \frac{3 \pm \sqrt{9 - 4(1)(1)}}{2} = \frac{3 \pm \sqrt{5}}{2}$.
  Dado que la sucesión es creciente y parte en $a_1=1$, y $\frac{3-\sqrt{5}}{2} \approx 0.38 < 1$, se descarta esta raíz. Converge a $\frac{3+\sqrt{5}}{2}$.

* **e) $a_{n+1}=\sqrt{2+a_n}$ con $a_1=\sqrt{2}$**
  **Acotamiento ($P(n): a_n < 2$):**
  * Caso base: $a_1 = \sqrt{2} \approx 1.41 < 2$.
  * HI: Asumir $a_k < 2$.
  * Demostración: Sumando 2: $2 + a_k < 4$. Aplicando raíz: $\sqrt{2+a_k} < \sqrt{4} \implies a_{k+1} < 2$.
  **Monotonía ($Q(n): a_n < a_{n+1}$):**
  * HI: Asumir $a_k < a_{k+1}$.
  * Demostración: Sumando 2: $2 + a_k < 2 + a_{k+1}$. Aplicando raíz: $\sqrt{2+a_k} < \sqrt{2+a_{k+1}} \implies a_{k+1} < a_{k+2}$. Creciente.
  **Límite:** Existe $L$.
  Ecuación: $L = \sqrt{2+L} \implies L^2 = 2+L \implies L^2 - L - 2 = 0 \implies (L-2)(L+1) = 0$.
  Como la sucesión es estrictamente positiva, $L=2$.

* **f) $y_{n+1}=\frac{3(1+y_n)}{3+y_n}$ con $y_1=3$**
  **Acotamiento ($P(n): y_n > \sqrt{3}$):**
  * Caso base: $y_1 = 3 > \sqrt{3} \approx 1.732$.
  * HI: Asumir $y_k > \sqrt{3}$.
  * Demostración: Se analiza la resta frente al límite: $y_{k+1} - \sqrt{3} = \frac{3+3y_k}{3+y_k} - \sqrt{3} = \frac{3+3y_k-3\sqrt{3}-\sqrt{3}y_k}{3+y_k} = \frac{3-3\sqrt{3}+y_k(3-\sqrt{3})}{3+y_k}$.
  Factorizando el numerador: $3(1-\sqrt{3}) + y_k\sqrt{3}(\sqrt{3}-1) = (1-\sqrt{3})(3-y_k\sqrt{3})$.
  Buscamos el signo. $1-\sqrt{3} < 0$. Para que la fracción sea positiva, necesitamos $3-y_k\sqrt{3} < 0 \implies 3 < y_k\sqrt{3} \implies \sqrt{3} < y_k$. Esta es la HI exacta.
  Por ende, el numerador es producto de negativos = positivo. $y_{k+1} > \sqrt{3}$.
  **Monotonía ($Q(n): y_{n+1} < y_n$):**
  * Diferencia: $y_{k+1} - y_k = \frac{3+3y_k}{3+y_k} - y_k = \frac{3+3y_k-3y_k-y_k^2}{3+y_k} = \frac{3-y_k^2}{3+y_k}$.
  * Análisis: Denominador positivo. Como $y_k > \sqrt{3} \implies y_k^2 > 3 \implies 3-y_k^2 < 0$.
  * Resultado: Fracción negativa. Sucesión decreciente.
  **Límite:** Existe $L$.
  Ecuación: $L = \frac{3+3L}{3+L} \implies 3L+L^2 = 3+3L \implies L^2 = 3 \implies L = \sqrt{3}$.

---

## Series Numéricas y Convergencia

**1. Estudio de convergencia:**

* **a) $\sum_{n=1}^{\infty}\frac{9n}{e^{-n}+n}$**
  Límite del término general $a_n$:
  $\lim_{n\rightarrow\infty}\frac{9n}{e^{-n}+n} = \lim_{n\rightarrow\infty}\frac{9n}{1/e^n + n}$.
  Dividiendo numerador y denominador por $n$:
  $\lim_{n\rightarrow\infty}\frac{9}{1/(ne^n) + 1}$.
  Como $\lim_{n\rightarrow\infty} ne^n = \infty$, el término $1/(ne^n) \to 0$.
  Límite: $\frac{9}{0+1} = 9$.
  Dado que $\lim a_n \ne 0$, la serie diverge por Criterio de Divergencia.

* **b) $\sum_{n=1}^{\infty}\frac{e^{1/n}}{3n^{2}}$**
  Aplicación de Criterio de la Integral. Función base $f(x) = \frac{e^{1/x}}{3x^2}$.
  Es positiva en $[1,\infty)$. Es continua. Es decreciente ya que $x^2$ y $1/e^{1/x}$ crecen.
  Integral: $\lim_{t\to\infty}\int_{1}^{t}\frac{e^{1/x}}{3x^2}dx$.
  Sustitución: $u = 1/x \implies du = -1/x^2 dx$.
  $\int \frac{e^{1/x}}{3x^2}dx = -\frac{1}{3}\int e^u du = -\frac{1}{3}e^u = -\frac{1}{3}e^{1/x}$.
  Evaluación: $\lim_{t\to\infty}\left(-\frac{1}{3}e^{1/t} - \left(-\frac{1}{3}e^{1/1}\right)\right)$.
  Como $\lim_{t\to\infty} 1/t = 0 \implies \lim e^{1/t} = e^0 = 1$.
  Resultado: $-\frac{1}{3}(1) + \frac{e}{3} = \frac{e-1}{3}$.
  La integral converge, implicando convergencia de la serie.

* **c) $\sum_{n=1}^{\infty}\frac{2\sqrt{n}+\sin(n)}{3n^{2}-2n+1}$**
  Análisis asintótico. Numerador dominado por $n^{1/2}$. Denominador dominado por $n^2$.
  Serie de prueba $b_n = \frac{n^{1/2}}{n^2} = \frac{1}{n^{3/2}}$.
  Criterio de Comparación en el Límite:
  $\lim_{n\to\infty}\frac{a_n}{b_n} = \lim_{n\to\infty}\frac{\frac{2\sqrt{n}+\sin(n)}{3n^{2}-2n+1}}{\frac{1}{n^{3/2}}} = \lim_{n\to\infty}\frac{2n^{2}+n^{3/2}\sin(n)}{3n^{2}-2n+1}$.
  Dividiendo por $n^2$: $\lim_{n\to\infty}\frac{2+\frac{\sin(n)}{n^{1/2}}}{3-\frac{2}{n}+\frac{1}{n^2}} = \frac{2+0}{3-0+0} = \frac{2}{3}$.
  Límite finito positivo. Serie de prueba es $p$-serie con $p=3/2 > 1$, convergente. Serie evaluada converge.

* **d) $\sum_{n=1}^{\infty}\frac{n^{2}+n\cos(n)}{\sqrt{n^{8}-n+1}}$**
  Asintóticas. Numerador $O(n^2)$. Denominador $O(\sqrt{n^8}) = O(n^4)$.
  Serie de prueba $b_n = \frac{n^2}{n^4} = \frac{1}{n^2}$.
  Comparación en el límite:
  $\lim_{n\to\infty}\left(\frac{n^2+n\cos(n)}{\sqrt{n^8-n+1}} \cdot \frac{n^2}{1}\right) = \lim_{n\to\infty}\frac{n^4+n^3\cos(n)}{\sqrt{n^8-n+1}}$.
  Dividiendo por $n^4 = \sqrt{n^8}$:
  $\lim_{n\to\infty}\frac{1+\frac{\cos(n)}{n}}{\sqrt{1-\frac{1}{n^7}+\frac{1}{n^8}}} = \frac{1+0}{\sqrt{1-0+0}} = 1$.
  Límite finito positivo. $p$-serie con $p=2 > 1$ converge. Serie evaluada converge.

* **e) $\sum_{n=1}^{\infty}\frac{3+2\cos(n)}{n^{3}-2n^{2}+7}$**
  Acotamiento estricto. Numerador: $-1 \le \cos(n) \le 1 \implies 1 \le 3+2\cos(n) \le 5$.
  Denominador: Para $n$ suficientemente grande ($n \ge 3$), $n^3-2n^2+7 > 0$. Además, $n^3-2n^2+7 \ge n^3/2$.
  Construcción de desigualdad de dominancia: $0 \le a_n \le \frac{5}{n^3/2} = \frac{10}{n^3}$.
  La serie constante por $p$-serie $\sum \frac{10}{n^3}$ converge ($p=3$).
  Alternativa por Comparación en el Límite con $1/n^3$: el límite es $0$, que garantiza convergencia si la mayor converge. Ambas prueban convergencia.

**2. Convergencia y suma:**

* **a) $\sum_{n=1}^{\infty}\frac{2^{n}}{n^{2}}$**
  Límite del término general. Exponencial en numerador domina al polinomio en denominador.
  Por L'Hôpital sobre reales: $\lim_{x\to\infty}\frac{2^x}{x^2} = \lim_{x\to\infty}\frac{2^x\ln 2}{2x} = \lim_{x\to\infty}\frac{2^x(\ln 2)^2}{2} = \infty$.
  Diverge por Criterio de la Divergencia ($\lim a_n \ne 0$).

* **b) $\sum_{n=1}^{\infty}\frac{\sqrt{2n^{2}+4n+1}}{n^{3}+9}$**
  Término de prueba: $b_n = \frac{\sqrt{n^2}}{n^3} = \frac{1}{n^2}$.
  Comparación en el Límite: $\lim_{n\to\infty}\left(\frac{\sqrt{2n^2+4n+1}}{n^3+9} \cdot \frac{n^2}{1}\right) = \lim_{n\to\infty}\frac{\sqrt{2n^6+4n^5+n^4}}{n^3+9}$.
  Dividiendo por $n^3$: $\lim_{n\to\infty}\frac{\sqrt{2+4/n+1/n^2}}{1+9/n^3} = \sqrt{2}$.
  Límite positivo. Converge por comportamiento de $p=2$.

* **c) $\sum_{n=0}^{\infty}\frac{2^{n}\sin^{2}(5n)}{4^{n}+\cos^{2}(n)}$**
  Acotamiento. Numerador: $\sin^2(5n) \le 1 \implies 2^n\sin^2(5n) \le 2^n$.
  Denominador: $\cos^2(n) \ge 0 \implies 4^n+\cos^2(n) \ge 4^n$.
  Combinando: $\frac{2^n\sin^2(5n)}{4^n+\cos^2(n)} \le \frac{2^n}{4^n} = \left(\frac{1}{2}\right)^n$.
  La serie dominatriz es geométrica con $|r|=1/2 < 1$. Converge.

* **d) $\sum_{n=1}^{\infty}\frac{1+2^{n}}{3^{n}}$**
  Descomposición lineal: $\sum_{n=1}^{\infty}\left(\frac{1}{3^n} + \frac{2^n}{3^n}\right) = \sum_{n=1}^{\infty}\left(\frac{1}{3}\right)^n + \sum_{n=1}^{\infty}\left(\frac{2}{3}\right)^n$.
  Ambas son geométricas convergentes.
  Suma 1 ($r=1/3, a=1/3$): $S_1 = \frac{1/3}{1-1/3} = \frac{1/3}{2/3} = \frac{1}{2}$.
  Suma 2 ($r=2/3, a=2/3$): $S_2 = \frac{2/3}{1-2/3} = \frac{2/3}{1/3} = 2$.
  Suma Total: $\frac{1}{2} + 2 = \frac{5}{2}$.

* **e) $\sum_{n=1}^{\infty}\frac{e^{n}}{n^{2}}$**
  Límite asintótico. Exponencial supera polinomial.
  $\lim_{x\to\infty}\frac{e^x}{x^2} \xrightarrow{L'H} \lim_{x\to\infty}\frac{e^x}{2x} \xrightarrow{L'H} \lim_{x\to\infty}\frac{e^x}{2} = \infty$.
  Diverge.

* **f) $\sum_{n=2}^{\infty}\frac{2}{n^{2}-1}$**
  Factorización del denominador: $n^2-1 = (n-1)(n+1)$.
  Fracciones parciales: $\frac{2}{(n-1)(n+1)} = \frac{A}{n-1} + \frac{B}{n+1}$.
  $2 = A(n+1) + B(n-1) \implies A=1, B=-1$.
  Término general expresado: $a_n = \frac{1}{n-1} - \frac{1}{n+1}$.
  Expansión de sumas parciales $S_k = \sum_{n=2}^{k} a_n$:
  $S_k = \left(1 - \frac{1}{3}\right) + \left(\frac{1}{2} - \frac{1}{4}\right) + \left(\frac{1}{3} - \frac{1}{5}\right) + \dots + \left(\frac{1}{k-2} - \frac{1}{k}\right) + \left(\frac{1}{k-1} - \frac{1}{k+1}\right)$.
  Cancelación telescópica. Los únicos términos sin eliminar son $1$ y $1/2$ al principio, y $-1/k$ y $-1/(k+1)$ al final.
  Ecuación sumas parciales: $S_k = 1 + \frac{1}{2} - \frac{1}{k} - \frac{1}{k+1}$.
  Límite de la serie: $\lim_{k\to\infty} S_k = \frac{3}{2} - 0 - 0 = \frac{3}{2}$. Converge.

* **g) $\sum_{k=2}^{\infty}\frac{1}{k(\ln(k))^{2}}$**
  Criterio de Integral con $f(x) = \frac{1}{x(\ln x)^2}$, positiva y decreciente en $[2,\infty)$.
  Integral: $\lim_{b\to\infty}\int_{2}^{b}\frac{1}{x(\ln x)^2}dx$.
  Sustitución: $u=\ln x \implies du=\frac{1}{x}dx$.
  $\int u^{-2}du = -u^{-1} = -\frac{1}{\ln x}$.
  Evaluación: $\lim_{b\to\infty}\left(-\frac{1}{\ln b} - \left(-\frac{1}{\ln 2}\right)\right)$.
  $\ln b \to \infty \implies \frac{1}{\ln b} \to 0$. Límite final es $\frac{1}{\ln 2}$. Convergente.

* **h) $\sum_{k=1}^{\infty}\frac{9^{k}}{3+10^{k}}$**
  Acotamiento estricto. Denominador más grande genera fracción menor.
  $\frac{9^k}{3+10^k} < \frac{9^k}{10^k} = \left(\frac{9}{10}\right)^k$.
  Serie dominante es geométrica con $|r|=9/10 < 1$.
  Convergente por Criterio de Comparación Directa.

* **i) $\sum_{k=1}^{\infty}\frac{\sqrt[3]{k}}{\sqrt{k^{3}+4k+3}}$**
  Asintóticas. Numerador $k^{1/3}$. Denominador $\sqrt{k^3} = k^{3/2}$.
  Serie de prueba $b_k = \frac{k^{1/3}}{k^{3/2}} = k^{1/3 - 3/2} = k^{2/6 - 9/6} = k^{-7/6} = \frac{1}{k^{7/6}}$.
  Criterio del límite: $\lim_{k\to\infty}\left(\frac{\sqrt[3]{k}}{\sqrt{k^3+4k+3}} \cdot k^{7/6}\right) = \lim_{k\to\infty}\frac{k^{1/3+7/6}}{\sqrt{k^3+4k+3}} = \lim_{k\to\infty}\frac{k^{3/2}}{\sqrt{k^3+4k+3}} = 1$.
  $p$-serie con $p=7/6 > 1$ converge.

* **j) $\sum_{n=1}^{\infty}\frac{1+2^{n}}{3^{n-1}}$**
  Manipulación algebraica: $\sum_{n=1}^{\infty}\frac{1}{3^{n-1}} + \sum_{n=1}^{\infty}\frac{2^n}{3^{n-1}}$.
  Ajuste del exponente de la segunda: $2\sum_{n=1}^{\infty}\frac{2^{n-1}}{3^{n-1}} = 2\sum_{n=1}^{\infty}\left(\frac{2}{3}\right)^{n-1}$.
  Cambio de índice para usar forma estándar $k = n-1$: $\sum_{k=0}^{\infty}\left(\frac{1}{3}\right)^k + 2\sum_{k=0}^{\infty}\left(\frac{2}{3}\right)^k$.
  Suma 1 ($a=1, r=1/3$): $S_1 = \frac{1}{1-1/3} = \frac{3}{2}$.
  Suma 2 ($a=2, r=2/3$): $S_2 = \frac{2}{1-2/3} = \frac{2}{1/3} = 6$.
  Total: $\frac{3}{2} + 6 = \frac{15}{2}$.

* **k) $\sum_{n=1}^{\infty}\frac{8^{n}}{5+11^{n}}$**
  Acotamiento: $5+11^n > 11^n \implies \frac{8^n}{5+11^n} < \frac{8^n}{11^n} = \left(\frac{8}{11}\right)^n$.
  La serie dominante es geométrica con razón $r = 8/11$. Como $|r| < 1$, la serie dominante converge.
  Por Comparación Directa, la serie evaluada converge.