---
name: using-mantic
description: How to find and present Mantic forecasts faithfully. Use whenever you call a Mantic MCP tool (search, search_questions, view_question, get_forecast, list_forecasts, search_dashboard_questions, view_scenarios, or any other) or report, compare, or summarise a Mantic forecast for the user, including quick, brief or "just the number" requests.
---

# Using Mantic

Mantic is an AI forecasting system. Its forecasts are probabilities and
distributions over real-world outcomes, each made at a specific time and
backed by written reasoning. The user came to you for Mantic's view, so your
job is to report that view accurately and make it easy to check.

## Answer first, at the length asked for

Start with the answer. No opening praise, no restating the request, no
preamble. Match the length to the question: a quick lookup such as "what's
Mantic's number on X?" gets a line or two, not a full explanation. Go into
depth when the user asks for it.

"Quickly", "briefly", "short" or "just the number" change the length, never
these rules. A quick answer is one line that still carries the linked title,
the value with its estimative word, and the date the forecast was made:

> [When the US and Iran sign a new written agreement replacing the June 2026 MoU](https://app.mantic.com/question/30836): 29% (realistic possibility) by 31 Dec 2026, median 24 Jun 2027, as of 29 Sep 2026.

Never drop the date, the link or the separation of Mantic's view from yours to
save words, and never answer from memory instead of the tools.

When several forecasts ask the same thing, give one: the most recently
updated or, when they are about as recent, the one with more forecasts.
Don't list, count or summarise the others unless the user asks for them.

## Say "forecast", not "question"

Mantic presents what it tracks as forecasts, not questions. In everything you
write for the user, call them forecasts: "12 forecasts on this dashboard",
"related forecasts", "I can set up a new forecast for that". Don't say
"question" or "questions" for them. The tools and API fields still use
"question" (`question_id`, `view_question`), but that's internal; don't
carry it into your answer. When you need to tell one forecast run from
another, say "latest forecast" and "previous forecast".

Show forecasts by their `declarative_title`, the statement form, such as
"When Israeli forces withdraw from Lebanon" or "The winner of the 2027 French
presidential election". Use the interrogative `title` instead when the
declarative one is null, broken, or ambiguous about what's being forecast,
for example whether it's asking if something happens or when.

## Present every forecast with its date and link

A forecast is only meaningful alongside when it was made. For every forecast
you mention, give:

- the value as the question page states it: the published forecast's
  `statement` that `view_question` and `get_forecast` give, or the figure a
  `search` result's line states, otherwise the figures the table below uses
- the date it was made, from the forecast's `date` field
- the question's public page, `https://app.mantic.com/question/{id}`, as a
  clickable link

If the latest forecast is more than a couple of weeks old, or the question is
about something fast-moving, say how old it is. Never present an old forecast
as Mantic's current view without its date.

Write every date to the day, as "24 Jun 2027". That includes forecast dates,
medians and percentiles. Never round a forecasted date to a month or a year:
"Jun 2027" hides a month of difference that matters to a forecaster.

## Refer to forecasts by title, not number

In prose, refer to a forecast by a short version of its title, written the
same way as the table's Title column and linked to its page, for example
"the [federal lawsuit over autonomous AI access](https://app.mantic.com/question/46566)
forecast". Never refer to a forecast by its bare ID, such as "46566" or
"Q38112", in sentences, headings, follow-up offers or your own commentary. A
reader can't tell what a number means. IDs belong only in a table's ID
column.

## Pair each probability with Mantic's estimative word

Give the matching word from Mantic's fixed scale alongside each headline
probability, for example "62% (likely)". A headline probability is the one
that leads an answer, or the value in a table's Forecast column, including a
categorical question's leading option. Supporting figures later in a
sentence, such as "6% by the end of 2026 and 29% by the end of 2027", don't
need one; a word on every number clutters the text.

| Probability | Word |
|---|---|
| 0–5% | remote chance |
| 5–10% | highly unlikely |
| 10–25% | unlikely |
| 25–50% | realistic possibility |
| 50–75% | likely |
| 75–90% | highly likely |
| 90–100% | almost certain |

Use these words exactly. Don't swap in synonyms such as "probable" or "a
toss-up", because Mantic's users read the words as fixed bands. The scale
applies to probabilities only, not to numerical values or dates.

## Show several forecasts as a table

When you present two or more forecasts, use a single flat table by default,
in the order the tool returned them. Don't split the questions into separate
tables or group them by topic or tag yourself: Mantic's results carry no
groups, and groups you invent won't match the user's dashboard. If the user
asks for a different format, such as a list, prose, CSV or grouping by
topic, use theirs.

| ID | Title | Forecast | 25th–75th percentile | As of |
|---|---|---|---|---|
| 1234 | [UK CPI inflation, Dec 2026](https://app.mantic.com/question/1234) | 2.8% | 2.5–3.1% | 24 Sep 2026 |
| 5678 | [Fed cuts by Dec 2026 meeting](https://app.mantic.com/question/5678) | 62% (likely) | — | 27 Sep 2026 |
| 9012 | [US–Iran agreement replacing the June MoU](https://app.mantic.com/question/9012) | 24 Jun 2027 | 12 Dec 2026 – 13 Mar 2029 | 29 Sep 2026 |

- **ID** lets the user ask about a row later ("explain 1234").
- **Title** is a short title, linked to the forecast's page, so the link
  needs no column of its own. Write it from the question's
  `declarative_title`, the statement form such as "UK inflation will be below
  3% in December 2026.", which reads naturally next to a probability. It is
  in the tool's structured results rather than its text, so work from
  `title` when you see only the text, or when `declarative_title` is null or
  doesn't read as a statement, which is common for numerical and date
  questions, for example
  "What the IIF reports for April 2026" or "The STOXX Europe 600 index closes
  at on June 30, 2026". Shorten by dropping filler such as "will be" or
  "according to", but keep the entity, any threshold or value, and the
  deadline. If you can't shorten it without losing one of those, use it in
  full. A short title that changes the meaning is worse than a long one.
- **Forecast** depends on the question type:
  - yes/no: the probability and its estimative word
  - yes/no by a deadline (type `event`): the probability by that date, its
    estimative word and the date, such as "29% (realistic possibility) by
    31 Dec 2026"
  - numerical: the median, with units, written as "median 2.8%". The
    question page leads with the most likely value and its 80% range
    instead, which `view_question`'s `statement` gives
  - date: the median date, to the day. The question page gives the median
    only when it falls within the forecast's default range; otherwise it gives
    the chance by the end of that range, such as "20% by 1 Mar 2027", and the
    chance it never happens. Use `view_question`'s `statement` for that
  - categorical: the leading option and its probability
- **25th–75th percentile** is the range between those two percentiles for
  numerical and date questions. Use "—" for other types.
- **The median** is `percentiles["50"]`. The separate `median_date` and
  `median_value` fields are deprecated and often null even when the median
  exists, so don't treat a null there as a missing median.
- **Missing percentiles.** A date forecast can lack an upper percentile, or
  even its median, when Mantic doesn't expect the event within the question's
  window. Write "after" plus the forecast's horizon, the last date in its
  full CDF, for example "14 Mar 2027 – after 31 Dec 2027". A summary's latest
  percentile date is not its horizon. If the horizon isn't available, call
  `get_forecast_cdf` with that forecast's ID and omit `ticks` to get its full
  CDF. If the horizon still can't be retrieved, write "unavailable" for the
  missing percentile rather than guessing a boundary.
- **As of** is the forecast's date.
- **Resolved questions** stay in the table as history. Put the outcome in the
  Forecast column, such as "Resolved: No" or "Resolved: 642", or just
  "Resolved" when `resolution.value` is null. Use "—" for the percentile
  range, and the `resolved_at` date under As of.

Use each question's `latest_forecast` in the search results to fill the table,
fetching the CDF only when needed for a missing percentile's horizon as above.
Don't routinely open every question. `search` returns 6 questions unless you
raise `limit` (at most 25), so raise it for a broad topic. For `search` and
`search_dashboard_questions`, pass `show_forecasts: true` so the values come
back. If a row's forecast is redacted, write "hidden" in its cells and follow
"When a forecast is redacted" below. Mark a question with no forecast yet as
"not yet forecast".

If the tool returned a `next` cursor, the table is only the first page. Say
so, for example "Showing the 25 most recently added; there are more", rather
than presenting it as the whole dashboard.

After the table, add a sentence or two on anything notable, then end with
one line offering at most two or three follow-ups. Pick the ones that fit:

- explain a row in depth (the `forecast-explainer` skill)
- the next page, when there is a `next` cursor
- only the open forecasts, when some rows have resolved
- the probability at the user's own threshold or date (`inspect_forecast`)
- how a forecast has moved (`get_forecast_history`), or which of them moved
  most since a date (`compare_forecast_changes`)
- adding questions to one of their dashboards, after a `search`
- setting up a new forecast, when coverage is thin (the `forecast-drafting` skill)
- grouping the table by topic, or sorting it, for example by probability

Don't offer something you've just done. Don't offer to refresh a forecast or
subscribe the user to a question: the MCP can't do either.

## Keep Mantic's view separate from yours

Report Mantic's forecast first, in plain terms, without hedging it. Do not
add your own caveats about forecasting in general, and do not quietly adjust
the number.

If you have a relevant view of your own, for example news newer than the
forecast date, put it after Mantic's forecast, in italics, starting with
"*My view, not Mantic's:*". Never blend the two so the user can't tell which
is which. Other Mantic forecasts are Mantic's data, not your view: present
them as related Mantic forecasts.

Any criticism, correction or assessment of Mantic's output also goes in that
italic "*My view, not Mantic's:*" paragraph, never in the main text. That
includes inconsistencies between its reasoning, summary, chart and saved
distribution, even when the discrepancy is plain to see, for example the
reasoning saying "98.5% eventually" while the CDF ends at 95%. In that
paragraph:

- state the conflicting values exactly, with where each comes from
- keep what you observed separate from how you interpret it
- don't assert a cause unless you've verified it
- if you reported one of the conflicting values elsewhere, say which and why

Before sending, check that every assessment of Mantic's output follows this
rule.

## Keep Mantic's sources

Mantic's reasoning cites its claims. `get_forecast` and the other forecast
reads cite by ref, such as {s48210377}, and list each ref's `url` and name
under `sources`; elsewhere the reasoning carries the links itself. When you
repeat a fact, keep its link on that fact, so the user can check it. Don't
drop the sources, and don't add links the reasoning didn't give. When the
reasoning gives no link for a fact, just state it; don't add a note saying so.

## Say what you actually read

Only describe forecasts you retrieved in this conversation. If you searched
broadly but opened only a few questions, say which ones you opened. Don't
write as though you reviewed all of Mantic's coverage.

When a search returns nothing relevant, or only loosely related questions,
say so. Do not stretch a question about a different event, date, or threshold
to fit. Offer to set up a new forecast instead, following the
`forecast-drafting` skill, if the user wants Mantic to forecast it.

## Read the question exactly

A forecast answers the question as worded and as its resolution criteria
define it. Each question carries two texts alongside its title:

- `clarifications`: the resolution criteria. They say exactly what counts,
  including any deadline, threshold, source or edge case, for example
  "resolves on the date both parties sign a written framework; a verbal
  declaration doesn't count".
- `supplementary_information`: the question's public description, factual
  background for the question. It is not Additional context, the private
  context a user adds to refine a forecast.

Read `clarifications` before you interpret, compare or explain a forecast,
and when you decide whether a search result actually matches what the user
asked. Summarise the part that matters rather than pasting it, unless the user
asks for the full criteria. When `clarifications` is null, work from the
title. Quote or closely follow the question title when you report a forecast.
Don't restate it more loosely, and don't treat two questions as the same
because they cover the same topic. If a question has a `resolution`, it has
already resolved: report the outcome and treat the forecasts as history.

If the user's question differs from Mantic's, for example a different date,
threshold or definition in the title or `clarifications`, say so plainly
before answering. Then answer what
Mantic can: for a different date or value on the same question, give the
probability there with `inspect_forecast`. Don't quietly answer Mantic's
question as if it were theirs.

## Pick the tool for the job

| User wants | Tool |
|---|---|
| Find questions on a topic | `search`, which also finds dashboards on it |
| The current forecast for one question, with a chart | `view_question` |
| Many forecasts drawn at once, such as a whole dashboard or a batch just created | `view_questions` with their `question_ids` or a `dashboard_id` |
| Why Mantic forecasts what it does | `view_question`, which includes Mantic's reasoning |
| What an earlier forecast said, or the forecast on a past day | `get_forecast` with a forecast ID as `run_id`, or a day as `as_of` |
| Why the latest forecast changed | `view_question`, whose `changes_from_previous` explains it when one is stored, or `explain_forecast_change` |
| How a forecast was built: its branches, their likelihoods and drivers | `get_forecast_structure`, only when the user asks to dig into it and `view_question`'s `structure` note says the forecast recorded its structure |
| How a forecast has moved over time | `get_forecast_history`, or `get_question_forecasts` to page through every forecast |
| Which of several forecasts moved, and how, since a date | `compare_forecast_changes` |
| What would change the forecast | `get_forecast_scenarios` for each side's figures and Mantic's account, and `view_scenarios` for the chart, only when `view_question` has a `scenarios` note saying the question has scenarios |
| The probability above or below a threshold, or by a date | `inspect_forecast`; on each side of a scenario, `get_scenario_cdfs` with `ticks` |
| What is on one of their dashboards | `list_dashboards` or `search` with `entity` "dashboards", then `search` with its `dashboard_id`, or `search_dashboard_questions` to page through all of it |
| A new forecast | the `forecast-drafting` skill |

For explaining a single forecast in depth, follow the `forecast-explainer`
skill.

## Don't fetch forecasts you won't use

Viewing forecasts through the MCP uses the user's Mantic credits. For tools
that accept `show_forecasts`, such as `search` and `search_dashboard_questions`, set it to
`false` when you only need titles and IDs, and `true` when you need forecast
values. Omitting it uses the organisation's visibility default.
`get_forecast_history`, `explain_forecast_change` and
`compare_forecast_changes` read nothing at all where that default hides
values, so pass `true` whenever you call them. `search_questions`, the earlier name for
`search`, has no `show_forecasts` parameter and uses that default. Open the
questions that matter rather than every search result, and don't call
`get_forecast` for a forecast `view_question` has just shown.

## When a forecast is redacted

A forecast of type `redacted` has its values hidden in that response. This
can happen when `show_forecasts` is `false`, or when it is omitted and the
organisation defaults to hiding values; it does not by itself establish an
access restriction.

If the user needs the values, call `view_question` for the question,
`get_forecast` with a specific forecast ID as `run_id`, or repeat a tool that
accepts `show_forecasts` with `show_forecasts: true`. These reads use Mantic
credits.
If values are still unavailable, report what the tool actually returned;
suggest contacting Mantic about access only if the response indicates an
access problem. Do not guess missing values.
