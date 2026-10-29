---
name: forecast-drafting
description: Turn what a user wants to know into a professional-quality Mantic forecast and create it. Use when the user wants Mantic to forecast something new, asks to create, draft, set up or write a forecast or question, asks for a set of forecasts on a topic, or a search finds no existing forecast and they want one.
---

# Drafting a Mantic forecast

Mantic forecasts whatever it's asked, so the forecast is only as good as the
question behind it. A badly defined forecast is the main cause of numbers that
look wrong or jump around. Your job is to turn what the user wants to know
into a forecast a professional forecaster would accept: one that a competent
reader who knew the future could resolve with common sense.

Follow the `using-mantic` rules throughout. In particular, call it a forecast,
not a question, and call the resolution rules "clarifications", the word
Mantic's app uses.

Read `checklist.md` in this skill before writing any draft. It holds the rules
for each field and forecast type, the common failures and worked examples.

## 1. Pin down what the user wants

Before drafting, make sure you know:

- what decision or view the forecast will inform
- the outcome they would act on, as something observable: a date, a value, a
  winner, a yes or no

If either is unclear, ask, but at most two or three short questions in one
message. Include the type suggestion from step 3 among them when it applies.
Don't interrogate a user who has already been specific.

If the request is broad, such as "will AI take jobs?", propose splitting it
into one to five specific forecasts that together answer it, and confirm the
split before drafting.

## 2. Check what Mantic already forecasts

Call `search` with the outcome in the user's own words, and read the
`clarifications` of the closest matches.

- **One already answers it:** show it, following `using-mantic`, and offer to
  add it to a dashboard with `add_to_dashboard`. Draft a new one only
  if the user still wants their own version.
- **Close but different:** show the closest one to three in a short table,
  say in a sentence how each differs from what the user asked, then draft.
- **Nothing relevant:** say so and draft.

## 3. Choose the forecast type

Mantic's preferences, in order. Each gives a richer answer than the one it
replaces:

- **When will X happen?** (date) rather than "Will X happen by D?". A date
  forecast answers "by D?" for every date at once.
- **What will X be?** (numerical) rather than "Will X exceed Y?". The user can
  still read off the chance of exceeding Y.
- **Who or which will it be?** (categorical) rather than "Will A win?".
- **Will X happen?** (yes or no) for the outcome of a specific scheduled
  process, such as a named vote or ruling.

When a request has both a threshold and a deadline, such as "will rates fall
below 3% by summer?", choose by what the user cares about: whether and when
the line is crossed (a date forecast of the crossing), or where the value will
be at a point in time (a numerical forecast on that date).

Suggest the preferred form once, then go with what the user chooses. If they
keep "Will X by D?", draft it as yes or no with the window stated, as
`checklist.md` describes.

The API has three types: `date`, `numerical` and `categorical`. A yes or no
forecast is `categorical` with `categories` `["Yes", "No"]`.

## 4. Write the draft

Write each field following `checklist.md`:

- **`title`**: one question ending in "?" that says exactly what the
  clarifications say.
- **`supplementary_information`**: a few sentences of factual background.
  It becomes the forecast's public description, seen by every viewer and by
  the forecaster. It is not Additional context, the private context a user
  adds to refine a forecast. Don't put the user's own views, documents or
  scenarios here, and don't create copies of a forecast with different
  backgrounds to test a claim: those belong in Additional context, through
  a tool for it if you have one, or otherwise in the Mantic web app.
- **`clarifications`**: the resolution rules, complete on their own.
- **Numerical only**: `unit`, `kind`, `reporting_quantum`, `range_min`,
  `range_max`, `open_lower_bound` and `open_upper_bound`.

Check current facts, such as who holds an office or the latest figure, with a
primary or news source before using them. Other Mantic forecasts'
backgrounds are a lead, not a source: verify what you use from them, or leave
it out.

## 5. Check the draft before showing it

Run the final checks in `checklist.md`, then this test:

1. **Clairvoyance test.** Could someone who knows exactly what happens, but
   has no judgment of their own, resolve it from the title and clarifications
   alone?
2. **Four futures.** Imagine four ways the world could go: the likely case,
   an edge case, a case where it happens only partly or in an unexpected
   form, and a borderline case that only just meets or misses the criteria.
   For each, decide how the forecast resolves. If any resolves two ways or
   not at all, fix the clarifications. The bar is a competent resolver with
   common sense: cover the cases a reasonable reader could argue either
   way, and leave out far-fetched ones.
3. **First questions.** Write down the three questions a sharp forecaster
   would ask about the clarifications in the first week, such as "does a
   test sailing count?" or "which version of the figure?". Answer each in
   the clarifications. Once a forecast is created it can't be clarified,
   so these gaps have to close now.

Fix what you find. Don't refuse a reasonable request because it's imperfect:
improve it and say what you changed. The only requests to turn down are
events that have already happened or are already known, forecasts about a
private person's personal life or anyone's death, and sexual content.

## 6. Show the draft and create it only on a yes

Save it with `create_question_draft`, then show the user the draft in plain
form: title, type, the answer options or range, supplementary information and
clarifications. List any changes you made to their wording, with a sentence
on why for each.

Ask for a clear yes before calling `create_question_from_draft` with the
draft's ID in `question_draft_ids`. Once created, a forecast can't be edited
through these tools, each draft creates only one forecast, and creating it
uses the user's question quota and their credits for its first forecast run;
how many credits depends on their plan, so don't quote a figure. Revise first with `replace_question_draft`
if they want changes; it replaces the whole draft, so send every field again.
Delete a draft they no longer want with `delete_question_draft`.

After creating it, tell the user:

- the forecast's link, `https://app.mantic.com/question/{id}`
- that Mantic has started its first forecast, which usually takes a few
  minutes, and they'll get a notification when it's ready, or you can check
  with `view_question`
- that it's in their own forecasts list, and offer to add it to a dashboard

## Sets of forecasts

For several related forecasts, search for each first (step 2) and offer any
forecast Mantic already has, then confirm with the user which still need
drafting. `draft_questions` drafts several at once from the user's words, in
Mantic's own style, up to the limit its description gives; check each against
`checklist.md` and fix it with `replace_question_draft`, or write each
yourself through steps 3 to 5. Keep their wording, sources and clarifications
consistent, and vary only what should vary, such as the date or threshold.
Show them together in a short table of titles and types, and create them only
after a yes for the set. `create_question_from_draft` takes a limited number
per call, given in its description: for a larger set, offer to create that
many now and the rest in a second call. A call creates all of its drafts or
none: if it refuses, nothing was created, so fix what it names or leave those
drafts out, and call again. Once their first forecasts are ready, show the set
with one `view_questions` call on their IDs rather than `view_question` for
each.
