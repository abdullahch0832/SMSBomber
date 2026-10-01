# 🎬 DEMO VIDEO 01 — "El misterio del faro de Eilean Mòr"

> **Test render · 3 minutes · Spanish · faceless documentary**
> Case: Flannan Isles / Eilean Mòr lighthouse disappearance (26 Dec 1900, Scotland) — 3 keepers vanished without a trace. Public, historical, **non-graphic**, atmospheric — perfect safe demo.
> Brand placeholder: **[TU CANAL]** (apne channel ke naam se replace karo).
> Animation target: **40%** shots animated (marked `[ANIM]`), baaki stills/clips.

---

## 1. TITLE (Spanish)
```
El misterio del faro donde 3 hombres desaparecieron sin dejar rastro | [TU CANAL]
```
Alt options:
- `El faro de Eilean Mòr | 3 hombres se esfumaron y nadie sabe por qué | [TU CANAL]`
- `Entraron al faro… pero jamás volvieron a salir | [TU CANAL]`

---

## 2. SCRIPT (Spanish · ~3 min · ~390 words · narrator: calm, grave, slow)

> **Narration only.** `[TIMESTAMP]` = section marker. Edge TTS: `es-MX-JorgeNeural --rate=-12% --pitch=-3Hz`.

```
[0:00 — HOOK]
La noche del 26 de diciembre de 1900, un barco se acercó a una pequeña isla
perdida en el Atlántico Norte. En lo alto de un acantilado se alzaba un faro
que debía brillar cada noche para guiar a los navegantes. Pero esa noche, la
luz estaba apagada. Y cuando los hombres subieron a buscar a los tres fareros
que vivían allí… no encontraron a nadie.

[0:28 — SETUP]
La isla se llamaba Eilean Mòr, parte de las Flannan, frente a la costa de
Escocia. Era un lugar solitario, azotado por el viento y rodeado de mar abierto.
Allí trabajaban tres hombres: James Ducat, el jefe; Thomas Marshall; y Donald
MacArthur. Hombres de mar, experimentados, acostumbrados a la soledad y a las
tormentas. Durante semanas, su único deber era mantener la luz encendida.

[1:00 — RISING]
Días antes, un barco que pasó cerca notó algo extraño: el faro no había
encendido su luz. Nadie respondió a las señales. Cuando por fin un relevo logró
desembarcar, encontraron la puerta cerrada, las camas vacías y los relojes
detenidos. La mesa estaba servida, pero la comida seguía intacta, como si los
tres hombres se hubieran levantado de golpe… y jamás hubieran regresado.

[1:38 — THE DETAILS]
Dentro del faro todo estaba en orden, salvo un detalle inquietante: una silla
volcada junto a la mesa. Dos de los tres abrigos impermeables habían
desaparecido; el tercero seguía colgado en su gancho. En el registro del faro,
la última anotación hablaba de una tormenta terrible… una tormenta que, según
los informes del clima, nunca había azotado la isla aquellos días.

[2:12 — THEORIES]
¿Qué pudo ocurrir? Algunos creyeron que una ola gigante los arrastró mientras
intentaban asegurar el equipo en el acantilado. Otros hablaron de un accidente,
de una discusión, incluso de fuerzas imposibles de explicar. Pero ninguna
teoría explica por completo la silla volcada, el abrigo que quedó atrás, ni esa
tormenta escrita que nunca existió.

[2:42 — ENDING]
Más de un siglo después, el faro de Eilean Mòr sigue encendido, automatizado y
vacío. Y la pregunta sigue flotando en el viento del Atlántico: ¿qué fue lo que
realmente se llevó a aquellos tres hombres aquella noche de invierno?

Si esta historia te mantuvo despierto, déjame tu teoría en los comentarios.
Esto ha sido [TU CANAL]. Hasta la próxima.
```

**Script techniques used** (Section 4.5 of pipeline): cold-open shock hook · specific dates/names/places · factual-restrained tone · eerie concrete details (overturned chair, stopped clocks, the coat, the fictitious storm) · mini-cliffhangers · reflective rhetorical ending · signature sign-off · second-person intimate address.

