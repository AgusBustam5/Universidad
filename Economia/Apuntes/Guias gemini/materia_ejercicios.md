# GUÍA METODOLÓGICA: CÁLCULOS Y JUSTIFICACIONES (ICS1513)

## 📚 TEMA 1: Fundamentos y Frontera de Producción

### 1. Costo de Oportunidad (Modelos Lineales)
* **¿Qué calcula?** Cuántas unidades de un bien "Y" debes sacrificar para producir una unidad adicional del bien "X".
* **Fórmula Matemática:** $$CO_x = \frac{\text{Cantidad Máxima de Y}}{\text{Cantidad Máxima de X}}$$
  O expresado como la pendiente en valor absoluto: $| \frac{\Delta Y}{\Delta X} |$
* **Procedimiento Paso a Paso:**
  1. Identifica la dotación total de recursos (ej. 100 horas).
  2. Calcula cuánto es lo máximo que puedes producir del Bien X si dedicas el 100% de los recursos a él. Haz lo mismo para el Bien Y.
  3. Divide la cantidad máxima del bien que estás sacrificando entre la cantidad máxima del bien que quieres analizar.
* **Justificación Económica:** Se fundamenta en el **Principio de Escasez y Disyuntivas**. Como los recursos (tiempo, trabajo, capital) son limitados, la única forma de producir más de un bien en una economía eficiente (sobre la FPP) es detrayendo recursos de la otra industria. El costo real de una cosa no es el dinero, es aquello a lo que renuncias para obtenerla.

### 2. Ventaja Comparativa
* **¿Qué calcula?** Identifica qué país o empresa es relativamente más eficiente produciendo un bien.
* **Procedimiento Paso a Paso:**
  1. Calcula el Costo de Oportunidad del bien "X" para el País A y para el País B.
  2. Compara ambos valores numéricos.
  3. El país que tenga el **menor costo de oportunidad** numérico tiene la Ventaja Comparativa.
* **Justificación Económica:** Se basa en la **Teoría del Comercio**. Es matemáticamente imposible tener ventaja comparativa en ambos bienes. Al especializarse el agente que tiene el menor costo de oportunidad, la producción total del sistema (o mundo) aumenta, permitiendo que ambos actores consuman más allá de sus FPP individuales mediante el intercambio.

---

## 📈 TEMA 2: Funcionamiento de los Mercados

### 3. Equilibrio de Mercado
* **¿Qué calcula?** El precio ($P^*$) y cantidad ($Q^*$) exactos donde el mercado se vacía (no sobra ni falta nada).
* **Fórmula Matemática:** $Q_D(P) = Q_S(P)$
* **Procedimiento Paso a Paso:**
  1. Si te dan las funciones inversas (ej. $P = 100 - Q$), despéjalas para dejar la Cantidad ($Q$) en función del Precio ($P$).
  2. Iguala algebraicamente la ecuación de Demanda con la ecuación de Oferta.
  3. Despeja la variable $P$ para encontrar el precio de equilibrio ($P^*$).
  4. Reemplaza $P^*$ en cualquiera de las dos ecuaciones originales para hallar la cantidad de equilibrio ($Q^*$).
* **Justificación Económica:** Representa la "Mano Invisible" de Adam Smith. Si el precio fuera mayor a $P^*$, los productores ofrecerían más de lo que la gente quiere comprar (exceso de oferta o escasez), obligando a las empresas a bajar los precios para liquidar stock. Si fuera menor, la gente querría comprar más de lo disponible (exceso de demanda), empujando el precio al alza.

### 4. Elasticidad Precio de la Demanda (Fórmula Punto)
* **¿Qué calcula?** Qué tan sensible es la cantidad demandada ante un cambio infinitamente pequeño en el precio.
* **Fórmula Matemática:** $\epsilon = \frac{\partial Q_D}{\partial P} \cdot \frac{P}{Q}$
* **Procedimiento Paso a Paso:**
  1. Toma la función de demanda directa $Q_D = a - bP$.
  2. Deriva $Q_D$ con respecto al precio. En funciones lineales, esto es simplemente la pendiente $-b$.
  3. Multiplica esa derivada por la fracción del precio sobre la cantidad en el punto específico de equilibrio $(P^* / Q^*)$.
  4. Analiza el valor absoluto: Si $>1$ es elástica; si $<1$ es inelástica.
* **Justificación Económica:** Mide la capacidad de reacción del consumidor. Si un bien es inelástico, significa que el consumidor no tiene sustitutos cercanos, es una necesidad básica, o lo consume a corto plazo, por lo que una subida de precio no reducirá drásticamente su consumo (lo que permite a las empresas o al Estado recaudar más subiendo precios/impuestos).

---

## ⚖️ TEMA 3: Eficiencia y Políticas Públicas

