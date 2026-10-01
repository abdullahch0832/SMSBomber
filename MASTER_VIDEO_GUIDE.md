# 🎬 MASTER VIDEO GUIDE — Spanish True-Crime Faceless Channel

> Ek hi file mein poora system: **topic → title → script → voiceover → images/clips → video → thumbnail → upload**.
> Har nayi video ke liye upar se neeche follow karo. Deep analysis ke liye `TRUE_CRIME_VIDEO_PIPELINE.md` dekho.
> Ready test video: **Section 11** (El misterio del faro de Eilean Mòr, 3 min).

---

## 0. Pura flow ek nazar mein

```
[1] NexLev  → viral topic + title
[2] Research → case ke verified facts
[3] Script  → Spanish, competitor formula (Section 4)
[4] Voiceover → ai33.pro API (Jorge voice)  (Section 5)
[5] Visuals → Gemini image engine + clip engine (Section 6)
[6] Video   → InVideo AI / Fliki / Fiverr editor / CapCut (Section 7)
[7] Thumbnail + description + upload (Section 8-9)
```

**Tumhare tools:**
| Kaam | Tool |
|---|---|
| Research / titles / thumbnail | NexLev |
| Voiceover | ai33.pro API (`edge_es-MX-JorgeNeural` ya apni voice ID) |
| AI images | Gemini image engine (`IMAGE-ENGINE-PORTABLE.md`) |
| Video clips | Clip-scrape engine (`VIDEO-CLIP-SCRAPE.md`) |
| SFX / music | Tumhara editing pack |

---

## 1. Competitor kya karta hai (short)

**Criminalista Nocturno:** 3.4M subs, 725 videos, ~1M avg views. Spanish, faceless, documentary style, Mexico.

| | Era 1 (2020-23) | Era 2 (2025-26) |
|---|---|---|
| Title | Famous killer ka naam + shocking detail | Naam chhupa ke curiosity |
| Views | **4M-11M** | 200K-700K |
| Editing | Fast (4-6s/clip), 90% video clips, bohot SFX | Slow (12-15s/clip), 70% stills, kam SFX |

👉 **Naya channel = Era 1 formula** (famous evergreen cases + shocking hook).

**Length:** 17-30 min normal videos (test ke liye 3 min theek hai).

---

## 2. STEP 1 — Topic / Title dhoondna (NexLev)

Kabhi khud se topic mat socho. Proven viral topics se shuru karo.

| Method | NexLev tool | Settings |
|---|---|---|
| Competitor ki viral videos | `youtube_channel_outliers` | channel_id, max_videos 150, threshold 2.0 |
| Niche-wide viral | `faceless_outliers_videos` | query: "caso criminal asesino" |
| Chhote channels ke breakouts | `search_viral_videos_small_channels` | query "caso", maxChannelSubCount 50000, minViews 300000 |
| Trending abhi | `search_youtube_suggested_videos` | isFromHomeFeed true, minOutlierScore 2 |

**Competitors (channel IDs):**
| Channel | Subs | ID |
|---|---|---|
| Criminalista Nocturno | 3.4M | `UC6yNnDoJZIFlHKZFWaRsn2g` |
| Investigadores Criminales | 1.2M | `UCCG6oAe_Yd6naBEXMaeRBEQ` |
| Lesma VR | 1.7M | `UCkRyqjV0MMw9L4AFQPNpTrQ` |
| Paul Landó | 1.4M | `UCeI3VMfMWQQspYVuDzPrung` |
| Criminalmente | 944K | `UCtKKKITpX5Eo9ipFZM26scg` |
| Martha Caballero | 397K | `UCXepLmTcO1wQHR0FVt_SL1A` |
| RELATOS CRIMINALES | 96K | `UCfcmItDi5gH-xLb5eNtxdkw` |
| Crímenes Nocturnos | 34K | `UC1jMiJuy3A6_OHq_HoTWzvA` |

**Title formula (Era 1):**
```
El Caso de <NOMBRE> | <DETALLE IMPACTANTE EN 4-7 PALABRAS> | <TU CANAL>
```
**Title formula (Era 2, curiosity):**
```
<Situación normal> pero <giro siniestro> | <TU CANAL>
```
Rules: brand suffix hamesha · 1-2 words CAPS · 60-90 characters · sensitive words soft karo (`asesin0`) taake demonetize na ho.

