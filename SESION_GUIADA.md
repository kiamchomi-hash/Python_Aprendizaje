# Sesion Guiada

Este archivo funciona como panel de trabajo. Aca voy dejando los pasos claros y actualizados para que no tengas que reconstruirlos desde el chat.

## Estado Actual

- Python: instalado, falta verificarlo en una terminal nueva.
- Git: instalado.
- VS Code: instalado.
- Git `user.name`: falta configurar.
- Git `user.email`: falta configurar.

## Metodo De Trabajo

Desde ahora:

1. Yo explico el paso.
2. Vos ejecutas los comandos.
3. Pegas el resultado.
4. Yo verifico si esta correcto.
5. Actualizo este archivo con el siguiente paso.

## Fase 1 - Paso 1: Verificar Entorno Base

### 1. Abrir una terminal nueva

Cerra la terminal actual y abri una nueva PowerShell.

Esto importa porque Python recien instalado puede no aparecer hasta que Windows recargue el `PATH`.

### 2. Verificar Python

Ejecutar:

```powershell
python --version
```

Resultado esperado:

```text
Python 3.12.10
```

Despues ejecutar:

```powershell
pip --version
```

Resultado esperado aproximado:

```text
pip 25.x from ... Python 3.12
```

### 3. Verificar Git

Ejecutar:

```powershell
git --version
```

Resultado esperado:

```text
git version 2.53.0.windows.1
```

### 4. Configurar identidad de Git

Ejecutar estos dos comandos, reemplazando con tu nombre y email reales:

```powershell
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@example.com"
```

Ejemplo:

```powershell
git config --global user.name "Matias Apellido"
git config --global user.email "matias@email.com"
```

Que significa:

- `user.name`: nombre que aparecera en tus commits.
- `user.email`: email asociado a tus commits.
- `--global`: aplica a todos tus proyectos.

### 5. Verificar la configuracion de Git

Ejecutar:

```powershell
git config --global user.name
git config --global user.email
```

Resultado esperado:

```text
Tu Nombre
tu-email@example.com
```

### 6. Verificar VS Code

Ejecutar:

```powershell
code --version
```

Resultado esperado: varias lineas. La primera deberia ser algo parecido a:

```text
1.117.0
```

## Comandos Para Pegar En La Terminal

```powershell
python --version
pip --version
git --version
git config --global user.name
git config --global user.email
code --version
```

## Que Me Tenes Que Pegar

Pegame el resultado de esos comandos. Con eso confirmamos si el entorno minimo quedo bien.