### 5. Excedentes del Consumidor y Productor (Bienestar)
* **¿Qué calcula?** El "beneficio neto" medido en dinero que la sociedad gana por comerciar en el mercado libre.
* **Fórmula Matemática:** Área de un triángulo $= \frac{\text{Base} \cdot \text{Altura}}{2}$
* **Procedimiento Paso a Paso:**
  1. Encuentra los **interceptos** (donde $Q=0$). En la demanda, es el precio máximo dispuesto a pagar. En la oferta, es el precio mínimo o costo marginal de la primera unidad.
  2. La **Base** de ambos triángulos siempre es la cantidad de equilibrio ($Q^*$).
  3. La **Altura** del Excedente del Consumidor (EC) es la resta entre el Intercepto de la Demanda y el Precio de equilibrio ($P^*$).
  4. La **Altura** del Excedente del Productor (EP) es la resta entre el Precio de equilibrio ($P^*$) y el Intercepto de la Oferta.
* **Justificación Económica:** El Excedente del Consumidor refleja la diferencia entre la **disposición al pago** (valoración subjetiva del bien) y lo que realmente pagó. El Excedente del Productor refleja la diferencia entre el precio al que vendió y su **costo marginal de producción**. La suma de ambos maximiza la eficiencia económica de la sociedad.

### 6. Imposición de Impuestos Específicos ($t$)
* **¿Qué calcula?** Cómo un impuesto altera las cantidades transadas y separa el precio que se paga del que se recibe.
* **Ecuación Clave de la Cuña Fiscal:** $P_D - P_S = t$   (o $P_D = P_S + t$)
* **Procedimiento Paso a Paso:**
  1. Usa las funciones inversas (P en función de Q) para que sea más fácil: $P_D(Q)$ y $P_S(Q)$.
  2. Sustituye las funciones en la ecuación clave: $P_D(Q) = P_S(Q) + t$.
  3. Despeja la variable $Q$ para encontrar la nueva (y menor) cantidad transada con impuesto ($Q_t$).
  4. Reemplaza $Q_t$ en la ecuación original de Demanda para saber cuánto paga el consumidor, y en la de Oferta para saber cuánto recibe el productor limpio.
* **Justificación Económica:** Los impuestos alteran los incentivos. Al introducir una "cuña", los compradores ven el bien más caro y los vendedores reciben menos rentabilidad. Esto destruye transacciones que antes ocurrían libremente, generando una **Pérdida Irrecuperable de Bienestar (Deadweight Loss)**. Quien absorbe más el golpe (incidencia) es quien sea más inelástico (a quien le cueste más salirse del mercado).

### 7. Otorgamiento de Subsidios ($s$)
* **¿Qué calcula?** El efecto de una ayuda estatal que incentiva la sobreproducción/sobreconsumo.
* **Ecuación Clave de la Cuña:** $P_S - P_D = s$
* **Procedimiento Paso a Paso:**
  1. Análogo al impuesto, pero la ecuación cambia: ahora el productor recibe el precio que paga el consumidor *más* el subsidio del Estado.
  2. Reemplaza las ecuaciones inversas: $P_S(Q) = P_D(Q) + s$.
  3. Despeja $Q$ para encontrar la nueva cantidad ($Q_s$), que será mayor al equilibrio original.
* **Justificación Económica:** Aunque parece positivo, un subsidio en un mercado sin externalidades es ineficiente. Obliga al Estado a gastar fondos públicos para forzar transacciones donde el costo real de producir el bien (Costo Marginal) terminó siendo mayor que el valor que la sociedad le da a esa unidad adicional (Disposición al Pago), creando también pérdida de bienestar.

---

## 🌍 TEMA 4: Comercio Internacional

### 8. Apertura al Comercio (Exportación / Importación)
* **¿Qué calcula?** Cuánto comerciará un país si se conecta al Precio Mundial ($P_M$).
* **Fórmula Matemática:** Evaluar $Q_D$ y $Q_S$ imponiendo el precio exógeno $P_M$.
* **Procedimiento Paso a Paso:**
  1. Toma la ecuación original de Demanda ($Q_D$) y Oferta ($Q_S$) nacionales.
  2. Sustituye el precio $P$ en ambas ecuaciones directamente por el Precio Mundial ($P_M$).
  3. Calcula los nuevos volúmenes.
  4. Si $Q_D > Q_S$ (el país quiere consumir más de lo que produce), la diferencia son **Importaciones**.
  5. Si $Q_S > Q_D$ (los productores nacionales fabrican más de lo que la gente consume), la diferencia son **Exportaciones**.
* **Justificación Económica:** Los países son "tomadores de precios" en el mercado global. El comercio internacional permite a los consumidores acceder a bienes más baratos que el equilibrio local (importaciones) o permite a los productores acceder a mercados más rentables (exportaciones), aumentando siempre el Excedente Total (bienestar) del país.

### 9. Aranceles (Impuestos a la Importación)
* **¿Qué calcula?** Cómo una barrera proteccionista reduce el comercio y afecta el bienestar local.
* **Fórmulas Clave:** * $P_{interno} = P_M + \tau$
  * $\text{Recaudación} = \tau \times \text{Importaciones}$
