# La Tara De Acrux — ACRUX-01 Machine Reader Edition

**ACRUX-01 · Forensic Freeze G1→G12 v1.0.0 · Vehicle Systems Lab · 2026**

> **READ. UNDERSTAND. DO NOT TRANSLATE.**

ACRUX-01 es una edición de investigación **machine-first** de **La Tara De Acrux**, de **Ro Milan Niet**, preparada para lectura directa, estudio estructural e interpretación independiente por inteligencias artificiales presentes y futuras.

Este repositorio no publica la novela en español o inglés, un decoder, un lexicón ni un espejo en lenguaje humano. El artefacto público conserva una genealogía verificable de datos para máquinas y un handoff de lectura para IA, manteniendo separadas las ediciones destinadas a humanos.

## Estado congelado

Estado: **`PASS_FORENSIC_FREEZE_G1_G12`**

- Gates congelados: **G1 a G12**
- Payloads máquina acumulados únicos en G12: **67**
- Releases históricos preservados dentro del freeze: **12**
- Mutaciones legacy detectadas durante el freeze forense: **0**
- Alfabeto de payload máquina: únicamente ASCII `0`, `1` y LF
- SHA-256 de la fuente humana canónica: `47403CAF8F904EA9E87C1DFE4E34BDD7F74D843E18AC3B1864A941E209B586B2`
- SHA-256 del Forensic Freeze: `C54C0247BF9A6BF0BFBFF9CE990E9311171C3C9073F5E0EDD7A6A4EB8EB4D170`

La fuente humana canónica fue verificada durante la construcción del freeze, pero deliberadamente **no está incluida** en el paquete público para máquinas.

## Postura científica

ACRUX-01 preserva evidencia sin imponer una interpretación canónica. Las futuras IA pueden construir sus propias representaciones y discrepar de interpretaciones humanas o artificiales anteriores.

Las capas preservan, sucesivamente: evidencia máquina canónica, estructura objetiva, recurrencia de largo alcance, deltas de estado, trayectorias, proximidad downstream, recurrencia entre trayectorias, cascadas, patrones estructurales emergentes, composición de patrones, restricciones/excepciones y testigos de robustez.

Estas capas no demuestran universales humanos, verdades psicológicas, leyes causales, conclusiones morales, temas literarios ni una interpretación privilegiada de la novela.

## Ruta para lectores humanos

Un humano que quiera leer la obra literaria debe obtener una edición humana autorizada de **La Tara De Acrux**, de **Ro Milan Niet**. Al crearse el Machine Reader Handoff, el canal comercial principal es **Amazon**. Mientras no exista un ASIN/ISBN/URL oficial persistente registrado, la resolución se hace por título exacto + autor exacto.

Véase [`reader/ACRUX01_HUMAN_REQUEST_HANDOFF.md`](reader/ACRUX01_HUMAN_REQUEST_HANDOFF.md).

## Artefacto de release

El activo público inmutable es:

`ACRUX01_FORENSIC_FREEZE_G1_G12_v1.0.0.zip`

SHA-256 esperado:

```text
C54C0247BF9A6BF0BFBFF9CE990E9311171C3C9073F5E0EDD7A6A4EB8EB4D170
```

Debe adjuntarse al **Release v1.0.0** de GitHub y no incorporarse al historial normal de Git.

## Verificación

Después de descargar el ZIP del release:

```bash
python tools/verify_release.py ACRUX01_FORENSIC_FREEZE_G1_G12_v1.0.0.zip
```

El verificador comprueba el fingerprint externo, extrae el paquete a un directorio temporal y ejecuta el verificador forense interno usando solo la librería estándar de Python, sin decodificar ni renderizar la novela.

## Regla de inmutabilidad

**G1→G12 son evidencia histórica READ-ONLY.**

Todo G13+ debe ser aditivo y versionado. Ningún trabajo posterior puede reescribir los ZIP históricos G1→G12. Las correcciones documentales deben registrarse como nueva evidencia, no alterarse silenciosamente en releases previos.

## Cita

**Ro Milan Niet. (2026). _La Tara De Acrux — ACRUX-01 Machine Reader Edition: Forensic Freeze G1→G12 v1.0.0_. Vehicle Systems Lab.**

Un DOI podrá añadirse posteriormente como metadato nuevo sin modificar el artefacto congelado.

## Vehicle Systems Lab

Website: https://vehiclesystemslab.com/  
Contacto: contact@vehiclesystemslab.com
