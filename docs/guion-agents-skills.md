# Guion — Bloque: AGENTS.md + skills como patrón de trabajo con IA

Duración estimada: 15-18 min. No requiere mostrar ningún repo puntual — los
fragmentos a proyectar están embebidos en este guion, listos para pegar en
una slide o en un editor en blanco.

---

## 1. Gancho (2 min)

> "Cuando trabajan con un agente de IA, la pregunta no es 'qué le pido' —
> es 'qué reglas lee siempre, antes de que yo le pida nada'. Eso es un
> archivo que se volvió medio estándar: `AGENTS.md`. Lo lee el agente al
> arrancar, en cualquier proyecto donde esté."

> "La idea de hoy es mostrarles el patrón: un archivo de reglas generales,
> más 'skills' — guías puntuales que se cargan solo cuando hacen falta, no
> todas juntas."

---

## 2. La filosofía — que la IA no resuelva, que pregunte (4 min)

Proyectar este fragmento (texto plano, no hace falta abrir ningún archivo):

```markdown
## Filosofía

El objetivo NO es que el agente entregue un proyecto terminado. Es que el
desarrollador entienda cada decisión: qué modelos definió y por qué, qué
patrón de diseño usó y por qué, qué regla de negocio va en el modelo y
cuál en la vista.

Si el agente genera código sin que el desarrollador haya explicado el
razonamiento primero, falló — aunque el código funcione.
```

Preguntar a la sala (dejar que contesten):

- *"¿A alguno la IA le generó modelos, vistas o estilos sin preguntarles
  nada del negocio primero? ¿Qué pasó cuando tuvieron que explicar por qué
  esa tabla tenía esos campos?"*

Seguir con las reglas obligatorias — leer 2 o 3, no las seis:

```markdown
1. No generar modelos sin levantamiento previo: entidades, atributos,
   relaciones y el porqué de cada una.
2. No elegir paleta de colores ni sistema de diseño sin preguntar primero
   por el rubro, el público y la identidad de marca.
4. Migraciones con contexto: mostrar el diff generado y confirmar que se
   entiende cada cambio antes de aplicarlo.
```

Comentario puente:

> "Esto no es limitar a la IA porque sí. Es la misma disciplina que les van
> a pedir en un trabajo real: nadie te aprueba un PR con un modelo que no
> sabés explicar."

---

## 3. El contrato de resultado — 3 puntos, no negociables (3 min)

Proyectar:

```markdown
## Resultado esperado (sin importar el negocio)

1. Estructura ordenada: apps separadas por dominio, sin lógica de negocio
   en templates.
2. Archivo de dependencias fiel a lo que se usa de verdad — cada paquete
   listado se importa en algún lado o se saca. Se audita con un grep de
   imports contra el archivo de dependencias antes de entregar.
3. Modelos definidos por el desarrollador a partir de SU levantamiento de
   negocio, no adivinados por la IA.
```

> "El punto 2 no es un capricho: un `requirements.txt` con librerías que
> alguien probó y nunca usó es una de las causas más comunes de que un
> proyecto no se pueda levantar en una máquina que no sea la del autor
> original. Antes de entregar, comparen lo que está instalado contra lo que
> el código realmente importa."

---

## 4. Router de skills — por qué no es un solo archivo gigante (4 min)

> "¿Por qué no ponemos todo en un archivo enorme? Porque si el agente tiene
> que leer 500 líneas de reglas para escribir un modelo, la mitad no le
> sirve en ese momento. El router carga solo la guía que corresponde a lo
> que se está haciendo ahora."

Proyectar la tabla:

```markdown
| Contexto / lo que se está por hacer                     | Skill a cargar     |
|----------------------------------------------------------|---------------------|
| Definir entidades y `models.py` desde requisitos de negocio | `django-modeling`  |
| Elegir colores, tipografía o maquetar templates           | `ui-color-patterns` |
```

Proyectar el frontmatter de una skill como ejemplo de formato:

```markdown
---
name: django-modeling
description: Guía para definir modelos de Django a partir de los
  requisitos de negocio, antes de escribir código. Usar cuando se va a
  crear o modificar models.py o definir entidades/relaciones de un dominio.
---
```

> "Esta parte de arriba — `name` y `description` — es lo único que el
> agente lee siempre, para decidir si esta skill aplica ahora. El resto del
> archivo recién se carga si aplica."

Proyectar el patrón genérico de la skill de modelado (sin nombres de
negocio puntuales, a propósito):

```markdown
Cuando dos entidades principales (A y B) se relacionan a través de un
concepto que tiene sus propios datos (una fecha, un estado, un monto), ESE
concepto es una entidad intermedia con FK a A y FK a B — no una
ManyToManyField directa entre A y B.

Pregunta clave: ¿qué perderían si lo modelaran como M2M directo?
(Respuesta esperada: los atributos propios de esa relación.)
```

> "Fíjense que no hay ningún nombre de negocio puntual acá — a propósito.
> Esta skill la va a usar un grupo que arma un sistema de turnos y otro que
> arma un e-commerce. Si la hubiéramos escrito con un negocio específico
> adentro, solo serviría para copiar, no para pensar."

Repetir la misma idea, más rápido, con la skill de colores — proyectar solo
la pregunta clave:

```markdown
Si mañana el "cliente" del proyecto pide cambiar el color primario,
¿cuántos archivos tendrían que tocar? La respuesta correcta es uno.
```

---

## 5. Cierre + consigna (2-3 min)

> "Nosotros ya tenemos armadas dos skills de ejemplo: modelado de datos y
> colores, porque son las dos decisiones que más se copian sin pensar. La
> consigna para cada grupo es: sumen al menos una skill más — views y
> permisos, forms y validación, testing, deploy — siguiendo el mismo
> proceso: primero identifiquen el momento de riesgo, después las
> preguntas, después el patrón genérico, recién al final el checklist
> técnico."

Última línea, para cerrar el bloque:

> "La IA como herramienta significa que ustedes dirigen y ella ejecuta —
> pero para dirigir tienen que poder explicar cada decisión. Eso es lo que
> este archivo fuerza, y es lo que les va a pedir cualquier senior el día de
> mañana."

---

## Notas para quien da la charla

- Todos los fragmentos de este guion están pensados para proyectarse tal
  cual (slide o editor en blanco) — no hace falta abrir ningún repo ni
  mostrar código de un proyecto real.
- Si sobra tiempo, armar en vivo una tercera skill con la sala (por ejemplo
  `django-views`) siguiendo el proceso del punto 5, partiendo de una hoja
  en blanco — es más contundente que explicarlo en abstracto.
- Si falta tiempo, cortar el punto 3 y saltar directo del punto 2 al 4.
