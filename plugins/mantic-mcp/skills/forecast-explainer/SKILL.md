---
name: forecast-explainer
description: Explain one Mantic forecast in depth - what Mantic predicts, why, how the forecast has moved, and what would change it. Use when the user asks why Mantic forecasts something, wants a forecast explained or broken down, asks what is driving or would move a forecast, asks how a Mantic forecast has changed over time, or asks why a forecast hasn't changed after some news.
---

# Explaining a Mantic forecast

Use this when the user wants to understand a single forecast, not just see
its value. Follow the `using-mantic` rules throughout: give dates and links,
and keep Mantic's view separate from yours.

## 1. Find the question

If the user gave a question ID or a `app.mantic.com/question/{id}` link, use
that. Otherwise call `search` with their topic. If several questions
fit, list the closest two or three with links and ask which one they mean.
Don't pick one silently.

## 2. Get the current forecast

Call `view_question`. It gives the question, the latest published forecast
and Mantic's reasoning. Note
the forecast's `statement`, when it was made, the exact wording of the
question and its `clarifications` (the resolution criteria), including any
threshold or deadline they state. The rest of the explanation depends on
exactly what is being forecast.

Only treat a date as the question's deadline when the title or
`clarifications` state it. Ignore any deadline field in the chart data that
the question's text doesn't mention.

`view_question` states the forecast as its page does: for numerical and date
questions its percentiles, ranges and chances by date. Take every probability
you state from those figures. For a date or value they don't list, call
`inspect_forecast`: one call per kind of figure (chances by date, chances
between values, or percentiles), asking for every figure of that kind. Never
estimate a probability from the chart or state one no tool returned.

A date forecast's CDF stops at its horizon, the last date it lists. The
probability there is the chance by that date, not the chance it ever happens.
Say "by" and the horizon date, not "eventually".

## 3. Read the reasoning

The reasoning in `view_question`'s text is Mantic's written report:
historical context, headwinds, tailwinds, key figures, uncertainties and a
conclusion. Call `get_forecast` only for an earlier forecast (`run_id`) or a
past day (`as_of`).

Summarise the reasoning. Don't paste it. Pull out:

- at most three factors that carry the most weight, including any base rate
  or historical comparison it leans on
- the main uncertainty: the first item in the reasoning's key uncertainties,
  not a headwind or a point you judge more important

Attribute these to Mantic ("Mantic's reasoning points to..."). Every fact you
attribute to Mantic, including names, dates, figures and events, must appear
in the `reasoning` text. Don't add facts from your own knowledge under
Mantic's name. If the report doesn't cover something the user asks about, say
so rather than filling the gap yourself.

### When the forecast recorded its structure

Don't fetch the structure for a first explanation. Call
`get_forecast_structure` with the question ID only when the user asks to dig
deeper (how the forecast was built, which branches it weighs, how likely each
is, or what drives it) and `view_question`'s `structure` note says the
forecast recorded its structure. For each sample it gives a `caption` walking through the tree, then
`layers` of `branches` with each one's `chance`, where it lands and why it is
in the forecast, and the `inputs` that drive the spread. Read the `caption`
first. Answer with the two or three largest branches, their chances and where
each lands, and the input that drives the most spread.

- A branch's `chance` is of its whole sample, not of the branch above it. A
  nested branch also gives `chance_within_parent`.
- The forecast pools its samples by `weight`. If the samples disagree, say
  so rather than averaging them yourself.
- Quote figures only as the structure states them. Never compute a new
  probability or value from it.
- If `omitted` lists anything, `read_the_rest` names the call that reads a sample whole: make it
  when the answer depends on what was left out.

If the user asks to dig deeper and the note says the forecast recorded no
structure, explain it from the `reasoning` alone and present no branches,
branch chances or drivers as Mantic's.

## 4. Show how it has moved

Call `get_forecast_history` for the question with `show_forecasts: true`.
Retrieving these values uses the user's Mantic credits; without the flag, an
organisation that hides forecasts by default gets nothing back. It lists the
newest forecasts (10 unless you raise `limit`, at most 25), each with its
figure as the question page states it and `what_changed` in one line, and,
where Mantic has split the history into regimes, the spells in which the
forecast held at one level. Call them regimes, never phases or periods.

