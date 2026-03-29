# Hoja de Ejercicios: Cálculo II

## Integrales Impropias (Clases 1 - 3)
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

3. Determine para qué valor de $C$ la integral $\int_{0}^{\infty}(\frac{x}{x^{2}+1}-\frac{C}{3x+1})dx$ converge. Evalúe la integral para el valor de $C$ encontrado.

4. Determine si la integral $\int_{-\infty}^{1}\frac{e^{-\sqrt{1-x}}}{\sqrt{1-x}}dx$ es convergente o divergente. En caso de convergencia, calcule el valor numérico de la integral.

---

## Sucesiones (Clases 4 - 5)

1. Determine si las siguientes sucesiones convergen o divergen. Si convergen, encuentre el límite:
    * a) $a_{n}=\frac{(-1)^{n}+n}{(-1)^{n}-n}$
    * b) $a_{n}=\frac{n \sin(n)}{n^{2}+1}$
    * c) $a_{n}=\frac{n!}{n^{n}}$
    * d) $a_{k}=\frac{3+5k^{2}}{k^{2}+k}$
    * e) $a_{k}=\frac{3^{k+2}}{5^{k}}$
    * f) $a_{k}=\frac{e^{k}+e^{-k}}{e^{2k}-1}$
    * g) $a_{k}=\frac{(-3)^{k}}{k!}$
    * h) $a_{n}=\frac{\ln(n+2)}{\ln(1+4n)}$
    * i) $a_{n}=\frac{1+(-1)^{n}}{n^{2}}$

2. Considere la sucesión $a_{k}=\frac{2k}{3k+1}$. Demuestre que la sucesión $a_{k}$ es convergente.

3. Considere la sucesión definida por $a_{n+1}=\sqrt{2a_{n}}$ con $a_{1}=1$.
    * a) Demuestre que la sucesión es monótona creciente y que $a_{n}\le2$ para todo $n\in\mathbb{N}$.
    * b) Demuestre que la sucesión converge y determine el límite.

4. Considere la sucesión recursiva definida por $a_{1}=5$ y $a_{n+1}=\frac{a_{n}+7}{2}$.
    * a) Demuestre que $a_{n}<7$.
    * b) Demuestre que $a_{n}$ es creciente.
    * c) Demuestre que $a_{n}$ converge y calcule el límite.

5. Considere la sucesión dada por recurrencia $x_{n+1}=\frac{x_{n}^{2}+1}{x_{n}+2}$ con $x_{1}=\frac{1}{3}$.
    * a) Pruebe que para todo $n\in\mathbb{N}$ se cumple $0<x_{n}<\frac{1}{2}$ y $x_{n}<x_{n+1}$.
    * b) Demuestre que el límite existe y determínelo.

---

## Series Numéricas y Convergencia (Clases 6 - 9)

1. Estudie la convergencia de las siguientes series:
    * a) $\sum_{n=1}^{\infty}\frac{9n}{e^{-n}+n}$
    * b) $\sum_{n=1}^{\infty}n^{4}e^{-n^{2}}$
    * c) $\sum_{n=1}^{\infty}\frac{e^{1/n}}{3n^{2}}$
    * d) $\sum_{n=1}^{\infty}\frac{2\sqrt{n}+\sin(n)}{3n^{2}-2n+1}$
    * e) $\sum_{n=1}^{\infty}\frac{n^{2}+n\cos(n)}{\sqrt{n^{8}-n+1}}$
    * f) $\sum_{n=1}^{\infty}\frac{3+2\cos(n)}{n^{3}-2n^{2}+7}$
    * g) $\sum_{n=1}^{\infty}\frac{n^{3}-3n}{n!}$

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
    * j) $\sum_{k=1}^{\infty}(1+\frac{1}{k})^{2}e^{-k}$
    * k) $\sum_{n=1}^{\infty}\frac{1+2^{n}}{3^{n-1}}$
    * l) $\sum_{n=1}^{\infty}\frac{8^{n}}{5+11^{n}}$