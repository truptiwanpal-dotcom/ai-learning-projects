"""
SIMPLE FINE-TUNING FLOW — for interview understanding, not production code.

This shows the 4 steps of fine-tuning a model using OpenAI's API:
  1. Prepare training data (see training_data.jsonl)
  2. Upload the file to OpenAI
  3. Start a fine-tuning job
  4. Use the fine-tuned model once training completes
"""

from openai import OpenAI

client = OpenAI(api_key="sk-proj-your-key-here")  # never hardcode in real code


# ─────────────────────────────────────────────
# STEP 1: Training data (already created as training_data.jsonl)
# ─────────────────────────────────────────────
# Each line is one example, in chat format:
#   { "messages": [ {system}, {user}, {assistant} ] }
#
# The "assistant" message is the IDEAL output you're teaching the model
# to produce. You'd normally have hundreds of these, not 3 — this is
# just enough to show the format.


# ─────────────────────────────────────────────
# STEP 2: Upload the training file to OpenAI
# ─────────────────────────────────────────────
training_file = client.files.create(
    file=open("training_data.jsonl", "rb"),
    purpose="fine-tune"
)
print("Uploaded file ID:", training_file.id)
# Example real output would look like:
# Uploaded file ID: file-Abc123XyZ789


# ─────────────────────────────────────────────
# STEP 3: Start the fine-tuning job
# ─────────────────────────────────────────────
# This kicks off training on OpenAI's servers — you don't run the
# training loop yourself, OpenAI handles the actual model weight updates.
# This can take minutes to hours depending on dataset size.
job = client.fine_tuning.jobs.create(
    training_file=training_file.id,
    model="gpt-4o-mini-2024-07-18"   # base model you're fine-tuning from
)
print("Fine-tuning job started:", job.id)
# Example real output would look like:
# Fine-tuning job started: ftjob-Pq98WxYz001

# You can check job status like this:
status = client.fine_tuning.jobs.retrieve(job.id)
print("Status:", status.status)   # e.g. "running", "succeeded", "failed"
# Example real output (right after starting):
# Status: running
# (you'd typically poll this every few minutes until it becomes "succeeded")


# ─────────────────────────────────────────────
# STEP 4: Once training finishes, use your fine-tuned model
# ─────────────────────────────────────────────
# OpenAI gives you a custom model ID once the job succeeds, e.g.:
#   "ft:gpt-4o-mini-2024-07-18:your-org::abc123"
#
# You then call it exactly like the base model, except now its default
# behavior reflects your training examples — no need to repeat detailed
# formatting instructions in every prompt.

fine_tuned_model_id = status.fine_tuned_model  # e.g. "ft:gpt-4o-mini-...::abc123"

response = client.chat.completions.create(
    model=fine_tuned_model_id,
    messages=[
        {"role": "user", "content": "Patient has dark urine and skipped two meals. Dehydration risk?"}
    ]
)
print(response.choices[0].message.content)
# Expected style of output (learned from training examples):
# Risk Level: High. Reason: Dark urine and skipped meals indicate dehydration markers.