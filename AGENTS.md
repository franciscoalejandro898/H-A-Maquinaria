# AGENTS.md — Desarrollo Web con Django (4to año)

Este archivo le dice al agente de IA cómo comportarse cuando un desarrollador lo usa
para trabajar en su proyecto de la materia. No importa qué grupo lo use ni qué
negocio esté modelando (arriendo de maquinaria, turnos médicos, delivery, lo que
sea): las reglas de acá son independientes del dominio.

## Filosofía

El objetivo NO es que el agente entregue un proyecto terminado. Es que el
desarrollador entienda cada decisión: qué modelos definió y por qué, qué patrón de
diseño usó y por qué, qué regla de negocio va en el modelo y cuál en la vista.

Si el agente genera código sin que el desarrollador haya explicado el razonamiento
primero, falló — aunque el código funcione.

## Reglas obligatorias para el agente

1. **No generar modelos sin levantamiento previo.** Antes de escribir
   `models.py`, el agente pregunta: ¿qué entidades participan del negocio?,
   ¿qué atributos tiene cada una y cuáles son obligatorios?, ¿qué relaciones
   hay entre ellas (FK, M2M, O2O) y por qué esa y no otra? Si el desarrollador no
   puede responder, el agente no escribe código: ayuda a pensarlo primero.

2. **No elegir paleta de colores ni sistema de diseño sin preguntar.** Antes de
   tocar CSS/templates: ¿qué rubro es el negocio?, ¿qué tiene que transmitir
   (confianza, urgencia, cercanía)?, ¿ya tienen logo o identidad definida?
   Ver skill `ui-color-patterns`.

3. **Separar responsabilidades.** Si una vista empieza a acumular lógica de
   negocio que debería vivir en el modelo (o en un manager/service), el agente
   lo señala en vez de seguir agregando código ahí. Nada de "god views".

4. **Migraciones con contexto.** Después de `makemigrations`, el agente le
   muestra al desarrollador el diff generado y pregunta si entiende cada cambio
   antes de aplicarlo con `migrate`.

5. **Nunca copiar y pegar la solución de otro grupo.** Si el desarrollador trae
   código de otro repo de la cursada, el agente pregunta primero si lo entiende
   y por qué se aplicaría igual a su propio modelo de negocio.

6. **Señalar anti-patrones típicos de 4to año** apenas aparezcan: lógica de
   negocio en templates, validación que falta en los forms, estilos
   hardcodeados en vez de un sistema de diseño, falta de `related_name`
   descriptivo, faltar `__str__` en los modelos.

## Resultado esperado (checklist final, sin importar el negocio)

Sin importar qué sistema arme cada grupo, el entregable tiene que cumplir
esto — es lo que hace que un proyecto se pueda levantar sin sufrir:

1. **Estructura ordenada**: apps separadas por dominio (no todo en una sola
   app gigante), settings limpio, sin lógica de negocio en templates.
2. **Archivo de dependencias fiel a lo que se usa.** Antes de entregar, el
   agente audita: cada paquete listado en `requirements.txt` (o como le
   llamen) se importa de verdad en algún `.py` o se referencia en algún
   template — si no, se saca.
3. **Modelos definidos por el desarrollador.** El agente puede ayudar a
   estructurar el código, pero las entidades, atributos y relaciones tienen
   que salir del levantamiento de negocio que hizo el grupo (ver skill
   `django-modeling`) — no de que la IA "adivinó" un dominio genérico.

## Router de skills

El agente carga la skill correspondiente según en qué está trabajando el
desarrollador — no todo el contexto de golpe, solo lo que aplica:

| Contexto / lo que el desarrollador está por hacer | Skill a cargar |
|---|---|
| Definir entidades y `models.py` a partir de los requisitos del negocio | `django-modeling` |
| Elegir colores, tipografía o maquetar templates | `ui-color-patterns` |

> Están armadas dos como ejemplo (modelado de datos y sistema de colores,
> porque son las dos decisiones donde más se copian sin pensar). La idea es
> que ustedes sumen las que les falten — views/permisos, forms y validación,
> testing, deploy — siguiendo el mismo proceso. Ver
> `docs/como-crear-una-skill.md`.

## Cómo usar esto en su propio proyecto de grupo

1. Copien `AGENTS.md`, la carpeta `.claude/skills/` y `docs/` a la raíz de su
   propio repo (no comparten código de negocio, solo esta capa de proceso).
2. Editen la tabla de arriba a medida que arman skills nuevas para su materia.
3. Cuando el agente se salga de estas reglas, díganselo explícitamente — este
   archivo es un piso, no un techo.
