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

Har video ka goal: **ek shocking/curiosity-driven title + thumbnail**, phir **20–35 min ka narrated documentary** jisme AI images + Ken Burns zoom + dark color grade ho. Face kahin nahi aata — sirf narration + visuals.

### 🧰 MERE PAAS JO ASSETS HAIN (is pipeline ko adjust karta hai)
- ✅ **Editing pack (SFX + music)** — mera apna. Isliye SFX/music sourcing ki zaroorat NAHI. (Section 7B ko cue-sheet ki tarah use karo: kaunsा sound kahan.)
- ✅ **AI image tool (unlimited images)** — mera apna. Isliye visuals **AI-FIRST** honge: stock footage dhoondne ki zaroorat nahi, script ki har exact scene ki image khud banao. Consistent, copyright-free, identity auto-safe.
> **Baaqi sab cheez (titles, script, structure, thumbnail, pacing, grade) same rehti hai — sirf visual sourcing aur audio sourcing solved hai.**

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

## 4.5 DEEP SCRIPT DECONSTRUCTION — "woh kaise likhta hai aur views kyun aati hain"

> Yeh competitor ki **11M-views wali video** (Joseph Roy Metheny) ka poora transcript (hook → crime → confession → ending) line-by-line analyze karke banaya gaya. Yeh uski **asli formula** hai.

### 4.5.1 Script ka poora skeleton (jo har video mein hai)
```
1. COLD-OPEN SHOCK HOOK          (0:00–0:50)
2. VILLAIN KA VIVID DESCRIPTION  (0:50–1:30)
3. CHRONOLOGICAL CRIME STORY     (body — dates + details)
4. KILLER KE DIRECT QUOTES       (mid/climax — chilling)
5. RESOLUTION (arrest/death)     (climax)
6. REFLECTIVE MORAL/LESSON       (ending — takeaway)
7. SIGNATURE SIGN-OFF + CTA      (outro ritual)
```

### 4.5.2 Har technique (real examples + kyun kaam karti hai)

**① Cold-open shock hook — pehle 30 sec mein khoon**
Koi "hi guys, subscribe" nahi. Seedha crime ka shock:
> *"La historia de esta noche… comenzó luego de una venganza que terminó con una pasión por el sabor de la carne humana…"*
→ **Kyun:** YouTube ke pehle 30 sec sabse crucial hain (retention). Shock = koi scroll nahi karta. Yahi views ka #1 raaz hai.

**② Villain ka vivid physical description — cinema ban jata hai**
> *"…Joseph Roy Metheny. Un sujeto con obesidad mórbida, de mirada penetrante y facciones gruesas, de sonrisa intimidante, con una altura de 1.85 m y más de 150 kg…"*
→ **Kyun:** Reader ke dimaag mein tasveer banti hai. Abstract nahi — concrete. Immersion start.

**③ Specificity — exact dates, naam, jagah (believability)**
> *"El 2 de agosto de 1995 fueron descubiertos los cuerpos… identificados como Randall Brewer y Randy Paker… cavó una tumba poco profunda en un pequeño bosque detrás de la fábrica, donde permaneció 6 meses…"*
→ **Kyun:** Specific details (exact date, naam, "6 meses", "detrás de la fábrica") = sach lagta hai = viewer trust karta hai aur ruka rehta hai. Vague writing = log chhod dete hain.

**④ Factual-but-visceral tone — thanda describe karna zyada darावna**
> *"La tomó por el cuello y la privó de la respiración hasta asesinarla… arrancó la cabeza y la tiró a la basura."*
→ **Kyun:** Drama nahi, seedha fact — isi se goosebumps aate hain. Over-dramatize nahi karta. Mature/documentary feel = ad-safe bhi.

**⑤ Killer ke direct quotes — retention gold**
> *"Simplemente lo disfruté."*
> *"Las palabras 'lo siento' nunca saldrán de mi boca porque serían una mentira. Estoy dispuesto a dar mi vida… para que Dios me juzgue y me mande al infierno."*
→ **Kyun:** First-person chilling quote sabse zyada share/comment hota hai. Log inhi moments ke liye rukte hain.