---

## 3. STEP 2 — Research
- Facts sirf verified sources se: Wikipedia, news, court records.
- Ek doc mein likho: `Fecha · Lugar · Víctima · Sospechoso · Qué pasó · Descubrimiento · Juicio · Condena`.
- Allegations ke saath "presuntamente / según las autoridades" lagao.
- Jo baat pakki nahi (legend), us par "según algunos relatos" lagao.
- Structure seekhne ke liye competitor video ka transcript nikaal sakte ho: NexLev `get_video_transcript`. Copy mat karo, sirf structure seekho.

---

## 4. STEP 3 — Script (competitor ka formula)

### Skeleton
```
1. COLD-OPEN HOOK (0:00-0:40)   date + normal moment → shock line
2. SETUP                        log, jagah, "todo parecía normal"
3. TIMELINE                     dates + exact details, har 2-3 min cliffhanger
4. THE CRIME / DISCOVERY        factual, thanda tone, gore nahi
5. INVESTIGATION + QUOTES       real quotes = retention
6. RESOLUTION                   arrest / court / mystery
7. MORAL ENDING                 ek lesson ya sawal
8. SIGN-OFF                     "Esto ha sido <TU CANAL>. Hasta la próxima."
```

### 9 techniques (views ka raaz)
1. Pehle 30 sec mein shock. "Hi guys" wala intro nahi.
2. Main character ki vivid description.
3. Exact dates, naam aur jagah.
4. Factual, restrained tone.
5. Real quotes.
6. Har 2-3 min ek cliffhanger ("pero lo que nadie sabía era…").
7. Moral ending.
8. Signature sign-off.
9. Viewer se seedhi baat ("la historia que estás a punto de escuchar…").

**Speed:** ~135 words/min → 3 min ≈ 400 words, 25 min ≈ 3,400 words.

### AI script prompt (kisi bhi AI mein paste karo)
```
You are a Spanish true-crime documentary scriptwriter (dark, cinematic, factual, suspenseful).
CASE FACTS: <paste verified facts>
Write a <25>-minute narration-only script in SPANISH (~135 words/minute).
- Cold open: a date + an ordinary moment, build dread, end the first 40 seconds with one shocking sentence or a real quote.
- Then setup → timeline with mini-cliffhangers every 2-3 min → the crime (factual, not gratuitous) → investigation → resolution → reflective ending + "Esto ha sido <TU CANAL>. Hasta la próxima."
- Short sentences. Respectful. Mark allegations "presuntamente". Mark legends "según algunos relatos".
- Output plain narration only, no headings, no stage directions.
```

---

## 5. STEP 4 — Voiceover (ai33.pro API)

> ✅ Tested: API kaam karti hai, Spanish voices available hain.
> 🔒 Key kabhi code ya git mein mat likho. Environment variable mein rakho:
> ```bash
> export AI33_API_KEY="<YOUR_KEY>"
> ```

### Basics
| Cheez | Value |
|---|---|
| Base URL | `https://api.ai33.pro` |
| Auth header | `xi-api-key: $AI33_API_KEY` |
| TTS endpoint | `POST /v3/text-to-speech` (form-data) |
| Task status | `GET /v1/task/{task_id}` |
| Voices | `GET /v3/voices?provider=edge&language=es&gender=male` |
| Credits | `GET /v1/credits` |

**Narrator voice (competitor jaisi):** `edge_es-MX-JorgeNeural` (Mexican male).
Alternatives: `edge_es-ES-AlvaroNeural`, `edge_es-US-AlonsoNeural`, ya ElevenLabs/clone voice ID.

### TTS fields
| Field | Required | Note |
|---|---|---|
| `text` | ✅ | max 1,000,000 chars (poori script ek baar mein) |
| `voice_id` | ✅ | prefix ke saath: `edge_` `elevenlabs_` `minimax_` `clone_` `kokoro_` `vbee_` `fishaudio_` |
| `speed` | – | 0.5-1.5, narrator ke liye **0.9** |
| `with_transcript` | – | `true` = subtitles timing bhi mile |
| `file_name` | – | output naam |
| `receive_url` | – | webhook (optional) |

