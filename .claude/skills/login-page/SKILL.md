---
name: login-page
description: Restringe cualquier ajuste al login de H&A Maquinaria a SOLO cambios visuales (CSS, tipografía, colores, spacing, layout, copy) dentro de arriendo/templates/base/login.html, usando como referencia de diseño exacta el canvas "Login H&A" de Claude Design. Documenta también el resultado final ya implementado y aprobado (contenido completo del template + el fix de ruteo de auth que hizo falta para que se viera) para poder reproducirlo sin complicaciones si se revierte. Fuera de reproducir ESE fix puntual, la skill PROHÍBE tocar settings.py, urls.py, views.py o mover/renombrar archivos. Usar SIEMPRE que se pida mejorar, pulir, retocar, rediseñar o restaurar visualmente el login — antes de tocar una sola línea. path de navegador que ve user para login es (basepath/)accounts/login, y el fix de ruteo documentado en esta skill asegura que cualquier redirect de @login_required también aterrice en el mismo template visualmente retocado.Importante que el boton de el inicio debe redirigir al mismo login que se esta mejorando.
---

# Retoque visual del login (H&A Maquinaria) — SOLO VISUAL

Regla de una línea para cualquier agente que lea esto: **el login ya
funciona, no se toca la autenticación bajo ningún motivo salvo el fix de
ruteo puntual documentado en la sección siguiente — todo lo demás es CSS y
HTML decorativo de un único archivo.**

## Estado implementado ()

Esto es el resultado final ya construido, revisado en navegador (login
exitoso, login fallido, redirect de `@login_required`) y aprobado por el
desarrollador. Si se revierte cualquiera de estos 3 archivos, reaplicar
exactamente lo de acá reproduce el mismo resultado sin tener que rediseñar ni
volver a preguntar — son cambios ya autorizados, no nuevos.

### 1. `arriendo/templates/base/login.html` (reemplazo completo del archivo)

Standalone (no extiende `base/base.html`, porque el diseño es full-bleed sin
navbar/footer del sitio), con foto de fondo real
(`arriendo/static/img/fondodef.JPG`, asset que ya existía en el repo — no se
importó nada nuevo), form real de Django, y CSS propio Barlow/IBM Plex Mono:

```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Iniciar sesión · H&amp;A Maquinaria</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Barlow:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #101418;
            --panel: #151a20;
            --input-bg: #1c232b;
            --blue: #1e6fd9;
            --blue-hover: #1a5fbb;
            --orange: #f5a623;
            --link: #4d9bff;
            --link-hover: #8cc0ff;
            --border: rgba(255,255,255,.13);
        }

        * { box-sizing: border-box; }

        html, body {
            margin: 0;
            min-height: 100vh;
            background: var(--bg);
            color: #fff;
            font-family: 'Barlow', system-ui, sans-serif;
            -webkit-font-smoothing: antialiased;
        }

        a { color: var(--link); text-decoration: none; }
        a:hover { color: var(--link-hover); }
        input { font-family: inherit; }
        input:focus { outline: none; }
        input::placeholder { color: rgba(255,255,255,.28); }

        .login-grid {
            display: grid;
            grid-template-columns: 1.15fr .85fr;
            min-height: 100vh;
        }

        /* ---------- Panel hero ---------- */
        .hero {
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 40px 48px;
            border-left: 6px solid;
            border-image: linear-gradient(180deg, var(--blue), var(--orange)) 1;
        }

        .hero-bg {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: 68% 35%;
            filter: saturate(.85) contrast(1.05);
            z-index: 0;
        }

        .hero-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(160deg, rgba(11,26,45,.9), rgba(16,20,24,.72) 45%, rgba(16,20,24,.96));
            z-index: 1;
        }

        .hero-brand, .hero-body, .hero-footer {
            position: relative;
            z-index: 2;
        }

        .hero-brand {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .hero-logo {
            width: 46px;
            height: 46px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--blue);
            clip-path: polygon(0 0, 100% 0, 100% 76%, 76% 100%, 0 100%);
            font-family: 'Barlow Condensed', sans-serif;
            font-weight: 700;
            font-size: 17px;
            letter-spacing: .02em;
        }

        .hero-brand-text { display: flex; flex-direction: column; gap: 2px; }

        .hero-brand-name {
            font-family: 'Barlow Condensed', sans-serif;
            font-weight: 600;
            font-size: 15px;
            letter-spacing: .16em;
            text-transform: uppercase;
        }

        .hero-brand-sub {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 10px;
            letter-spacing: .14em;
            text-transform: uppercase;
            color: rgba(255,255,255,.45);
        }

        .hero-body {
            max-width: 520px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .hero-headline {
            font-family: 'Barlow Condensed', sans-serif;
            font-weight: 700;
            font-size: clamp(38px, 4vw, 58px);
            line-height: .95;
            text-transform: uppercase;
            letter-spacing: -.01em;
            margin: 0;
        }

        .hero-headline em {
            font-style: normal;
            color: var(--orange);
        }

        .hero-desc {
            font-size: 15px;
            line-height: 1.6;
            color: rgba(255,255,255,.68);
            max-width: 400px;
            margin: 0;
        }

        .hero-pills {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 2px;
        }

        .hero-pill {
            padding: 7px 13px;
            border: 1px solid rgba(255,255,255,.18);
            border-radius: 999px;
            background: rgba(255,255,255,.05);
            font-family: 'IBM Plex Mono', monospace;
            font-size: 11px;
            letter-spacing: .06em;
            text-transform: uppercase;
            color: rgba(255,255,255,.75);
        }

        .hero-stats {
            display: flex;
            gap: 34px;
            padding-top: 8px;
            border-top: 1px solid rgba(255,255,255,.14);
            margin-top: 6px;
        }

        .hero-stat { display: flex; flex-direction: column; gap: 2px; padding-top: 12px; }

        .hero-stat-value {
            font-family: 'Barlow Condensed', sans-serif;
            font-weight: 600;
            font-size: 24px;
        }

        .hero-stat-label {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 10.5px;
            letter-spacing: .1em;
            text-transform: uppercase;
            color: rgba(255,255,255,.45);
        }

        .hero-footer {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 11px;
            letter-spacing: .08em;
            color: rgba(255,255,255,.4);
        }

        /* ---------- Panel form ---------- */
        .form-panel {
            background: var(--panel);
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 48px 56px;
            border-left: 1px solid rgba(255,255,255,.07);
        }

        .form-wrap {
            width: 100%;
            max-width: 360px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 26px;
        }

        .form-head { display: flex; flex-direction: column; gap: 9px; }

        .eyebrow {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 10px;
            letter-spacing: .2em;
            text-transform: uppercase;
            color: var(--orange);
            margin: 0;
        }

        .form-title {
            font-family: 'Barlow Condensed', sans-serif;
            font-weight: 700;
            font-size: 34px;
            line-height: 1;
            text-transform: uppercase;
            letter-spacing: .01em;
            margin: 0;
        }

        .form-subtitle {
            font-size: 13.5px;
            line-height: 1.55;
            color: rgba(255,255,255,.5);
            margin: 0;
        }

        .error-banner {
            display: flex;
            gap: 10px;
            align-items: center;
            padding: 11px 14px;
            background: rgba(245,166,35,.1);
            border-left: 3px solid var(--orange);
            font-size: 12.5px;
            line-height: 1.45;
            color: #f7c67a;
        }

        .error-banner p { margin: 0; }
        .error-banner p + p { margin-top: 4px; }

        .login-fields { display: flex; flex-direction: column; gap: 16px; }

        .field { display: flex; flex-direction: column; gap: 7px; }

        .field-label-row {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
        }

        .field label {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 10px;
            letter-spacing: .14em;
            text-transform: uppercase;
            color: rgba(255,255,255,.45);
        }

        .field-link { font-size: 11.5px; color: var(--link); }
        .field-link:hover { color: var(--link-hover); }

        .field-row { position: relative; }

        input[name="username"],
        input[name="password"] {
            width: 100%;
            height: 48px;
            background: var(--input-bg);
            border: 1px solid var(--border);
            border-radius: 3px;
            color: #fff;
            font-size: 14.5px;
            padding: 0 15px;
            transition: border-color .16s, box-shadow .16s;
        }

        input[name="password"] { padding-right: 74px; }

        input[name="username"]:focus,
        input[name="password"]:focus {
            border-color: var(--blue);
            box-shadow: 0 0 0 3px rgba(30,111,217,.22);
        }

        .field-error { margin: 0; font-size: 12px; color: var(--orange); }

        .password-toggle {
            position: absolute;
            right: 7px;
            top: 8px;
            height: 32px;
            padding: 0 11px;
            border: none;
            border-radius: 2px;
            background: rgba(255,255,255,.08);
            font-family: 'IBM Plex Mono', monospace;
            font-size: 10px;
            letter-spacing: .08em;
            text-transform: uppercase;
            color: rgba(255,255,255,.65);
            cursor: pointer;
        }

        .password-toggle:hover { background: rgba(255,255,255,.16); }

        .remember-row {
            display: flex;
            align-items: center;
            gap: 9px;
            cursor: pointer;
            user-select: none;
            margin-top: 2px;
        }

        .remember-row input[type="checkbox"] {
            width: 15px;
            height: 15px;
            accent-color: var(--blue);
            cursor: pointer;
            margin: 0;
        }

        .remember-row span { font-size: 13px; color: rgba(255,255,255,.6); }

        .btn-submit {
            height: 50px;
            margin-top: 6px;
            width: 100%;
            border: none;
            border-radius: 3px;
            background: var(--blue);
            color: #fff;
            font-family: 'Barlow Condensed', sans-serif;
            font-weight: 600;
            font-size: 13px;
            letter-spacing: .18em;
            text-transform: uppercase;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            transition: background .16s, transform .12s;
        }

        .btn-submit:hover { background: var(--blue-hover); }
        .btn-submit:active { transform: translateY(1px); }
        .btn-submit:disabled { opacity: .8; cursor: default; }

        .btn-spinner {
            width: 13px;
            height: 13px;
            border: 2px solid rgba(255,255,255,.35);
            border-top-color: #fff;
            border-radius: 50%;
            display: none;
            animation: spin .7s linear infinite;
        }

        .btn-submit.is-loading .btn-spinner { display: inline-block; }

        @keyframes spin { to { transform: rotate(360deg); } }

        .back-link {
            text-align: center;
            font-size: 12.5px;
            color: rgba(255,255,255,.45);
            margin-top: 2px;
        }

        .back-link:hover { color: #fff; }

        .form-footer {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,.08);
        }

        .form-footer-text {
            font-size: 11.5px;
            line-height: 1.5;
            color: rgba(255,255,255,.35);
        }

        .icon-btns { display: flex; gap: 8px; }

        .icon-btn {
            width: 34px;
            height: 34px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid rgba(255,255,255,.13);
            border-radius: 3px;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 10px;
            color: rgba(255,255,255,.6);
        }

        .icon-btn:hover { border-color: var(--blue); color: #fff; }

        @media (max-width: 900px) {
            .login-grid { grid-template-columns: 1fr; }
            .hero { display: none; }
            .form-panel { padding: 32px 20px; border-left: none; }
        }
    </style>
</head>
<body>
<div class="login-grid">

    <section class="hero">
        <img class="hero-bg" src="{% static 'img/fondodef.JPG' %}" alt="">
        <div class="hero-overlay"></div>

        <div class="hero-brand">
            <div class="hero-logo">H&amp;A</div>
            <div class="hero-brand-text">
                <div class="hero-brand-name">Maquinarias y Equipos</div>
                <div class="hero-brand-sub">Arriendo de maquinaria para construcción</div>
            </div>
        </div>

        <div class="hero-body">
            <h1 class="hero-headline">Arriendo de<br>maquinaria pesada<br><em>para construcción.</em></h1>
            <p class="hero-desc">Camiones, equipos de compactación y maquinaria pesada: disponibilidad, contratos y mantenciones en un solo panel operativo.</p>

            <div class="hero-pills">
                <span class="hero-pill">Camiones</span>
                <span class="hero-pill">Compactación</span>
                <span class="hero-pill">Elevación</span>
            </div>

            <div class="hero-stats">
                <div class="hero-stat">
                    <div class="hero-stat-value">24/7</div>
                    <div class="hero-stat-label">Soporte en obra</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-value">+120</div>
                    <div class="hero-stat-label">Equipos disponibles</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-value">100%</div>
                    <div class="hero-stat-label">Certificados</div>
                </div>
            </div>
        </div>

        <div class="hero-footer">Francisco Donaire · © Todos los derechos reservados</div>
    </section>

    <section class="form-panel">
        <div class="form-wrap">

            <div class="form-head">
                <p class="eyebrow">Acceso al sistema</p>
                <h2 class="form-title">Inicio de sesión</h2>
                <p class="form-subtitle">Usa las credenciales entregadas por administración.</p>
            </div>

            {% if form.non_field_errors %}
            <div class="error-banner">
                {% for error in form.non_field_errors %}
                <p>{{ error }}</p>
                {% endfor %}
            </div>
            {% endif %}

            <form action="" method="post" id="login-form" class="login-fields">
                {% csrf_token %}

                <div class="field">
                    <label for="{{ form.username.id_for_label }}">Nombre de usuario</label>
                    <div class="field-row">{{ form.username }}</div>
                    {% for error in form.username.errors %}
                    <p class="field-error">{{ error }}</p>
                    {% endfor %}
                </div>

                <div class="field">
                    <div class="field-label-row">
                        <label for="{{ form.password.id_for_label }}">Contraseña</label>
                        <a href="#" class="field-link">Recuperar</a>
                    </div>
                    <div class="field-row">
                        {{ form.password }}
                        <button type="button" class="password-toggle" id="toggle-password">Ver</button>
                    </div>
                    {% for error in form.password.errors %}
                    <p class="field-error">{{ error }}</p>
                    {% endfor %}
                </div>

                <label class="remember-row">
                    <input type="checkbox" checked>
                    <span>Mantener sesión iniciada</span>
                </label>

                <button type="submit" class="btn-submit" id="submit-btn">
                    <span class="btn-spinner"></span>
                    <span class="btn-label">Iniciar sesión</span>
                </button>
            </form>

            <a href="{% url 'home' %}" class="back-link">← Regresar a inicio</a>

            <div class="form-footer">
                <div class="form-footer-text">¿Sin acceso?<br>Contacta a administración.</div>
                <div class="icon-btns">
                    <a href="https://github.com/tuusuario" class="icon-btn">GH</a>
                    <a href="https://www.instagram.com/tuusuario/" class="icon-btn">IG</a>
                </div>
            </div>

        </div>
    </section>

</div>

<script>
    (function () {
        var usernameInput = document.querySelector('input[name="username"]');
        if (usernameInput && !usernameInput.placeholder) usernameInput.placeholder = 'f.donaire';

        var passwordInput = document.querySelector('input[name="password"]');
        if (passwordInput && !passwordInput.placeholder) passwordInput.placeholder = '••••••••';

        var toggleBtn = document.getElementById('toggle-password');
        if (toggleBtn && passwordInput) {
            toggleBtn.addEventListener('click', function () {
                var isHidden = passwordInput.type === 'password';
                passwordInput.type = isHidden ? 'text' : 'password';
                toggleBtn.textContent = isHidden ? 'Ocultar' : 'Ver';
            });
        }

        var form = document.getElementById('login-form');
        var submitBtn = document.getElementById('submit-btn');
        if (form && submitBtn) {
            form.addEventListener('submit', function () {
                submitBtn.classList.add('is-loading');
                submitBtn.disabled = true;
            });
        }
    })();
</script>
</body>
</html>
```