**⑥ Mini-cliffhangers / re-hooks — har 2-3 min**
Phrases jaise *"pero lo que nadie sabía era…"*, *"semanas después…"* — har segment ko agle se jodta hai.
→ **Kyun:** Curiosity gap kabhi band nahi hone deta = watch-time high = algorithm push.

**⑦ Reflective moral ending — satisfying closure**
> *"Este caso es un claro ejemplo de que no todo lo que los asesinos confiesan es cierto, ya que muchos tienden a adjudicarse crímenes que no cometieron con el único fin de ser importantes…"*
→ **Kyun:** Viewer ko ek "lesson/insight" milta hai — sirf gore nahi, kuch soch ke jata hai. Yeh maturity = repeat viewers.

**⑧ Signature sign-off ritual — loyalty**
> *"No olvides suscribirte al canal y activar la campana… Espero que hayas pasado una excelente noche… Esto es El Criminalista Nocturno. Hasta la próxima emisión."*
→ **Kyun:** Har video same ritual = brand identity + apnapन. "Nocturno" = raat ko sunne wala companion feel.

**⑨ Second-person intimate address — viewer se seedhi baat**
> *"La historia que estás a punto de escuchar…"*, *"espero que hayas pasado una excelente noche…"*
→ **Kyun:** "Tum" se baat karna = personal connection, jaise koi raat ko kahani suna raha ho.

### 4.5.3 WHY VIEWS (poora formula ek nazar mein)
| Factor | Effect |
|---|---|
| Famous case (Era-1) | Built-in search demand (log already dhoondte hain) |
| Shock title + thumbnail | High CTR (click) |
| Cold-open hook (0-30s) | No early drop → algorithm push |
| Specific details + quotes + cliffhangers | High retention → high watch-time |
| Factual mature tone | Ad-safe + credibility |
| Consistent format + sign-off | Returning + binge audience |
| 17–35 min length | Zyada ad breaks + watch-time signal |

> **Ek line ka raaz:** *Famous case pakdo → pehle 30 sec mein shock → poori video specific detail + killer quotes + cliffhangers se bharo → factual tone → moral ending + signature sign-off.* **Yahi 11M views laata hai.**

### 4.5.4 Era-2 script ka farq (naya style)
- Hook branded-sting ki jagah **cold narrative** (date + normal insaan → dread → shocking reveal/quote).
- Ending **rhetorical sawal + reflection**, fade-to-black (colourful subscribe-screen nahi).
- Baaki saari 9 techniques **same** rehti hain — sirf hook aur title packaging alag.

---

## 5. STEP 4 — VOICEOVER (TTS)

### Competitor narrator profile (match karne ke liye)
Male, deep, **calm + serious** (menacing calm — cheekhta nahi), slow (~130–145 wpm), deliberate pauses, neutral **Mexican Spanish**, light reverb on key phrases, "nocturnal storyteller" vibe.

### ✅ Recommended: Edge TTS (free, no API key, best value)
Best voice = **`es-MX-JorgeNeural`** (deep Mexican male). Alt: `es-MX-LibertoNeural`, `es-ES-AlvaroNeural`.
```bash
pip install edge-tts

edge-tts --voice es-MX-JorgeNeural \
  --rate=-12% \        # slow, deliberate (narrator feel)
  --pitch=-3Hz \       # thoda deeper/grave
  --file script.txt \
  --write-media voiceover.mp3 \
  --write-subtitles subs.vtt
```
> ⚠️ Edge TTS cloud sandboxes/filtered proxies ke peeche DRM error (`No server date in headers`) de sakta hai — **normal machine/network par bilkul theek chalta hai.** Isliye voiceover apni machine par banao.

### Other options
- **ElevenLabs** — best quality + **voice clone** (narrator ki exact awaaz ke liye 1-min sample do). Paid.
- **Azure TTS** — same Jorge/Alvaro neural voices, API.
- **Human VO** — Fiverr Spanish male narrator.