### Commands
```bash
# 1) Voices list (Spanish male)
curl "https://api.ai33.pro/v3/voices?provider=edge&language=es&gender=male&limit=50" \
  -H "xi-api-key: $AI33_API_KEY"

# 2) Voiceover banao → task_id milega
curl -X POST "https://api.ai33.pro/v3/text-to-speech" \
  -H "xi-api-key: $AI33_API_KEY" \
  -F text="$(cat script_es.txt)" \
  -F voice_id="edge_es-MX-JorgeNeural" \
  -F speed="0.9" \
  -F with_transcript="true" \
  -F file_name="voiceover"

# 3) Status check (jab tak "done" na ho, har 5 sec)
curl "https://api.ai33.pro/v1/task/<TASK_ID>" -H "xi-api-key: $AI33_API_KEY"
```
Jab `status` = `done` ho jaye, task ke JSON mein `metadata` ke andar audio ka link milega (`audio_url`). Usse download kar lo.

### Python (ek command mein voiceover download)
```python
# tts_ai33.py  —  usage: python3 tts_ai33.py script_es.txt voiceover.mp3 [voice_id]
import os, sys, time, json, urllib.request
import requests  # pip install requests

API = "https://api.ai33.pro"
KEY = os.environ["AI33_API_KEY"]
H = {"xi-api-key": KEY}
text = open(sys.argv[1], encoding="utf-8").read()
out = sys.argv[2]
voice = sys.argv[3] if len(sys.argv) > 3 else "edge_es-MX-JorgeNeural"

r = requests.post(f"{API}/v3/text-to-speech", headers=H,
                  data={"text": text, "voice_id": voice, "speed": "0.9", "with_transcript": "true"})
r.raise_for_status()
task = r.json()["task_id"]
print("task:", task)

while True:
    t = requests.get(f"{API}/v1/task/{task}", headers=H)
    if t.status_code == 429:
        time.sleep(int(t.headers.get("Retry-After", 5))); continue
    j = t.json()
    data = j.get("data", j)
    status = data.get("status")
    print("status:", status, data.get("progress"))
    if status == "done":
        meta = data.get("metadata", {})
        print(json.dumps(meta, indent=1)[:800])  # yahan audio / transcript links dikhenge
        url = meta.get("audio_url")
        if url:
            urllib.request.urlretrieve(url, out)
            print("saved:", out)
        break
    if status in ("error", "failed"):
        print("ERROR:", data.get("error_message")); break
    time.sleep(5)
```

### Rate limits
- HTTP **429** aaye → `Retry-After` header jitne second ruko, phir retry karo.
- HTTP **503** `server_busy` → thodi der baad retry.
- Status polling har 5 sec kaafi hai.

### Voice clone (narrator ki apni awaaz chahiye)
```bash
curl -X POST "https://api.ai33.pro/v3/text-to-speech/voice-clone" \
  -H "xi-api-key: $AI33_API_KEY" \
  -F voice_name="mi_narrador" \
  -F audio_file=@sample.mp3        # max 10MB, saaf awaaz
```
Jo `voice_id` mile, use `clone_<voice_id>` likh kar TTS mein use karo.

### Naam ka sahi uchcharan (pronunciation dictionary)
Agar koi naam galat bole (jaise "MacArthur"), to `/v3/dictionaries` mein rule banao (`{from, to, matchType}`) aur TTS mein `pronunciation_dictionary_id` bhejo.

---

## 6. STEP 5 — Visuals

### A) AI images (Gemini engine)
- Har 10-15 sec narration = 1 image. 3 min ≈ 18 images, 25 min ≈ 120-150 images.
- `tools/gemini/prompts/<video>.txt` mein ek line = ek prompt, phir `node tools/gemini/lib/run.js normal` chalao.
- **Har prompt ke end mein yeh style suffix lagao (brand look):**
```
, cinematic true-crime documentary still, dark moody lighting, desaturated cold color grade, film grain, heavy vignette, 16:9, no text, somber atmosphere
```

### B) Video clips (clip engine)
- Script ke har beat se visual queries banao (title se nahi), jaise: `"stormy ocean waves night"`, `"police tape house night"`.
- Clips 3-6 sec rakho (7 sec se kam), bina burned-in subtitles.

### C) Animation (40%)
- ~40% shots ko move karwao: **Runway / Kling / Luma / Pika** mein image daalo → "subtle motion, slow camera push".
- Baaki stills par slow zoom (Ken Burns).

