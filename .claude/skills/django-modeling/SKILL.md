---
name: django-modeling
description: Guía al desarrollador para definir modelos de Django a partir de los requisitos de negocio, antes de escribir código. Usar cuando se va a crear o modificar models.py, agregar una app nueva, o definir entidades/relaciones de un dominio.
---

# Modelado de datos en Django

Esta skill se activa ANTES de escribir una sola línea de `models.py`. El
objetivo es que el desarrollador piense el dominio, no que copie una plantilla.

## Paso 1 — Levantar el negocio, no el código

Preguntarle al desarrollador (en ese orden, uno por vez, sin avanzar hasta tener
respuesta):

1. ¿Qué entidades del negocio real necesitan quedar registradas en la base de
   datos? (personas, objetos, eventos, documentos)
2. Para cada entidad: ¿qué datos son obligatorios y cuáles opcionales? ¿por
   qué esos y no otros?
3. ¿Cómo se relacionan entre sí? Para cada relación: ¿es de uno-a-muchos,
   muchos-a-muchos o uno-a-uno? ¿qué pasaría si eligieran la otra opción?
4. ¿Hay reglas de negocio que restringen los datos (fechas que no se pisan,
   stock que no puede ser negativo, un cliente que no puede tener dos
   contratos activos)? Esas reglas van a `clean()`/`save()` o a validadores,
   NO a la vista.

No generar el modelo hasta que el desarrollador haya contestado con sus propias
palabras. Si contesta con código en vez de explicación, repreguntar "¿por qué
esa relación y no otra?".

## Paso 2 — Patrón general a aplicar (independiente del negocio)

Esto NO es sobre copiar entidades de ningún proyecto puntual — cada grupo
modela un negocio distinto (turnos, delivery, arriendo, lo que sea). Lo que
se enseña es el PATRÓN, con nombres genéricos:

- Cuando dos entidades principales (A y B) se relacionan a través de un
  concepto que tiene sus propios datos (una fecha, un estado, un monto), ESE
  concepto es una entidad intermedia con FK a A y FK a B — no una
  `ManyToManyField` directa entre A y B. Preguntarle al desarrollador: ¿qué
  perderían si lo modelaran como M2M directo? (Respuesta esperada: perderían
  los atributos propios de esa relación — fechas, montos, estado — porque una
  M2M simple no tiene lugar para guardarlos.)
- Un modelo que cambia de campos entre una migración y la siguiente no es un
  error de diseño, es señal de que se iteró en base a lo que el negocio
  realmente necesitaba. Pedirle al desarrollador que revise el historial de sus
  propias migraciones (`app/migrations/000X_*.py`) y explique qué decisión
  cambió en cada una — no hace falta que sea perfecto de entrada, tiene que
  poder explicar por qué cambió.
- Si tienen dudas de cómo se ve esto aplicado en un proyecto real y ordenado
  (no como ejemplo de negocio, sino de organización), pueden mirar la
  estructura de `arriendo/models.py` en el repo `H-A-Maquinaria` como
  referencia de calidad — pero el nombre de sus entidades y la lógica de su
  negocio tienen que salir de SU levantamiento, del Paso 1.

## Paso 3 — Checklist técnico (recién acá se escribe código)

- `related_name` descriptivo en cada FK/M2M (no dejar el default genérico).
- `__str__` definido en cada modelo — sin esto, el admin y los `ver_*` templates
  son ilegibles.
- `Meta.ordering` si el listado tiene un orden natural (por fecha, por nombre).
- Validaciones de negocio en el modelo (`clean()`) o en un validador, no
  repetidas en cada vista.
- Recién ahora: `python manage.py makemigrations` y mostrarle el diff al
  desarrollador antes de aplicar `migrate` (ver regla 4 de `AGENTS.md`).
