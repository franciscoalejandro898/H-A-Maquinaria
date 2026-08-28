---
name: ui-color-patterns
description: Guía al desarrollador para definir una paleta de colores y sistema de diseño coherente antes de maquetar templates, en vez de elegir clases de Bootstrap al azar. Usar cuando se van a crear o editar templates, estilos, o elegir colores/tipografía del proyecto.
---

# Paleta de colores y sistema de diseño

Se activa ANTES de escribir CSS o elegir clases de color en un template. El
objetivo es que la identidad visual sea una decisión, no un accidente de ir
probando clases de Bootstrap hasta que "se vea bien".

## Paso 1 — Preguntas antes de tocar un solo `<div>`

1. ¿A qué rubro pertenece el negocio del proyecto? (logística, salud, retail,
   gastronomía...)
2. ¿Qué tiene que transmitir la interfaz? (confianza y solidez → azules/grises
   oscuros; urgencia/acción → rojos/naranjas; cercanía → colores cálidos y
   redondeados)
3. ¿Ya tienen logo o colores de marca definidos por la cátedra o el "cliente"
   ficticio del TP? Si sí, la paleta sale de ahí, no se inventa.
4. ¿Cuántos colores necesitan realmente? Con 1 primario + 1 secundario + 2-3
   neutros (fondo, texto, borde) alcanza para casi cualquier CRUD académico.
   Si el desarrollador propone 6 colores "porque quedan lindos", frenar ahí.

## Paso 2 — Patrón general a aplicar (independiente del framework CSS)

Esto aplica sea que el grupo use Bootstrap, Tailwind o CSS plano — el
principio no depende del framework:

- La paleta tiene que salir de **un solo lugar** (variables CSS, el theme de
  Bootstrap, o el `tailwind.config` si usan Tailwind) y desde ahí propagarse a
  toda la app. Si encuentran un color hardcodeado tipo
  `style="color: #ff0000"` repetido en varios templates, es la señal de que
  no hay una fuente única de verdad todavía — hay que centralizarlo antes de
  seguir agregando pantallas.
- Preguntarle al desarrollador: si mañana el "cliente" del TP pide cambiar el
  color primario, ¿cuántos archivos tendrían que tocar? La respuesta correcta
  es "uno". Si la respuesta es "no sé, hay que buscar en todos los
  templates", ahí está el problema a corregir.
- Si quieren ver este principio aplicado en un proyecto real y ordenado (no
  como ejemplo de qué colores elegir, sino de cómo se centraliza la
  decisión), pueden mirar cómo `H-A-Maquinaria` resuelve el estilo de sus
  forms vía una sola configuración de tema en `core/settings.py` en vez de
  estilos sueltos por template — la paleta puntual de ESE repo no importa,
  la estructura sí.

## Paso 3 — Checklist antes de dar el estilo por terminado

- ¿La paleta está definida en un solo lugar (variables CSS, o las variables
  de Bootstrap si usan ese framework) y no repetida archivo por archivo?
- ¿El contraste entre texto y fondo cumple accesibilidad básica (AA de
  WCAG)? Un texto gris claro sobre blanco es el error más común.
- ¿Los mismos componentes (botones primarios, alertas, badges de estado) usan
  siempre el mismo color en toda la app, o cambia según quién escribió esa
  vista?
- ¿Pueden explicar, en una frase, por qué eligieron ese color primario para
  ESE negocio en particular? Si no pueden, todavía no está lista la decisión.