### Visual style (competitor jaisa)
| Element | Style |
|---|---|
| Color | Dark, desaturated, cold blue/green |
| Effects | Film grain + dust overlay + strong vignette |
| Motion | Har still par slow zoom/pan, kabhi static nahi |
| Transitions | Simple cuts + soft dissolves |
| Intro | 10-20s montage + logo |
| Branding | Logo watermark top-right poori video mein |
| Pacing | Intro 1-2s/clip, body 10-15s/clip |

---

## 7. STEP 6 — Video jodna (bina editing skill ke)

### Option 1 — InVideo AI ⭐ (sabse aasaan, koi editing nahi)
1. invideo.io kholo → **AI video** (prompt se video).
2. Yeh prompt paste karo, phir apni script:
```
Create a Spanish true-crime documentary video, dark and mysterious style like a late-night
crime channel. Use my exact script below as narration, word for word. Male Spanish narrator
(Mexican accent), slow and serious. Dark cinematic visuals, cold desaturated colors, film
grain, vignette, slow zooms, subtle animations. Low tense ambient music, no upbeat music.
No on-screen people talking to camera. Subtitles off. 16:9.

SCRIPT:
<paste script here>
```
3. Generate dabao. Kuch badalna ho to chat mein likho: *"make visuals darker"*, *"slower narration"*, *"replace scene 3 with a stormy lighthouse"*.
4. Apni ai33 voiceover use karni ho → InVideo mein **Upload voiceover** option se MP3 daal do.

### Option 2 — Fliki / Pictory
Script paste karo → Spanish male voice ya apna MP3 → auto visuals → export.

### Option 3 — Fiverr editor ($10-20 per 3 min)
"faceless youtube video editor" search karo. Use yeh folder bhejo:
```
voiceover.mp3        (ai33 se)
subtitles.srt        (with_transcript se)
images/01.png …      (Gemini engine se, shot order mein)
clips/               (clip engine se)
music+sfx/           (tumhara pack)
TIMING.md            (Section 11 ka shot list + cue sheet)
STYLE: Section 6 ki visual style table
```

### Option 4 — CapCut (khud karna ho)
1. Voiceover timeline par daalo.
2. Images shot order mein rakho, har ek ki lambai shot list ke hisab se.
3. Har image par **Zoom in** effect lagao.
4. Filter: dark/cold, upar se grain + vignette.
5. Music track neeche (-20dB) aur SFX reveal points par.
6. Logo top-right.
7. Export 1080p.

---

## 8. STEP 7 — Thumbnail
- Real/AI portrait close-up (aankhen dikhen), dark background, red accent, 1-3 bold words.
- Brand icon corner mein.
- **NexLev:** `generate_thumbnail` → title + competitor thumbnail URL (`https://i.ytimg.com/vi/<id>/maxresdefault.jpg`) as reference, `imageModel: pro`.
- 2-3 versions banao, best chuno.

---

## 9. STEP 8 — Description, tags, upload

### Description template
```
<1-2 line hook about the case>

En este video de <TU CANAL> analizamos el caso de <...>, uno de los
crímenes más <impactantes/misteriosos> de <país/año>.

⏱️ Capítulos:
0:00 Introducción
...

#TrueCrime #CasosCriminales #<NombreDelCaso> #<TuCanal>

Fuentes: <links>
Contenido con fines informativos y educativos.
```

### Tags
```
casos criminales, true crimen, casos criminales reales, casos sin resolver,
casos criminales famosos, asesinos en serie, crimen real, documental criminal,
<nombre del caso>, <país>
```

### Upload
- Spanish language, captions on.
- Playlist mein daalo.
- End screen + pinned comment (agle video ka tease).
- México/España ke evening time par publish karo.

---

## 10. Har video ki checklist

```
□ 1. NexLev se topic + title (outliers / small channel breakouts)
□ 2. 2+ sources se facts verify kiye
□ 3. Script (hook, cliffhangers, quotes, moral ending, sign-off)
□ 4. Accuracy check (presuntamente / según algunos relatos)
□ 5. ai33 voiceover + subtitles download
□ 6. Images (Gemini) + clips (clip engine), ~40% animated
□ 7. Video jodi (InVideo / Fliki / Fiverr / CapCut)
□ 8. Music + SFX (apna pack)
□ 9. Thumbnail (2-3 versions)
□ 10. Description + chapters + tags + playlist
□ 11. Publish + pinned comment
□ 12. 48 ghante baad CTR + retention check karo, seekho
```

