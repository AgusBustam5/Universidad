# Solucionario Detallado: Cálculo II

## Integrales Impropias (Clases 1 - 3)

**1. Convergencia de integrales impropias:**

* **a) $\int_{2}^{\infty}\frac{x+\sin x}{x^{2}-x}dx$**
    Se sabe que $\sin x \ge -1$ , por lo que $x+\sin x \ge x-1$.
    Para $x \ge 2$, se tiene que $x^{2} > x$, lo que implica $x^{2}-x > 0$.
    Dividiendo ambas expresiones se obtiene: $\frac{x+\sin x}{x^{2}-x} \ge \frac{x-1}{x^{2}-x} = \frac{x-1}{x(x-1)} = \frac{1}{x}$.
    La integral $\int_{2}^{\infty}\frac{1}{x}dx$ diverge al ser una integral $p$ con $p=1$.
    Por el criterio de comparación, la integral original es divergente.

* **b) $\int_{1}^{3}\frac{x}{(x-3)^{3}}dx$**
    Aplicando la sustitución $u = x-3$, donde $du = dx$.
    La integral indefinida es: $\int\frac{u+3}{u^{3}}du = \int\left(\frac{3}{u^{3}}+\frac{1}{u^{2}}\right)du = -\frac{3}{2u^{2}} - \frac{1}{u}$.
    Volviendo a la variable original: $-\frac{3}{2(x-3)^{2}} - \frac{1}{x-3}$.
    Evaluando el límite en la asíntota vertical $x=3$: $\lim_{b\rightarrow3^{-}}\left(-\frac{3}{2(b-3)^{2}} - \frac{1}{b-3}\right) - \left(-\frac{3}{2(-2)^{2}} - \frac{1}{-2}\right) = -\infty$.
    La integral diverge.

* **c) $\int_{0}^{1}\frac{\ln(x)}{\sqrt{x}}dx$**
    Integración por partes: $u = \ln(x) \Rightarrow du = \frac{1}{x}dx$ y $dv = \frac{1}{\sqrt{x}}dx \Rightarrow v = 2\sqrt{x}$.
    Se establece el límite: $\lim_{t\rightarrow0^{+}}\left[2\ln(x)\sqrt{x}\Big|_{t}^{1} - \int_{t}^{1}\frac{2}{\sqrt{x}}dx\right] = \lim_{t\rightarrow0^{+}}\left(-2\ln(t)\sqrt{t} - 4 + 4\sqrt{t}\right)$.
    Evaluando por L'Hôpital: $-4 - 2\lim_{t\rightarrow0^{+}}\frac{1/t}{-\frac{1}{2}t^{-3/2}} = -4 + 4\lim_{t\rightarrow0^{+}}\sqrt{t} = -4$.
    La integral converge a $-4$.

* **d) $\int_{-\infty}^{\infty}\frac{6x^{3}}{(x^{4}+1)^{2}}dx$**
    Se separa la integral en $x=0$: $\int_{-\infty}^{0}\frac{6x^{3}}{(x^{4}+1)^{2}}dx + \int_{0}^{\infty}\frac{6x^{3}}{(x^{4}+1)^{2}}dx$.
    Con la sustitución $u = x^{4}+1$, se obtiene la antiderivada $-\frac{3}{2(x^{4}+1)}$.
    Límite inferior: $\lim_{t\rightarrow-\infty}\left(-\frac{3}{2(0^{4}+1)} + \frac{3}{2(t^{4}+1)}\right) = -\frac{3}{2}$.
    Límite superior: $\lim_{t\rightarrow\infty}\left(-\frac{3}{2(t^{4}+1)} + \frac{3}{2(0^{4}+1)}\right) = \frac{3}{2}$.
    La suma es $-\frac{3}{2} + \frac{3}{2} = 0$. La integral converge a $0$.

* **e) $\int_{3}^{\infty}\frac{1}{(x-2)^{3/2}}dx$**
    Se evalúa el límite: $\lim_{b\rightarrow\infty}\int_{3}^{b}(x-2)^{-3/2}dx$.
    La antiderivada es $-2(x-2)^{-1/2}$.
    Evaluando límites: $\lim_{b\rightarrow\infty}\left(\frac{-2}{\sqrt{b-2}} - \frac{-2}{\sqrt{1}}\right) = 0 + 2 = 2$.
    La integral converge a $2$.

