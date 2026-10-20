# Forecast drafting checklist

The rules behind a professional-quality forecast, drawn from Mantic's own
question standards, Metaculus's question-writing guidance, and the
resolution disputes in recent Metaculus Cup, Quarterly Cup, ACX and
Bridgewater tournaments.

## Title

- One question, ending in "?". No "What's the probability that…".
- Name specific entities: "Germany", not "any European country"; "Apple", not
  "a big tech company".
- One trigger. No "and" between two steps ("agreed and in force") and no "or"
  between outcomes. Split them into separate forecasts.
- Absolute dates ("31 December 2026"), never relative ones ("in the next
  five years", "this year"). Never write "the resolution date".
- No negatives: "When will X happen?", not "Will X not happen?".
- Units for any value: "in nominal USD", "12-month rate, %".
- For date forecasts, no cut-off in the title. "When will the ECB next cut
  rates?" already covers every date.
- The title promises exactly what the clarifications deliver, no more and no
  less.

## Supplementary information

- A few sentences of factual background a forecaster would want: the current
  state, the latest figure, what's scheduled.
- Verified facts only, written neutrally. No advice, no opinion, and no
  instructions to the forecaster.
- Public and part of the forecast itself. It is not Additional context:
  the user's private context, documents or what-if claims belong in
  Additional context, not here.

## Clarifications

They must settle the forecast on their own, without the title or background.

- **What counts.** Necessary and sufficient conditions, in plain words.
- **What doesn't count.** List the two or three near misses a reasonable
  reader might count, such as "a verbal announcement does not count" or "a
  pause of under 7 days does not count".
- **Which stage counts.** Announced, signed, passed, in force or completed.
  Prefer a substantive step over an announcement.
- **Vague words get numbers.** Replace "major", "significant", "large" or
  "properly" with a threshold: "a deal worth over $1bn", "a 7-day average of
  at least 60 transits". Add a minimum duration where a brief blip could
  otherwise count.
- **Contested terms get defined.** Does "electric vehicle" include plug-in
  hybrids? Does "launch" mean announced or on sale?
- **Outcome, not route.** Describe the state of the world, not one way of
  reaching it: "becomes law", not "is signed by the Governor". Say which
  actors count, such as subsidiaries, government agencies other than the
  armed forces, or a company acquired to get there, and whether a renamed
  entity or product still counts.
- **What proves it.** Name the public record that shows it happened, such as
  a joint statement, a gazette entry or a court order, not a legal step
  nobody outside can see. Say whether one party's own claim is enough; where
  the party controls the fact or gains from it, prefer an independent
  record. Resolve only on positive confirmation, never on "no credible
  source reports otherwise".
- **Source of record.** Name the publisher or record that settles it, such as
  a statistics agency, a court docket or an official gazette. Where no
  single record exists, say which kinds of reporting count.
  - Prefer free sources: Mantic has to be able to read the source to
    resolve the forecast. Use a paywalled one only if the user asks for it,
    and tell them it may not resolve automatically.
  - Check that the source really publishes this figure and how often it
    updates.
  - For a page that changes during the day, name the exact view (the table,
    the chart or the download) and when it's read: "as shown at 17:00 UK
    time on 30 June 2027".
  - Give the fallback a concrete trigger, such as "if the ONS has published
    nothing for 21 days", and say what replaces a value that is clearly
    wrong, such as one far outside every other source.
  - For benchmarks and leaderboards, say which entry or variant counts and
    what happens if the method or version changes.
- **Revisions.** For any figure that gets revised, including trackers and
  counts, not only official statistics, say whether the first published
  figure or a later one counts. Only ask for first-published figures from a
  source that keeps its earlier releases; otherwise use the figure as
  published on the day it resolves.
- **Only after today.** Events before today don't count: write "after
  [today's date]" or "the next…". For a count that has already started
  accumulating, count only from today or ask about "the rest of 2026".
- **Missing figures.** For a value on a date, say which figure counts if the
  source publishes nothing that day, such as the last close before it.
- **Time zone** wherever a day boundary matters, and "before 1 January 2027"
  rather than "by the end of 2026".
- **Edges of the window.** Say whether a minimum duration must be complete
  inside the window or only start in it. For dated publications such as
  weekly charts, say whether the publication date or the date printed on
  it counts.
- **One-offs and partial cases.** Say whether a pilot, a test, a single
  instance or a partial step counts, ideally with a minimum: "at least 5
  commercial sailings within 30 days".
- **Scope.** Say who and where counts. If the group's members could change
  before the forecast resolves, say which date's list counts: "EU member
  states as of 1 January 2027", "companies in the S&P 500 on the day it
  resolves".
- **Totals and groups.** For a figure across members or parts, say how an
  opt-out, an exemption or a split target is treated. For an average over
  days, say what happens if some days are missing.
- **Borderline examples.** For a term that's easy to argue about, one or two
  short examples of what counts and what doesn't settle it faster than a
  longer definition.
- **Every outcome has a rule.** For yes or no and categorical forecasts, say
  what makes each outcome happen.
- **No instructions to the forecaster** ("include a prediction for each
  date", "only consider…"). Clarifications describe the world, not the task.
- **No annulment or "resolves ambiguous" clauses.** Give every case a rule
  instead.
- **Keep them tight.** Short paragraphs or bullets. The detail goes here,
  not in the title, but add a rule only when it settles something a reader
  could otherwise get wrong.

## By forecast type

### Date ("When will X?")

- One discrete event, with a rule that makes the calendar day unambiguous:
  "the date the law is published in the official gazette", "the first day
  the 7-day average is at or above 50".
- Use the date the event happened, as the source of record dates it, not the
  date news coverage appears.
- No upper bound and no "if it hasn't happened by D, resolves…" clause.
  Mantic handles the event not happening within its range.
- For "how long will X last?", ask "When will X end?".

### Numerical ("What will X be?")

- Ask "What will…", "How much…" or "How many…", with the measurement date
  and source: "What will the UK CPI 12-month rate be for December 2026, as
  first published by the ONS?".
- `unit`: always set it, such as "%", "USD bn", "people".
- `kind`: `discrete` for counts and administered steps (seats, a policy rate
  set in 0.25 points); `continuous` for measurements, even if published
  rounded.
- `reporting_quantum`: the step the source publishes in: 1 for a count, 0.25
  for a policy rate, 0.1 for a CPI rate published to one decimal place. Watch
  unit multipliers: a count reported in thousands to one decimal place has a
  step of 0.1. Leave it out only for a figure you'd compute yourself, such as
  an average of several releases.
- `discrete` always needs a `reporting_quantum`, or creation fails.
- `range_min` and `range_max`: wide enough that the real value is very
  unlikely to fall outside, but no wider, using natural round numbers and
  natural limits such as 0 for a count. For a volatile series, such as a
  price or a monthly change, size the range from its largest past moves
  over a similar period, not from today's value. With a step set, both ends must be
  values the source could publish, a whole number of steps apart, or creation
  fails. Keep the range to 400 steps or fewer, or the step is ignored.
- Open bounds: set `open_lower_bound` and `open_upper_bound` to `true` unless
  a value beyond the bound is impossible, such as below 0 for a count or
  above 100 for a percentage share. When in doubt, open: an outcome outside a
  closed bound voids the forecast, and the API defaults both to closed.
- A count whose likeliest value is zero is a yes or no forecast in disguise.
  Ask whether, or when, it happens instead.

### Categorical ("Who or which will it be?")

- Options are mutually exclusive and cover every possibility: exactly one
  can resolve. The API doesn't check this, so you must.
- Add a closing option, such as "Someone else" or "No decision before 1
  January 2027", unless the listed options are truly exhaustive.
- Rule on the edges you can foresee: a tie, a runoff, a withdrawal, a
  postponement.
- The title doesn't name a favourite: "Who will win the 2027 French
  presidential election?", not "Will X win…?".
- If several options could all happen, such as which countries a leader
  visits, ask which happens first.
- No time ranges as options. That's a date forecast.
- Between 2 and about 10 options, with no duplicates.

### Yes or no

- For a specific scheduled process: "Will the Senate confirm X?", "Will the
  court rule for Y?".
- Also when the user keeps a deadline after you've suggested a date
  forecast. Then the clarifications state the window, "after [today] and
  before [D], [time zone]", and say that No means it did not happen in that
  window.
- `categories` exactly `["Yes", "No"]`.

## Common failures

- **Spurious resolution.** The wording is met but the intent isn't, such as
  an accidental collision resolving a "military conflict" forecast. Close it
  off with "does not count" rules.
- **Proxy drift.** A clear forecast that tracks the wrong thing. Check it
  measures what the user actually cares about.
- **Already known or certain.** The event has happened, or the threshold is
  set so the answer is obvious. Check pending decisions and earlier claims
  too: a ruling due next week, or a past announcement that already meets
  the wording. Aim for a genuinely uncertain forecast.
- **Easy to move.** It resolves on something one participant can shift,
  such as a thin prediction market, a single poll or a social media count.
- **Deadline bias.** "Will the agency decide by D?" almost always resolves
  No because institutions slip. A date forecast avoids this.
- **Unobservable.** Resolving needs private data, many sources, or a
  paywall. Mantic has thin data on topics such as house prices and social
  media activity, so warn the user before drafting one.
- **Self-referential.** Depends on Mantic, the user or the forecast itself.

## Worked examples

These show the transformation. They are illustrations, not real Mantic
forecasts.

**Threshold to value.** "Will EV sales pass 25% of new cars in the EU next
year?" becomes "What will battery-electric cars' share of new car
registrations in the EU be for 2027, as first reported by ACEA?", numerical,
`unit` "%", `kind` continuous, `reporting_quantum` 0.1, range 10 to 40, both
bounds open. Clarifications say battery-electric only, so plug-in hybrids
don't count. The user can still read off the chance of passing 25%.

**Deadline to date.** "Will the UK pass a universal basic income law by
2030?" becomes "When will an Act of the UK Parliament establishing a
universal basic income receive Royal Assent?", date. Clarifications: Royal
Assent counts even if payments start later; the scheme must cover at least
90% of adult residents and pay at least £5,000 a year; pilots, trials,
means-tested schemes and legislation from the devolved parliaments don't
count.

**Winner, not favourite.** "Will Lagarde stay on at the ECB?" becomes "Who
will be the next President of the European Central Bank?", categorical, with
the leading candidates plus "Someone else". Clarifications: the person
formally appointed by the European Council counts, not a nominee; an acting
president doesn't count.

**Stage that counts.** For a central bank decision: "the date the decision is
announced counts, not the date it takes effect".

## Final checks

The most often missed. Confirm each before showing the draft:

1. The title and clarifications describe exactly the same outcome.
2. The clarifications say what doesn't count.
3. Only events, or counts, after today count, and every date is after today
   and in the right year.
4. Every outcome has a rule.
5. No two clarifications contradict each other.
6. The source publishes the figure where the clarifications say.
7. Numerical: unit, kind and step consistent with the range, and open bounds
   unless impossible.
