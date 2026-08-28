# Cómo se arma una skill (demo)

Esto es la posta de cómo se construyeron `django-modeling` y
`ui-color-patterns` en `.claude/skills/`. Sirve como demo para que los
desarrolladores armen las suyas (views/permisos, forms y validación, testing,
deploy — lo que les falte).

## 1. Anatomía de una skill

Una skill es una carpeta con un `SKILL.md` adentro:

```
.claude/skills/
  nombre-de-la-skill/
    SKILL.md
```

El `SKILL.md` tiene dos partes:

```markdown
---
name: nombre-de-la-skill
description: Una frase que dice CUÁNDO usarla y QUÉ hace. Esto es lo único
  que el agente lee siempre — tiene que alcanzar para decidir si aplica.
---

# Cuerpo de la skill

Acá va la guía en sí: pasos, preguntas que hay que hacerle al desarrollador,
checklists, ejemplos concretos del propio proyecto.
```

La `description` es la parte más importante del archivo entero: es lo que el
agente usa para decidir si esta skill aplica a lo que se está haciendo ahora.
Si es vaga ("ayuda con Django"), nunca se va a disparar en el momento
correcto. Si es específica ("usar cuando se va a crear o modificar
models.py"), se dispara justo cuando hace falta.

## 2. El proceso que se siguió acá (paso a paso)

1. **Se identificó el momento de riesgo**, no el tema en general. No es
   "ayudame con Django", es "el desarrollador está a punto de escribir
   `models.py` sin haber pensado el negocio" o "está a punto de elegir
   colores al voleo". Cuanto más puntual el disparador, mejor la skill.

2. **Se escribieron las preguntas ANTES que las respuestas.** El cuerpo de
   ambas skills arranca con una lista de preguntas al desarrollador, no con
   código de ejemplo. Eso es a propósito: la skill existe para frenar al
   agente, no para darle un atajo.

3. **Se buscó un ejemplo real en el propio repo** para discutir en vez de
   inventar uno genérico. `django-modeling` usa `arriendo/models.py` y la
   migración `0002_remove_arriendos_fecha_arriendo.py` como disparadores de
   conversación real. Esto es clave: un ejemplo de un proyecto que
   funciona de verdad enseña más que un `Foo`/`Bar` inventado.

4. **Se cerró con un checklist técnico**, recién al final. Primero el
   razonamiento de negocio/diseño, después las reglas técnicas concretas
   (`related_name`, `__str__`, contraste de colores, etc.). Si el checklist
   va primero, el desarrollador lo lee como una lista de sintaxis y se saltea el
   razonamiento.

## 3. Cómo armar la próxima (por ejemplo, `django-views`)

Seguí el mismo orden:

1. ¿Cuál es el momento exacto de riesgo? (ej: la vista empieza a acumular
   `if`s de lógica de negocio que deberían estar en el modelo)
2. ¿Qué preguntas hay que hacerle al desarrollador antes de dejarlo escribir esa
   vista?
3. ¿Hay un ejemplo real en `arriendo/views.py` para señalar (una vista que ya
   hace demasiado, o una que está bien separada)?
4. ¿Cuál es el checklist técnico final?

Escribí eso en `.claude/skills/django-views/SKILL.md` con el mismo formato de
frontmatter, y sumá la fila correspondiente en la tabla del router de
`AGENTS.md`.

> Tip: Claude Code trae una skill (`skill-creator`) que automatiza el
> armado del `SKILL.md` con el formato correcto — pero vale la pena hacer la
> primera a mano, como acá, para entender bien qué va en cada parte antes de
> delegarle el trámite a la IA.