### 2. El fix de ruteo (por qué hizo falta y qué se tocó)

El paso 1 solo no alcanzaba: el login se veía bien en `/login/`, pero
cualquier redirect de `@login_required`, o entrar a mano a
`/accounts/login/`, aterrizaba en un template viejo sin estilos. Causa:
`core/urls.py` registraba el login DOS veces — una vez en `arriendo.urls`
(`/login/`, con nuestro `template_name='base/login.html'`) y otra vez vía
`include('django.contrib.auth.urls')` en `/accounts/login/` (sin
`template_name`, así que caía al `registration/login.html` viejo). Como
`LOGIN_URL` no estaba definido en `settings.py`, Django usaba su default
(`/accounts/login/`) para cualquier redirect de auth — por eso el diseño
nuevo no se veía salvo que entraras a `/login/` directo.

Esto **sí implicó tocar `.py`**, fuera del alcance normal de "solo visual"
de esta skill — se hizo con confirmación explícita del desarrollador
(pregunta directa antes de tocar el archivo). Reaplicar exactamente este
mismo cambio si se revierte NO requiere volver a preguntar, porque es el
mismo fix ya aprobado, no uno nuevo:

**`core/urls.py`** — sacar la línea del include de `accounts/`:

```diff
 urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('arriendo.urls')),
-    path('accounts/', include('django.contrib.auth.urls')),
 ]
```