* **f) $\int_{-\infty}^{0}5^{t}dt$**
    Se evalúa el límite: $\lim_{t\rightarrow-\infty}\int_{t}^{0}5^{x}dx$.
    La antiderivada es $\frac{5^{x}}{\ln 5}$.
    Evaluando límites: $\lim_{t\rightarrow-\infty}\left(\frac{5^{0}}{\ln 5} - \frac{5^{t}}{\ln 5}\right) = \frac{1}{\ln 5} - 0 = \frac{1}{\ln 5}$.
    La integral converge a $\frac{1}{\ln 5}$.

* **g) $\int_{0}^{9}\frac{1}{\sqrt[3]{x-1}}dx$**
    Existe discontinuidad infinita en $x=1$. Se separa en $\int_{0}^{1}(x-1)^{-1/3}dx + \int_{1}^{9}(x-1)^{-1/3}dx$.
    La antiderivada es $\frac{3}{2}(x-1)^{2/3}$.
    Primer tramo: $\lim_{t\rightarrow1^{-}}\left[\frac{3}{2}(x-1)^{2/3}\right]_{0}^{t} = 0 - \frac{3}{2}(-1)^{2/3} = -\frac{3}{2}$.
    Segundo tramo: $\lim_{t\rightarrow1^{+}}\left[\frac{3}{2}(x-1)^{2/3}\right]_{t}^{9} = \frac{3}{2}(8)^{2/3} - 0 = \frac{3}{2}(4) = 6$.
    La suma es $-\frac{3}{2} + 6 = \frac{9}{2}$. La integral converge.

* **h) $\int_{0}^{1}\frac{\sec^{2}(x)}{x\sqrt{x}}dx$**
    Para $x \in (0,1]$, se cumple que $\sec^{2}(x) \ge 1$.
    Se establece la desigualdad: $\frac{\sec^{2}(x)}{x^{3/2}} \ge \frac{1}{x^{3/2}}$.
    La integral $\int_{0}^{1}\frac{1}{x^{3/2}}dx$ es divergente al ser una integral $p$ con $p=3/2 \ge 1$.
    Por el criterio de comparación, la integral original diverge.

* **i) $\int_{0}^{\infty}\frac{\sqrt{x^{5}+3x^{3}+5x}}{x^{4}+x^{2}+1}dx$**
    Se separa la integral en $x=1$. La porción en $[0,1]$ no es impropia y converge.
    Para $x \ge 1$, se acota el numerador: $\sqrt{x^{5}+3x^{3}+5x} < \sqrt{x^{5}+3x^{5}+5x^{5}} = 3x^{5/2}$.
    Se acota la expresión completa: $\frac{3x^{5/2}}{x^{4}+x^{2}+1} < \frac{3x^{5/2}}{x^{4}} = \frac{3}{x^{3/2}}$.
    Como $\int_{1}^{\infty}\frac{1}{x^{3/2}}dx$ converge, la integral evaluada converge por comparación.

* **j) $\int_{1}^{\infty}\frac{\cos(1/t)}{\sqrt{t}}dt$**
    Para $t \ge 1$, se tiene $0 < \frac{1}{t} \le 1$.
    Dado que $\cos(x)$ es decreciente en $(0,1]$, $\cos(1/t) \ge \cos(1) > 0$.
    Se genera la cota inferior: $\frac{\cos(1/t)}{\sqrt{t}} \ge \frac{\cos(1)}{\sqrt{t}}$.
    La integral $\int_{1}^{\infty}\frac{\cos(1)}{\sqrt{t}}dt$ diverge por ser $p=1/2 \le 1$.
    Por el criterio de comparación, la integral evaluada diverge.

**2. Criterio de comparación:**

* **a) $\int_{0}^{\infty}\frac{x}{x^{3}+1}dx$**
    Se separa el análisis en $x=1$. En $[1,\infty)$, se acota el denominador: $x^{3}+1 > x^{3}$.
    Se genera la desigualdad: $\frac{x}{x^{3}+1} < \frac{x}{x^{3}} = \frac{1}{x^{2}}$.
    Dado que $\int_{1}^{\infty}\frac{1}{x^{2}}dx$ converge ($p=2 > 1$), la integral original converge.