If there is only one forecast, say it is Mantic's first and move on.

When there are more, say which way it is trending: where it started, where it
is now, and any sharp change, with dates. Use each forecast's figure as the
history states it. The oldest regime says where the forecast started, unless
the history reports `regimes_shown`, which means older regimes were left out;
then, or without regimes, say how far back you looked.

Then say why, from Mantic's own explanation: each forecast's `what_changed`,
the regimes' headlines, and `view_question`'s `changes_from_previous` for the
latest forecast. For the biggest change, call `explain_forecast_change` with
that forecast's `forecast_id` as `run_id`, or a regime's `first_forecast_id`
for the step into it. It returns Mantic's account of what changed since the
forecast before, or a `note` saying why there is none. When none of these
explains it, call `get_forecast` with the forecast just before it as `run_id`,
then the one just
after, and compare their reasoning: what does the later one cite that the
earlier one didn't, or weigh differently? A missing account means none is
stored, not that nothing changed. Attribute the explanation to
Mantic, keep its source links, and if neither explains the change, say so
rather than guessing. Keep this to two or three sentences, unless the user asked
about the history specifically, in which case cover each notable change.

### When a forecast didn't move after big news

If the user asks why a forecast hasn't changed after a significant event,
or you know of one, check the dates first. `get_forecast_signals` lists what
Mantic has weighed on the forecast lately and what came of each item,
including news that didn't move it:

- **No forecast since the event.** If the latest forecast predates the event,
  Mantic hasn't re-forecast the question yet. Say so plainly: the forecast
  doesn't reflect the event, and it isn't evidence that the event doesn't
  matter. Offer to refresh it, and call `refresh_forecast` only after the
  user's yes.
- **Forecasts since the event, little movement.** Call `get_forecast` with the
  first forecast after the event as `run_id` and look for the event in its
  reasoning. If
  it's there, explain why Mantic judged it didn't shift the outcome much, for
  example because it was already expected, or because it doesn't bear on
  what resolves the question. If the reasoning doesn't mention the event, say
  that, rather than inventing Mantic's view of it.

Describing the event itself, if it came from you rather than Mantic, belongs
under your view, in italics. So does any judgement of how the event bears on
the forecast or its resolution that Mantic's reasoning doesn't make, even when
the user told you about the event.

## 5. Show what would change it

When `view_question` has a `scenarios` note saying the question has
scenarios, call `get_forecast_scenarios`, and `view_scenarios` to draw them. Each scenario is
a related event, its chance, and where Mantic's forecast lands if that event
happens and if it doesn't, with Mantic's `why` for each side. Report the one
or two scenarios that move the forecast most, saying which figure moves:
`default` is the forecast's own figure of the same kind, which may not be its
headline.

If the user asks about a specific threshold under a scenario, call
`get_scenario_cdfs` with `ticks`. Without a `scenarios` note, skip this step
without calling either tool. If the question has no scenarios, leave the
section out of the explanation; don't mention that there are none.

State that scenario outcomes are Mantic's conditional estimates, not events
that have happened.

## 6. Find related questions

Call `search` with the question's topic, in a few words rather than
its full title. From the results, pick up to three other questions that bear
directly on this one: a narrower or broader version, an upstream event, or
the same event on a different timeline. Skip loosely related ones. If none
fit, leave the section out. Use the latest forecasts in the search results;
follow `using-mantic` to retrieve a missing date percentile's horizon when
needed.

## 7. Write the explanation

Keep it short enough to read in a minute:

