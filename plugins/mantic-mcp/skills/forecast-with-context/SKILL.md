---
name: forecast-with-context
description: Request a Mantic forecast using relevant user-specific context, such as private knowledge, internal plans or constraints. Do not use for general news, public research or background information.
---

# Forecast with context

Use `additional_context` only when the user has relevant information specific
to their situation that Mantic would not otherwise have. Examples include
unpublished sales figures, internal operating plans or contractual constraints.
Public news, general research and generic “what if” assumptions do not qualify
just because the user mentioned them.

Check that the context bears on the existing question and its resolution
criteria. Include only the relevant details, preserving the user's meaning
and distinguishing known facts from plans or assumptions. Do not pad the
context with your own research.

For example, when forecasting a company's margins: “Our procurement team has
fixed next quarter's copper purchase price at $8,000 per tonne.”

Call `create_question_forecast` with `question_id` and `additional_context`.
The text limit is 20,000 characters.
The result is visible to the user and their organisation.

The returned `id` identifies the requested run; pass it to `get_forecast` as
`run_id`. Until the run completes, `get_forecast` reports it as not found;
retain the ID rather than submitting again.
Explain what Mantic made of the user's context from `changes_from_previous`
or `reasoning`; do not assume it accepted the context or changed its forecast.
Follow [using-mantic](../using-mantic/SKILL.md) when presenting the result.