* **b) $\int_{1}^{\infty}\frac{w^{2}+1}{w^{3}(\cos^{2}(w)+1)}dw$**
    Se acota el numerador: $w^{2}+1 > w^{2}$.
    Se establece: $\frac{w^{2}+1}{w^{3}(\cos^{2}(w)+1)} > \frac{1}{w(\cos^{2}(w)+1)}$.
    Se acota el denominador: $\cos^{2}(w) \le 1$, por lo tanto $\cos^{2}(w)+1 \le 2$.
    Resulta en: $\frac{1}{w(\cos^{2}(w)+1)} \ge \frac{1}{2w}$.
    La integral $\int_{1}^{\infty}\frac{1}{2w}dw$ diverge al ser $p=1$. La integral evaluada diverge.

**3. Valor de $C$:**
Se establece el límite superior: $\lim_{t\rightarrow\infty}\int_{0}^{t}\left(\frac{x}{x^{2}+1}-\frac{C}{3x+1}\right)dx$.
Integrando: $\lim_{t\rightarrow\infty}\left[\frac{1}{2}\ln(x^{2}+1) - \frac{C}{3}\ln(3x+1)\right]_{0}^{t}$.
Agrupando el logaritmo: $\lim_{t\rightarrow\infty}\ln\left(\frac{(t^{2}+1)^{1/2}}{(3t+1)^{C/3}}\right)$.
El límite del argumento debe ser finito y no nulo. Los grados del numerador y denominador deben ser iguales. Grado numerador es $1$, grado denominador es $C/3$.
Se iguala $1 = C/3 \Rightarrow C=3$.
Evaluando el límite del argumento con $C=3$: $\lim_{t\rightarrow\infty}\frac{t}{3t} = \frac{1}{3}$. El valor de la integral es $\ln(1/3)$.

**4. $\int_{-\infty}^{1}\frac{e^{-\sqrt{1-x}}}{\sqrt{1-x}}dx$**
Se separa la integral: $\lim_{t\rightarrow-\infty}\int_{t}^{0}\frac{e^{-\sqrt{1-x}}}{\sqrt{1-x}}dx + \lim_{t\rightarrow1^{-}}\int_{0}^{t}\frac{e^{-\sqrt{1-x}}}{\sqrt{1-x}}dx$.
Cambio de variable: $u = -\sqrt{1-x} \Rightarrow du = \frac{1}{2\sqrt{1-x}}dx$.
Evaluación del primer límite: $\lim_{t\rightarrow-\infty}2\int_{-\sqrt{1-t}}^{-1}e^{u}du = \lim_{t\rightarrow-\infty}2(e^{-1}-e^{-\sqrt{1-t}}) = 2e^{-1}$.
Evaluación del segundo límite: $\lim_{t\rightarrow1^{-}}2\int_{-1}^{-\sqrt{1-t}}e^{u}du = \lim_{t\rightarrow1^{-}}2(e^{-\sqrt{1-t}}-e^{-1}) = 2(1-e^{-1})$.
La suma resulta en $2e^{-1} + 2 - 2e^{-1} = 2$. La integral converge a $2$.

---

## Sucesiones (Clases 4 - 5)

**1. Convergencia de sucesiones:**

* **a) $a_{n}=\frac{(-1)^{n}+n}{(-1)^{n}-n}$**
    Dividiendo el numerador y denominador por $n$: $\lim_{n\rightarrow\infty}\frac{\frac{(-1)^{n}}{n}+1}{\frac{(-1)^{n}}{n}-1}$.
    Puesto que $\lim_{n\rightarrow\infty}\frac{(-1)^{n}}{n} = 0$, se obtiene $\frac{1}{-1} = -1$. Convergente a $-1$.

* **b) $a_{n}=\frac{n \sin(n)}{n^{2}+1}$**
    Se utiliza el teorema del sándwich. $|\sin(n)| \le 1$.
    $0 \le |a_{n}| \le \frac{n}{n^{2}+1}$.
    $\lim_{n\rightarrow\infty}\frac{n}{n^{2}+1} = \lim_{n\rightarrow\infty}\frac{1/n}{1+1/n^{2}} = 0$. Convergente a $0$.