---

## 11. READY TEST VIDEO — "El misterio del faro de Eilean Mòr" (3 min)

**Case:** Dec 1900, Eilean Mòr (Islas Flannan, Scotland) ke lighthouse se 3 keepers gayab. Public historical case, non-graphic.

### Title
```
El misterio del faro donde 3 hombres desaparecieron sin dejar rastro | <TU CANAL>
```

### Script (`script_es.txt` mein yeh paste karo)
```
La noche del veintiséis de diciembre de mil novecientos, un barco se acercó a una pequeña isla perdida en el Atlántico Norte.
En lo alto de un acantilado se alzaba un faro que debía brillar cada noche para guiar a los navegantes.
Pero esa noche, la luz estaba apagada.
Y cuando los hombres subieron a buscar a los tres fareros que vivían allí, no encontraron a nadie.

La isla se llamaba Eilean Mòr, parte de las islas Flannan, frente a la costa de Escocia. Era un lugar solitario, azotado por el viento y rodeado de mar abierto.
Allí trabajaban tres hombres: James Ducat, el jefe; Thomas Marshall; y Donald MacArthur.
Hombres de mar, experimentados, acostumbrados a la soledad y a las tormentas. Durante semanas, su único deber era mantener la luz encendida.

Días antes, un barco que pasó cerca notó algo extraño: el faro no había encendido su luz. Nadie respondió a las señales.
Cuando por fin un relevo logró desembarcar, encontraron la puerta cerrada, las camas vacías y los relojes detenidos.
No había señales de lucha. No había notas de despedida. Simplemente, no había nadie.

Según algunos relatos, la mesa estaba servida y la comida seguía intacta, como si los tres hombres se hubieran levantado de golpe, y jamás hubieran regresado.
Y otro detalle inquietante: una silla volcada junto a la mesa.
Lo que sí está documentado es esto: dos de los tres abrigos impermeables habían desaparecido. El tercero seguía colgado en su gancho.

Años después circuló la historia de unas anotaciones en el registro del faro, que hablaban de una tormenta terrible. Una tormenta que, según los informes del clima, nunca azotó la isla.

¿Qué pudo ocurrir? La teoría oficial dice que una ola gigante los arrastró mientras intentaban asegurar el equipo en el acantilado.
Otros hablaron de un accidente, de una discusión, incluso de fuerzas imposibles de explicar. Pero ninguna teoría responde a todas las preguntas.

Más de un siglo después, el faro de Eilean Mòr sigue encendido, automatizado y vacío. Y la pregunta sigue flotando en el viento del Atlántico: ¿qué fue lo que realmente se llevó a aquellos tres hombres aquella noche de invierno?

Si esta historia te mantuvo despierto, déjame tu teoría en los comentarios. Esto ha sido <TU CANAL>. Hasta la próxima noche.
```
> Accuracy note: officially documented = keepers gayab, darwaza band, ek oilskin coat peeche reh gaya, official theory badi lehar. Khana, ulti kursi aur logbook ki toofan entries baad ki kahaniyan hain, isliye script mein unke saath "según algunos relatos / circuló la historia" likha hai.

### Voiceover
```bash
python3 tts_ai33.py script_es.txt voiceover.mp3 edge_es-MX-JorgeNeural
```

### Shot list + image prompts (har prompt ke end mein Section 6 ka style suffix lagao)
`[ANIM]` = animate karo · `[STILL]` = sirf slow zoom · `[CLIP]` = clip engine se