**`core/settings.py`** — agregar `LOGIN_URL` (queda junto a los otros
settings de auth, cerca de la línea 140):

```diff
+LOGIN_URL = "login"
 LOGIN_REDIRECT_URL = "/"
 LOGOUT_REDIRECT_URL = "/"
```

No se tocó `arriendo/urls.py` (ya estaba bien: define `login`/`logout`
apuntando a `base/login.html`) ni ningún `views.py`.

### 3. Lo que NO se tocó (y no hace falta tocar para reproducir esto)

- `arriendo/static/img/fondodef.JPG` — ya existía en el repo (se usaba en
  `base.html`). No se subió ni se generó ningún asset nuevo.
- `arriendo/templates/registration/login.html` y `login2.html` — siguen
  existiendo como código muerto (nadie los renderiza tras el fix de
  ruteo). Se dejaron así a propósito, no hace falta borrarlos para que el
  resultado de arriba funcione.
- `arriendo/urls.py` — sin cambios.

## Especificación de diseño de referencia (Claude Design: "Login H&A")

Resumen rápido de las decisiones detrás del HTML de arriba — sale del canvas
`Login H&A.dc.html` del proyecto de diseño (paleta, tipografía y layout; la
foto de fondo del mockup se reemplazó por el asset que ya existía en el
proyecto, `fondodef.JPG`, no por el del canvas de diseño).