* **c) $a_{n}=\frac{n!}{n^{n}}$**
    Se desarrolla la expresión: $\frac{n!}{n^{n}} = \frac{1}{n} \cdot \frac{2}{n} \cdots \frac{n}{n}$.
    Todos los factores son $\le 1$, por tanto $0 \le a_{n} \le \frac{1}{n}$.
    $\lim_{n\rightarrow\infty}\frac{1}{n} = 0$. Por teorema del sándwich, converge a $0$.

* **d) $a_{k}=\frac{3+5k^{2}}{k^{2}+k}$**
    Dividiendo por la potencia mayor $k^{2}$: $\lim_{k\rightarrow\infty}\frac{3/k^{2}+5}{1+1/k} = \frac{0+5}{1+0} = 5$. Convergente a $5$.

* **e) $a_{k}=\frac{3^{k+2}}{5^{k}}$**
    Se reescribe la sucesión: $a_{k} = 3^{2} \cdot \frac{3^{k}}{5^{k}} = 9\left(\frac{3}{5}\right)^{k}$.
    Corresponde a una progresión geométrica de razón $3/5 < 1$. Convergente a $0$.

* **f) $a_{k}=\frac{e^{k}+e^{-k}}{e^{2k}-1}$**
    Multiplicando numerador y denominador por $e^{-2k}$: $\lim_{k\rightarrow\infty}\frac{e^{-k}+e^{-3k}}{1-e^{-2k}} = \frac{0+0}{1-0} = 0$. Convergente a $0$.

* **g) $a_{k}=\frac{(-3)^{k}}{k!}$**
    Se evalúa la serie $\sum\frac{(-3)^{k}}{k!}$. Su convergencia implica que $\lim_{k\rightarrow\infty}a_{k} = 0$.
    Alternativamente, el crecimiento factorial domina al exponencial. Convergente a $0$.

* **h) $a_{n}=\frac{\ln(n+2)}{\ln(1+4n)}$**
    Se define la función continua $f(x) = \frac{\ln(x+2)}{\ln(1+4x)}$.
    El límite es de la forma $\infty/\infty$. Aplicando L'Hôpital: $\lim_{x\rightarrow\infty}\frac{\frac{1}{x+2}}{\frac{4}{1+4x}} = \lim_{x\rightarrow\infty}\frac{1+4x}{4(x+2)} = 1$. Convergente a $1$.

* **i) $a_{n}=\frac{1+(-1)^{n}}{n^{2}}$**
    Se acota el numerador: $0 \le 1+(-1)^{n} \le 2$.
    Resulta en $0 \le a_{n} \le \frac{2}{n^{2}}$.
    Dado que $\lim_{n\rightarrow\infty}\frac{2}{n^{2}} = 0$, converge a $0$ por sándwich.

**2. $a_k = \frac{2k}{3k+1}$:**
Dividiendo por $k$: $\lim_{k\rightarrow\infty}\frac{2}{3+1/k} = \frac{2}{3}$. La sucesión converge.

**3. Sucesión $a_{n+1}=\sqrt{2a_{n}}$ con $a_{1}=1$:**
* **a)** Demostración por inducción para acotamiento: $a_{1}=1 \le 2$. Si $a_{k} \le 2$, entonces $2a_{k} \le 4$, por lo que $a_{k+1}=\sqrt{2a_{k}} \le \sqrt{4} = 2$.
    Demostración por inducción para monotonía: $1=a_{1} \le \sqrt{2}=a_{2}$. Si $a_{k} \le a_{k+1}$, entonces $2a_{k} \le 2a_{k+1}$, aplicando raíz $a_{k+1}=\sqrt{2a_{k}} \le \sqrt{2a_{k+1}}=a_{k+2}$. Es creciente.
* **b)** Toda sucesión monótona y acotada converge a un límite $L$.
    $L = \sqrt{2L} \Rightarrow L^{2} = 2L \Rightarrow L(L-2) = 0$.
    Como $a_{n} \ge 1$, el límite es $L=2$.

