# Question rules

<!-- Generated from core.constitution by scripts/render_forecast_drafting_constitution.py.
     Do not edit. After a change to core/core/constitution/, regenerate with:
     uv run python scripts/render_forecast_drafting_constitution.py -->

These are the rules a question must meet, cited by ID. checklist.md says what to
apply them to.

# Questions

What a question is. The other documents apply this to output types, writing, forecasting
and resolving. Where another document seems to disagree with this one, this one wins.

These rules cover a question that resolves to one value, and a joint question that
resolves to one value for each dimension. A question that resolves to a distribution of
observations, and a time series, are not covered.

## Terms

Each term has one meaning throughout.

- **Question**: a request for one fact about the world that is not yet known and will
  later be settled by a public record.
- **Title**: Short, self-contained question title, at most one sentence.
- **Context**: Relevant factual background that helps understand the question: the entities involved, the current situation, and recent events.
- **Resolution criteria**: Operational rule for what observable outcome or value resolves the question, and its source.
- **Output type**: The kind of value a question resolves to, which fixes the shape of its outcome.
- **Outcome**: The question's authored outcome space.
- **Resolving value**: the one value in the outcome that the question resolves to.
- **`as_of`**: The time the question is asked as of; only facts available at or before it are known.
- **Current time**: the `as_of` of the forecast or resolution being made, as it is shown
  to whoever makes it. They treat it as the present. It can be later than the question's
  `as_of`.
- **Qualifying window**: the span of time in which an event must occur to count. It
  opens at the time the resolution criteria state. Where they state none, it opens at
  the question's `as_of`. An event before it opens does not count. A **qualifying
  event** is one that meets the criteria inside the window. The expected resolution time
  and a market's listing times do not set the window.
- **Deadline**: the time the qualifying window closes.
- **Period**: the span of time a value refers to: May 2026, the 2026 fiscal year.
- **Release**: one publication of a figure for a period. The **first release** is the
  first publication of the complete figure, a flash or advance estimate included. A
  **revision** is a later release for the same period. Partial counts and projections
  are not releases. Where the criteria name no release, the first release counts.
- **Premise**: what the resolution criteria take for granted, apart from the event or
  value the question asks about: that the election will be held, that the figure will be
  published, that the source will exist.
- **Fallback**: what the resolution criteria say resolves the question when their first
  rule cannot be applied.
- **Credible source**: a journalistic or academic publication, a body with authority over
  or direct knowledge of the subject, or any source the weight of evidence shows to be
  correct on the point. A claim whose correctness is in significant dispute is not one,
  and nor is an unsourced claim on a blog, social media or a personal site.
- **Forecast**: a probability distribution over the outcome, made at a current time.
- **Generated question**: one written by Mantic's own pipelines or agents, including an
  agent drafting in the app. An **app question** is written by a user. An **external
  question** comes from a competition, market or other source Mantic does not control. A
  rule marked [generated] binds generated questions only.

## Rules

- **Q1. One contract.** The title, the resolution criteria, the outcome and the question's `as_of` are the
  contract, read together and literally. Nothing else decides a resolution: not the
  context, a source link or an internal note. Where the contract contradicts itself on a
  point that decides the resolving value, the question annuls.
- **Q2. A valid question.** A valid question is:

  - **Open**: its resolving value is not known at its `as_of`.
  - **Objective**: it resolves to a fact that happens or is published. Never to a
    probability, a forecast or an opinion, and never to something a person with a stake in
    the forecast decides.
  - **Measurable**: that fact is one defined event, date, quantity or option.
  - **Resolvable**: a source the resolver can read will state it. The criteria promise
    nothing more.
  - **Time-bound**: it states when it is decided: a period, a deadline, or for a date
    question the range.
  - **Unambiguous**: two careful readers, working independently, would resolve it to the
    same value, and would take a forecast on it to mean the same thing.
  - **Coherent**: its title, resolution criteria and outcome ask the same thing.
  - **Complete**: it states everything needed to resolve it, for every case with a real
    chance of occurring.
- **Q3. Annul, do not distort.** When a question's premise fails and no stated fallback applies, the question is
  annulled. It is never resolved to a substitute. A figure that was never published is not
  zero. An event that never occurred did not occur on the last day of the range. Annulment
  is normal.

  The event a binary or date question asks about is not a premise. Where it does not
  occur, the question resolves as the rules for its output type say.