| # | ~Time | Type | Narration (shuru) | Image prompt |
|---|---|---|---|---|
| 0 | 0:00 | [ANIM] | (intro, 5s, music + title) | Lonely lighthouse on a cliff at night, lamp dark, title space on the left |
| 1 | 0:05 | [ANIM] | La noche del veintiséis… | A lone lighthouse on a cliff at night, its lamp unlit, black stormy ocean, rain |
| 2 | 0:13 | [CLIP] | En lo alto de un acantilado… | clip: "rough north atlantic sea waves night drone" |
| 3 | 0:20 | [ANIM] | Pero esa noche, la luz estaba apagada. | A small wooden boat approaching a remote rocky island in dark churning water |
| 4 | 0:24 | [STILL] | Y cuando los hombres subieron… | Low angle view up at a tall dark lighthouse on steep black cliffs |
| 5 | 0:31 | [STILL] | La isla se llamaba Eilean Mòr… | Vintage aged map of remote Scottish islands in the North Atlantic |
| 6 | 0:43 | [ANIM] | Allí trabajaban tres hombres… | Three lighthouse keepers in early 1900s coats, vintage photo style, silhouettes |
| 7 | 0:50 | [ANIM] | Hombres de mar, experimentados… | Huge waves crashing on dark rocks at night, spray, storm |
| 8 | 1:01 | [ANIM] | Días antes, un barco que pasó cerca… | A ship with lit windows passing a dark lighthouse at night |
| 9 | 1:10 | [STILL] | Cuando por fin un relevo… | Dark empty stone lighthouse room, unlit oil lamp on a table |
| 10 | 1:19 | [STILL] | No había señales de lucha… | Empty narrow bed in a cold stone room, blanket undisturbed |
| 11 | 1:26 | [ANIM] | Según algunos relatos, la mesa… | Table set with untouched plates, a stopped clock on the stone wall, candlelight |
| 12 | 1:38 | [STILL] | Y otro detalle inquietante… | A wooden chair knocked over on a stone floor beside a table |
| 13 | 1:43 | [STILL] | Lo que sí está documentado… | One old yellow oilskin coat on an iron hook, two empty hooks beside it |
| 14 | 1:53 | [ANIM] | Años después circuló la historia… | Open handwritten 1900s logbook on a desk, candle flame, faded ink |
| 15 | 2:07 | [ANIM] | ¿Qué pudo ocurrir? … | A giant wave rising against a cliff at night, three tiny figures on the edge |
| 16 | 2:17 | [STILL] | Otros hablaron de un accidente… | Three dark silhouettes on a cliff edge in heavy wind, backs turned |
| 17 | 2:30 | [ANIM] | Más de un siglo después… | A lighthouse beam sweeping over an empty island at night, present day |
| 18 | 2:47 | [STILL] | Si esta historia te mantuvo despierto… | Lonely grey ocean at dusk, empty horizon, faint warm glow |

≈ 10/19 shots animated (~45%). Exact time voiceover ke hisab se thoda badlega.

### Music / SFX cue sheet (apne pack se)
| ~Time | Cue |
|---|---|
| 0:00 | Dark ambient drone shuru (poori video, -20dB) + deep impact on title |
| 0:22 | Stinger: "la luz estaba apagada" |
| 0:29 | Sharp impact: "no encontraron a nadie" |
| 0:31 | Whoosh into map |
| 1:01 | Riser build-up |
| 1:10 | Deep impact: "relojes detenidos" |
| 1:26 | Stinger: "comida seguía intacta" |
| 1:38 | Riser → sharp impact: "silla volcada" |
| 2:07 | Deep impact + thunder: "ola gigante" |
| 2:30 | Music soft pad (ending) |
| 3:00 | Music fade out + black |

### Thumbnail
Dark lighthouse on a cliff at night, lamp OFF, huge stormy wave, cold teal, vignette. Text: **¿QUÉ PASÓ AQUÍ?** (red/white). Red circle on the dark lantern window.

### Description
```
En 1900, tres fareros desaparecieron de la isla de Eilean Mòr sin dejar rastro.
La puerta cerrada, un abrigo olvidado y ninguna explicación. ¿Qué ocurrió realmente? | <TU CANAL>

⏱️ 0:00 La luz apagada · 0:31 Eilean Mòr · 1:01 El relevo · 1:26 Los detalles · 2:07 Las teorías · 2:30 El misterio continúa

#MisterioSinResolver #CasosReales #EileanMor #TrueCrimeEspañol
```

---

## 12. Zaroori files (repo mein)
| File | Kya hai |
|---|---|
| `MASTER_VIDEO_GUIDE.md` | Yeh file (sab kuch) |
| `TRUE_CRIME_VIDEO_PIPELINE.md` | Competitor ka deep analysis (script, editing, sound) |
| `DEMO_VIDEO_01_Eilean_Mor.md` | Test video ka pehla blueprint |
| `video_build/scenes.py` | 19 test scenes ka original artwork generator (`python3 -c "import scenes"` + Pillow) |

> 🔒 Security: API key sirf environment variable / API credentials mein rakho. Yeh key chat mein share ho chuki hai, isliye ai33.pro par nayi key bana lo.