**4. Sucesión $a_{n+1}=\frac{a_{n}+7}{2}$ con $a_{1}=5$:**
* **a)** Inducción: $a_{1}=5 < 7$. Si $a_{k} < 7$, entonces $a_{k}+7 < 14$, dividiendo resulta $a_{k+1} = \frac{a_{k}+7}{2} < 7$.
* **b)** Monotonía: $a_{k+1} > a_{k} \iff \frac{a_{k}+7}{2} > a_{k} \iff a_{k}+7 > 2a_{k} \iff 7 > a_{k}$. Esto se cumple por (a), la sucesión es creciente.
* **c)** Al ser monótona y acotada, converge a $L$.
    $L = \frac{L+7}{2} \Rightarrow 2L = L+7 \Rightarrow L = 7$.

**5. Sucesión $x_{n+1}=\frac{x_{n}^{2}+1}{x_{n}+2}$ con $x_{1}=\frac{1}{3}$:**
* **a)** Inducción acotamiento: $x_{1} = 1/3 \in (0, 1/2)$. Si $x_{k} < 1/2$, se requiere demostrar $x_{k+1} < 1/2$. $\frac{x_{k}^{2}+1}{x_{k}+2} < \frac{1}{2} \iff 2x_{k}^{2}+2 < x_{k}+2 \iff 2x_{k}^{2} < x_{k} \iff x_{k} < 1/2$.
    Monotonía: $x_{k+1}-x_{k} = \frac{x_{k}^{2}+1-x_{k}^{2}-2x_{k}}{x_{k}+2} = \frac{1-2x_{k}}{x_{k}+2}$. Al ser $x_{k} < 1/2$, $1-2x_{k} > 0$. Creciente.
* **b)** Converge por monotonía y acotamiento. $L = \frac{L^{2}+1}{L+2} \Rightarrow L^{2}+2L = L^{2}+1 \Rightarrow 2L = 1 \Rightarrow L = \frac{1}{2}$.

---

## Series Numéricas y Convergencia (Clases 6 - 9)

**1. Estudio de convergencia:**

* **a) $\sum_{n=1}^{\infty}\frac{9n}{e^{-n}+n}$**
    Límite del término general: $\lim_{n\rightarrow\infty}\frac{9n}{\frac{1}{e^{n}}+n} = \lim_{n\rightarrow\infty}\frac{9}{-\frac{1}{ne^{n}}+1} = 9 \ne 0$. Diverge por criterio de divergencia.

* **b) $\sum_{n=1}^{\infty}n^{4}e^{-n^{2}}$**
    Criterio de la razón: $\lim_{n\rightarrow\infty}\left|\frac{(n+1)^{4}}{e^{(n+1)^{2}}} \cdot \frac{e^{n^{2}}}{n^{4}}\right| = \lim_{n\rightarrow\infty}\left(\frac{n+1}{n}\right)^{4} \cdot \frac{1}{e^{2n+1}} = 1 \cdot 0 = 0 < 1$. Converge absolutamente.

* **c) $\sum_{n=1}^{\infty}\frac{e^{1/n}}{3n^{2}}$**
    Se aplica el criterio de la integral. La función $f(x)=\frac{e^{1/x}}{3x^{2}}$ es continua, positiva y decreciente.
    $\int_{1}^{\infty}\frac{e^{1/x}}{3x^{2}}dx$. Sustitución $u=1/x \Rightarrow du=-1/x^{2}dx$. Antiderivada: $-\frac{1}{3}e^{1/x}$.
    $\lim_{t\rightarrow\infty}\left(-\frac{1}{3}e^{1/t} + \frac{1}{3}e\right) = \frac{e-1}{3}$. Converge.

* **d) $\sum_{n=1}^{\infty}\frac{2\sqrt{n}+\sin(n)}{3n^{2}-2n+1}$**
    Comparación límite con $b_{n} = \frac{1}{n^{3/2}}$.
    $\lim_{n\rightarrow\infty}\frac{a_{n}}{b_{n}} = \frac{2}{3}$.
    Al converger $\sum\frac{1}{n^{3/2}}$ (serie $p$ con $p=3/2 > 1$), la serie converge.