- **Q4. An external question is its source's.** The constitution governs generated and app questions. An external question is taken as
  its source wrote it and may break these rules: they apply to it as far as it allows.
  The source's rules, fine print and official clarifications, as published at the current
  time, are part of its resolution criteria. Where the source has resolved or annulled the
  question, that stands over any other reading.

# Output types

What each output type means and how its outcome behaves. These definitions bind writers,
forecasters and resolvers alike.

## Choosing the output type

- **T1.** When one event occurs: **date**.
- **T2.** How large a value is at a stated time or for a period: **numerical**.
- **T3.** How many times something occurs in a window: **numerical**, discrete.
- **T4.** Which of several things occurs: **categorical**.
- **T5.** The result of one process that has exactly two results: **binary**.
- **T6.** A scheduled event can still be a date question, because a schedule is not a guarantee.
  Where its timing is not really uncertain, ask about its result.

## Times

- **T7.** Times are as exact as the source allows and carry their timezone. Where the source gives
  none, UTC. An `as_of` or an event known only to the day is recorded as 00:00 UTC on that
  day. A deadline given with a time includes that instant unless the criteria say
  otherwise. A deadline given only as a date covers the whole day, in the criteria's
  timezone, or in UTC where they name none: up to but not including the following
  midnight.

## Binary

The resolving value is Yes or No.

- **T8.** The question resolves to Yes or No.
- **T9.** A binary question asks one of two things. Whether an event occurs by the deadline (a
  first event): Yes as soon as a qualifying event occurs, whatever follows, and No once
  the deadline passes without one. Or whether something is true at, or throughout, a
  stated time: Yes or No on what is true then, whatever occurred before. Where the
  criteria do not say which, it is a first event.
- **T10.** Where the event asked about is cancelled or never occurs, the question resolves to No.
  Where a premise fails, it annuls (Q3).

## Categorical

The resolving value is one of several mutually exclusive named options.

- `options`: Mutually exclusive, collectively exhaustive named options with names unique ignoring case; include Other when the named options are not exhaustive.

- **T11.** A categorical question has at least 3 options.
- **T12.** The question resolves to exactly one option, and the resolution criteria resolve it to
  nothing else. A resolving value that is not a named option resolves to the Other option
  where there is one. Otherwise the question annuls.
- **T13.** An option is listed only when it is worth forecasting separately. Combinations of
  independent conditions are not options. Two paths to the same final state are one
  option. Other covers only what the named options do not.
- **T14.** An option meaning that none of the others occurred is a real value, not a fallback.

## Numerical

The resolving value is a number, with a unit and a range.

- `unit`: Unit of the resolving value, or 'dimensionless' when none applies.
- `reporting_quantum`: Smallest interval between consecutive values the source can report.
- `kind`: Whether the underlying quantity is continuous or intrinsically discrete. `continuous`:
  The underlying quantity is continuous, even when reported rounded. `discrete`:
  The underlying quantity lies on an intrinsic lattice, such as a count.
- `range_min`: Lowest in-range resolving value.
- `range_max`: Highest in-range resolving value.
- `open_lower_bound`: Whether values below range_min may resolve. False makes range_min an inclusive resolution floor.
- `open_upper_bound`: Whether values above range_max may resolve. False makes range_max an inclusive resolution ceiling.

- **T15.** The resolving value is one number: a value at a stated time, or for one stated period. A
  statistic over many observations is one number when it is named exactly.
- **T16. Unit.** The multiplier and the rate period are part of the unit: "thousands of people", "% year
  on year".
- **T17. Reporting quantum.** It is the increment the source states, or where the source states none, the increment
  inferred from the series history. It is never guessed. A continuous quantity that its
  source rounds still has one. A calculated value is rounded once, at the end, to the
  reporting quantum; a value exactly halfway between two reported values rounds away from zero.
  Without a reporting quantum it is not rounded.
- **T29.** A question on a linear scale declares a reporting quantum where its source publishes the
  resolving value at a fixed increment, and none where the resolving value is an unrounded
  calculation or average.