1. **The forecast.** A short summary list, one bold label per bullet, for
   example:

   - **Title:** [When the US and Iran sign a new written agreement replacing the June 2026 Memorandum of Understanding](https://app.mantic.com/question/30836)
   - **Chance by 31 Dec 2026:** 29% (realistic possibility)
   - **Median:** 24 Jun 2027
   - **25th–75th percentile:** 12 Dec 2026 – 13 Mar 2029
   - **As of:** 29 Sep 2026 (1 day old)

   Then a small table comparing it with the previous forecast:

   | | Made on | Chance by 31 Dec 2026 | Median | 25th–75th percentile |
   |---|---|---|---|---|
   | Latest | 29 Sep 2026 | 29% | 24 Jun 2027 | 12 Dec 2026 – 13 Mar 2029 |
   | Previous | 28 Sep 2026 | 29% | 19 Jun 2027 | 15 Dec 2026 – 12 May 2028 |
   | Change | 1 day apart | unchanged | 5 days later | upper end 10 months later |

   - **Title** is the full `declarative_title`, linked to the forecast's
     page, falling back to `title` as `using-mantic` describes. The summary
     has room for it, unlike a table, so don't shorten it. Never use a bare
     "forecast page" link.
   - The value lines depend on the question type:
     - yes/no: **Probability**, with its estimative word
     - date: **Chance by deadline** when the title or `clarifications`
       state one, otherwise **Chance by** the end of a meaningful year;
       then **Median** and **25th–75th percentile**
     - numerical: **Median** and **25th–75th percentile**, with units
     - categorical: **Leading options**, the top two or three with their
       probabilities
   - The comparison table's **Previous** row is the forecast made just
     before the latest one, as `get_forecast_history` lists it. Its columns
     are the date each forecast was made plus the same headline figures as
     the summary list. The **Change** row says how each figure moved in plain
     words, such as "up 4 points", "median 5 days earlier" or "unchanged".
     For a figure the history doesn't state, such as a percentile or a
     probability by the same date, call `inspect_forecast` with the previous
     forecast's `forecast_id` as `run_id`, one call per kind of figure, so
     the two rows compare like with like. If the latest forecast is
     Mantic's first, skip the table and say so in one line.
   - For a missing percentile on a date question, write "after" plus the
     forecast's horizon, the last date in its CDF, as in the example above.
     If the CDF is unavailable, follow `using-mantic` to fetch it or report
     the missing percentile as "unavailable".
     Don't add a mean: Mantic's forecasts don't include one.

   After the block, you may add one line of supporting figures, such as
   year-end probabilities or the chance by the horizon. Add nothing else,
   including comments of your own on the forecast.
2. **Why.** At most three bullets from the reasoning, keeping its source
   links on the facts you use. A base rate or historical comparison goes in
   one of the three, not after them. When the forecast recorded its
   structure, lead with its largest branches and their shares instead.
3. **Main uncertainty.** One sentence on the uncertainty Mantic lists first,
   plus at most one line listing any others. Where it turns on what counts
   for resolution, say what the `clarifications` require.
4. **How it has moved.** Which way it is trending and why, in two or three
   sentences, or more if the user asked about the history. If it hasn't moved
   despite big news, say whether that's because there's been no forecast
   since, or what Mantic's reasoning says about the event.
5. **What would change it.** The top scenarios, with both sides. Leave
   this section out when the question has no scenarios.
6. **Related Mantic forecasts, if any.** The questions from step 6, each by
   short linked title with its own forecast and date, and a few words on how
   it relates, such as "narrower: charges against a developer only". Give
   each forecast the way the `using-mantic` table does, including its rules
   for missing date percentiles and retrieving the actual horizon. These are
   Mantic's data, so don't put them under your view.
7. **Your view, if any.** In italics, starting "*My view, not Mantic's:*",
   for something from outside Mantic that the forecast doesn't reflect, such
   as news after its date, and for any criticism of Mantic's output or
   inconsistency in it, following the `using-mantic` rules for stating it.

Write only these sections, in this order, with nothing between them. The
one exception: if the user also asked a direct question, such as whether a
particular event would count, answer it in one or two sentences before the
summary, from the `clarifications` where it's about resolution. When
the user asked how the forecast has changed, move **How it has moved**
straight after the summary, and cut **Why** to one or two sentences on the
current forecast, so the same points don't appear twice.

End with one line offering the obvious next step: the probability at the
user's own date or value, a comparison with a related forecast (by title), or
adding the forecast to one of their dashboards.