**Paleta:** fondo base `#101418` · panel del form `#151a20` · fondo de
inputs `#1c232b` · azul primario `#1e6fd9` (hover `#1a5fbb`) · naranja de
acento `#f5a623` · link `#4d9bff` (hover `#8cc0ff`) · banner de error fondo
`rgba(245,166,35,.1)` con borde `#f5a623` y texto `#f7c67a`.

**Tipografía:** `Barlow Condensed` 500/600/700 para títulos/botones/labels
en mayúscula; `Barlow` 400/500/600 para copy; `IBM Plex Mono` 400/500 para
labels de campo, tags y stats con `letter-spacing` amplio.

**Layout:** grid `1.15fr .85fr` a 100vh. Panel hero con foto + degradé,
logo, headline, pills de rubro, stats y footer. Panel form centrado a
360px con eyebrow → título → subtítulo → banner de error condicional →
campos → checkbox → submit → back-link → footer con contacto e íconos.

## PERMITIDO (esto sí se puede tocar libremente)

- El bloque `<style>` completo: colores, tipografía, spacing, sombras,
  bordes, animaciones, estados `:hover`/`:focus`, breakpoints responsive.
- Markup puramente decorativo: iconos, imágenes, el orden visual de bloques
  que no sean el `<form>`, textos visibles (títulos, subtítulos, placeholder
  de copy, labels que no sean `name`/`for` funcionales).