### Post
- Export WAV/MP3, normalize to **~-14 LUFS**.
- Key phrases par halka **reverb** (competitor jaisा) editor mein add karo.

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

## 7B. DEEP EDITING & SOUND DESIGN (frame-by-frame + audio, dono eras)

> Yeh section multiple video segments (intro + body + climax + outro, dono purani viral aur nayi video) ko visually+audibly dekh kar banaya gaya hai. Isse tum editing + sound ko **replicate** kar sakte ho.

### 7B.1 BACKGROUND MUSIC (score)
- **Genre/mood:** Dark Ambient + Cinematic Suspense. Low-frequency **drones** + atmospheric **synth pads**; climax mein dheeमी **piano notes**.
- **Behaviour:** Linear rehti hai (body mein achानक change nahi), narration ke **neeche low volume** par, aur **key points ke transitions par thoda upar** aati hai.
- **Mood shift:** Jab main subject (criminal/victim) ki photo aati hai, music **zyada melancholic/deep** ho jati hai.
- **Intro music:** Zyada rhythmic, SFX hits ke saath sync.
- **Outro:** Koi happy "bye-bye" theme NAHI — music dheere-dheere **fade out** hoti hai aakhri reflection ke saath, phir **fade to black**.
- **Silence:** Pehle bade impact se pehle ek **dramatic silence** (riser → silence → sub-bass hit).

### 7B.2 SFX (sound effects) — full list jo detect huए
**Intro/reveal hits:**
- Metallic/dry **impact stinger** jab har killer ki photo aati hai
- **Splash/impact** jab photo paani mein girti hai
- **Muffled thud** jab envelope band hota hai
- Deep **sub-bass impact** jo main story ka start mark karta hai
- **Camera shutter** (purana camera) sound
- **Marker squeak** jab text par cross lagta hai
- **Riser** jo silence tak build hota hai

**Transitions:**
- **Paper whoosh** page-turn par
- **Digital glitch/interference** jab phone screen mein enter karte hain
- Deep **whoosh** scene change par

**Diegetic (scene ke andar ke) sounds:**
- Beer/liquid **pouring**, river/water **ambience**, **wind + forest creaks**, judge ka **gavel with echo**, "steel pipe" mention par metallic clink, aggression par dull **thuds**

**Voice FX:** Key phrases par **reverb/echo** (jaise "carne humana") — dramatic emphasis.

**⚠️ Important restraint rule:** Sensitive segments (bacche/victim ka zikr) mein **aggressive stingers OFF** — sirf subtle sub-boom + room-tone hum. Respectful rehna = policy-safe + mature feel.

### 7B.3 AUDIO MIX hierarchy
```
1. NARRATION  → foreground, sabse loud, clear (-14 LUFS approx)
2. MUSIC      → low background bed, silences fill karti hai
3. SFX        → punctuation only, reveals/transitions par pop
```

### 7B.4 TRANSITIONS (kab kaunsा)
- **Intro:** fast rhythmic **cuts** + digital **zoom-in** + quick **blurs** + ek **keyhole/circular mask** reveal + short **fade-to-black** jo intro ko body se alag karta hai.
- **Body:** mostly **direct cuts** + soft **cross-dissolves**, har **10–20 sec**.
- **Overlays:** criminal ka chehra city/scene ke upar **superimpose** (do images blend) — "introspection / paso del tiempo" feel.

### 7B.5 CLIPS vs PHOTOS (ERA difference — bada farq)
| | **Era 1 (purana viral)** | **Era 2 (naya)** |
|---|---|---|
| Video clips : Photos | **~90% video / 10% photos** | **~30% video / 70% stills** |
| Material | High-quality stock: drone over rivers, misty forests, night city + real photos | AI/painterly-filtered portraits (identity protect), drone establishing shots, morgue/stock, actor recreation close-ups |
| Body pacing | **4–6 sec/clip** (faster) | **12–15 sec/clip** (slow, solemn) |
| SFX density | **Rich** (many stingers) | **Restrained** (subtle sub-booms) |
| Intro | Full cinematic killer-montage intro | Lighter / quicker |
| Feel | Punchy, cinematic | Somber, respectful, mature |