* **e) $\sum_{n=1}^{\infty}\frac{n^{2}+n\cos(n)}{\sqrt{n^{8}-n+1}}$**
    Acotamiento: $n^{2}-n \le n^{2}+n\cos(n) \le n^{2}+n$.
    Se compara en el límite con $b_{n} = \frac{1}{n^{2}}$.
    $\lim_{n\rightarrow\infty}\frac{n^{4}+n^{3}\cos(n)}{\sqrt{n^{8}-n+1}} = 1 > 0$. Converge.

* **f) $\sum_{n=1}^{\infty}\frac{3+2\cos(n)}{n^{3}-2n^{2}+7}$**
    Comparación al límite con $\sum\frac{1}{n^{2}}$.
    $\lim_{n\rightarrow\infty}\frac{\frac{3}{n}+\frac{2\cos(n)}{n}}{1-\frac{2}{n}+\frac{7}{n^{3}}} = \frac{0}{1} = 0$. Convergente.

* **g) $\sum_{n=1}^{\infty}\frac{n^{3}-3n}{n!}$**
    Criterio del cociente: $\lim_{n\rightarrow\infty}\frac{(n+1)^{3}-3(n+1)}{(n+1)!} \cdot \frac{n!}{n^{3}-3n}$.
    $\lim_{n\rightarrow\infty}\frac{(n+1)^{3}-3(n+1)}{(n+1)(n^{3}-3n)} = 0 < 1$. Convergente.

**2. Convergencia y suma:**

* **a) $\sum_{n=1}^{\infty}\frac{2^{n}}{n^{2}}$**
    Criterio de divergencia evaluando $f(x)=\frac{2^{x}}{x^{2}}$.
    L'Hôpital dos veces: $\lim_{x\rightarrow\infty}\frac{2^{x}\ln(2)}{2x} = \lim_{x\rightarrow\infty}\frac{2^{x}\ln^{2}(2)}{2} = \infty$. Divergente.

* **b) $\sum_{n=1}^{\infty}\frac{\sqrt{2n^{2}+4n+1}}{n^{3}+9}$**
    Comparación al límite con $b_{n}=\frac{\sqrt{2n^{2}}}{n^{3}} = \frac{\sqrt{2}}{n^{2}}$.
    $\lim_{n\rightarrow\infty}\frac{\sqrt{2n^{2}+4n+1}}{n^{3}+9} \cdot \frac{n^{2}}{\sqrt{2}} = 1$. Converge.

* **c) $\sum_{n=0}^{\infty}\frac{2^{n}\sin^{2}(5n)}{4^{n}+\cos^{2}(n)}$**
    Se establece que $4^{n}+\cos^{2}(n) > 4^{n}$.
    $\frac{2^{n}\sin^{2}(5n)}{4^{n}+\cos^{2}(n)} < \frac{2^{n}}{4^{n}} = \left(\frac{1}{2}\right)^{n}$. Convergente por comparación con serie geométrica $r=1/2$.

* **d) $\sum_{n=1}^{\infty}\frac{1+2^{n}}{3^{n}}$**
    Se divide en dos series geométricas: $\sum\left(\frac{1}{3}\right)^{n} + \sum\left(\frac{2}{3}\right)^{n}$.
    Suma de la primera ($r=1/3, a=1/3$): $\frac{1/3}{1-1/3} = \frac{1}{2}$.
    Suma de la segunda ($r=2/3, a=2/3$): $\frac{2/3}{1-2/3} = 2$.
    Suma total: $\frac{1}{2} + 2 = \frac{5}{2}$. Convergente.

* **e) $\sum_{n=1}^{\infty}\frac{e^{n}}{n^{2}}$**
    Límite del término general aplicando L'Hôpital: $\lim_{n\rightarrow\infty}\frac{e^{n}}{n^{2}} = \lim_{n\rightarrow\infty}\frac{e^{n}}{2n} = \lim_{n\rightarrow\infty}\frac{e^{n}}{2} = \infty \ne 0$. Divergente.

