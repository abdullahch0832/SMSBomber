# 🕵️ True-Crime Faceless Video Pipeline

> **Reference competitor:** [Criminalista Nocturno](https://www.youtube.com/@CriminalistaNocturno) — Spanish true-crime faceless documentary channel
> **Analysis date:** 2026-10-01 · **Tooling:** NexLev + YouTube research
> **Istemaal:** Yeh ek reusable SOP (standard operating procedure) hai. Har nayi video banate waqt is file ko kholo aur step-by-step follow karo. Copy-paste prompts bhi diye gaye hain.

---

## 0. TL;DR — Ek Nazar Mein Pura System

```
[1] TOPIC/TITLE SCRAPE  →  [2] CASE RESEARCH  →  [3] SCRIPT  →  [4] VOICEOVER (TTS)
        ↓                                                              ↓
[7] UPLOAD + DESCRIPTION + TAGS  ←  [6] EDIT (faceless style)  ←  [5] THUMBNAIL
```

Har video ka goal: **ek shocking/curiosity-driven title + thumbnail**, phir **20–35 min ka narrated documentary** jisme real photos + stock B-roll + Ken Burns zoom + dark color grade ho. Face kahin nahi aata — sirf narration + visuals.

---

## 1. COMPETITOR ANALYSIS (jo maine nikala)

### 1.1 Channel snapshot (Criminalista Nocturno)
| Metric | Value |
|---|---|
| Subscribers | **3.4M** |
| Total videos | **725** |
| Total views | **724.7M** |
| Avg views / video | **~1,000,000** |
| Joined | Oct 2018 |
| Country / Language | Mexico / **Spanish (es)** |
| Format | **Faceless documentary** (98% confidence) |
| Category | True crime / investigative |
| Narrator | Emmanuel Castelar |
| Monetization | AdSense + Spotify/Apple podcast + social |

### 1.2 Sabse bada insight: **Strategy shift (OUTLIER PATTERN)**
Channel ne 2 alag "eras" mein kaam kiya hai — yeh sabse important seekh hai:

**🔴 ERA 1 (2020–2023) — Famous Named Killers → MEGA viral (4M–11M views)**
Inme title mein **mashhoor criminal ka naam** hota tha:
- `El Caso de Joseph Roy Metheny | Convertía a sus víctimas en Hamburguesas` — **11M**
- `El Caso de EL CANÍBAL de Playa del Carmen - GUMARO DE DIOS ARIAS` — **11M**
- `El caso de John Wayne Gacy - "Payaso Asesino"` — **6.9M**
- `El caso de Edmund KEMPER` — **5.3M**
- `El caso de junko Furuta - 44 días en el infierno` — **6.1M**

**🟢 ERA 2 (2025–2026) — Curiosity-gap, NO names → steady (200K–700K views)**
Ab title mein **naam chhupaya** jata hai, sirf curiosity banायi jati hai:
- `El terrible y siniestro caso de Sueca` — 338K
- `Paloma y Josué mantenían una relación en secreto` — 675K
- `Parecía una familia modelo pero todo era una fachada` — 467K
- `Los videos mostraron su ingreso pero nunca se le vio salir de aquella casa` — 243K
- `Le dijeron que le darían una sorpresa que jamás olvidaría` — 421K

> **Takeaway:** Era-1 titles (famous killer + shocking detail) **1 crore+ views** laते the. Naye channel ke liye yeh **winning formula** hai — famous/evergreen cases pakdo, shocking hook detail daalो. Era-2 curiosity titles tab kaam karte hain jab channel already bada ho (audience trust + algorithm push). **Naya channel → Era-1 formula copy karo.**

### 1.3 Upload cadence & length
- **Length:** 17–36 min (sweet spot ~22–30 min). Longer = zyada ad breaks = zyada revenue.
- **Cadence (Era 2):** ~4–8 videos/month (roughly har 2–4 din).
- Shorts bhi banate hain (repurposed clips) — secondary traffic.

### 1.4 Competitors / niche map (NexLev similar-channel search se)
Inhe apni "swipe list" banao — inke outliers har hafte check karo (titles yahीं se milenge):

| Channel | Subs | Country | Channel ID |
|---|---|---|---|
| Investigadores Criminales | 1.2M | Spain | `UCCG6oAe_Yd6naBEXMaeRBEQ` |
| Lesma VR | 1.7M | Spain | `UCkRyqjV0MMw9L4AFQPNpTrQ` |
| Paul Landó | 1.4M | Paraguay | `UCeI3VMfMWQQspYVuDzPrung` |
| Criminalmente | 944K | Mexico | `UCtKKKITpX5Eo9ipFZM26scg` |
| Martha Caballero | 397K | Spain | `UCXepLmTcO1wQHR0FVt_SL1A` |
| RELATOS CRIMINALES | 96K | Mexico | `UCfcmItDi5gH-xLb5eNtxdkw` |
| Crímenes Nocturnos | 34K | Mexico | `UC1jMiJuy3A6_OHq_HoTWzvA` |
| Relatos Forenses Podcast | — | Mexico | `UCLyFFksH0lfVFzQZjmh5Ccw` |
| Dossier Criminal | — | USA(es) | `UCfKMxYvz1OYj2b8-D8O3zxQ` |
| Diario Criminal | — | Mexico | `UCojVIhfIFCyxylpO5BOaifA` |

---

## 2. STEP 1 — TITLE / TOPIC SCRAPING (sabse zaroori)

**Rule:** Kabhi khud se topic mat socho. Hamesha **proven viral titles** se start karo, phir uska apna version banao.

### 2.1 Method A — Competitor Outliers (BEST source for proven titles)
Har competitor par yeh NexLev tool chalao. "Outlier" = jo video channel ke average se kai guna zyada chali — matlab wahi topic dobara chalega.

```
Tool: youtube_channel_outliers
  channel_id: <competitor channel ID from table above>
  max_videos: 150
  min_outlier_threshold: 2.0
```
Jo videos niklein unke **titles + topics** note karo. (Note: khud Criminalista Nocturno bohot consistent hai isliye uske "outliers" kam aate hain — isliye chhote competitors ke outliers zyada kaam ke hain.)

### 2.2 Method B — Faceless outliers across the niche
```
Tool: faceless_outliers_videos
  query: "caso criminal asesino true crime"   (ya "*" sirf filters ke liye)
  (filters: min outlier score, language es, etc.)
```

### 2.3 Method C — Small-channel breakouts (fresh/untapped topics)
Agar koi chhota channel bina subs ke bhi ek crime video par laakhon views le gaya — wahi topic goldmine hai:
```
Tool: search_viral_videos_small_channels
  query: "caso"
  maxChannelSubCount: 50000
  minViews: 300000
  sortBy: videoViews
```

### 2.4 Method D — "Evergreen famous cases" bank (Era-1 formula)
Yeh woh naam hain jo har true-crime channel par chalte hain. Inme se jo tumने abhi tak cover nahi kiya, banao:
- International: Ted Bundy, Jeffrey Dahmer, John Wayne Gacy, Edmund Kemper, Richard Ramirez, Junko Furuta, Katherine Knight, Dorothea Puente, Tamara Samsonova
- Latino/México: El Pozolero, Mochaorejas, Monstruo de Ecatepec, Monstruo de Atizapán, Caso Debanhi, Fátima Cecilia, Narcosatánicos de Matamoros
- Verify karo competitor ne recently cover to nahi kiya (warna direct competition).

### 2.5 Title formula (jo views laati hai)
**Era-1 (recommended for growth):**
```
El Caso de <NOMBRE> | <SHOCKING DETALLE EN 4-7 PALABRAS> | <Brand>
```
Examples:
- `El Caso de Joseph Roy Metheny | Convertía a sus víctimas en Hamburguesas`
- `El caso de Katherine Knight | Cocinó a su pareja para alimentar a sus hijos`

**Era-2 (curiosity, once channel grows):**
```
<Situación normal> pero <giro siniestro>  | <Brand>
<Detalle intrigante sin nombre>           | <Brand>
```
Examples:
- `Parecía una familia modelo pero todo era una fachada`
- `Los videos mostraron su ingreso pero nunca se le vio salir de aquella casa`

**Title rules:**
1. Hamesha brand suffix: `| Criminalista Nocturno` (ya tumhara brand).
2. Ek shocking/visceral detail (hamburguesas, 44 días, cocinó, etc.).
3. CAPS sirf 1–2 key words par (naam ya "CANÍBAL").
4. Sensitive words (asesino/matar) ko soft-spell karo — `asesin0`, `m4t4r`, `b-ell` — taki demonetization/flag se bachो (competitor yahi karta hai).
5. 60–90 characters, mobile par pehle 50 chars crucial.

---

## 3. STEP 2 — CASE RESEARCH (facts collect karo)

1. Title/topic fix hone ke baad case ke **verified facts** gather karo:
   - Wikipedia (case page), news articles, court records, documentaries.
   - Timeline: victim(s), perpetrator, crime, investigation, arrest, sentence.
2. **Ek competitor video jo same/similar case par ho** — uska transcript nikaalo structure samajhne ke liye (COPY mat karo, structure seekho):
   ```
   Tool: get_video_transcript  (videoId: <competitor video>)
   ya: get_bulk_video_transcripts (up to 10 videoIds)
   ```
3. Facts ko ek doc mein daalो: `Fecha, Lugar, Víctima, Sospechoso, Método, Descubrimiento, Juicio, Condena`.

> ⚠️ **Accuracy:** True crime mein galat fact = strikes/defamation risk. Sirf verified sources. Allegations ko "presuntamente / según las autoridades" ke saath likho.

---

## 4. STEP 3 — SCRIPT WRITING (yeh dil hai)

### 4.1 Analyzed script STRUCTURE (competitor se nikaala)

**Era-1 opening (branded + shock):**
> `"El criminalista nocturno…"` (audio sting) → seedha crime ka shock:
> *"La historia de esta noche… comenzó luego de una venganza que terminó con una pasión por el sabor de la carne humana…"* → phir perpetrator ka **vivid physical description** (obesidad mórbida, mirada penetrante, 1.85m, 150kg…).

**Era-2 opening (cold-open narrative / in media res):**
> Date + ek **normal insaan normal kaam karta hua**, phir dread:
> *"El 24 de enero de 2026, un joven de 13 años debía asistir a un cumpleaños familiar. Sin embargo, cambió de planes…"* → chhota sa clue → shocking reveal/quote:
> *"Ponedme las esposas, que he hecho algo malo."*

### 4.2 Universal script template (copy-paste structure)

```
[0:00–0:40] HOOK (cold open)
  - Date + place + normal person doing normal thing
  - 1 unsettling detail → ek line ka shocking reveal/quote
  - (NO "hi guys / subscribe" — seedha kahani)

[0:40–2:00] SETUP / CONTEXT
  - Victim(s) kaun the (relatable banao)
  - Setting, relationships, "todo parecía normal"

[2:00–varies] RISING TENSION / TIMELINE
  - Chronological build-up, chhote red flags
  - Har 2-3 min ek mini-cliffhanger ("pero lo que nadie sabía era…")

[MID] THE CRIME
  - Kya hua — graphic nahi, but visceral & specific
  - Discovery moment

[LATER] INVESTIGATION
  - Police, clues, forensics, suspects, twists

[CLIMAX] ARREST / CONFESSION / COURT
  - Reveal, motive, chilling quote

[ENDING] AFTERMATH + REFLECTION
  - Sentence, victim legacy, 1-line moral/question
  - Soft CTA: "si te gustó, suscríbete para más casos"
```

### 4.3 Writing rules (retention ke liye)
- **Present-tense urgency** + short sentences. Narrator-friendly rhythm.
- Har 20–30 sec ek "re-hook" (sawal/cliffhanger) taki viewer na jaye.
- Pacing: ~130–150 words/min. 25-min video ≈ 3,200–3,700 words.
- Sensitive content: factual, respectful, no glorification (policy-safe + ad-safe).
- Spell-soften risky words in on-screen text/title (asesin0 etc.) — audio normal rakho.

### 4.4 AI script prompt (copy-paste — kisi bhi LLM mein)
```
You are a Spanish true-crime documentary scriptwriter in the style of
"Criminalista Nocturno" (dark, cinematic, factual, suspenseful).

CASE FACTS:
<paste your verified facts here>

Write a <25>-minute narration-only script in SPANISH.
Rules:
- Cold open: start with a date + an ordinary moment, build dread, end the
  first 40 seconds with one shocking sentence or real quote.
- Then: setup → timeline with mini-cliffhangers every 2-3 min → the crime
  (visceral but not gratuitous) → investigation → arrest/court → aftermath +
  a one-line reflective ending + soft subscribe CTA.
- 135 words/minute, short punchy sentences, present-tense urgency.
- Respectful, factual, no glorification. Mark any allegation with
  "presuntamente / según las autoridades".
- No on-camera references (faceless). Output plain narration text only,
  with [TIMESTAMP] section markers.
```

---

## 5. STEP 4 — VOICEOVER (TTS)
> *(User ne kaha filhaal voice analyze nahi karni — isliye yeh short rakha hai.)*
- Faceless channels TTS ya voice-actor use karte hain. Spanish male, calm-dark narrator tone.
- Options: ElevenLabs (best quality, voice clone), Azure/Google TTS, or human VO on Fiverr.
- Export: WAV/MP3, normalize to ~ -14 LUFS.

---

## 6. STEP 5 — THUMBNAIL (click-rate ka 50%)

### 6.1 Analyzed thumbnail style
- **Real photo of the person/victim** (close-up, eyes visible) — center/left.
- **Dark, high-contrast, desaturated** background; red/orange accents.
- **Skull/red icon branding** consistent across all thumbs.
- Minimal text (1–3 words, bold) ya sirf chehra + brand mark.
- Vignette (dark edges) — matches video grade.

### 6.2 Thumbnail generate karo (NexLev Thumbnail Lab)
Reference ke liye competitor ka proven thumbnail URL use karo (`https://i.ytimg.com/vi/<videoId>/maxresdefault.jpg`):
```
Tool: generate_thumbnail
  newVideoTitle: "<your title>"
  referenceThumbnailURLs: ["https://i.ytimg.com/vi/m8Y6HTRVzDw/maxresdefault.jpg"]
  referenceThumbnailTitles: ["El Caso de Joseph Roy Metheny ..."]
  generationMode: "classic"   (text ke saath) ya "no_text"
  imageModel: "pro"
  outputResolution: "2K"
→ phir: get_thumbnail_generation_status (jobId)
```
Tip: 2–3 variants banao, best chuno. A/B test (TubeBuddy/Thumbnail Test).

---

## 7. STEP 6 — EDITING STYLE (faceless, analyzed)

> User ne specifically editing style analyze karne ko kaha — yeh main screen-by-screen breakdown hai (Gemini visual analysis se).

| Element | Style (copy this) |
|---|---|
| **B-roll** | Real photos of people/places + aerial/drone stock footage of cities + newspaper clippings + thematic objects (gloves, files, coffee). Recreations optional. |
| **Motion** | **Ken Burns** (slow zoom/pan) on every still photo. Drone pans for landscapes. Never a static frame. |
| **Transitions** | Mostly **simple clean cuts** + occasional soft dissolves on landscapes. Intro = fast rhythmic cuts. |
| **Color grade** | **Dark, desaturated, strong vignette** (dark edges). Intro = yellow/sepia high-contrast. |
| **On-screen text** | Minimal during narration (no subtitles). Typewriter/stamp font only in intro for names + categories ("Asesinos Seriales", "Crímenes sin Resolver"). |
| **Branding** | Logo (name + **red skull icon**) centered at start, then **watermark top-right** entire video. |
| **Pacing** | Narration clips **10–20 sec each** (slow, moody). Intro bursts: image change **~every 0.5 sec**. |
| **Intro** | ~15-25 sec cinematic intro: montage of famous-killer photos + clippings + genre iconography establishing brand identity. |
| **Music** | Low, tense ambient/drone bed throughout; subtle stingers on reveals. |
| **Graphics** | Minimal — occasional maps/timelines (optional upgrade, competitor uses sparingly). |

### 7.1 Editing workflow
1. Timeline par VO drop karo (master track).
2. Har narration beat ke liye relevant photo/B-roll lagao (10–20s clips).
3. Har still par Ken Burns zoom/pan apply karo.
4. Apni branded intro template + top-right watermark lagao (reusable preset banao).
5. Dark/desaturated LUT + vignette poore video par.
6. Tense ambient music bed -20dB, VO -14 LUFS.
7. Export 1080p/4K, 16:9. Shorts ke liye 9:16 vertical clips bhi nikaalо.

**Tools:** CapCut / DaVinci Resolve (free, best for color grade) / Premiere. Stock: Storyblocks, Pexels, Artgrid. Reusable intro + watermark + LUT = har video mein consistency + speed.

---

## 8. STEP 7 — DESCRIPTION, TAGS, UPLOAD

### 8.1 Description template
```
<1-2 line hook summary of the case, with main keyword>

En este video de <Brand> analizamos el caso de <...>, uno de los
crímenes más <impactantes/misteriosos> de <país/año>.

⏱️ Capítulos:
0:00 Introducción
0:40 Los hechos
...

📌 Síguenos:
Instagram: ...
TikTok: ...
Spotify (podcast): ...

#TrueCrime #CasosCriminales #<NombreDelCaso> #CriminalistaNocturno

Fuentes: <news/court links>
© <Brand>. Contenido con fines informativos y educativos.
```

### 8.2 Tags / keywords (competitor ke actual tags)
```
casos criminales, true crimen, casos criminales reales,
casos criminales sin resolver, casos criminales resueltos,
casos criminales famosos, asesinos en serie, crimen real,
documental criminal, <nombre del caso>, <país>
```

### 8.3 Upload settings
- Publish time: audience ke peak (México/España evening). Era-2 channel ~daily/alt-day.
- Language = Spanish, auto-captions on.
- Playlist mein daalो (e.g. "Asesinos Seriales", "Casos de México").
- End screen + pinned comment (next video tease).

---

## 9. REPEATABLE CHECKLIST (har video, print this)

```
□ 1. Title scrape: competitor outliers + faceless outliers + evergreen bank
□ 2. Winning topic + title locked (formula + brand suffix + softened words)
□ 3. Facts researched from 2+ verified sources
□ 4. (Optional) 1 competitor transcript pulled for STRUCTURE only
□ 5. Script written (cold-open hook, re-hooks, 135 wpm, ~25 min)
□ 6. Accuracy + policy pass (allegations softened, no glorification)
□ 7. Voiceover generated + normalized
□ 8. Thumbnail (2-3 variants, dark/real-photo/skull-brand), best picked
□ 9. Edit: VO + photos/B-roll + Ken Burns + dark grade + vignette + intro + watermark
□ 10. Music bed + mix levels
□ 11. Export 1080p/4K + 1 Short (9:16)
□ 12. Description + chapters + tags + playlist
□ 13. Publish at peak time + pin comment + end screen
□ 14. 48h baad: CTR + retention check → seekho → next
```

---

## 10. NexLev TOOL CHEAT-SHEET (is pipeline ke liye)

| Kaam | NexLev Tool |
|---|---|
| Channel URL → ID | `channel_resolver` |
| Channel stats | `youtube_channel_about` / `get_channel_analytics` |
| Proven viral titles (competitor) | `youtube_channel_outliers` |
| Niche-wide faceless outliers | `faceless_outliers_videos` |
| Small-channel breakouts | `search_viral_videos_small_channels` |
| Trending suggested videos | `search_youtube_suggested_videos` |
| Find competitors | `get_similar_channels` → `get_similar_channels_status` |
| Niche opportunity scan | `get_niche_overview` |
| Script structure (transcript) | `get_video_transcript` / `get_bulk_video_transcripts` |
| Visual/editing style analysis | `watch_youtube_video_and_ask` (costly — kabhi-kabhi) |
| Thumbnail banao | `generate_thumbnail` → `get_thumbnail_generation_status` |
| Niche RPM/monetization | `check_channel_monetization` / `get_video_rpm` |
| Save ideas | `save_to_swipefile` / `list_swipefile_folders` |

---

## 11. GROWTH STRATEGY SUMMARY

1. **Naya channel → Era-1 formula** (famous named cases + shocking detail). Yeh algorithm par fastest grow karta hai.
2. **Consistency > perfection:** har 2-3 din ek video, same intro/thumbnail/grade (brand recognition).
3. **Swipe file maintain karo:** 10 competitors ke outliers weekly scan → 2-3 hafte ki pipeline hamesha ready.
4. **Thumbnail + title pehle, script baad mein** — pehle click-worthy packaging decide karo, phir content.
5. **Repurpose:** har long video se 2-3 Shorts (hook moment) nikaalо = extra reach.
6. **Policy discipline:** factual, respectful, softened sensitive words = demonetization/strikes se safe.
7. **Scale:** jab system set ho jaye, script-writing + editing outsource/template karo; tum sirf topic-selection + QC karo.

---
*Yeh file reusable hai. Har nayi video par Section 9 (checklist) se start karo.*