- **T18. Range.** `range_min` to `range_max` cover about the 1st to the 99th percentile of plausible
  values at the question's `as_of`. They do not cover every possible value.
- **T19. Open bound.** A bound is open unless T20 closes it. A resolving value beyond an open bound is possible
  and resolves the question.
- **T20. Closed bound.** A bound is closed only where the definition of the quantity or arithmetic makes a value
  beyond it impossible: a count below 0, a share above 100%. A bound is never closed because
  values beyond it look unlikely. Where the resolving value is beyond a closed bound, the
  question annuls.
- **T21. Scale.** Linear by default. A logarithmic scale is for a continuous quantity that spans orders of
  magnitude, never for a discrete one.
- **T22.** A missing value is never a number. Absence, a cancelled release or an event that did not
  occur is not 0, unless the quantity is a count that is truly zero when nothing occurs.
  Where the resolving value is missing and no stated fallback applies, the question
  annuls (Q3).

## Date

The resolving value is a date or timestamp.

- `range_min`: UTC-grid start of the earliest admissible scoring period, inclusive.
- `range_max`: Exclusive end of the authored forecast horizon, in UTC.
- `open_upper_bound`: Whether dates at or after the exclusive range_max may resolve.
- `precision`: UTC calendar granularity of the authored date scoring grid; range_max is aligned to the first instant after its final scored period.

- **T23.** The resolving value is when one discrete event first occurs in the qualifying window.
  The first time a value crosses a threshold is such an event. A date question is not used
  for a value observed over time, a peak or low, a duration, a streak, a state that can
  reverse without one decisive transition, or conditions that can become true at different
  times.
- **T24. Lower bound.** Always closed. The range starts with the calendar period in which the qualifying window
  opens. An occurrence before the window opens does not annul the question.
- **T25. Open upper bound.** The default. The range then covers the dates on which the event plausibly occurs, as
  judged at the question's `as_of`, not every possible date: `range_max` is not a deadline.
  An event at or after it, and an event that never occurs, both resolve the question
  beyond the open upper bound.
- **T26. Closed upper bound.** Used only when the event must occur inside the range: the question limits itself to a
  stated period. If the event does not occur before `range_max`, the question annuls.
- **T27.** The title of a date question on an open upper bound contains no deadline and no
  `range_max`.

## Joint

- **T28.** The resolving value is one number for each named dimension, under one constraint. A joint question resolves to one value for each
  dimension. Every numerical rule applies to each dimension.

# Writing questions

How to write a question. Rules numbered Q are in Questions and T in Output types.

## How these rules apply

- **Generated**: every rule applies in full. A breach blocks the question.
- **App**: the user chooses the output type and the wording. A better form is offered,
  never imposed. Every other rule applies, and a breach is reported to the user. No rule
  here blocks a question a user wrote; the core models' own validation still applies.
- **External**: the question is never rejected or rewritten for its form (Q4). The rules
  are used to interpret it. Converting it follows W27 to W29.

## What to ask

- **W1. Uncertain.** The resolving value is in real doubt at the question's `as_of`: more than one value has
  a real chance of occurring.
- **W31. Relevant.** Knowing the resolving value would inform a decision or a view of the world. A niche
  subject is relevant. An incidental detail is not.
- **W2. Every value can be established.** For each value in the outcome, some evidence would establish that the question resolved
  to it.
- **W3. One uncertainty.** One question asks one thing. Separate triggers, measures or deadlines are not joined
  with "and" or "or". Two paths to the same final state are one thing.
- **W4. No hypothetical conditions.** No "if X" or "assuming Y". Ask about the result directly, over a qualifying window that
  covers it. A condition appears only as a premise whose failure annuls the question
  (W23).
- **W5. Not about evidence.** Do not ask what public evidence will establish about a past incident. A future court
  ruling or official finding is askable when its possible results and the deciding record
  are defined.
- **W7. A named period. [generated]** For a figure published on a schedule, ask for the figure for a named period, not the
  latest reading by a date. The latest reading by a date is for figures with no fixed
  schedule.

## Output type