* **f) $\sum_{n=2}^{\infty}\frac{2}{n^{2}-1}$**
    Descomposición en fracciones parciales: $\frac{2}{(n-1)(n+1)} = \frac{1}{n-1} - \frac{1}{n+1}$.
    Desarrollo de la serie telescópica $S_{k}$: $\left(1 - \frac{1}{3}\right) + \left(\frac{1}{2} - \frac{1}{4}\right) + \left(\frac{1}{3} - \frac{1}{5}\right) + \dots + \left(\frac{1}{k-1} - \frac{1}{k+1}\right)$.
    Los términos se cancelan excepto: $1 + \frac{1}{2} - \frac{1}{k} - \frac{1}{k+1}$.
    Límite $\lim_{k\rightarrow\infty}S_{k} = \frac{3}{2}$. Convergente a $3/2$.

* **g) $\sum_{k=1}^{\infty}\frac{1}{k(\ln(k))^{2}}$**
    Criterio de la integral con $f(x) = \frac{1}{x(\ln(x))^{2}}$.
    Sustitución $u = \ln(x) \Rightarrow du = \frac{1}{x}dx$.
    $\lim_{b\rightarrow\infty}\int_{\ln 2}^{\ln b}\frac{1}{u^{2}}du = \lim_{b\rightarrow\infty}\left(-\frac{1}{u}\right) \Big|_{\ln 2}^{\ln b} = \frac{1}{\ln 2}$. Convergente.

* **h) $\sum_{k=1}^{\infty}\frac{9^{k}}{3+10^{k}}$**
    Se establece la cota $\frac{9^{k}}{3+10^{k}} < \frac{9^{k}}{10^{k}} = \left(\frac{9}{10}\right)^{k}$.
    Convergente por comparación directa con serie geométrica $r=9/10 < 1$.

* **i) $\sum_{k=1}^{\infty}\frac{\sqrt[3]{k}}{\sqrt{k^{3}+4k+3}}$**
    Comparación al límite con $b_{k} = \frac{k^{1/3}}{\sqrt{k^{3}}} = \frac{k^{1/3}}{k^{3/2}} = \frac{1}{k^{7/6}}$.
    $\lim_{k\rightarrow\infty}\frac{\sqrt[3]{k}}{\sqrt{k^{3}+4k+3}} \cdot k^{7/6} = \lim_{k\rightarrow\infty}\frac{k^{3/2}}{\sqrt{k^{3}+4k+3}} = 1$.
    Al converger $\sum\frac{1}{k^{7/6}}$ ($p=7/6 > 1$), la serie converge.

* **j) $\sum_{k=1}^{\infty}(1+\frac{1}{k})^{2}e^{-k}$**
    Criterio de la raíz: $\lim_{k\rightarrow\infty}\left(\left(1+\frac{1}{k}\right)^{2}e^{-k}\right)^{1/k} = \lim_{k\rightarrow\infty}\left(1+\frac{1}{k}\right)^{2/k}e^{-1}$.
    Se sabe que $\lim_{k\rightarrow\infty}\left(1+\frac{1}{k}\right)^{2/k} = 1^{0} = 1$.
    El límite es $1/e < 1$. Convergente.

* **k) $\sum_{n=1}^{\infty}\frac{1+2^{n}}{3^{n-1}}$**
    Separando la serie: $\sum_{n=1}^{\infty}\left(\frac{1}{3}\right)^{n-1} + \sum_{n=1}^{\infty}2\left(\frac{2}{3}\right)^{n-1}$.
    Ajustando el índice a $n=0$: $\sum_{n=0}^{\infty}\left(\frac{1}{3}\right)^{n} + \sum_{n=0}^{\infty}2\left(\frac{2}{3}\right)^{n}$.
    Cálculo de sumas geométricas: $\frac{1}{1-1/3} + \frac{2}{1-2/3} = \frac{3}{2} + 6 = \frac{15}{2}$. Convergente a $15/2$.

* **l) $\sum_{n=1}^{\infty}\frac{8^{n}}{5+11^{n}}$**
    Se tiene que $0 < \frac{8^{n}}{5+11^{n}} < \frac{8^{n}}{11^{n}} = \left(\frac{8}{11}\right)^{n}$.
    La serie geométrica de razón $8/11 < 1$ converge, por tanto, la serie evaluada converge por comparación directa.