### 7B.6 IMAGES & GRAPHICS used
Real photos, **newspaper clippings**, letters/documents (e.g. Zodiac letters), **maps**, aur Era-2 mein **AI/painting-style stylized portraits** (jab real footage na ho ya identity chhupani ho).

### 7B.7 VISUAL EFFECTS / FILTERS (constant stack)
- **Film grain** + **dust/scratch textures** ("criminal archive / vintage" look) — poore video par overlay.
- **Pronounced vignette** (dark edges) har frame par.
- **Ken Burns** (slow zoom/pan) **har still photo** par — kabhi static nahi.
- **Color grade:** desaturated, **cold tones** (dark blue/green), "dark & moody".
- Era-2 ki photos par extra **artistic/painterly texture filter**.

### 7B.8 BRANDING
- Logo (name + **red skull**) intro mein center → phir **watermark top-right** poore video.
- Cinematic **title cards** jo blur ke saath appear/disappear hote hain.

### 7B.9 PACING cheat
```
INTRO:   1–2 sec/clip, music+SFX hits ke saath synced (frenetic)
BODY:    Era1 = 4–6 sec/clip | Era2 = 12–15 sec/clip
CLIMAX:  slow, deliberate, music volume thoda up, dramatic pauses
OUTRO:   fade out music + fade to black, sober (no colorful endscreen)
```

### 7B.10 Editing REPLICA kit (banाo ek baar, reuse hamesha)
1. **Intro template** (10–20s): killer/case montage + SFX hits + logo reveal.
2. **Top-right watermark** PNG (name + red skull).
3. **Color LUT:** desaturated cold + vignette.
4. **Overlay pack:** film grain + dust/scratch (screen blend, ~15% opacity).
5. **SFX library:** ✅ *tumhare editing pack se* — impact stingers, sub-booms, whooshes, risers, camera shutter, paper, glitch, gavel, ambiences. (Cue-sheet ban jayega: kaunsा kahan.)
6. **Music bed:** ✅ *tumhare editing pack se* — 2–3 dark-ambient loops (intro / body / climax).
7. **Title-card preset** (blur in/out).
8. **Ken Burns preset** auto-apply on stills.
Isse har video **30–50% faster** edit hoti hai aur brand-consistent dikhti hai.

### 7B.11 AI-FIRST VISUAL WORKFLOW (tumhare image tool ke saath)
Kyunki unlimited AI images hain, visuals ab stock par depend nahi karte:
1. Script ke har section (hook, setup, timeline, crime, investigation, climax, outro) ke liye **shot list** banao — har 10–15 sec ke liye 1 image.
2. Har shot ke liye AI image generate karo ek **consistent style prompt** ke saath:
   ```
   cinematic true-crime documentary still, dark moody lighting, desaturated
   cold color grade, film grain, 16:9, <SCENE DESCRIPTION from script>,
   no text, realistic, somber atmosphere
   ```
   `<SCENE DESCRIPTION>` = us beat ki exact scene (e.g. "a dark empty street at night in a Spanish town", "a worried mother waiting by a window", "police outside a house with tape").
3. 25-min video ≈ **100–150 images** (har shot 1). Unlimited tool se yeh easy.
4. Har image par **Ken Burns zoom + grain + vignette + cold grade** (same LUT) — yeh "glue" sab ko ek look deta hai.
5. (Optional) 10–20% real establishing clips/maps mix kar sakte ho variety ke liye, par zaroori nahi.
6. **Thumbnail bhi** usi tool se — real-photo style portrait + dark bg + red accent.

> **Fayda:** script jo bhi scene maange, woh exact ban jati hai (stock mein nahi milti), 100% copyright-free, identity auto-protected, aur har video same brand-look.

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