Word count ≈ 390 → at −12% rate ≈ **~3:00**.

---

## 3. SHOT LIST + AI IMAGE PROMPTS (for your Gemini image engine)

> 1 line = 1 image → paste into `tools/gemini/prompts/demo01.txt`, run `node tools/gemini/lib/run.js normal`.
> **Style suffix (append to EVERY line for brand consistency):**
> `, cinematic true-crime documentary still, dark moody lighting, desaturated cold color grade, film grain, heavy vignette, 16:9, no text, somber atmosphere`
>
> **Legend:** `[ANIM]` = animate this image (AI-video / motion) · `[STILL]` = Ken Burns only · `[CLIP]` = use scraped footage (Section 4). **40%+ marked `[ANIM]`.**

| # | Time | Type | Prompt (add style suffix) |
|---|---|---|---|
| 1 | 0:00 | `[ANIM]` | A lone lighthouse on a cliff at night, its lamp dark and unlit, black stormy ocean around it |
| 2 | 0:08 | `[CLIP]` | *(clip query)* rough north atlantic sea waves at night drone |
| 3 | 0:14 | `[ANIM]` | A small wooden boat approaching a remote rocky island in dark churning water |
| 4 | 0:22 | `[STILL]` | View from a boat looking up at a tall lighthouse on steep black cliffs |
| 5 | 0:30 | `[STILL]` | A vintage map of remote scottish islands in the north atlantic, aged paper |
| 6 | 0:40 | `[ANIM]` | Three weathered lighthouse keepers in early 1900s coats standing by a lamp, vintage photo style |
| 7 | 0:52 | `[CLIP]` | *(clip query)* stormy ocean waves crashing on rocks |
| 8 | 1:02 | `[STILL]` | A dark empty lighthouse interior, a single oil lamp unlit on a table |
| 9 | 1:12 | `[ANIM]` | A ship passing a dark lighthouse at night that shows no light, eerie |
| 10 | 1:24 | `[STILL]` | An empty narrow bed in a cold stone lighthouse room, blanket undisturbed |
| 11 | 1:32 | `[ANIM]` | A table set for a meal, untouched food, a stopped clock on the wall, dim light |
| 12 | 1:42 | `[STILL]` | A single wooden chair knocked over on a stone floor beside a table |
| 13 | 1:52 | `[STILL]` | An old raincoat hanging alone on an iron hook in a dark room |
| 14 | 2:00 | `[ANIM]` | A handwritten 1900s logbook open on a desk, candlelight, faded ink |
| 15 | 2:14 | `[ANIM]` | A giant wave rising against a cliff at night, tiny figures silhouetted, dramatic |
| 16 | 2:26 | `[STILL]` | Dark silhouettes of three men on a cliff edge in heavy wind, backs turned |
| 17 | 2:42 | `[ANIM]` | A modern automated lighthouse beam sweeping over an empty island at night |
| 18 | 2:52 | `[STILL]` | Wind over a lonely grey ocean at dusk, empty horizon, melancholic |

→ ~7 of 18 shots are `[ANIM]` ≈ **39%** animation. (Ek aur `[STILL]` ko `[ANIM]` karke exactly 40%+ kar sakte ho.)

### Animation kaise banाना (40%)
- `[ANIM]` images ko AI-video tool se animate karo: **Runway / Kling / Luma / Pika** → "subtle motion, slow camera push, waves moving, flickering light".
- Ya simplest: Gemini image → editor mein **parallax / 2.5D motion** + slow zoom. (Dono chalega.)

---

## 4. CLIP QUERIES (for your clip-scrape engine)

> Feed these to the engine (one search each). It keeps clean 3–6s segments (`< 7s`), no burned captions.

```
rough north atlantic sea waves night drone
stormy ocean waves crashing on rocks dark
remote rocky island cliffs scotland aerial
lighthouse beam at night storm
vintage oil lamp flame close up
dark stormy sky clouds timelapse
old stone lighthouse interior
candle flame dark room close up
```

---