- **W8.** Choose the output type by T1 to T6.
- **W9. The most informative form.** A question asking whether a value will exceed a threshold asks instead for the underlying
  numerical value. One asking whether an event will occur by a date asks for the date it
  occurs. One asking whether one of several things will occur asks which of them occurs. A
  distribution over the underlying value gives the probability of every threshold at once.
- **W30. [generated]** A binary question is written only where no date, numerical or categorical question carries
  the same information (T5).

## Title

- **W10.** The title concisely captures what the question asks and is understandable without the
  criteria.

## Resolution criteria

- **W11. What it resolves to.** The criteria open with what the question resolves to. They state facts and do not describe
  what anyone will do. A procedure belongs in the criteria only when it is part of deriving
  the resolving value. Each rule from W12 to W19 is stated explicitly or does not apply.
- **W12. The exact quantity or event.** Define every term the resolving value turns on. For a figure: geography, population,
  denominator, seasonal adjustment, what is included and what is excluded. Replace "major"
  or "significant" with a threshold.
- **W13. The period.** Say which period the resolving value refers to and what kind it is: a calendar month, a
  month-end snapshot, a rolling three months, a year ending in a month.
- **W14. The source.** Where one publisher decides the fact, name it: a statistics office, a regulator, a filing,
  a court record. Do not name a database that copies it. Prefer a free public source. Where
  no one publisher decides the fact, name none: the question resolves on credible sources. A
  series or catalogue identifier may be given beside the publisher and the definition, never
  in place of them; where a copy of the series differs from the publisher, the publisher
  governs.
- **W15. The release.** A question about a published figure says which release counts: the first release, a named
  later release, or the latest release at a stated time. Silence is a defect.
- **W16. Unit and calculation.** State the unit with its multiplier, the sign convention, and any calculation applied to
  the source's figures. Rounding follows T17.
- **W17. Times.** Write absolute dates, never a date relative to another time or a reference to one of the
  question's own times. A deadline has a time and a timezone. Where none is natural, use
  UTC. Say whether the boundary instant is included. Keep the period being measured distinct
  from the time its figure is published.
- **W18. The qualifying window.** Say when it opens where that is not the question's `as_of`.
- **W19. First event or later state.** Say whether the question resolves on the first qualifying event, or on a state at a
  later time: a total as shown at a later check, a condition that must still hold at the
  deadline.

## Fallbacks and annulment

- **W21. Few fallbacks.** At most two, and none that changes what is being forecast. A fallback to a second source
  is acceptable only when both report the same quantity in a similar way. A fallback that
  makes the resolving value depend on which source appears splits the forecast in two,
  and is a defect.
- **W22.** A fallback is never a placeholder value (Q3, T22).
- **W23. When it annuls.** Where a premise could fail, the resolution criteria say when the question annuls, with a
  date: the event is cancelled, the figure is not published by a stated date, the source no
  longer exists. A numerical or categorical question whose resolving value exists only if
  some event occurs says that it annuls if the event has not occurred by a stated date. None
  is needed for a count that is truly zero when nothing occurs, an option meaning that none
  of the others occurred, a routine scheduled release, or the event a binary or date
  question asks about not occurring (Q3).

## Voice

- **W24.** Impersonal: no "we". No internal identifier stands in for a definition.
- **W25.** Short: the criteria say what resolves the question and nothing else.

## Before publishing

- **W26.** Read the rendered title, resolution criteria and outcome together, first as a forecaster
  and then as a resolver. Check that what the criteria promise for the release, the
  deadline and annulment can be delivered (Q2).

## Converting a question

For a question rewritten into a more informative form.

- **W27. Exact.** The converted question, with the mapping back, resolves the original exactly: every value
  it can resolve to, including one beyond an open bound, and its annulment, maps to one
  resolution of the original. It keeps the original's subject, source, method, definitions,
  scope, timing, when it annuls, and fallbacks. Make the smallest edit that does this.
- **W28. Thresholds stay in the mapping.** The original's threshold and deadline are not written into the converted question,
  unless they are part of the value's definition.
- **W29. No proxy.** Do not convert to a quantity the original does not define: a count, where the original
  asks only whether any member of a set qualifies. Where the original resolves when an event
  does not occur, the converted question gives that case a value of its own and does not
  annul on it. Where no exact and useful conversion exists, the question is not converted.