- Clases CSS agregadas a elementos existentes, siempre que no se toquen los
  atributos funcionales listados abajo.
- JS puramente de UI (toggle mostrar/ocultar contraseña, estado
  `:focus`/`:hover`, spinner/`disabled` visual en el botón mientras se envía
  el form): es visual porque no cambia a dónde ni cómo se envía el form —
  solo se puede agregar si no toca `action`, `method`, `name` de los campos
  ni la lógica de submit real (dejar que el `<form>` haga el POST normal).

## PROHIBIDO (esto NUNCA se toca sin confirmación explícita)

1. **Ningún archivo `.py`**, salvo para reaplicar textualmente el fix de
   ruteo documentado arriba en "Estado implementado" si se revierte. Un
   cambio de `.py` distinto de ese (otro archivo, otra línea, otra lógica)
   sigue prohibido sin preguntar primero.
2. **Dentro de `login.html`, estos atributos/bloques quedan intocables:**
   - `<form action="..." method="...">` — el `action` y `method` tal como
     están.
   - `{% csrf_token %}` — no eliminar, no mover fuera del `<form>`.
   - `name="username"` / `name="password"` (y cualquier `id` que el JS use
     para el toggle "Ver" o el submit) — cambiarlos rompe el login silenciosamente.
   - `{% url 'login' %}`, `{% url 'home' %}`, `{% url 'logout' %}` y
     cualquier otro `{% url %}` — se pueden usar tal cual, nunca reemplazar
     por un link hardcodeado ni borrar.
   - Cualquier `{% if form.errors %}` / lógica de template ligada al form.
3. **No crear, borrar, mover ni renombrar archivos** (ni templates nuevos en
   `registration/`, ni duplicar `login.html`, ni tocar `static/`).
4. **No agregar funcionalidad nueva** aunque el mockup la insinúe: si el
   pedido implica "recuperar contraseña" funcional, un segundo tipo de
   usuario, cambiar a dónde redirige el login, o cualquier cosa que no sea
   pintar la pantalla que ya existe — **parar y avisar** que eso excede el
   alcance visual de esta skill, no improvisarlo.

## Si algo visual parece requerir tocar lo prohibido

Ejemplo típico: "que el botón deshabilitado muestre un spinner mientras
autentica" es visual (CSS/JS de UI) hasta que se le ocurra a alguien
implementarlo llamando al backend distinto — en ese punto, avisar y frenar en
vez de tocar `views.py`. La duda se resuelve siempre a favor de NO tocar
código de Python ni atributos funcionales del form, salvo el único caso ya
documentado y aprobado en "Estado implementado".

## Checklist antes de dar el retoque por terminado

- `git diff` (o `git status`) muestra cambios **únicamente** en
  `arriendo/templates/base/login.html` (más `core/urls.py` y
  `core/settings.py` SOLO si se estaba reaplicando el fix de ruteo
  documentado arriba). Cero archivos `.py` tocados fuera de eso.
- Dentro de ese diff, `action`, `method`, `{% csrf_token %}`, `name=`,
  `id=` funcionales y los `{% url %}` existentes siguen igual que antes del
  cambio.
- El formulario se sigue pudiendo enviar (probar un login real, exitoso y
  fallido, en el navegador) — si algo dejó de andar, el problema es que se
  tocó algo de la lista prohibida y hay que revertirlo, no debuggear el auth.
- `/login/` muestra el diseño nuevo Y una vista protegida sin sesión (ej.
  `/maquinaria/`) redirige a `/login/?next=...` — si redirige a
  `/accounts/login/` o muestra el template viejo, falta reaplicar el fix de
  ruteo de la sección "Estado implementado".
- El contraste de texto sobre el fondo oscuro sigue cumpliendo AA de WCAG
  después del retoque.
- Los colores/tipografía nuevos quedan centralizados en el propio `<style>`
  del archivo, no repetidos como `style="..."` inline suelto por cada
  elemento.