## 5. VOICEOVER (Edge TTS — run on your machine)
1. Script ka `[TIMESTAMP]`/section labels hata ke plain text `script_es.txt` mein save karo.
2. Run:
```bash
edge-tts --voice es-MX-JorgeNeural --rate=-12% --pitch=-3Hz \
  --file script_es.txt --write-media voiceover.mp3 --write-subtitles subs.vtt
```
3. Normalize to ~-14 LUFS; key lines (hook + "silla volcada" + ending) par halka reverb.

---

## 6. SFX / MUSIC CUE-SHEET (placeholder — apne pack se map karo)

> Jab pack ka file-list do, main `[SLOT]` ko asli file naam se bhar dunga. Abhi generic slots:

| Time | Cue | Slot (your pack) |
|---|---|---|
| 0:00 | Low dark drone starts (bed, whole video) | `[MUSIC_dark_ambient_loop]` |
| 0:05 | Deep sub-bass impact on "la luz estaba apagada" | `[SFX_impact_deep]` |
| 0:14 | Wind ambience under boat scene | `[SFX_wind_ambience]` |
| 0:26 | Soft whoosh into title/setup | `[SFX_whoosh]` |
| 1:00 | Subtle riser as mystery builds | `[SFX_riser]` |
| 1:32 | Stinger on "comida intacta / relojes detenidos" | `[SFX_stinger]` |
| 1:42 | Sharp sub-boom on "silla volcada" (overturned chair) | `[SFX_impact_sharp]` |
| 2:00 | Eerie texture under logbook | `[SFX_eerie_texture]` |
| 2:14 | Rising tension → brief swell on the giant-wave shot | `[SFX_riser_big]` |
| 2:42 | Music softens for reflective ending | `[MUSIC_soft_pad]` |
| 2:58 | Music fade-out to black | `[MUSIC_fade_out]` |

Narration foreground · music low bed · SFX only on reveals. Mix: VO −14 LUFS, music ~−22 LUFS.

---

## 7. THUMBNAIL concept (make with your Gemini engine or NexLev)
- **Visual:** dark lighthouse on a cliff at night, lamp OFF, huge stormy wave, cold blue/teal grade, heavy vignette.
- **Text (2–3 words, bold):** `¿QUÉ PASÓ AQUÍ?` or `SIN RASTRO` — red/white.
- **Add:** a red circle/arrow on the dark lighthouse window. Your brand skull/logo corner.
- **Prompt:** `A dark ominous lighthouse on a cliff at night with its lamp unlit, a massive stormy wave behind it, cold teal color grade, dramatic, cinematic, heavy vignette, space for bold text, 16:9`

---

## 8. DESCRIPTION + TAGS
```
En 1900, tres fareros desaparecieron de la isla de Eilean Mòr sin dejar rastro.
La puerta cerrada, una silla volcada, los relojes detenidos y una tormenta que
nunca existió. ¿Qué ocurrió realmente aquella noche? | [TU CANAL]

⏱️ Capítulos:
0:00 La luz apagada
0:28 La isla de Eilean Mòr
1:00 El relevo
1:38 Los detalles inquietantes
2:12 Las teorías
2:42 El misterio continúa

#MisterioSinResolver #CasosReales #EileanMor #TrueCrimeEspañol #[TuCanal]
```
Tags: `misterio sin resolver, casos reales, faro, desaparición, true crime español, historias de misterio, casos inexplicables, eilean mor, flannan`

---

## 9. EDIT TIMELINE (assembly order)
```
1. voiceover.mp3 → master audio track
2. Har section ke shots lagao (table order), har image par Ken Burns
3. [ANIM] shots ko animated version se replace karo (~40%)
4. [CLIP] slots par scraped 3–6s clips
5. Dark/cold LUT + grain overlay + vignette (poore video par)
6. Top-right watermark (apna logo) + intro card
7. Music bed + SFX cue-sheet (Section 6) place karo
8. Mix levels → export 1080p/4K, 16:9
9. Thumbnail attach → upload (Section 8)
```

---
*Pack ka file-list do → cue-sheet ke `[SLOT]` asli naam se bhar dunga. Baaki sab ready hai.*