* **Procedimiento Paso a Paso:**
  1. Identifica el Precio Mundial ($P_M$) y súmale el valor del arancel ($\tau$) para obtener el nuevo Precio Interno.
  2. Ingresa este Nuevo Precio Interno en las funciones locales de Demanda y Oferta.
  3. Las Importaciones con arancel serán la nueva diferencia entre la demanda local (que ahora es menor por el precio más alto) y la oferta local (que ahora es mayor por la protección).
* **Justificación Económica:** Los aranceles se imponen por presiones políticas para proteger a los productores nacionales (que ganan excedente), pero son económicamente ineficientes. Perjudican severamente a los consumidores y generan pérdida de bienestar por dos motivos: obligan al país a fabricar localmente unidades que a nivel mundial eran más baratas de hacer (ineficiencia productiva) y privan a los consumidores de comprar bienes que sí valoraban al precio mundial original (subconsumo).

### 🔠 GLOSARIO DE VARIABLES Y TÉRMINOS EN ECUACIONES

Para comprender a la perfección las fórmulas matemáticas del curso, aquí tienes la definición exacta de cada variable utilizada en los modelos:

**1. Variables de Mercado (Oferta y Demanda)**
* **$P$ (Precio):** El valor monetario de un bien en el mercado. Se grafica siempre en el eje vertical (Y).
* **$Q$ (Cantidad - *Quantity*):** El número de unidades de un bien. Se grafica siempre en el eje horizontal (X).
* **$Q_D$ (Cantidad Demandada):** Las unidades exactas que los consumidores están dispuestos a comprar a un precio determinado.
* **$Q_S$ (Cantidad Ofrecida - *Supply*):** Las unidades exactas que los productores están dispuestos a fabricar y vender a un precio determinado.
* **$P^*, Q^*$ (Punto de Equilibrio):** El asterisco denota la situación de "equilibrio de libre mercado", el momento exacto donde $Q_D = Q_S$.
* **$\alpha, c$ (Interceptos):** Son las constantes en las ecuaciones lineales (ej. $Q_D = \alpha - \beta P$). Representan los extremos del gráfico: la cantidad máxima demandada si el bien fuera gratis ($P=0$), o el precio mínimo/máximo de asfixia al despejar la ecuación.
* **$\beta, d$ (Pendientes / Sensibilidad):** Acompañan a la variable $P$. Indican en cuántas unidades cambia la cantidad de la demanda o de la oferta cuando el precio sube en un peso. 

**2. Variables de Elasticidad**
* **$\epsilon$ (Elasticidad):** Medida adimensional de sensibilidad.
* **$\epsilon_P$ (Elasticidad Precio de la Demanda/Oferta):** Mide el cambio porcentual en $Q$ ante un cambio porcentual en $P$.
* **$\epsilon_I$ (Elasticidad Ingreso):** Mide la respuesta de la demanda ante cambios en el ingreso promedio del consumidor ($I$).
* **$\frac{\partial Q}{\partial P}$ (Derivada parcial):** En la fórmula punto de la elasticidad, representa el cambio marginal de la cantidad respecto al precio (matemáticamente, es la pendiente de la curva de demanda/oferta directa).

**3. Variables de Intervención (Políticas de Gobierno)**
* **$t$ (Impuesto - *Tax*):** Un recargo monetario fijo por unidad impuesto por el Estado. Rompe el equilibrio al crear una "cuña" (diferencia) entre el precio de compra y el de venta.
* **$s$ (Subsidio):** Una ayuda monetaria del Estado por unidad transada. Funciona matemáticamente como un "impuesto negativo".
* **$P_D$ (Precio de la Demanda con intervención):** El precio final que saca de su bolsillo el consumidor cuando hay un impuesto o subsidio.
* **$P_S$ (Precio de la Oferta con intervención):** El precio neto que recibe y se guarda el productor tras pagar el impuesto o sumar el subsidio.
* **$EC$ (Excedente del Consumidor):** Área del gráfico que mide el beneficio neto de los compradores.
* **$EP$ (Excedente del Productor):** Área del gráfico que mide el beneficio neto de los vendedores.
* **$RF$ (Recaudación Fiscal):** Dinero que junta el Estado por un impuesto ($RF = t \cdot Q_t$).
* **$GF$ (Gasto Fiscal):** Dinero que gasta el Estado en un subsidio ($GF = s \cdot Q_s$).
* **$PIE / PBS$ (Pérdida Irrecuperable de Eficiencia / Pérdida de Bienestar Social):** El valor de las transacciones (medido en los triángulos de los excedentes) que se destruyen por culpa de una intervención que aleja al mercado de su equilibrio $Q^*$.

**4. Variables de Comercio Internacional**
* **$P_M$ o $P_W$ (Precio Mundial - *World Price*):** El precio al que se transa un bien en el mercado internacional. El país local, al ser pequeño, asume este precio de forma horizontal al abrirse al comercio.
* **$\tau$ (Arancel - *Tariff*):** Un impuesto que se cobra exclusivamente a las unidades importadas. Eleva el precio interno artificialmente a $P_M + \tau$ protegiendo a la oferta local pero dañando el bienestar general.