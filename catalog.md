# OpenRouter モデルカタログ（全344モデル）

- 取得日時: 2026-06-06T22:51:37
- プロバイダ数: 57 / 無料枠あり: 27

## プロバイダ別サマリ

| Provider | モデル数 | 最安入力($/1M) | 最高入力($/1M) | 最大Context |
|---|--:|--:|--:|--:|
| openai | 63 | 0.00 | 150.00 | 1,050,000 |
| qwen | 49 | 0.00 | 1.25 | 1,048,576 |
| google | 26 | 0.00 | 2.00 | 1,048,756 |
| mistralai | 19 | 0.02 | 2.00 | 262,144 |
| anthropic | 15 | 0.25 | 30.00 | 1,000,000 |
| meta-llama | 14 | 0.00 | 0.51 | 10,000,000 |
| z-ai | 13 | 0.00 | 1.20 | 202,752 |
| nvidia | 12 | 0.00 | 0.50 | 1,000,000 |
| deepseek | 12 | 0.10 | 0.70 | 1,048,576 |
| minimax | 8 | 0.15 | 0.40 | 1,048,576 |
| openrouter | 6 | 0.00 | 0.00 | 2,000,000 |
| moonshotai | 6 | 0.00 | 0.68 | 262,144 |
| arcee-ai | 6 | 0.04 | 0.90 | 262,144 |
| amazon | 5 | 0.04 | 2.50 | 1,000,000 |
| perplexity | 5 | 1.00 | 3.00 | 200,000 |
| nousresearch | 5 | 0.00 | 1.00 | 131,072 |
| x-ai | 4 | 1.00 | 2.00 | 2,000,000 |
| bytedance-seed | 4 | 0.07 | 0.25 | 262,144 |
| aion-labs | 4 | 0.70 | 4.00 | 131,072 |
| thedrummer | 4 | 0.17 | 0.55 | 131,072 |
| cohere | 4 | 0.04 | 2.50 | 256,000 |
| sao10k | 4 | 0.04 | 3.00 | 131,072 |
| inclusionai | 3 | 0.01 | 0.07 | 262,144 |
| ~anthropic | 3 | 1.00 | 5.00 | 1,000,000 |
| xiaomi | 3 | 0.10 | 0.43 | 1,048,576 |
| liquid | 3 | 0.00 | 0.03 | 128,000 |
| microsoft | 3 | 0.07 | 0.62 | 131,072 |
| stepfun | 2 | 0.09 | 0.20 | 262,144 |
| ibm-granite | 2 | 0.02 | 0.05 | 131,072 |
| poolside | 2 | 0.00 | 0.00 | 262,144 |
| ~openai | 2 | 0.75 | 5.00 | 1,050,000 |
| ~google | 2 | 1.50 | 2.00 | 1,048,576 |
| tencent | 2 | 0.06 | 0.14 | 262,144 |
| rekaai | 2 | 0.10 | 0.10 | 65,536 |
| relace | 2 | 0.85 | 1.00 | 256,000 |
| baidu | 2 | 0.14 | 0.42 | 131,072 |
| morph | 2 | 0.80 | 0.90 | 262,144 |
| inflection | 2 | 2.50 | 2.50 | 8,000 |
| perceptron | 1 | 0.15 | 0.15 | 32,768 |
| ~moonshotai | 1 | 0.68 | 0.68 | 262,144 |
| kwaipilot | 1 | 0.30 | 0.30 | 256,000 |
| inception | 1 | 0.25 | 0.25 | 128,000 |
| upstage | 1 | 0.15 | 0.15 | 128,000 |
| writer | 1 | 0.60 | 0.60 | 1,040,000 |
| nex-agi | 1 | 0.14 | 0.14 | 131,072 |
| essentialai | 1 | 0.15 | 0.15 | 32,768 |
| prime-intellect | 1 | 0.20 | 0.20 | 131,072 |
| allenai | 1 | 0.15 | 0.15 | 65,536 |
| deepcogito | 1 | 1.25 | 1.25 | 128,000 |
| ai21 | 1 | 2.00 | 2.00 | 256,000 |
| bytedance | 1 | 0.10 | 0.10 | 128,000 |
| switchpoint | 1 | 0.85 | 0.85 | 131,072 |
| cognitivecomputations | 1 | 0.00 | 0.00 | 32,768 |
| anthracite-org | 1 | 3.00 | 3.00 | 32,768 |
| mancer | 1 | 0.75 | 0.75 | 8,000 |
| undi95 | 1 | 0.45 | 0.45 | 6,144 |
| gryphe | 1 | 0.06 | 0.06 | 4,096 |

## モデル詳細

### ▎ai21（1）

#### AI21: Jamba Large 1.7

- **ID**: `ai21/jamba-large-1.7`
- **Provider**: ai21
- **Context**: 256K (256,000) tok / max出力 4,096 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $8.00/1M
- **Capabilities**: Function calling, Tool choice, JSON mode
- **Knowledge cutoff**: 2024-08-31
- **登録日**: 2025-08-09
- **HF**: `ai21labs/AI21-Jamba-Large-1.7`
- **対応パラメータ**: max_tokens, response_format, stop, temperature, tool_choice, tools, top_p

Jamba Large 1.7 is the latest model in the Jamba open family, offering improvements in grounding, instruction-following, and overall efficiency. Built on a hybrid SSM-Transformer architecture with a 256K context...

### ▎aion-labs（4）

#### AionLabs: Aion-1.0

- **ID**: `aion-labs/aion-1.0`
- **Provider**: aion-labs
- **Context**: 131K (131,072) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $4.00/1M · 出力 $8.00/1M
- **Capabilities**: Reasoning(思考), Reasoning出力
- **登録日**: 2025-02-05
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, temperature, top_p

Aion-1.0 is a multi-model system designed for high performance across various tasks, including reasoning and coding. It is built on DeepSeek-R1, augmented with additional models and techniques such as Tree...

#### AionLabs: Aion-1.0-Mini

- **ID**: `aion-labs/aion-1.0-mini`
- **Provider**: aion-labs
- **Context**: 131K (131,072) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.7/1M · 出力 $1.40/1M
- **Capabilities**: Reasoning(思考), Reasoning出力
- **登録日**: 2025-02-05
- **HF**: `FuseAI/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, temperature, top_p

Aion-1.0-Mini 32B parameter model is a distilled version of the DeepSeek-R1 model, designed for strong performance in reasoning domains such as mathematics, coding, and logic. It is a modified variant...

#### AionLabs: Aion-2.0

- **ID**: `aion-labs/aion-2.0`
- **Provider**: aion-labs
- **Context**: 131K (131,072) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.8/1M · 出力 $1.60/1M · キャッシュ読 $0.2/1M
- **Capabilities**: Reasoning(思考), Reasoning出力
- **登録日**: 2026-02-24
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, temperature, top_p

Aion-2.0 is a variant of DeepSeek V3.2 optimized for immersive roleplaying and storytelling. It is particularly strong at introducing tension, crises, and conflict into stories, making narratives feel more engaging....

#### AionLabs: Aion-RP 1.0 (8B)

- **ID**: `aion-labs/aion-rp-llama-3.1-8b`
- **Provider**: aion-labs
- **Context**: 32K (32,768) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.8/1M · 出力 $1.60/1M
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2025-02-05
- **対応パラメータ**: max_tokens, temperature, top_p

Aion-RP-Llama-3.1-8B ranks the highest in the character evaluation portion of the RPBench-Auto benchmark, a roleplaying-specific variant of Arena-Hard-Auto, where LLMs evaluate each other’s responses. It is a fine-tuned base model...

### ▎allenai（1）

#### AllenAI: Olmo 3 32B Think

- **ID**: `allenai/olmo-3-32b-think`
- **Provider**: allenai
- **Context**: 65K (65,536) tok / max出力 65,536 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.15/1M · 出力 $0.5/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-11-22
- **HF**: `allenai/Olmo-3-32B-Think`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_p

Olmo 3 32B Think is a large-scale, 32-billion-parameter model purpose-built for deep reasoning, complex logic chains and advanced instruction-following scenarios. Its capacity enables strong performance on demanding evaluation tasks and...

### ▎amazon（5）

#### Amazon: Nova 2 Lite

- **ID**: `amazon/nova-2-lite-v1`
- **Provider**: amazon
- **Context**: 1M (1,000,000) tok / max出力 65,535 tok
- **Modality**: text+image+file+video->text  (in: text,image,video,file → out: text)
- **Pricing**: 入力 $0.3/1M · 出力 $2.50/1M
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力
- **登録日**: 2025-12-03
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, stop, temperature, tool_choice, tools, top_k, top_p

Nova 2 Lite is a fast, cost-effective reasoning model for everyday workloads that can process text, images, and videos to generate text. Nova 2 Lite demonstrates standout capabilities in processing...

#### Amazon: Nova Lite 1.0

- **ID**: `amazon/nova-lite-v1`
- **Provider**: amazon
- **Context**: 300K (300,000) tok / max出力 5,120 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.06/1M · 出力 $0.24/1M
- **Capabilities**: Function calling
- **Knowledge cutoff**: 2024-10-31
- **登録日**: 2024-12-06
- **対応パラメータ**: max_tokens, stop, temperature, tools, top_k, top_p

Amazon Nova Lite 1.0 is a very low-cost multimodal model from Amazon that focused on fast processing of image, video, and text inputs to generate text output. Amazon Nova Lite...

#### Amazon: Nova Micro 1.0

- **ID**: `amazon/nova-micro-v1`
- **Provider**: amazon
- **Context**: 128K (128,000) tok / max出力 5,120 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.035/1M · 出力 $0.14/1M
- **Capabilities**: Function calling
- **Knowledge cutoff**: 2024-10-31
- **登録日**: 2024-12-06
- **対応パラメータ**: max_tokens, stop, temperature, tools, top_k, top_p

Amazon Nova Micro 1.0 is a text-only model that delivers the lowest latency responses in the Amazon Nova family of models at a very low cost. With a context length...

#### Amazon: Nova Premier 1.0

- **ID**: `amazon/nova-premier-v1`
- **Provider**: amazon
- **Context**: 1M (1,000,000) tok / max出力 32,000 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $2.50/1M · 出力 $12.50/1M · キャッシュ読 $0.625/1M
- **Capabilities**: Function calling
- **登録日**: 2025-11-01
- **対応パラメータ**: max_tokens, stop, temperature, tools, top_k, top_p

Amazon Nova Premier is the most capable of Amazon’s multimodal models for complex reasoning tasks and for use as the best teacher for distilling custom models.

#### Amazon: Nova Pro 1.0

- **ID**: `amazon/nova-pro-v1`
- **Provider**: amazon
- **Context**: 300K (300,000) tok / max出力 5,120 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.8/1M · 出力 $3.20/1M
- **Capabilities**: Function calling
- **Knowledge cutoff**: 2024-10-31
- **登録日**: 2024-12-06
- **対応パラメータ**: max_tokens, stop, temperature, tools, top_k, top_p

Amazon Nova Pro 1.0 is a capable multimodal model from Amazon focused on providing a combination of accuracy, speed, and cost for a wide range of tasks. As of December...

### ▎anthracite-org（1）

#### Magnum v4 72B

- **ID**: `anthracite-org/magnum-v4-72b`
- **Provider**: anthracite-org
- **Context**: 32K (32,768) tok / max出力 2,048 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $3.00/1M · 出力 $5.00/1M
- **Capabilities**: JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2024-10-22
- **HF**: `anthracite-org/magnum-v4-72b`
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, temperature, top_a, top_k, top_logprobs, top_p

This is a series of models designed to replicate the prose quality of the Claude 3 models, specifically Sonnet(https://openrouter.ai/anthropic/claude-3.5-sonnet) and Opus(https://openrouter.ai/anthropic/claude-3-opus).

The model is fine-tuned on top of [Qwen2.5 72B](https://openrouter.ai/qwen/qwen-2.5-72b-instruct).

### ▎anthropic（15）

#### Anthropic: Claude 3 Haiku

- **ID**: `anthropic/claude-3-haiku`
- **Provider**: anthropic
- **Context**: 200K (200,000) tok / max出力 4,096 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.25/1M · 出力 $1.25/1M · キャッシュ読 $0.03/1M · キャッシュ書 $0.3/1M
- **Capabilities**: Function calling, Tool choice
- **Knowledge cutoff**: 2023-08-31
- **登録日**: 2024-03-13
- **対応パラメータ**: max_tokens, stop, temperature, tool_choice, tools, top_k, top_p

Claude 3 Haiku is Anthropic's fastest and most compact model for
near-instant responsiveness. Quick and accurate targeted performance.

See the launch announcement and benchmark results [here](https://www.anthropic.com/news/claude-3-haiku)

#multimodal

#### Anthropic: Claude 3.5 Haiku

- **ID**: `anthropic/claude-3.5-haiku`
- **Provider**: anthropic
- **Context**: 200K (200,000) tok / max出力 8,192 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.8/1M · 出力 $4.00/1M · キャッシュ読 $0.08/1M · キャッシュ書 $1.00/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice
- **Knowledge cutoff**: 2024-07-31
- **登録日**: 2024-11-04
- **対応パラメータ**: max_tokens, stop, temperature, tool_choice, tools, top_k, top_p

Claude 3.5 Haiku features offers enhanced capabilities in speed, coding accuracy, and tool use. Engineered to excel in real-time applications, it delivers quick response times that are essential for dynamic...

#### Anthropic: Claude Haiku 4.5

- **ID**: `anthropic/claude-haiku-4.5`
- **Provider**: anthropic
- **Context**: 200K (200,000) tok / max出力 64,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $1.00/1M · 出力 $5.00/1M · キャッシュ読 $0.1/1M · キャッシュ書 $1.25/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2025-10-16
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Claude Haiku 4.5 is Anthropic’s fastest and most efficient model, delivering near-frontier intelligence at a fraction of the cost and latency of larger Claude models. Matching Claude Sonnet 4’s performance...

#### Anthropic: Claude Opus 4

- **ID**: `anthropic/claude-opus-4`
- **Provider**: anthropic
- **Context**: 200K (200,000) tok / max出力 32,000 tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $15.00/1M · 出力 $75.00/1M · キャッシュ読 $1.50/1M · キャッシュ書 $18.75/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-05-23
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, stop, temperature, tool_choice, tools, top_p

Claude Opus 4 is benchmarked as the world’s best coding model, at time of release, bringing sustained performance on complex, long-running tasks and agent workflows. It sets new benchmarks in...

#### Anthropic: Claude Opus 4.1

- **ID**: `anthropic/claude-opus-4.1`
- **Provider**: anthropic
- **Context**: 200K (200,000) tok / max出力 32,000 tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $15.00/1M · 出力 $75.00/1M · キャッシュ読 $1.50/1M · キャッシュ書 $18.75/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-08-06
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Claude Opus 4.1 is an updated version of Anthropic’s flagship model, offering improved performance in coding, reasoning, and agentic tasks. It achieves 74.5% on SWE-bench Verified and shows notable gains...

#### Anthropic: Claude Opus 4.5

- **ID**: `anthropic/claude-opus-4.5`
- **Provider**: anthropic
- **Context**: 200K (200,000) tok / max出力 64,000 tok
- **Modality**: text+image+file->text  (in: file,image,text → out: text)
- **Pricing**: 入力 $5.00/1M · 出力 $25.00/1M · キャッシュ読 $0.5/1M · キャッシュ書 $6.25/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2025-11-25
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, verbosity

Claude Opus 4.5 is Anthropic’s frontier reasoning model optimized for complex software engineering, agentic workflows, and long-horizon computer use. It offers strong multimodal capabilities, competitive performance across real-world coding and...

#### Anthropic: Claude Opus 4.6

- **ID**: `anthropic/claude-opus-4.6`
- **Provider**: anthropic
- **Context**: 1M (1,000,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $5.00/1M · 出力 $25.00/1M · キャッシュ読 $0.5/1M · キャッシュ書 $6.25/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-02-05
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p, verbosity

Opus 4.6 is Anthropic’s strongest model for coding and long-running professional tasks. It is built for agents that operate across entire workflows rather than single prompts, making it especially effective...

#### Anthropic: Claude Opus 4.6 (Fast)

- **ID**: `anthropic/claude-opus-4.6-fast`
- **Provider**: anthropic
- **Context**: 1M (1,000,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $30.00/1M · 出力 $150.00/1M · キャッシュ読 $3.00/1M · キャッシュ書 $37.50/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-04-08
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_p, verbosity

Fast-mode variant of [Opus 4.6](/anthropic/claude-opus-4.6) - identical capabilities with higher output speed at premium 6x pricing.

Learn more in Anthropic's docs: https://platform.claude.com/docs/en/build-with-claude/fast-mode

#### Anthropic: Claude Opus 4.7

- **ID**: `anthropic/claude-opus-4.7`
- **Provider**: anthropic
- **Context**: 1M (1,000,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $5.00/1M · 出力 $25.00/1M · キャッシュ読 $0.5/1M · キャッシュ書 $6.25/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-04-16
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, tool_choice, tools, verbosity

Opus 4.7 is the next generation of Anthropic's Opus family, built for long-running, asynchronous agents. Building on the coding and agentic strengths of Opus 4.6, it delivers stronger performance on...

#### Anthropic: Claude Opus 4.7 (Fast)

- **ID**: `anthropic/claude-opus-4.7-fast`
- **Provider**: anthropic
- **Context**: 1M (1,000,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $30.00/1M · 出力 $150.00/1M · キャッシュ読 $3.00/1M · キャッシュ書 $37.50/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-05-13
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, tool_choice, tools, verbosity

Fast-mode variant of [Opus 4.7](/anthropic/claude-opus-4.7) - identical capabilities with higher output speed at premium 6x pricing.

Learn more in Anthropic's docs: https://platform.claude.com/docs/en/build-with-claude/fast-mode

#### Anthropic: Claude Opus 4.8

- **ID**: `anthropic/claude-opus-4.8`
- **Provider**: anthropic
- **Context**: 1M (1,000,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $5.00/1M · 出力 $25.00/1M · キャッシュ読 $0.5/1M · キャッシュ書 $6.25/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-05-28
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, tool_choice, tools, verbosity

Claude Opus 4.8 is Anthropic's most capable generally available model in the Opus family. It supports text, image, and file inputs with text output, with reasoning support and a 1M-token...

#### Anthropic: Claude Opus 4.8 (Fast)

- **ID**: `anthropic/claude-opus-4.8-fast`
- **Provider**: anthropic
- **Context**: 1M (1,000,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $10.00/1M · 出力 $50.00/1M · キャッシュ読 $1.00/1M · キャッシュ書 $12.50/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-05-28
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, tool_choice, tools, verbosity

Fast-mode variant of [Opus 4.8](/anthropic/claude-opus-4.8) - identical capabilities with higher output speed at 2x pricing relative to regular Opus 4.8.

Learn more in Anthropic's docs: https://platform.claude.com/docs/en/build-with-claude/fast-mode

#### Anthropic: Claude Sonnet 4

- **ID**: `anthropic/claude-sonnet-4`
- **Provider**: anthropic
- **Context**: 1M (1,000,000) tok / max出力 64,000 tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $3.00/1M · 出力 $15.00/1M · キャッシュ読 $0.3/1M · キャッシュ書 $3.75/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-05-23
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, stop, temperature, tool_choice, tools, top_k, top_p

Claude Sonnet 4 significantly enhances the capabilities of its predecessor, Sonnet 3.7, excelling in both coding and reasoning tasks with improved precision and controllability. Achieving state-of-the-art performance on SWE-bench (72.7%),...

#### Anthropic: Claude Sonnet 4.5

- **ID**: `anthropic/claude-sonnet-4.5`
- **Provider**: anthropic
- **Context**: 1M (1,000,000) tok / max出力 64,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $3.00/1M · 出力 $15.00/1M · キャッシュ読 $0.3/1M · キャッシュ書 $3.75/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-09-30
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Claude Sonnet 4.5 is Anthropic’s most advanced Sonnet model to date, optimized for real-world agents and coding workflows. It delivers state-of-the-art performance on coding benchmarks such as SWE-bench Verified, with...

#### Anthropic: Claude Sonnet 4.6

- **ID**: `anthropic/claude-sonnet-4.6`
- **Provider**: anthropic
- **Context**: 1M (1,000,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $3.00/1M · 出力 $15.00/1M · キャッシュ読 $0.3/1M · キャッシュ書 $3.75/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-02-18
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p, verbosity

Sonnet 4.6 is Anthropic's most capable Sonnet-class model yet, with frontier performance across coding, agents, and professional work. It excels at iterative development, complex codebase navigation, end-to-end project management with...

### ▎arcee-ai（6）

#### Arcee AI: Coder Large

- **ID**: `arcee-ai/coder-large`
- **Provider**: arcee-ai
- **Context**: 32K (32,768) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.5/1M · 出力 $0.8/1M
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-05-06
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, stop, temperature, top_k, top_p

Coder‑Large is a 32 B‑parameter offspring of Qwen 2.5‑Instruct that has been further trained on permissively‑licensed GitHub, CodeSearchNet and synthetic bug‑fix corpora. It supports a 32k context window, enabling multi‑file...

#### Arcee AI: Maestro Reasoning

- **ID**: `arcee-ai/maestro-reasoning`
- **Provider**: arcee-ai
- **Context**: 131K (131,072) tok / max出力 32,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.9/1M · 出力 $3.30/1M
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-05-06
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, stop, temperature, top_k, top_p

Maestro Reasoning is Arcee's flagship analysis model: a 32 B‑parameter derivative of Qwen 2.5‑32 B tuned with DPO and chain‑of‑thought RL for step‑by‑step logic. Compared to the earlier 7 B...

#### Arcee AI: Spotlight

- **ID**: `arcee-ai/spotlight`
- **Provider**: arcee-ai
- **Context**: 131K (131,072) tok / max出力 65,537 tok
- **Modality**: text+image->text  (in: image,text → out: text)
- **Pricing**: 入力 $0.18/1M · 出力 $0.18/1M
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-05-06
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, stop, temperature, top_k, top_p

Spotlight is a 7‑billion‑parameter vision‑language model derived from Qwen 2.5‑VL and fine‑tuned by Arcee AI for tight image‑text grounding tasks. It offers a 32 k‑token context window, enabling rich multimodal...

#### Arcee AI: Trinity Large Thinking

- **ID**: `arcee-ai/trinity-large-thinking`
- **Provider**: arcee-ai
- **Context**: 262K (262,144) tok / max出力 262,144 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.22/1M · 出力 $0.85/1M · キャッシュ読 $0.06/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-04-02
- **HF**: `arcee-ai/Trinity-Large-Thinking`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Trinity Large Thinking is a powerful open source reasoning model from the team at Arcee AI. It shows strong performance in PinchBench, agentic workloads, and reasoning tasks. Launch video: https://youtu.be/Gc82AXLa0Rg?si=4RLn6WBz33qT--B7...

#### Arcee AI: Trinity Mini

- **ID**: `arcee-ai/trinity-mini`
- **Provider**: arcee-ai
- **Context**: 131K (131,072) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.045/1M · 出力 $0.15/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2025-12-02
- **HF**: `arcee-ai/Trinity-Mini`
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_p

Trinity Mini is a 26B-parameter (3B active) sparse mixture-of-experts language model featuring 128 experts with 8 active per token. Engineered for efficient reasoning over long contexts (131k) with robust function...

#### Arcee AI: Virtuoso Large

- **ID**: `arcee-ai/virtuoso-large`
- **Provider**: arcee-ai
- **Context**: 131K (131,072) tok / max出力 64,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.75/1M · 出力 $1.20/1M
- **Capabilities**: Function calling, Tool choice
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-05-06
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, stop, temperature, tool_choice, tools, top_k, top_p

Virtuoso‑Large is Arcee's top‑tier general‑purpose LLM at 72 B parameters, tuned to tackle cross‑domain reasoning, creative writing and enterprise QA. Unlike many 70 B peers, it retains the 128 k...

### ▎baidu（2）

#### Baidu: ERNIE 4.5 VL 28B A3B

- **ID**: `baidu/ernie-4.5-vl-28b-a3b`
- **Provider**: baidu
- **Context**: 131K (131,072) tok / max出力 8,000 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.14/1M · 出力 $0.56/1M
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-08-13
- **HF**: `baidu/ERNIE-4.5-VL-28B-A3B-PT`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, seed, stop, temperature, tool_choice, tools, top_k, top_p

A powerful multimodal Mixture-of-Experts chat model featuring 28B total parameters with 3B activated per token, delivering exceptional text and vision understanding through its innovative heterogeneous MoE structure with modality-isolated routing....

#### Baidu: ERNIE 4.5 VL 424B A47B 

- **ID**: `baidu/ernie-4.5-vl-424b-a47b`
- **Provider**: baidu
- **Context**: 131K (131,072) tok / max出力 16,000 tok
- **Modality**: text+image->text  (in: image,text → out: text)
- **Pricing**: 入力 $0.42/1M · 出力 $1.25/1M
- **Capabilities**: Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-07-01
- **HF**: `baidu/ERNIE-4.5-VL-424B-A47B-PT`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, seed, stop, temperature, top_k, top_p

ERNIE-4.5-VL-424B-A47B is a multimodal Mixture-of-Experts (MoE) model from Baidu’s ERNIE 4.5 series, featuring 424B total parameters with 47B active per token. It is trained jointly on text and image data...

### ▎bytedance（1）

#### ByteDance: UI-TARS 7B 

- **ID**: `bytedance/ui-tars-1.5-7b`
- **Provider**: bytedance
- **Context**: 128K (128,000) tok / max出力 2,048 tok
- **Modality**: text+image->text  (in: image,text → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.2/1M · キャッシュ読 $0.1/1M
- **Capabilities**: Seed固定
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-07-23
- **HF**: `ByteDance-Seed/UI-TARS-1.5-7B`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p

UI-TARS-1.5 is a multimodal vision-language agent optimized for GUI-based environments, including desktop interfaces, web browsers, mobile systems, and games. Built by ByteDance, it builds upon the UI-TARS framework with reinforcement...

### ▎bytedance-seed（4）

#### ByteDance Seed: Seed 1.6

- **ID**: `bytedance-seed/seed-1.6`
- **Provider**: bytedance-seed
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text+image+video->text  (in: image,text,video → out: text)
- **Pricing**: 入力 $0.25/1M · 出力 $2.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2025-12-24
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_p

Seed 1.6 is a general-purpose model released by the ByteDance Seed team. It incorporates multimodal capabilities and adaptive deep thinking with a 256K context window.

#### ByteDance Seed: Seed 1.6 Flash

- **ID**: `bytedance-seed/seed-1.6-flash`
- **Provider**: bytedance-seed
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text+image+video->text  (in: image,text,video → out: text)
- **Pricing**: 入力 $0.075/1M · 出力 $0.3/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2025-12-24
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_p

Seed 1.6 Flash is an ultra-fast multimodal deep thinking model by ByteDance Seed, supporting both text and visual understanding. It features a 256k context window and can generate outputs of...

#### ByteDance Seed: Seed-2.0-Lite

- **ID**: `bytedance-seed/seed-2.0-lite`
- **Provider**: bytedance-seed
- **Context**: 262K (262,144) tok / max出力 131,072 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.25/1M · 出力 $2.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-03-11
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_p

Seed-2.0-Lite is a versatile, cost‑efficient enterprise workhorse that delivers strong multimodal and agent capabilities while offering noticeably lower latency, making it a practical default choice for most production workloads across...

#### ByteDance Seed: Seed-2.0-Mini

- **ID**: `bytedance-seed/seed-2.0-mini`
- **Provider**: bytedance-seed
- **Context**: 262K (262,144) tok / max出力 131,072 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.4/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-02-27
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_p

Seed-2.0-mini targets latency-sensitive, high-concurrency, and cost-sensitive scenarios, emphasizing fast response and flexible inference deployment. It delivers performance comparable to ByteDance-Seed-1.6, supports 256k context, four reasoning effort modes (minimal/low/medium/high), multimodal understanding,...

### ▎cognitivecomputations（1）

#### Venice: Uncensored (free)

- **ID**: `cognitivecomputations/dolphin-mistral-24b-venice-edition:free`
- **Provider**: cognitivecomputations
- **Context**: 32K (32,768) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode
- **Knowledge cutoff**: 2024-04-30
- **登録日**: 2025-07-10
- **HF**: `cognitivecomputations/Dolphin-Mistral-24B-Venice-Edition`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, stop, structured_outputs, temperature, top_k, top_p

Venice Uncensored Dolphin Mistral 24B Venice Edition is a fine-tuned variant of Mistral-Small-24B-Instruct-2501, developed by dphn.ai in collaboration with Venice.ai. This model is designed as an “uncensored” instruct-tuned LLM, preserving...

### ▎cohere（4）

#### Cohere: Command A

- **ID**: `cohere/command-a`
- **Provider**: cohere
- **Context**: 256K (256,000) tok / max出力 8,192 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $2.50/1M · 出力 $10.00/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-08-31
- **登録日**: 2025-03-14
- **HF**: `CohereForAI/c4ai-command-a-03-2025`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_p

Command A is an open-weights 111B parameter model with a 256k context window focused on delivering great performance across agentic, multilingual, and coding use cases. Compared to other leading proprietary...

#### Cohere: Command R (08-2024)

- **ID**: `cohere/command-r-08-2024`
- **Provider**: cohere
- **Context**: 128K (128,000) tok / max出力 4,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.15/1M · 出力 $0.6/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-03-31
- **登録日**: 2024-08-30
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

command-r-08-2024 is an update of the [Command R](/models/cohere/command-r) with improved performance for multilingual retrieval-augmented generation (RAG) and tool use. More broadly, it is better at math, code and reasoning and...

#### Cohere: Command R+ (08-2024)

- **ID**: `cohere/command-r-plus-08-2024`
- **Provider**: cohere
- **Context**: 128K (128,000) tok / max出力 4,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $2.50/1M · 出力 $10.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-03-31
- **登録日**: 2024-08-30
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

command-r-plus-08-2024 is an update of the [Command R+](/models/cohere/command-r-plus) with roughly 50% higher throughput and 25% lower latencies as compared to the previous Command R+ version, while keeping the hardware footprint...

#### Cohere: Command R7B (12-2024)

- **ID**: `cohere/command-r7b-12-2024`
- **Provider**: cohere
- **Context**: 128K (128,000) tok / max出力 4,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.0375/1M · 出力 $0.15/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-08-31
- **登録日**: 2024-12-14
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_p

Command R7B (12-2024) is a small, fast update of the Command R+ model, delivered in December 2024. It excels at RAG, tool use, agents, and similar tasks requiring complex reasoning...

### ▎deepcogito（1）

#### Deep Cogito: Cogito v2.1 671B

- **ID**: `deepcogito/cogito-v2.1-671b`
- **Provider**: deepcogito
- **Context**: 128K (128,000) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $1.25/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2025-11-14
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, stop, structured_outputs, temperature, top_k, top_p

Cogito v2.1 671B MoE represents one of the strongest open models globally, matching performance of frontier closed and open models. This model is trained using self play with reinforcement learning...

### ▎deepseek（12）

#### DeepSeek: DeepSeek V3

- **ID**: `deepseek/deepseek-chat`
- **Provider**: deepseek
- **Context**: 131K (131,072) tok / max出力 16,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.2002/1M · 出力 $0.8001/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-07-31
- **登録日**: 2024-12-27
- **HF**: `deepseek-ai/DeepSeek-V3`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

DeepSeek-V3 is the latest model from the DeepSeek team, building upon the instruction following and coding abilities of the previous versions. Pre-trained on nearly 15 trillion tokens, the reported evaluations...

#### DeepSeek: DeepSeek V3 0324

- **ID**: `deepseek/deepseek-chat-v3-0324`
- **Provider**: deepseek
- **Context**: 163K (163,840) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.2/1M · 出力 $0.77/1M · キャッシュ読 $0.135/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-07-31
- **登録日**: 2025-03-24
- **HF**: `deepseek-ai/DeepSeek-V3-0324`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

DeepSeek V3, a 685B-parameter, mixture-of-experts model, is the latest iteration of the flagship chat model family from the DeepSeek team. It succeeds the [DeepSeek V3](/deepseek/deepseek-chat-v3) model and performs really well...

#### DeepSeek: DeepSeek V3.1

- **ID**: `deepseek/deepseek-chat-v3.1`
- **Provider**: deepseek
- **Context**: 163K (163,840) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.21/1M · 出力 $0.79/1M · キャッシュ読 $0.13/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-08-21
- **HF**: `deepseek-ai/DeepSeek-V3.1`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

DeepSeek-V3.1 is a large hybrid reasoning model (671B parameters, 37B active) that supports both thinking and non-thinking modes via prompt templates. It extends the DeepSeek-V3 base with a two-phase long-context...

#### DeepSeek: R1

- **ID**: `deepseek/deepseek-r1`
- **Provider**: deepseek
- **Context**: 163K (163,840) tok / max出力 16,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.7/1M · 出力 $2.50/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-07-31
- **登録日**: 2025-01-20
- **HF**: `deepseek-ai/DeepSeek-R1`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_completion_tokens, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

DeepSeek R1 is here: Performance on par with [OpenAI o1](/openai/o1), but open-sourced and with fully open reasoning tokens. It's 671B parameters in size, with 37B active in an inference pass....

#### DeepSeek: R1 0528

- **ID**: `deepseek/deepseek-r1-0528`
- **Provider**: deepseek
- **Context**: 163K (163,840) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.5/1M · 出力 $2.15/1M · キャッシュ読 $0.35/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-05-29
- **HF**: `deepseek-ai/DeepSeek-R1-0528`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

May 28th update to the [original DeepSeek R1](/deepseek/deepseek-r1) Performance on par with [OpenAI o1](/openai/o1), but open-sourced and with fully open reasoning tokens. It's 671B parameters in size, with 37B active...

#### DeepSeek: R1 Distill Llama 70B

- **ID**: `deepseek/deepseek-r1-distill-llama-70b`
- **Provider**: deepseek
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.7/1M · 出力 $0.8/1M
- **Capabilities**: JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-07-31
- **登録日**: 2025-01-24
- **HF**: `deepseek-ai/DeepSeek-R1-Distill-Llama-70B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, top_k, top_p

DeepSeek R1 Distill Llama 70B is a distilled large language model based on [Llama-3.3-70B-Instruct](/meta-llama/llama-3.3-70b-instruct), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). The model combines advanced distillation techniques to achieve high performance across...

#### DeepSeek: R1 Distill Qwen 32B

- **ID**: `deepseek/deepseek-r1-distill-qwen-32b`
- **Provider**: deepseek
- **Context**: 128K (128,000) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.29/1M · 出力 $0.29/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **Knowledge cutoff**: 2024-07-31
- **登録日**: 2025-01-30
- **HF**: `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_logprobs, top_p

DeepSeek R1 Distill Qwen 32B is a distilled large language model based on [Qwen 2.5 32B](https://huggingface.co/Qwen/Qwen2.5-32B), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). It outperforms OpenAI's o1-mini across various benchmarks, achieving new...

#### DeepSeek: DeepSeek V3.1 Terminus

- **ID**: `deepseek/deepseek-v3.1-terminus`
- **Provider**: deepseek
- **Context**: 163K (163,840) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.27/1M · 出力 $0.95/1M · キャッシュ読 $0.13/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-09-22
- **HF**: `deepseek-ai/DeepSeek-V3.1-Terminus`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

DeepSeek-V3.1 Terminus is an update to [DeepSeek V3.1](/deepseek/deepseek-chat-v3.1) that maintains the model's original capabilities while addressing issues reported by users, including language consistency and agent capabilities, further optimizing the model's...

#### DeepSeek: DeepSeek V3.2

- **ID**: `deepseek/deepseek-v3.2`
- **Provider**: deepseek
- **Context**: 131K (131,072) tok / max出力 64,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.2288/1M · 出力 $0.3432/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-12-01
- **HF**: `deepseek-ai/DeepSeek-V3.2`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

DeepSeek-V3.2 is a large language model designed to harmonize high computational efficiency with strong reasoning and agentic tool-use performance. It introduces DeepSeek Sparse Attention (DSA), a fine-grained sparse attention mechanism...

#### DeepSeek: DeepSeek V3.2 Exp

- **ID**: `deepseek/deepseek-v3.2-exp`
- **Provider**: deepseek
- **Context**: 163K (163,840) tok / max出力 65,536 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.27/1M · 出力 $0.41/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-07-31
- **登録日**: 2025-09-29
- **HF**: `deepseek-ai/DeepSeek-V3.2-Exp`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

DeepSeek-V3.2-Exp is an experimental large language model released by DeepSeek as an intermediate step between V3.1 and future architectures. It introduces DeepSeek Sparse Attention (DSA), a fine-grained sparse attention mechanism...

#### DeepSeek: DeepSeek V4 Flash

- **ID**: `deepseek/deepseek-v4-flash`
- **Provider**: deepseek
- **Context**: 1.04858M (1,048,576) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.0983/1M · 出力 $0.1966/1M · キャッシュ読 $0.0197/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-04-24
- **HF**: `deepseek-ai/DeepSeek-V4-Flash`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

DeepSeek V4 Flash is an efficiency-optimized Mixture-of-Experts model from DeepSeek with 284B total parameters and 13B activated parameters, supporting a 1M-token context window. It is designed for fast inference and...

#### DeepSeek: DeepSeek V4 Pro

- **ID**: `deepseek/deepseek-v4-pro`
- **Provider**: deepseek
- **Context**: 1.04858M (1,048,576) tok / max出力 384,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.435/1M · 出力 $0.87/1M · キャッシュ読 $0.0036/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-04-24
- **HF**: `deepseek-ai/DeepSeek-V4-Pro`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

DeepSeek V4 Pro is a large-scale Mixture-of-Experts model from DeepSeek with 1.6T total parameters and 49B activated parameters, supporting a 1M-token context window. It is designed for advanced reasoning, coding,...

### ▎essentialai（1）

#### EssentialAI: Rnj 1 Instruct

- **ID**: `essentialai/rnj-1-instruct`
- **Provider**: essentialai
- **Context**: 32K (32,768) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.15/1M · 出力 $0.15/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode
- **登録日**: 2025-12-07
- **HF**: `EssentialAI/rnj-1-instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Rnj-1 is an 8B-parameter, dense, open-weight model family developed by Essential AI and trained from scratch with a focus on programming, math, and scientific reasoning. The model demonstrates strong performance...

### ▎google（26）

#### Google: Gemini 2.5 Flash

- **ID**: `google/gemini-2.5-flash`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,535 tok
- **Modality**: text+image+file+audio+video->text  (in: file,image,text,audio,video → out: text)
- **Pricing**: 入力 $0.3/1M · 出力 $2.50/1M · キャッシュ読 $0.03/1M · キャッシュ書 $0.0833/1M · 推論 $2.50/1M · 画像 $3e-07/枚 · 音声 $1.00/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-06-18
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Gemini 2.5 Flash is Google's state-of-the-art workhorse model, specifically designed for advanced reasoning, coding, mathematics, and scientific tasks. It includes built-in "thinking" capabilities, enabling it to provide responses with greater...

#### Google: Nano Banana (Gemini 2.5 Flash Image)

- **ID**: `google/gemini-2.5-flash-image`
- **Provider**: google
- **Context**: 32K (32,768) tok / max出力 32,768 tok
- **Modality**: text+image->text+image  (in: image,text → out: image,text)
- **Pricing**: 入力 $0.3/1M · 出力 $2.50/1M · キャッシュ読 $0.03/1M · キャッシュ書 $0.0833/1M · 推論 $2.50/1M · 画像 $3e-07/枚 · 音声 $1.00/1M · Web検索 $0.014
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-10-08
- **対応パラメータ**: max_tokens, response_format, seed, stop, structured_outputs, temperature, top_p

Gemini 2.5 Flash Image, a.k.a. "Nano Banana," is now generally available. It is a state of the art image generation model with contextual understanding. It is capable of image generation,...

#### Google: Gemini 2.5 Flash Lite

- **ID**: `google/gemini-2.5-flash-lite`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,535 tok
- **Modality**: text+image+file+audio+video->text  (in: text,image,file,audio,video → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.4/1M · キャッシュ読 $0.01/1M · キャッシュ書 $0.0833/1M · 推論 $0.4/1M · 画像 $1e-07/枚 · 音声 $0.3/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-07-23
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Gemini 2.5 Flash-Lite is a lightweight reasoning model in the Gemini 2.5 family, optimized for ultra-low latency and cost efficiency. It offers improved throughput, faster token generation, and better performance...

#### Google: Gemini 2.5 Flash Lite Preview 09-2025

- **ID**: `google/gemini-2.5-flash-lite-preview-09-2025`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,535 tok
- **Modality**: text+image+file+audio+video->text  (in: text,image,file,audio,video → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.4/1M · キャッシュ読 $0.01/1M · キャッシュ書 $0.0833/1M · 推論 $0.4/1M · 画像 $1e-07/枚 · 音声 $0.3/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-09-26
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Gemini 2.5 Flash-Lite is a lightweight reasoning model in the Gemini 2.5 family, optimized for ultra-low latency and cost efficiency. It offers improved throughput, faster token generation, and better performance...

#### Google: Gemini 2.5 Pro

- **ID**: `google/gemini-2.5-pro`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,536 tok
- **Modality**: text+image+file+audio+video->text  (in: text,image,file,audio,video → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $10.00/1M · キャッシュ読 $0.125/1M · キャッシュ書 $0.375/1M · 推論 $10.00/1M · 画像 $1.25e-06/枚 · 音声 $1.25/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-06-17
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Gemini 2.5 Pro is Google’s state-of-the-art AI model designed for advanced reasoning, coding, mathematics, and scientific tasks. It employs “thinking” capabilities, enabling it to reason through responses with enhanced accuracy...

#### Google: Gemini 2.5 Pro Preview 06-05

- **ID**: `google/gemini-2.5-pro-preview`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,536 tok
- **Modality**: text+image+file+audio->text  (in: file,image,text,audio → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $10.00/1M · キャッシュ読 $0.125/1M · キャッシュ書 $0.375/1M · 推論 $10.00/1M · 画像 $1.25e-06/枚 · 音声 $1.25/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-06-06
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Gemini 2.5 Pro is Google’s state-of-the-art AI model designed for advanced reasoning, coding, mathematics, and scientific tasks. It employs “thinking” capabilities, enabling it to reason through responses with enhanced accuracy...

#### Google: Gemini 2.5 Pro Preview 05-06

- **ID**: `google/gemini-2.5-pro-preview-05-06`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,535 tok
- **Modality**: text+image+file+audio+video->text  (in: text,image,file,audio,video → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $10.00/1M · キャッシュ読 $0.125/1M · キャッシュ書 $0.375/1M · 推論 $10.00/1M · 画像 $1.25e-06/枚 · 音声 $1.25/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-05-07
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Gemini 2.5 Pro is Google’s state-of-the-art AI model designed for advanced reasoning, coding, mathematics, and scientific tasks. It employs “thinking” capabilities, enabling it to reason through responses with enhanced accuracy...

#### Google: Gemini 3 Flash Preview

- **ID**: `google/gemini-3-flash-preview`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,536 tok
- **Modality**: text+image+file+audio+video->text  (in: text,image,file,audio,video → out: text)
- **Pricing**: 入力 $0.5/1M · 出力 $3.00/1M · キャッシュ読 $0.05/1M · キャッシュ書 $0.0833/1M · 推論 $3.00/1M · 画像 $5e-07/枚 · 音声 $1.00/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-12-18
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Gemini 3 Flash Preview is a high speed, high value thinking model designed for agentic workflows, multi turn chat, and coding assistance. It delivers near Pro level reasoning and tool...

#### Google: Nano Banana Pro (Gemini 3 Pro Image Preview)

- **ID**: `google/gemini-3-pro-image-preview`
- **Provider**: google
- **Context**: 65K (65,536) tok / max出力 32,768 tok
- **Modality**: text+image->text+image  (in: image,text → out: image,text)
- **Pricing**: 入力 $2.00/1M · 出力 $12.00/1M · キャッシュ読 $0.2/1M · キャッシュ書 $0.375/1M · 推論 $12.00/1M · 画像 $2e-06/枚 · 音声 $2.00/1M · Web検索 $0.014
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-11-21
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, top_p

Nano Banana Pro is Google’s most advanced image-generation and editing model, built on Gemini 3 Pro. It extends the original Nano Banana with significantly improved multimodal reasoning, real-world grounding, and...

#### Google: Nano Banana 2 (Gemini 3.1 Flash Image Preview)

- **ID**: `google/gemini-3.1-flash-image-preview`
- **Provider**: google
- **Context**: 131K (131,072) tok / max出力 65,536 tok
- **Modality**: text+image->text+image  (in: image,text → out: image,text)
- **Pricing**: 入力 $0.5/1M · 出力 $3.00/1M · Web検索 $0.014
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-02-27
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, top_p

Gemini 3.1 Flash Image Preview, a.k.a. "Nano Banana 2," is Google’s latest state of the art image generation and editing model, delivering Pro-level visual quality at Flash speed. It combines...

#### Google: Gemini 3.1 Flash Lite

- **ID**: `google/gemini-3.1-flash-lite`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,536 tok
- **Modality**: text+image+file+audio+video->text  (in: text,image,video,file,audio → out: text)
- **Pricing**: 入力 $0.25/1M · 出力 $1.50/1M · キャッシュ読 $0.025/1M · キャッシュ書 $0.0833/1M · 推論 $1.50/1M · 画像 $2.5e-07/枚 · 音声 $0.5/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-05-08
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Gemini 3.1 Flash Lite is Google’s GA high-efficiency multimodal model optimized for low-latency, high-volume workloads. It supports text, image, video, audio, and PDF inputs, and is designed for lightweight agentic...

#### Google: Gemini 3.1 Flash Lite Preview

- **ID**: `google/gemini-3.1-flash-lite-preview`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,536 tok
- **Modality**: text+image+file+audio+video->text  (in: text,image,video,file,audio → out: text)
- **Pricing**: 入力 $0.25/1M · 出力 $1.50/1M · キャッシュ読 $0.025/1M · キャッシュ書 $0.0833/1M · 推論 $1.50/1M · 画像 $2.5e-07/枚 · 音声 $0.5/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-03-03
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Gemini 3.1 Flash Lite Preview is Google's high-efficiency model optimized for high-volume use cases. It outperforms Gemini 2.5 Flash Lite on overall quality and approaches Gemini 2.5 Flash performance across...

#### Google: Gemini 3.1 Pro Preview

- **ID**: `google/gemini-3.1-pro-preview`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,536 tok
- **Modality**: text+image+file+audio+video->text  (in: audio,file,image,text,video → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $12.00/1M · キャッシュ読 $0.2/1M · キャッシュ書 $0.375/1M · 推論 $12.00/1M · 画像 $2e-06/枚 · 音声 $2.00/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-02-19
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Gemini 3.1 Pro Preview is Google’s frontier reasoning model, delivering enhanced software engineering performance, improved agentic reliability, and more efficient token usage across complex workflows. Building on the multimodal foundation...

#### Google: Gemini 3.1 Pro Preview Custom Tools

- **ID**: `google/gemini-3.1-pro-preview-customtools`
- **Provider**: google
- **Context**: 1.04876M (1,048,756) tok / max出力 65,536 tok
- **Modality**: text+image+file+audio+video->text  (in: text,audio,image,video,file → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $12.00/1M · キャッシュ読 $0.2/1M · キャッシュ書 $0.375/1M · 推論 $12.00/1M · 画像 $2e-06/枚 · 音声 $2.00/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-02-26
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Gemini 3.1 Pro Preview Custom Tools is a variant of Gemini 3.1 Pro that improves tool selection behavior by preventing overuse of a general bash tool when more efficient third-party...

#### Google: Gemini 3.5 Flash

- **ID**: `google/gemini-3.5-flash`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,536 tok
- **Modality**: text+image+file+audio+video->text  (in: text,image,video,file,audio → out: text)
- **Pricing**: 入力 $1.50/1M · 出力 $9.00/1M · キャッシュ読 $0.15/1M · キャッシュ書 $0.0833/1M · 推論 $9.00/1M · 画像 $1.5e-06/枚 · 音声 $3.00/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-01-01
- **登録日**: 2026-05-19
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Gemini 3.5 Flash is Google's high-efficiency multimodal model, bringing near-Pro level coding and reasoning at Flash-tier cost and speed. It is highly optimized for coding proficiency and parallel agentic execution...

#### Google: Gemma 2 27B

- **ID**: `google/gemma-2-27b-it`
- **Provider**: google
- **Context**: 8K (8,192) tok / max出力 2,048 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.65/1M · 出力 $0.65/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2024-07-13
- **HF**: `google/gemma-2-27b-it`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_p

Gemma 2 27B by Google is an open model built from the same research and technology used to create the [Gemini models](/models?q=gemini). Gemma models are well-suited for a variety of...

#### Google: Gemma 3 12B

- **ID**: `google/gemma-3-12b-it`
- **Provider**: google
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.04/1M · 出力 $0.13/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-08-31
- **登録日**: 2025-03-14
- **HF**: `google/gemma-3-12b-it`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Gemma 3 introduces multimodality, supporting vision-language input and text outputs. It handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities,...

#### Google: Gemma 3 27B

- **ID**: `google/gemma-3-27b-it`
- **Provider**: google
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.08/1M · 出力 $0.16/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-08-31
- **登録日**: 2025-03-12
- **HF**: `google/gemma-3-27b-it`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Gemma 3 introduces multimodality, supporting vision-language input and text outputs. It handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities,...

#### Google: Gemma 3 4B

- **ID**: `google/gemma-3-4b-it`
- **Provider**: google
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.04/1M · 出力 $0.08/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-08-31
- **登録日**: 2025-03-14
- **HF**: `google/gemma-3-4b-it`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_p

Gemma 3 introduces multimodality, supporting vision-language input and text outputs. It handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities,...

#### Google: Gemma 3n 4B

- **ID**: `google/gemma-3n-e4b-it`
- **Provider**: google
- **Context**: 32K (32,768) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.06/1M · 出力 $0.12/1M
- **Knowledge cutoff**: 2024-08-31
- **登録日**: 2025-05-21
- **HF**: `google/gemma-3n-E4B-it`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, stop, temperature, top_k, top_p

Gemma 3n E4B-it is optimized for efficient execution on mobile and low-resource devices, such as phones, laptops, and tablets. It supports multimodal inputs—including text, visual data, and audio—enabling diverse tasks...

#### Google: Gemma 4 26B A4B 

- **ID**: `google/gemma-4-26b-a4b-it`
- **Provider**: google
- **Context**: 262K (262,144) tok
- **Modality**: text+image+video->text  (in: image,text,video → out: text)
- **Pricing**: 入力 $0.06/1M · 出力 $0.33/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-04-03
- **HF**: `google/gemma-4-26B-A4B-it`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

Gemma 4 26B A4B IT is an instruction-tuned Mixture-of-Experts (MoE) model from Google DeepMind. Despite 25.2B total parameters, only 3.8B activate per token during inference — delivering near-31B quality at...

#### Google: Gemma 4 26B A4B  (free)

- **ID**: `google/gemma-4-26b-a4b-it:free`
- **Provider**: google
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text+image+video->text  (in: image,text,video → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-04-03
- **HF**: `google/gemma-4-26B-A4B-it`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, temperature, tool_choice, tools, top_p

Gemma 4 26B A4B IT is an instruction-tuned Mixture-of-Experts (MoE) model from Google DeepMind. Despite 25.2B total parameters, only 3.8B activate per token during inference — delivering near-31B quality at...

#### Google: Gemma 4 31B

- **ID**: `google/gemma-4-31b-it`
- **Provider**: google
- **Context**: 262K (262,144) tok / max出力 8,192 tok
- **Modality**: text+image+video->text  (in: image,text,video → out: text)
- **Pricing**: 入力 $0.12/1M · 出力 $0.36/1M · キャッシュ読 $0.09/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-04-03
- **HF**: `google/gemma-4-31B-it`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

Gemma 4 31B Instruct is Google DeepMind's 30.7B dense multimodal model supporting text and image input with text output. Features a 256K token context window, configurable thinking/reasoning mode, native function...

#### Google: Gemma 4 31B (free)

- **ID**: `google/gemma-4-31b-it:free`
- **Provider**: google
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text+image+video->text  (in: image,text,video → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-04-03
- **HF**: `google/gemma-4-31B-it`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, temperature, tool_choice, tools, top_p

Gemma 4 31B Instruct is Google DeepMind's 30.7B dense multimodal model supporting text and image input with text output. Features a 256K token context window, configurable thinking/reasoning mode, native function...

#### Google: Lyria 3 Clip Preview

- **ID**: `google/lyria-3-clip-preview`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,536 tok
- **Modality**: text+image->text+audio  (in: text,image → out: text,audio)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: JSON mode, Seed固定
- **登録日**: 2026-03-31
- **対応パラメータ**: max_tokens, response_format, seed, temperature, top_p

30 second duration clips are priced at $0.04 per clip. Lyria 3 is Google's family of music generation models, available through the Gemini API. With Lyria 3, you can generate...

#### Google: Lyria 3 Pro Preview

- **ID**: `google/lyria-3-pro-preview`
- **Provider**: google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,536 tok
- **Modality**: text+image->text+audio  (in: text,image → out: text,audio)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: JSON mode, Seed固定
- **登録日**: 2026-03-31
- **対応パラメータ**: max_tokens, response_format, seed, temperature, top_p

Full-length songs are priced at $0.08 per song. Lyria 3 is Google's family of music generation models, available through the Gemini API. With Lyria 3, you can generate high-quality, 48kHz...

### ▎gryphe（1）

#### MythoMax 13B

- **ID**: `gryphe/mythomax-l2-13b`
- **Provider**: gryphe
- **Context**: 4K (4,096) tok / max出力 4,096 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.06/1M · 出力 $0.06/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2023-06-30
- **登録日**: 2023-07-02
- **HF**: `Gryphe/MythoMax-L2-13b`
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_a, top_k, top_logprobs, top_p

One of the highest performing and most popular fine-tunes of Llama 2 13B, with rich descriptions and roleplay. #merge

### ▎ibm-granite（2）

#### IBM: Granite 4.0 Micro

- **ID**: `ibm-granite/granite-4.0-h-micro`
- **Provider**: ibm-granite
- **Context**: 131K (131,000) tok / max出力 131,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.017/1M · 出力 $0.112/1M
- **Capabilities**: Seed固定
- **登録日**: 2025-10-20
- **HF**: `ibm-granite/granite-4.0-h-micro`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p

Granite-4.0-H-Micro is a 3B parameter from the Granite 4 family of models. These models are the latest in a series of models released by IBM. They are fine-tuned for long...

#### IBM: Granite 4.1 8B

- **ID**: `ibm-granite/granite-4.1-8b`
- **Provider**: ibm-granite
- **Context**: 131K (131,072) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.05/1M · 出力 $0.1/1M · キャッシュ読 $0.05/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2026-05-01
- **HF**: `ibm-granite/granite-4.1-8b`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Granite 4.1 8B is a dense, decoder-only 8-billion-parameter language model from IBM, part of the Granite 4.1 family. It supports a 131K-token context window and is designed for enterprise tasks...

### ▎inception（1）

#### Inception: Mercury 2

- **ID**: `inception/mercury-2`
- **Provider**: inception
- **Context**: 128K (128,000) tok / max出力 50,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.25/1M · 出力 $0.75/1M · キャッシュ読 $0.025/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-03-04
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools

Mercury 2 is an extremely fast reasoning LLM, and the first reasoning diffusion LLM (dLLM). Instead of generating tokens sequentially, Mercury 2 produces and refines multiple tokens in parallel, achieving...

### ▎inclusionai（3）

#### inclusionAI: Ling-2.6-1T

- **ID**: `inclusionai/ling-2.6-1t`
- **Provider**: inclusionai
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.075/1M · 出力 $0.625/1M · キャッシュ読 $0.015/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2026-04-23
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Ling-2.6-1T is an instant (instruct) model from inclusionAI and the company’s trillion-parameter flagship, designed for real-world agents that require fast execution and high efficiency at scale. It uses a “fast...

#### inclusionAI: Ling-2.6-flash

- **ID**: `inclusionai/ling-2.6-flash`
- **Provider**: inclusionai
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.01/1M · 出力 $0.03/1M · キャッシュ読 $0.002/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2026-04-22
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Ling-2.6-flash is an instant (instruct) model from inclusionAI with 104B total parameters and 7.4B active parameters, designed for real-world agents that require fast responses, strong execution, and high token efficiency....

#### inclusionAI: Ring-2.6-1T

- **ID**: `inclusionai/ring-2.6-1t`
- **Provider**: inclusionai
- **Context**: 262K (262,144) tok / max出力 65,536 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.075/1M · 出力 $0.625/1M · キャッシュ読 $0.015/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-05-08
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p

Ring-2.6-1T is a 1T-parameter-scale thinking model with 63B active parameters, built for real-world agent workflows that require both strong capability and operational efficiency. It is optimized for coding agents, tool...

### ▎inflection（2）

#### Inflection: Inflection 3 Pi

- **ID**: `inflection/inflection-3-pi`
- **Provider**: inflection
- **Context**: 8K (8,000) tok / max出力 1,024 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $2.50/1M · 出力 $10.00/1M
- **Knowledge cutoff**: 2024-10-31
- **登録日**: 2024-10-11
- **対応パラメータ**: max_tokens, stop, temperature, top_p

Inflection 3 Pi powers Inflection's [Pi](https://pi.ai) chatbot, including backstory, emotional intelligence, productivity, and safety. It has access to recent news, and excels in scenarios like customer support and roleplay. Pi...

#### Inflection: Inflection 3 Productivity

- **ID**: `inflection/inflection-3-productivity`
- **Provider**: inflection
- **Context**: 8K (8,000) tok / max出力 1,024 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $2.50/1M · 出力 $10.00/1M
- **Knowledge cutoff**: 2024-10-31
- **登録日**: 2024-10-11
- **対応パラメータ**: max_tokens, stop, temperature, top_p

Inflection 3 Productivity is optimized for following instructions. It is better for tasks requiring JSON output or precise adherence to provided guidelines. It has access to recent news. For emotional...

### ▎kwaipilot（1）

#### Kwaipilot: KAT-Coder-Pro V2

- **ID**: `kwaipilot/kat-coder-pro-v2`
- **Provider**: kwaipilot
- **Context**: 256K (256,000) tok / max出力 80,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.3/1M · 出力 $1.20/1M · キャッシュ読 $0.06/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2026-03-28
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

KAT-Coder-Pro V2 is the latest high-performance model in KwaiKAT’s KAT-Coder series, designed for complex enterprise-grade software engineering and SaaS integration. It builds on the agentic coding strengths of earlier versions,...

### ▎liquid（3）

#### LiquidAI: LFM2-24B-A2B

- **ID**: `liquid/lfm-2-24b-a2b`
- **Provider**: liquid
- **Context**: 128K (128,000) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.03/1M · 出力 $0.12/1M
- **登録日**: 2026-02-26
- **HF**: `LiquidAI/LFM2-24B-A2B`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, stop, temperature, top_k, top_p

LFM2-24B-A2B is the largest model in the LFM2 family of hybrid architectures designed for efficient on-device deployment. Built as a 24B parameter Mixture-of-Experts model with only 2B active parameters per...

#### LiquidAI: LFM2.5-1.2B-Instruct (free)

- **ID**: `liquid/lfm-2.5-1.2b-instruct:free`
- **Provider**: liquid
- **Context**: 32K (32,768) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Seed固定
- **登録日**: 2026-01-21
- **HF**: `LiquidAI/LFM2.5-1.2B-Instruct`
- **対応パラメータ**: frequency_penalty, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p

LFM2.5-1.2B-Instruct is a compact, high-performance instruction-tuned model built for fast on-device AI. It delivers strong chat quality in a 1.2B parameter footprint, with efficient edge inference and broad runtime support.

#### LiquidAI: LFM2.5-1.2B-Thinking (free)

- **ID**: `liquid/lfm-2.5-1.2b-thinking:free`
- **Provider**: liquid
- **Context**: 32K (32,768) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-01-21
- **HF**: `LiquidAI/LFM2.5-1.2B-Thinking`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, seed, stop, temperature, top_k, top_p

LFM2.5-1.2B-Thinking is a lightweight reasoning-focused model optimized for agentic tasks, data extraction, and RAG—while still running comfortably on edge devices. It supports long context (up to 32K tokens) and is...

### ▎mancer（1）

#### Mancer: Weaver (alpha)

- **ID**: `mancer/weaver`
- **Provider**: mancer
- **Context**: 8K (8,000) tok / max出力 2,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.75/1M · 出力 $1.00/1M
- **Capabilities**: JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2023-06-30
- **登録日**: 2023-08-02
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, temperature, top_a, top_k, top_logprobs, top_p

An attempt to recreate Claude-style verbosity, but don't expect the same level of coherence or memory. Meant for use in roleplay/narrative situations.

### ▎meta-llama（14）

#### Meta: Llama 3 70B Instruct

- **ID**: `meta-llama/llama-3-70b-instruct`
- **Provider**: meta-llama
- **Context**: 8K (8,192) tok / max出力 8,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.51/1M · 出力 $0.74/1M
- **Capabilities**: Structured outputs(JSONスキーマ), Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-04-18
- **HF**: `meta-llama/Meta-Llama-3-70B-Instruct`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, repetition_penalty, seed, stop, structured_outputs, temperature, top_k, top_p

Meta's latest class of model (Llama 3) launched with a variety of sizes & flavors. This 70B instruct-tuned version was optimized for high quality dialogue usecases. It has demonstrated strong...

#### Meta: Llama 3 8B Instruct

- **ID**: `meta-llama/llama-3-8b-instruct`
- **Provider**: meta-llama
- **Context**: 8K (8,192) tok / max出力 8,192 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.04/1M · 出力 $0.04/1M
- **Capabilities**: JSON mode, Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-04-18
- **HF**: `meta-llama/Meta-Llama-3-8B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, temperature, top_k, top_p

Meta's latest class of model (Llama 3) launched with a variety of sizes & flavors. This 8B instruct-tuned version was optimized for high quality dialogue usecases. It has demonstrated strong...

#### Meta: Llama 3.1 70B Instruct

- **ID**: `meta-llama/llama-3.1-70b-instruct`
- **Provider**: meta-llama
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.4/1M · 出力 $0.4/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-07-23
- **HF**: `meta-llama/Meta-Llama-3.1-70B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Meta's latest class of model (Llama 3.1) launched with a variety of sizes & flavors. This 70B instruct-tuned version is optimized for high quality dialogue usecases. It has demonstrated strong...

#### Meta: Llama 3.1 8B Instruct

- **ID**: `meta-llama/llama-3.1-8b-instruct`
- **Provider**: meta-llama
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.02/1M · 出力 $0.03/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-07-23
- **HF**: `meta-llama/Meta-Llama-3.1-8B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Meta's latest class of model (Llama 3.1) launched with a variety of sizes & flavors. This 8B instruct-tuned version is fast and efficient. It has demonstrated strong performance compared to...

#### Meta: Llama 3.2 11B Vision Instruct

- **ID**: `meta-llama/llama-3.2-11b-vision-instruct`
- **Provider**: meta-llama
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.245/1M · 出力 $0.245/1M
- **Capabilities**: JSON mode, Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-09-25
- **HF**: `meta-llama/Llama-3.2-11B-Vision-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, temperature, top_k, top_p

Llama 3.2 11B Vision is a multimodal model with 11 billion parameters, designed to handle tasks combining visual and textual data. It excels in tasks such as image captioning and...

#### Meta: Llama 3.2 1B Instruct

- **ID**: `meta-llama/llama-3.2-1b-instruct`
- **Provider**: meta-llama
- **Context**: 131K (131,072) tok / max出力 60,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.027/1M · 出力 $0.201/1M
- **Capabilities**: Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-09-25
- **HF**: `meta-llama/Llama-3.2-1B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p

Llama 3.2 1B is a 1-billion-parameter language model focused on efficiently performing natural language tasks, such as summarization, dialogue, and multilingual text analysis. Its smaller size allows it to operate...

#### Meta: Llama 3.2 3B Instruct

- **ID**: `meta-llama/llama-3.2-3b-instruct`
- **Provider**: meta-llama
- **Context**: 131K (131,072) tok / max出力 80,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.0509/1M · 出力 $0.335/1M
- **Capabilities**: Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-09-25
- **HF**: `meta-llama/Llama-3.2-3B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p

Llama 3.2 3B is a 3-billion-parameter multilingual large language model, optimized for advanced natural language processing tasks like dialogue generation, reasoning, and summarization. Designed with the latest transformer architecture, it...

#### Meta: Llama 3.2 3B Instruct (free)

- **ID**: `meta-llama/llama-3.2-3b-instruct:free`
- **Provider**: meta-llama
- **Context**: 131K (131,072) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-09-25
- **HF**: `meta-llama/Llama-3.2-3B-Instruct`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, stop, temperature, top_k, top_p

Llama 3.2 3B is a 3-billion-parameter multilingual large language model, optimized for advanced natural language processing tasks like dialogue generation, reasoning, and summarization. Designed with the latest transformer architecture, it...

#### Meta: Llama 3.3 70B Instruct

- **ID**: `meta-llama/llama-3.3-70b-instruct`
- **Provider**: meta-llama
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.32/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-12-07
- **HF**: `meta-llama/Llama-3.3-70B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

The Meta Llama 3.3 multilingual large language model (LLM) is a pretrained and instruction tuned generative model in 70B (text in/text out). The Llama 3.3 instruction tuned text only model...

#### Meta: Llama 3.3 70B Instruct (free)

- **ID**: `meta-llama/llama-3.3-70b-instruct:free`
- **Provider**: meta-llama
- **Context**: 131K (131,072) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-12-07
- **HF**: `meta-llama/Llama-3.3-70B-Instruct`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, stop, temperature, tool_choice, tools, top_k, top_p

The Meta Llama 3.3 multilingual large language model (LLM) is a pretrained and instruction tuned generative model in 70B (text in/text out). The Llama 3.3 instruction tuned text only model...

#### Meta: Llama 4 Maverick

- **ID**: `meta-llama/llama-4-maverick`
- **Provider**: meta-llama
- **Context**: 1.04858M (1,048,576) tok / max出力 16,384 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.15/1M · 出力 $0.6/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-08-31
- **登録日**: 2025-04-06
- **HF**: `meta-llama/Llama-4-Maverick-17B-128E-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Llama 4 Maverick 17B Instruct (128E) is a high-capacity multimodal language model from Meta, built on a mixture-of-experts (MoE) architecture with 128 experts and 17 billion active parameters per forward...

#### Meta: Llama 4 Scout

- **ID**: `meta-llama/llama-4-scout`
- **Provider**: meta-llama
- **Context**: 10M (10,000,000) tok / max出力 16,384 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.08/1M · 出力 $0.3/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-08-31
- **登録日**: 2025-04-06
- **HF**: `meta-llama/Llama-4-Scout-17B-16E-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Llama 4 Scout 17B Instruct (16E) is a mixture-of-experts (MoE) language model developed by Meta, activating 17 billion parameters out of a total of 109B. It supports native multimodal input...

#### Llama Guard 3 8B

- **ID**: `meta-llama/llama-guard-3-8b`
- **Provider**: meta-llama
- **Context**: 131K (131,072) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.484/1M · 出力 $0.03/1M
- **Capabilities**: Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2025-02-13
- **HF**: `meta-llama/Llama-Guard-3-8B`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p

Llama Guard 3 is a Llama-3.1-8B pretrained model, fine-tuned for content safety classification. Similar to previous versions, it can be used to classify content in both LLM inputs (prompt classification)...

#### Meta: Llama Guard 4 12B

- **ID**: `meta-llama/llama-guard-4-12b`
- **Provider**: meta-llama
- **Context**: 163K (163,840) tok / max出力 16,384 tok
- **Modality**: text+image->text  (in: image,text → out: text)
- **Pricing**: 入力 $0.18/1M · 出力 $0.18/1M
- **Capabilities**: JSON mode, Seed固定
- **Knowledge cutoff**: 2024-08-31
- **登録日**: 2025-04-30
- **HF**: `meta-llama/Llama-Guard-4-12B`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, temperature, top_k, top_p

Llama Guard 4 is a Llama 4 Scout-derived multimodal pretrained model, fine-tuned for content safety classification. Similar to previous versions, it can be used to classify content in both LLM...

### ▎microsoft（3）

#### Microsoft: Phi 4

- **ID**: `microsoft/phi-4`
- **Provider**: microsoft
- **Context**: 16K (16,384) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.065/1M · 出力 $0.14/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-01-10
- **HF**: `microsoft/phi-4`
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_logprobs, top_p

[Microsoft Research](/microsoft) Phi-4 is designed to perform well in complex reasoning tasks and can operate efficiently in situations with limited memory or where quick responses are needed. At 14 billion...

#### Microsoft: Phi 4 Mini Instruct

- **ID**: `microsoft/phi-4-mini-instruct`
- **Provider**: microsoft
- **Context**: 131K (131,072) tok / max出力 128,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.08/1M · 出力 $0.35/1M · キャッシュ読 $0.08/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2025-10-18
- **HF**: `microsoft/Phi-4-mini-instruct`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_p

Phi-4-mini-instruct is a lightweight open model built upon synthetic data and filtered publicly available websites - with a focus on high-quality, reasoning dense data. The model belongs to the Phi-4...

#### WizardLM-2 8x22B

- **ID**: `microsoft/wizardlm-2-8x22b`
- **Provider**: microsoft
- **Context**: 65K (65,536) tok / max出力 8,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.62/1M · 出力 $0.62/1M
- **Capabilities**: JSON mode, Seed固定
- **Knowledge cutoff**: 2024-04-30
- **登録日**: 2024-04-16
- **HF**: `microsoft/WizardLM-2-8x22B`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, temperature, top_k, top_p

WizardLM-2 8x22B is Microsoft AI's most advanced Wizard model. It demonstrates highly competitive performance compared to leading proprietary models, and it consistently outperforms all existing state-of-the-art opensource models. It is...

### ▎minimax（8）

#### MiniMax: MiniMax-01

- **ID**: `minimax/minimax-01`
- **Provider**: minimax
- **Context**: 1.00019M (1,000,192) tok / max出力 1,000,192 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.2/1M · 出力 $1.10/1M
- **Knowledge cutoff**: 2024-03-31
- **登録日**: 2025-01-15
- **HF**: `MiniMaxAI/MiniMax-Text-01`
- **対応パラメータ**: max_tokens, temperature, top_p

MiniMax-01 is a combines MiniMax-Text-01 for text generation and MiniMax-VL-01 for image understanding. It has 456 billion parameters, with 45.9 billion parameters activated per inference, and can handle a context...

#### MiniMax: MiniMax M1

- **ID**: `minimax/minimax-m1`
- **Provider**: minimax
- **Context**: 1M (1,000,000) tok / max出力 40,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.4/1M · 出力 $2.20/1M
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-06-18
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, seed, stop, temperature, tool_choice, tools, top_k, top_p

MiniMax-M1 is a large-scale, open-weight reasoning model designed for extended context and high-efficiency inference. It leverages a hybrid Mixture-of-Experts (MoE) architecture paired with a custom "lightning attention" mechanism, allowing it...

#### MiniMax: MiniMax M2

- **ID**: `minimax/minimax-m2`
- **Provider**: minimax
- **Context**: 204K (204,800) tok / max出力 196,608 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.255/1M · 出力 $1.00/1M · キャッシュ読 $0.03/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-10-24
- **HF**: `MiniMaxAI/MiniMax-M2`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

MiniMax-M2 is a compact, high-efficiency large language model optimized for end-to-end coding and agentic workflows. With 10 billion activated parameters (230 billion total), it delivers near-frontier intelligence across general reasoning,...

#### MiniMax: MiniMax M2-her

- **ID**: `minimax/minimax-m2-her`
- **Provider**: minimax
- **Context**: 65K (65,536) tok / max出力 2,048 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.3/1M · 出力 $1.20/1M · キャッシュ読 $0.03/1M
- **登録日**: 2026-01-23
- **対応パラメータ**: max_tokens, temperature, top_p

MiniMax M2-her is a dialogue-first large language model built for immersive roleplay, character-driven chat, and expressive multi-turn conversations. Designed to stay consistent in tone and personality, it supports rich message...

#### MiniMax: MiniMax M2.1

- **ID**: `minimax/minimax-m2.1`
- **Provider**: minimax
- **Context**: 204K (204,800) tok / max出力 196,608 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.29/1M · 出力 $0.95/1M · キャッシュ読 $0.03/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-12-23
- **HF**: `MiniMaxAI/MiniMax-M2.1`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

MiniMax-M2.1 is a lightweight, state-of-the-art large language model optimized for coding, agentic workflows, and modern application development. With only 10 billion activated parameters, it delivers a major jump in real-world...

#### MiniMax: MiniMax M2.5

- **ID**: `minimax/minimax-m2.5`
- **Provider**: minimax
- **Context**: 204K (204,800) tok / max出力 196,608 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.15/1M · 出力 $1.15/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-02-13
- **HF**: `MiniMaxAI/MiniMax-M2.5`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, parallel_tool_calls, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

MiniMax-M2.5 is a SOTA large language model designed for real-world productivity. Trained in a diverse range of complex real-world digital working environments, M2.5 builds upon the coding expertise of M2.1...

#### MiniMax: MiniMax M2.7

- **ID**: `minimax/minimax-m2.7`
- **Provider**: minimax
- **Context**: 204K (204,800) tok / max出力 196,608 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.279/1M · 出力 $1.20/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-03-18
- **HF**: `MiniMaxAI/MiniMax-M2.7`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

MiniMax-M2.7 is a next-generation large language model designed for autonomous, real-world productivity and continuous improvement. Built to actively participate in its own evolution, M2.7 integrates advanced agentic capabilities through multi-agent...

#### MiniMax: MiniMax M3

- **ID**: `minimax/minimax-m3`
- **Provider**: minimax
- **Context**: 1.04858M (1,048,576) tok / max出力 512,000 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.3/1M · 出力 $1.20/1M · キャッシュ読 $0.06/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-06-01
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, temperature, tool_choice, tools, top_p

MiniMax-M3 is a multimodal foundation model from MiniMax. It supports text, image, and video inputs with text output, a 1M-token context window, and is suited for long-horizon agentic work, coding,...

### ▎mistralai（19）

#### Mistral: Codestral 2508

- **ID**: `mistralai/codestral-2508`
- **Provider**: mistralai
- **Context**: 256K (256,000) tok
- **Modality**: text+file->text  (in: text,file → out: text)
- **Pricing**: 入力 $0.3/1M · 出力 $0.9/1M · キャッシュ読 $0.03/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-08-02
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Mistral's cutting-edge language model for coding released end of July 2025. Codestral specializes in low-latency, high-frequency tasks such as fill-in-the-middle (FIM), code correction and test generation.

[Blog Post](https://mistral.ai/news/codestral-25-08)

#### Mistral: Devstral 2 2512

- **ID**: `mistralai/devstral-2512`
- **Provider**: mistralai
- **Context**: 262K (262,144) tok
- **Modality**: text+file->text  (in: text,file → out: text)
- **Pricing**: 入力 $0.4/1M · 出力 $2.00/1M · キャッシュ読 $0.04/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2025-12-09
- **HF**: `mistralai/Devstral-2-123B-Instruct-2512`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Devstral 2 is a state-of-the-art open-source model by Mistral AI specializing in agentic coding. It is a 123B-parameter dense transformer model supporting a 256K context window. Devstral 2 supports exploring...

#### Mistral: Ministral 3 14B 2512

- **ID**: `mistralai/ministral-14b-2512`
- **Provider**: mistralai
- **Context**: 262K (262,144) tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.2/1M · 出力 $0.2/1M · キャッシュ読 $0.02/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **登録日**: 2025-12-02
- **HF**: `mistralai/Ministral-3-14B-Instruct-2512`
- **対応パラメータ**: frequency_penalty, logprobs, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

The largest model in the Ministral 3 family, Ministral 3 14B offers frontier capabilities and performance comparable to its larger Mistral Small 3.2 24B counterpart. A powerful and efficient language...

#### Mistral: Ministral 3 3B 2512

- **ID**: `mistralai/ministral-3b-2512`
- **Provider**: mistralai
- **Context**: 131K (131,072) tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.1/1M · キャッシュ読 $0.01/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **登録日**: 2025-12-02
- **HF**: `mistralai/Ministral-3-3B-Instruct-2512`
- **対応パラメータ**: frequency_penalty, logprobs, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

The smallest model in the Ministral 3 family, Ministral 3 3B is a powerful, efficient tiny language model with vision capabilities.

#### Mistral: Ministral 3 8B 2512

- **ID**: `mistralai/ministral-8b-2512`
- **Provider**: mistralai
- **Context**: 262K (262,144) tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.15/1M · 出力 $0.15/1M · キャッシュ読 $0.015/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **登録日**: 2025-12-02
- **HF**: `mistralai/Ministral-3-8B-Instruct-2512`
- **対応パラメータ**: frequency_penalty, logprobs, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

A balanced model in the Ministral 3 family, Ministral 3 8B is a powerful, efficient tiny language model with vision capabilities.

#### Mistral Large

- **ID**: `mistralai/mistral-large`
- **Provider**: mistralai
- **Context**: 128K (128,000) tok
- **Modality**: text+file->text  (in: text,file → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $6.00/1M · キャッシュ読 $0.2/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-11-30
- **登録日**: 2024-02-26
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

This is Mistral AI's flagship model, Mistral Large 2 (version `mistral-large-2407`). It's a proprietary weights-available model and excels at reasoning, code, JSON, chat, and more. Read the launch announcement [here](https://mistral.ai/news/mistral-large-2407/)....

#### Mistral Large 2407

- **ID**: `mistralai/mistral-large-2407`
- **Provider**: mistralai
- **Context**: 131K (131,072) tok
- **Modality**: text+file->text  (in: text,file → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $6.00/1M · キャッシュ読 $0.2/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-03-31
- **登録日**: 2024-11-19
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

This is Mistral AI's flagship model, Mistral Large 2 (version mistral-large-2407). It's a proprietary weights-available model and excels at reasoning, code, JSON, chat, and more. Read the launch announcement [here](https://mistral.ai/news/mistral-large-2407/)....

#### Mistral: Mistral Large 3 2512

- **ID**: `mistralai/mistral-large-2512`
- **Provider**: mistralai
- **Context**: 262K (262,144) tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $0.5/1M · 出力 $1.50/1M · キャッシュ読 $0.05/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2025-12-02
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Mistral Large 3 2512 is Mistral’s most capable model to date, featuring a sparse mixture-of-experts architecture with 41B active parameters (675B total), and released under the Apache 2.0 license.

#### Mistral: Mistral Medium 3

- **ID**: `mistralai/mistral-medium-3`
- **Provider**: mistralai
- **Context**: 131K (131,072) tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $0.4/1M · 出力 $2.00/1M · キャッシュ読 $0.04/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-05-07
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Mistral Medium 3 is a high-performance enterprise-grade language model designed to deliver frontier-level capabilities at significantly reduced operational cost. It balances state-of-the-art reasoning and multimodal performance with 8× lower cost...

#### Mistral: Mistral Medium 3.5

- **ID**: `mistralai/mistral-medium-3-5`
- **Provider**: mistralai
- **Context**: 262K (262,144) tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $1.50/1M · 出力 $7.50/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-05-01
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Mistral Medium 3.5 is a dense 128B instruction-following model from Mistral AI. It supports text and image inputs with text output, and is designed for agentic workflows, coding, and complex...

#### Mistral: Mistral Medium 3.1

- **ID**: `mistralai/mistral-medium-3.1`
- **Provider**: mistralai
- **Context**: 131K (131,072) tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $0.4/1M · 出力 $2.00/1M · キャッシュ読 $0.04/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-06-30
- **登録日**: 2025-08-13
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Mistral Medium 3.1 is an updated version of Mistral Medium 3, which is a high-performance enterprise-grade language model designed to deliver frontier-level capabilities at significantly reduced operational cost. It balances...

#### Mistral: Mistral Nemo

- **ID**: `mistralai/mistral-nemo`
- **Provider**: mistralai
- **Context**: 131K (131,072) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.02/1M · 出力 $0.03/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-04-30
- **登録日**: 2024-07-19
- **HF**: `mistralai/Mistral-Nemo-Instruct-2407`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

A 12B parameter model with a 128k token context length built by Mistral in collaboration with NVIDIA. The model is multilingual, supporting English, French, German, Spanish, Italian, Portuguese, Chinese, Japanese,...

#### Mistral: Saba

- **ID**: `mistralai/mistral-saba`
- **Provider**: mistralai
- **Context**: 32K (32,768) tok
- **Modality**: text+file->text  (in: text,file → out: text)
- **Pricing**: 入力 $0.2/1M · 出力 $0.6/1M · キャッシュ読 $0.02/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-09-30
- **登録日**: 2025-02-17
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Mistral Saba is a 24B-parameter language model specifically designed for the Middle East and South Asia, delivering accurate and contextually relevant responses while maintaining efficient performance. Trained on curated regional...

#### Mistral: Mistral Small 3

- **ID**: `mistralai/mistral-small-24b-instruct-2501`
- **Provider**: mistralai
- **Context**: 32K (32,768) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.05/1M · 出力 $0.08/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2025-01-31
- **HF**: `mistralai/Mistral-Small-24B-Instruct-2501`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_p

Mistral Small 3 is a 24B-parameter language model optimized for low-latency performance across common AI tasks. Released under the Apache 2.0 license, it features both pre-trained and instruction-tuned versions designed...

#### Mistral: Mistral Small 4

- **ID**: `mistralai/mistral-small-2603`
- **Provider**: mistralai
- **Context**: 262K (262,144) tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.15/1M · 出力 $0.6/1M · キャッシュ読 $0.015/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-03-17
- **HF**: `mistralai/Mistral-Small-4-119B-2603`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Mistral Small 4 is the next major release in the Mistral Small family, unifying the capabilities of several flagship Mistral models into a single system. It combines strong reasoning from...

#### Mistral: Mistral Small 3.1 24B

- **ID**: `mistralai/mistral-small-3.1-24b-instruct`
- **Provider**: mistralai
- **Context**: 128K (128,000) tok / max出力 128,000 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.351/1M · 出力 $0.555/1M
- **Capabilities**: Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2025-03-18
- **HF**: `mistralai/Mistral-Small-3.1-24B-Instruct-2503`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p

Mistral Small 3.1 24B Instruct is an upgraded variant of Mistral Small 3 (2501), featuring 24 billion parameters with advanced multimodal capabilities. It provides state-of-the-art performance in text-based reasoning and...

#### Mistral: Mistral Small 3.2 24B

- **ID**: `mistralai/mistral-small-3.2-24b-instruct`
- **Provider**: mistralai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text+image->text  (in: image,text → out: text)
- **Pricing**: 入力 $0.075/1M · 出力 $0.2/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2025-06-21
- **HF**: `mistralai/Mistral-Small-3.2-24B-Instruct-2506`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Mistral-Small-3.2-24B-Instruct-2506 is an updated 24B parameter model from Mistral optimized for instruction following, repetition reduction, and improved function calling. Compared to the 3.1 release, version 3.2 significantly improves accuracy on...

#### Mistral: Mixtral 8x22B Instruct

- **ID**: `mistralai/mixtral-8x22b-instruct`
- **Provider**: mistralai
- **Context**: 65K (65,536) tok
- **Modality**: text+file->text  (in: text,file → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $6.00/1M · キャッシュ読 $0.2/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-01-31
- **登録日**: 2024-04-17
- **HF**: `mistralai/Mixtral-8x22B-Instruct-v0.1`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Mistral's official instruct fine-tuned version of [Mixtral 8x22B](/models/mistralai/mixtral-8x22b). It uses 39B active parameters out of 141B, offering unparalleled cost efficiency for its size. Its strengths include: - strong math, coding,...

#### Mistral: Voxtral Small 24B 2507

- **ID**: `mistralai/voxtral-small-24b-2507`
- **Provider**: mistralai
- **Context**: 32K (32,000) tok
- **Modality**: text+file+audio->text  (in: text,audio,file → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.3/1M · キャッシュ読 $0.01/1M · 音声 $100.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2025-10-30
- **HF**: `mistralai/Voxtral-Small-24B-2507`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

Voxtral Small is an enhancement of Mistral Small 3, incorporating state-of-the-art audio input capabilities while retaining best-in-class text performance. It excels at speech transcription, translation and audio understanding. Input audio...

### ▎moonshotai（6）

#### MoonshotAI: Kimi K2 0711

- **ID**: `moonshotai/kimi-k2`
- **Provider**: moonshotai
- **Context**: 131K (131,072) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.57/1M · 出力 $2.30/1M
- **Capabilities**: Function calling, Tool choice, Seed固定
- **Knowledge cutoff**: 2024-12-31
- **登録日**: 2025-07-12
- **HF**: `moonshotai/Kimi-K2-Instruct`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, repetition_penalty, seed, stop, temperature, tool_choice, tools, top_k, top_p

Kimi K2 Instruct is a large-scale Mixture-of-Experts (MoE) language model developed by Moonshot AI, featuring 1 trillion total parameters with 32 billion active per forward pass. It is optimized for...

#### MoonshotAI: Kimi K2 0905

- **ID**: `moonshotai/kimi-k2-0905`
- **Provider**: moonshotai
- **Context**: 262K (262,144) tok / max出力 262,144 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.6/1M · 出力 $2.50/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-12-31
- **登録日**: 2025-09-05
- **HF**: `moonshotai/Kimi-K2-Instruct-0905`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Kimi K2 0905 is the September update of [Kimi K2 0711](moonshotai/kimi-k2). It is a large-scale Mixture-of-Experts (MoE) language model developed by Moonshot AI, featuring 1 trillion total parameters with 32...

#### MoonshotAI: Kimi K2 Thinking

- **ID**: `moonshotai/kimi-k2-thinking`
- **Provider**: moonshotai
- **Context**: 262K (262,144) tok / max出力 262,144 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.6/1M · 出力 $2.50/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-11-06
- **HF**: `moonshotai/Kimi-K2-Thinking`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Kimi K2 Thinking is Moonshot AI’s most advanced open reasoning model to date, extending the K2 series into agentic, long-horizon reasoning. Built on the trillion-parameter Mixture-of-Experts (MoE) architecture introduced in...

#### MoonshotAI: Kimi K2.5

- **ID**: `moonshotai/kimi-k2.5`
- **Provider**: moonshotai
- **Context**: 262K (262,144) tok / max出力 262,144 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.4/1M · 出力 $1.90/1M · キャッシュ読 $0.09/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-01-27
- **HF**: `moonshotai/Kimi-K2.5`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

Kimi K2.5 is Moonshot AI's native multimodal model, delivering state-of-the-art visual coding capability and a self-directed agent swarm paradigm. Built on Kimi K2 with continued pretraining over approximately 15T mixed...

#### MoonshotAI: Kimi K2.6

- **ID**: `moonshotai/kimi-k2.6`
- **Provider**: moonshotai
- **Context**: 262K (262,144) tok / max出力 262,144 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.684/1M · 出力 $3.42/1M · キャッシュ読 $0.144/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-04-21
- **HF**: `moonshotai/Kimi-K2.6`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, parallel_tool_calls, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

Kimi K2.6 is Moonshot AI's next-generation multimodal model, designed for long-horizon coding, coding-driven UI/UX generation, and multi-agent orchestration. It handles complex end-to-end coding tasks across Python, Rust, and Go, and...

#### MoonshotAI: Kimi K2.6 (free)

- **ID**: `moonshotai/kimi-k2.6:free`
- **Provider**: moonshotai
- **Context**: 262K (262,144) tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力
- **登録日**: 2026-04-21
- **HF**: `moonshotai/Kimi-K2.6`
- **対応パラメータ**: include_reasoning, reasoning, tool_choice, tools

Kimi K2.6 is Moonshot AI's next-generation multimodal model, designed for long-horizon coding, coding-driven UI/UX generation, and multi-agent orchestration. It handles complex end-to-end coding tasks across Python, Rust, and Go, and...

### ▎morph（2）

#### Morph: Morph V3 Fast

- **ID**: `morph/morph-v3-fast`
- **Provider**: morph
- **Context**: 81K (81,920) tok / max出力 38,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.8/1M · 出力 $1.20/1M
- **登録日**: 2025-07-08
- **対応パラメータ**: max_tokens, stop, temperature

Morph's fastest apply model for code edits. ~10,500 tokens/sec with 96% accuracy for rapid code transformations. The model requires the prompt to be in the following format: <instruction>{instruction}</instruction> <code>{initial_code}</code> <update>{edit_snippet}</update>...

#### Morph: Morph V3 Large

- **ID**: `morph/morph-v3-large`
- **Provider**: morph
- **Context**: 262K (262,144) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.9/1M · 出力 $1.90/1M
- **登録日**: 2025-07-08
- **対応パラメータ**: max_tokens, stop, temperature

Morph's high-accuracy apply model for complex code edits. ~4,500 tokens/sec with 98% accuracy for precise code transformations. The model requires the prompt to be in the following format: <instruction>{instruction}</instruction> <code>{initial_code}</code>...

### ▎nex-agi（1）

#### Nex AGI: DeepSeek V3.1 Nex N1

- **ID**: `nex-agi/deepseek-v3.1-nex-n1`
- **Provider**: nex-agi
- **Context**: 131K (131,072) tok / max出力 163,840 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.135/1M · 出力 $0.5/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode
- **登録日**: 2025-12-08
- **HF**: `nex-agi/DeepSeek-V3.1-Nex-N1`
- **対応パラメータ**: frequency_penalty, max_tokens, response_format, structured_outputs, temperature, tool_choice, tools, top_k, top_p

DeepSeek V3.1 Nex-N1 is the flagship release of the Nex-N1 series — a post-trained model designed to highlight agent autonomy, tool use, and real-world productivity. Nex-N1 demonstrates competitive performance across...

### ▎nousresearch（5）

#### Nous: Hermes 3 405B Instruct

- **ID**: `nousresearch/hermes-3-llama-3.1-405b`
- **Provider**: nousresearch
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $1.00/1M · 出力 $1.00/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-08-16
- **HF**: `NousResearch/Hermes-3-Llama-3.1-405B`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_p

Hermes 3 is a generalist language model with many improvements over Hermes 2, including advanced agentic capabilities, much better roleplaying, reasoning, multi-turn conversation, long context coherence, and improvements across the...

#### Nous: Hermes 3 405B Instruct (free)

- **ID**: `nousresearch/hermes-3-llama-3.1-405b:free`
- **Provider**: nousresearch
- **Context**: 131K (131,072) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-08-16
- **HF**: `NousResearch/Hermes-3-Llama-3.1-405B`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, stop, temperature, top_k, top_p

Hermes 3 is a generalist language model with many improvements over Hermes 2, including advanced agentic capabilities, much better roleplaying, reasoning, multi-turn conversation, long context coherence, and improvements across the...

#### Nous: Hermes 3 70B Instruct

- **ID**: `nousresearch/hermes-3-llama-3.1-70b`
- **Provider**: nousresearch
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.3/1M · 出力 $0.3/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-08-18
- **HF**: `NousResearch/Hermes-3-Llama-3.1-70B`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_p

Hermes 3 is a generalist language model with many improvements over [Hermes 2](/models/nousresearch/nous-hermes-2-mistral-7b-dpo), including advanced agentic capabilities, much better roleplaying, reasoning, multi-turn conversation, long context coherence, and improvements across the...

#### Nous: Hermes 4 405B

- **ID**: `nousresearch/hermes-4-405b`
- **Provider**: nousresearch
- **Context**: 131K (131,072) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $1.00/1M · 出力 $3.00/1M
- **Capabilities**: JSON mode, Reasoning(思考), Reasoning出力
- **Knowledge cutoff**: 2024-08-31
- **登録日**: 2025-08-27
- **HF**: `NousResearch/Hermes-4-405B`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, temperature, top_k, top_p

Hermes 4 is a large-scale reasoning model built on Meta-Llama-3.1-405B and released by Nous Research. It introduces a hybrid reasoning mode, where the model can choose to deliberate internally with...

#### Nous: Hermes 4 70B

- **ID**: `nousresearch/hermes-4-70b`
- **Provider**: nousresearch
- **Context**: 131K (131,072) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.13/1M · 出力 $0.4/1M
- **Capabilities**: JSON mode, Reasoning(思考), Reasoning出力
- **Knowledge cutoff**: 2024-08-31
- **登録日**: 2025-08-27
- **HF**: `NousResearch/Hermes-4-70B`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, temperature, top_k, top_p

Hermes 4 70B is a hybrid reasoning model from Nous Research, built on Meta-Llama-3.1-70B. It introduces the same hybrid mode as the larger 405B release, allowing the model to either...

### ▎nvidia（12）

#### NVIDIA: Llama 3.3 Nemotron Super 49B V1.5

- **ID**: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- **Provider**: nvidia
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.4/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-03-31
- **登録日**: 2025-10-10
- **HF**: `nvidia/Llama-3_3-Nemotron-Super-49B-v1_5`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p

Llama-3.3-Nemotron-Super-49B-v1.5 is a 49B-parameter, English-centric reasoning/chat model derived from Meta’s Llama-3.3-70B-Instruct with a 128K context. It’s post-trained for agentic workflows (RAG, tool calling) via SFT across math, code, science, and...

#### NVIDIA: Nemotron 3 Nano 30B A3B

- **ID**: `nvidia/nemotron-3-nano-30b-a3b`
- **Provider**: nvidia
- **Context**: 262K (262,144) tok / max出力 228,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.05/1M · 出力 $0.2/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-12-15
- **HF**: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p

NVIDIA Nemotron 3 Nano 30B A3B is a small language MoE model with highest compute efficiency and accuracy for developers to build specialized agentic AI systems. The model is fully...

#### NVIDIA: Nemotron 3 Nano 30B A3B (free)

- **ID**: `nvidia/nemotron-3-nano-30b-a3b:free`
- **Provider**: nvidia
- **Context**: 256K (256,000) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-12-15
- **HF**: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, seed, temperature, tool_choice, tools, top_p

NVIDIA Nemotron 3 Nano 30B A3B is a small language MoE model with highest compute efficiency and accuracy for developers to build specialized agentic AI systems. The model is fully...

#### NVIDIA: Nemotron 3 Nano Omni (free)

- **ID**: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- **Provider**: nvidia
- **Context**: 256K (256,000) tok / max出力 65,536 tok
- **Modality**: text+image+audio+video->text  (in: text,audio,image,video → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-04-29
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, seed, temperature, tool_choice, tools, top_p

NVIDIA Nemotron™ 3 Nano Omni is a 30B-A3B open multimodal model designed to function as a perception and context sub-agent in enterprise agent systems. It accepts text, image, video, and...

#### NVIDIA: Nemotron 3 Super

- **ID**: `nvidia/nemotron-3-super-120b-a12b`
- **Provider**: nvidia
- **Context**: 1M (1,000,000) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.09/1M · 出力 $0.45/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-03-12
- **HF**: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_logprobs, top_p

NVIDIA Nemotron 3 Super is a 120B-parameter open hybrid MoE model, activating just 12B parameters for maximum compute efficiency and accuracy in complex multi-agent applications. Built on a hybrid Mamba-Transformer...

#### NVIDIA: Nemotron 3 Super (free)

- **ID**: `nvidia/nemotron-3-super-120b-a12b:free`
- **Provider**: nvidia
- **Context**: 1M (1,000,000) tok / max出力 262,144 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-03-12
- **HF**: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

NVIDIA Nemotron 3 Super is a 120B-parameter open hybrid MoE model, activating just 12B parameters for maximum compute efficiency and accuracy in complex multi-agent applications. Built on a hybrid Mamba-Transformer...

#### NVIDIA: Nemotron 3 Ultra

- **ID**: `nvidia/nemotron-3-ultra-550b-a55b`
- **Provider**: nvidia
- **Context**: 1M (1,000,000) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.5/1M · 出力 $2.50/1M · キャッシュ読 $0.15/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-06-04
- **HF**: `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

NVIDIA Nemotron 3 Ultra is an open frontier-reasoning and orchestration model from NVIDIA, with 55B active parameters out of 550B total (MoE). Built on a hybrid Transformer-Mamba mixture-of-experts architecture, it...

#### NVIDIA: Nemotron 3 Ultra (free)

- **ID**: `nvidia/nemotron-3-ultra-550b-a55b:free`
- **Provider**: nvidia
- **Context**: 1M (1,000,000) tok / max出力 65,536 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-06-04
- **HF**: `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, seed, temperature, tool_choice, tools, top_p

NVIDIA Nemotron 3 Ultra is an open frontier-reasoning and orchestration model from NVIDIA, with 55B active parameters out of 550B total (MoE). Built on a hybrid Transformer-Mamba mixture-of-experts architecture, it...

#### NVIDIA: Nemotron 3.5 Content Safety (free)

- **ID**: `nvidia/nemotron-3.5-content-safety:free`
- **Provider**: nvidia
- **Context**: 128K (128,000) tok / max出力 8,192 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-06-04
- **HF**: `nvidia/Nemotron-3.5-Content-Safety`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, seed, temperature, top_p

NVIDIA Nemotron 3.5 Content Safety is a compact 4B-parameter multimodal guardrail model from NVIDIA, fine-tuned from Google Gemma-3-4B. It moderates both inputs to and responses from LLMs and VLMs, accepting...

#### NVIDIA: Nemotron Nano 12B 2 VL (free)

- **ID**: `nvidia/nemotron-nano-12b-v2-vl:free`
- **Provider**: nvidia
- **Context**: 128K (128,000) tok / max出力 128,000 tok
- **Modality**: text+image+video->text  (in: image,text,video → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-10-29
- **HF**: `nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, seed, temperature, tool_choice, tools, top_p

NVIDIA Nemotron Nano 2 VL is a 12-billion-parameter open multimodal reasoning model designed for video understanding and document intelligence. It introduces a hybrid Transformer-Mamba architecture, combining transformer-level accuracy with Mamba’s...

#### NVIDIA: Nemotron Nano 9B V2

- **ID**: `nvidia/nemotron-nano-9b-v2`
- **Provider**: nvidia
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.04/1M · 出力 $0.16/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-09-06
- **HF**: `nvidia/NVIDIA-Nemotron-Nano-9B-v2`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p

NVIDIA-Nemotron-Nano-9B-v2 is a large language model (LLM) trained from scratch by NVIDIA, and designed as a unified model for both reasoning and non-reasoning tasks. It responds to user queries and...

#### NVIDIA: Nemotron Nano 9B V2 (free)

- **ID**: `nvidia/nemotron-nano-9b-v2:free`
- **Provider**: nvidia
- **Context**: 128K (128,000) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-09-06
- **HF**: `nvidia/NVIDIA-Nemotron-Nano-9B-v2`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

NVIDIA-Nemotron-Nano-9B-v2 is a large language model (LLM) trained from scratch by NVIDIA, and designed as a unified model for both reasoning and non-reasoning tasks. It responds to user queries and...

### ▎openai（63）

#### OpenAI: GPT-3.5 Turbo

- **ID**: `openai/gpt-3.5-turbo`
- **Provider**: openai
- **Context**: 16K (16,385) tok / max出力 4,096 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.5/1M · 出力 $1.50/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2021-09-30
- **登録日**: 2023-05-28
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

GPT-3.5 Turbo is OpenAI's fastest model. It can understand and generate natural language or code, and is optimized for chat and traditional completion tasks.

Training data up to Sep 2021.

#### OpenAI: GPT-3.5 Turbo (older v0613)

- **ID**: `openai/gpt-3.5-turbo-0613`
- **Provider**: openai
- **Context**: 4K (4,095) tok / max出力 4,096 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $1.00/1M · 出力 $2.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2021-09-30
- **登録日**: 2024-01-25
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_completion_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

GPT-3.5 Turbo is OpenAI's fastest model. It can understand and generate natural language or code, and is optimized for chat and traditional completion tasks.

Training data up to Sep 2021.

#### OpenAI: GPT-3.5 Turbo 16k

- **ID**: `openai/gpt-3.5-turbo-16k`
- **Provider**: openai
- **Context**: 16K (16,385) tok / max出力 4,096 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $3.00/1M · 出力 $4.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2021-09-30
- **登録日**: 2023-08-28
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_completion_tokens, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

This model offers four times the context length of gpt-3.5-turbo, allowing it to support approximately 20 pages of text in a single request at a higher cost. Training data: up...

#### OpenAI: GPT-3.5 Turbo Instruct

- **ID**: `openai/gpt-3.5-turbo-instruct`
- **Provider**: openai
- **Context**: 4K (4,095) tok / max出力 4,096 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $1.50/1M · 出力 $2.00/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2021-09-30
- **登録日**: 2023-09-28
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, top_logprobs, top_p

This model is a variant of GPT-3.5 Turbo tuned for instructional prompts and omitting chat-related optimizations. Training data: up to Sep 2021.

#### OpenAI: GPT-4

- **ID**: `openai/gpt-4`
- **Provider**: openai
- **Context**: 8K (8,191) tok / max出力 4,096 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $30.00/1M · 出力 $60.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2021-09-30
- **登録日**: 2023-05-28
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_completion_tokens, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

OpenAI's flagship model, GPT-4 is a large-scale multimodal language model capable of solving difficult problems with greater accuracy than previous models due to its broader general knowledge and advanced reasoning...

#### OpenAI: GPT-4 Turbo (older v1106)

- **ID**: `openai/gpt-4-1106-preview`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 4,096 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $10.00/1M · 出力 $30.00/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2023-04-30
- **登録日**: 2023-11-06
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

The latest GPT-4 Turbo model with vision capabilities. Vision requests can now use JSON mode and function calling.

Training data: up to April 2023.

#### OpenAI: GPT-4 Turbo

- **ID**: `openai/gpt-4-turbo`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 4,096 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $10.00/1M · 出力 $30.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-04-09
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

The latest GPT-4 Turbo model with vision capabilities. Vision requests can now use JSON mode and function calling.

Training data: up to December 2023.

#### OpenAI: GPT-4 Turbo Preview

- **ID**: `openai/gpt-4-turbo-preview`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 4,096 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $10.00/1M · 出力 $30.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-01-25
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

The preview GPT-4 model with improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. Training data: up to Dec 2023. **Note:** heavily rate limited by OpenAI while...

#### OpenAI: GPT-4.1

- **ID**: `openai/gpt-4.1`
- **Provider**: openai
- **Context**: 1.04758M (1,047,576) tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $8.00/1M · キャッシュ読 $0.5/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-04-15
- **対応パラメータ**: max_completion_tokens, max_tokens, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

GPT-4.1 is a flagship large language model optimized for advanced instruction following, real-world software engineering, and long-context reasoning. It supports a 1 million token context window and outperforms GPT-4o and...

#### OpenAI: GPT-4.1 Mini

- **ID**: `openai/gpt-4.1-mini`
- **Provider**: openai
- **Context**: 1.04758M (1,047,576) tok / max出力 32,768 tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $0.4/1M · 出力 $1.60/1M · キャッシュ読 $0.1/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-04-15
- **対応パラメータ**: max_completion_tokens, max_tokens, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

GPT-4.1 Mini is a mid-sized model delivering performance competitive with GPT-4o at substantially lower latency and cost. It retains a 1 million token context window and scores 45.1% on hard...

#### OpenAI: GPT-4.1 Nano

- **ID**: `openai/gpt-4.1-nano`
- **Provider**: openai
- **Context**: 1.04758M (1,047,576) tok / max出力 32,768 tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.4/1M · キャッシュ読 $0.025/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-04-15
- **対応パラメータ**: max_completion_tokens, max_tokens, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

For tasks that demand low latency, GPT‑4.1 nano is the fastest and cheapest model in the GPT-4.1 series. It delivers exceptional performance at a small size with its 1 million...

#### OpenAI: GPT-4o

- **ID**: `openai/gpt-4o`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $2.50/1M · 出力 $10.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Web検索, logprobs, Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2024-05-13
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_completion_tokens, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p, web_search_options

GPT-4o ("o" for "omni") is OpenAI's latest AI model, supporting both text and image inputs with text outputs. It maintains the intelligence level of [GPT-4 Turbo](/models/openai/gpt-4-turbo) while being twice as...

#### OpenAI: GPT-4o (2024-05-13)

- **ID**: `openai/gpt-4o-2024-05-13`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 4,096 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $5.00/1M · 出力 $15.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Web検索, logprobs, Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2024-05-13
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_completion_tokens, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p, web_search_options

GPT-4o ("o" for "omni") is OpenAI's latest AI model, supporting both text and image inputs with text outputs. It maintains the intelligence level of [GPT-4 Turbo](/models/openai/gpt-4-turbo) while being twice as...

#### OpenAI: GPT-4o (2024-08-06)

- **ID**: `openai/gpt-4o-2024-08-06`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $2.50/1M · 出力 $10.00/1M · キャッシュ読 $1.25/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Web検索, logprobs, Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2024-08-06
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_completion_tokens, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p, web_search_options

The 2024-08-06 version of GPT-4o offers improved performance in structured outputs, with the ability to supply a JSON schema in the respone_format. Read more [here](https://openai.com/index/introducing-structured-outputs-in-the-api/). GPT-4o ("o" for "omni") is...

#### OpenAI: GPT-4o (2024-11-20)

- **ID**: `openai/gpt-4o-2024-11-20`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $2.50/1M · 出力 $10.00/1M · キャッシュ読 $1.25/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Web検索, logprobs, Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2024-11-21
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p, web_search_options

The 2024-11-20 version of GPT-4o offers a leveled-up creative writing ability with more natural, engaging, and tailored writing to improve relevance & readability. It’s also better at working with uploaded...

#### OpenAI: GPT-4o-mini

- **ID**: `openai/gpt-4o-mini`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $0.15/1M · 出力 $0.6/1M · キャッシュ読 $0.075/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Web検索, logprobs, Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2024-07-18
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_completion_tokens, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p, web_search_options

GPT-4o mini is OpenAI's newest model after [GPT-4 Omni](/models/openai/gpt-4o), supporting both text and image inputs with text outputs. As their most advanced small model, it is many multiples more affordable...

#### OpenAI: GPT-4o-mini (2024-07-18)

- **ID**: `openai/gpt-4o-mini-2024-07-18`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $0.15/1M · 出力 $0.6/1M · キャッシュ読 $0.075/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Web検索, logprobs, Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2024-07-18
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p, web_search_options

GPT-4o mini is OpenAI's newest model after [GPT-4 Omni](/models/openai/gpt-4o), supporting both text and image inputs with text outputs. As their most advanced small model, it is many multiples more affordable...

#### OpenAI: GPT-4o-mini Search Preview

- **ID**: `openai/gpt-4o-mini-search-preview`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.15/1M · 出力 $0.6/1M · Web検索 $0.0275
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Web検索
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2025-03-13
- **対応パラメータ**: max_tokens, response_format, structured_outputs, web_search_options

GPT-4o mini Search Preview is a specialized model for web search in Chat Completions. It is trained to understand and execute web search queries.

#### OpenAI: GPT-4o Search Preview

- **ID**: `openai/gpt-4o-search-preview`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $2.50/1M · 出力 $10.00/1M · Web検索 $0.035
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Web検索
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2025-03-13
- **対応パラメータ**: max_tokens, response_format, structured_outputs, web_search_options

GPT-4o Search Previewis a specialized model for web search in Chat Completions. It is trained to understand and execute web search queries.

#### OpenAI: GPT-5

- **ID**: `openai/gpt-5`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $10.00/1M · キャッシュ読 $0.125/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-09-30
- **登録日**: 2025-08-08
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5 is OpenAI’s most advanced model, offering major improvements in reasoning, code quality, and user experience. It is optimized for complex tasks that require step-by-step reasoning, instruction following, and accuracy...

#### OpenAI: GPT-5 Chat

- **ID**: `openai/gpt-5-chat`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text+image+file->text  (in: file,image,text → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $10.00/1M · キャッシュ読 $0.125/1M · Web検索 $0.01
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-09-30
- **登録日**: 2025-08-08
- **対応パラメータ**: max_tokens, response_format, seed, structured_outputs

GPT-5 Chat is designed for advanced, natural, multimodal, and context-aware conversations for enterprise applications.

#### OpenAI: GPT-5 Codex

- **ID**: `openai/gpt-5-codex`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $10.00/1M · キャッシュ読 $0.125/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-09-30
- **登録日**: 2025-09-24
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5-Codex is a specialized version of GPT-5 optimized for software engineering and coding workflows. It is designed for both interactive development sessions and long, independent execution of complex engineering tasks....

#### OpenAI: GPT-5 Image

- **ID**: `openai/gpt-5-image`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text+image  (in: image,text,file → out: image,text)
- **Pricing**: 入力 $10.00/1M · 出力 $10.00/1M · キャッシュ読 $1.25/1M · Web検索 $0.01
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2025-10-14
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, top_logprobs, top_p

[GPT-5](https://openrouter.ai/openai/gpt-5) Image combines OpenAI's GPT-5 model with state-of-the-art image generation capabilities. It offers major improvements in reasoning, code quality, and user experience while incorporating GPT Image 1's superior instruction following,...

#### OpenAI: GPT-5 Image Mini

- **ID**: `openai/gpt-5-image-mini`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text+image  (in: file,image,text → out: image,text)
- **Pricing**: 入力 $2.50/1M · 出力 $2.00/1M · キャッシュ読 $0.25/1M · Web検索 $0.01
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2025-10-16
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, top_logprobs, top_p

GPT-5 Image Mini combines OpenAI's advanced language capabilities, powered by [GPT-5 Mini](https://openrouter.ai/openai/gpt-5-mini), with GPT Image 1 Mini for efficient image generation. This natively multimodal model features superior instruction following, text...

#### OpenAI: GPT-5 Mini

- **ID**: `openai/gpt-5-mini`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $0.25/1M · 出力 $2.00/1M · キャッシュ読 $0.025/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-05-31
- **登録日**: 2025-08-08
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5 Mini is a compact version of GPT-5, designed to handle lighter-weight reasoning tasks. It provides the same instruction-following and safety-tuning benefits as GPT-5, but with reduced latency and cost....

#### OpenAI: GPT-5 Nano

- **ID**: `openai/gpt-5-nano`
- **Provider**: openai
- **Context**: 400K (400,000) tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $0.05/1M · 出力 $0.4/1M · キャッシュ読 $0.01/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-05-31
- **登録日**: 2025-08-08
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5-Nano is the smallest and fastest variant in the GPT-5 system, optimized for developer tools, rapid interactions, and ultra-low latency environments. While limited in reasoning depth compared to its larger...

#### OpenAI: GPT-5 Pro

- **ID**: `openai/gpt-5-pro`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $15.00/1M · 出力 $120.00/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-09-30
- **登録日**: 2025-10-07
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5 Pro is OpenAI’s most advanced model, offering major improvements in reasoning, code quality, and user experience. It is optimized for complex tasks that require step-by-step reasoning, instruction following, and...

#### OpenAI: GPT-5.1

- **ID**: `openai/gpt-5.1`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $10.00/1M · キャッシュ読 $0.13/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-11-14
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.1 is the latest frontier-grade model in the GPT-5 series, offering stronger general-purpose reasoning, improved instruction adherence, and a more natural conversational style compared to GPT-5. It uses adaptive reasoning...

#### OpenAI: GPT-5.1 Chat

- **ID**: `openai/gpt-5.1-chat`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 32,000 tok
- **Modality**: text+image+file->text  (in: file,image,text → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $10.00/1M · キャッシュ読 $0.13/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2025-11-14
- **対応パラメータ**: max_completion_tokens, max_tokens, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.1 Chat (AKA Instant is the fast, lightweight member of the 5.1 family, optimized for low-latency chat while retaining strong general intelligence. It uses adaptive reasoning to selectively “think” on...

#### OpenAI: GPT-5.1-Codex

- **ID**: `openai/gpt-5.1-codex`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $10.00/1M · キャッシュ読 $0.13/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-11-14
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.1-Codex is a specialized version of GPT-5.1 optimized for software engineering and coding workflows. It is designed for both interactive development sessions and long, independent execution of complex engineering tasks....

#### OpenAI: GPT-5.1-Codex-Max

- **ID**: `openai/gpt-5.1-codex-max`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $10.00/1M · キャッシュ読 $0.125/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-12-05
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.1-Codex-Max is OpenAI’s latest agentic coding model, designed for long-running, high-context software development tasks. It is based on an updated version of the 5.1 reasoning stack and trained on agentic...

#### OpenAI: GPT-5.1-Codex-Mini

- **ID**: `openai/gpt-5.1-codex-mini`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 100,000 tok
- **Modality**: text+image->text  (in: image,text → out: text)
- **Pricing**: 入力 $0.25/1M · 出力 $2.00/1M · キャッシュ読 $0.025/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-11-14
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.1-Codex-Mini is a smaller and faster version of GPT-5.1-Codex

#### OpenAI: GPT-5.2

- **ID**: `openai/gpt-5.2`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: file,image,text → out: text)
- **Pricing**: 入力 $1.75/1M · 出力 $14.00/1M · キャッシュ読 $0.175/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-12-11
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.2 is the latest frontier-grade model in the GPT-5 series, offering stronger agentic and long context perfomance compared to GPT-5.1. It uses adaptive reasoning to allocate computation dynamically, responding quickly...

#### OpenAI: GPT-5.2 Chat

- **ID**: `openai/gpt-5.2-chat`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text+image+file->text  (in: file,image,text → out: text)
- **Pricing**: 入力 $1.75/1M · 出力 $14.00/1M · キャッシュ読 $0.175/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2025-12-11
- **対応パラメータ**: max_completion_tokens, max_tokens, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.2 Chat (AKA Instant) is the fast, lightweight member of the 5.2 family, optimized for low-latency chat while retaining strong general intelligence. It uses adaptive reasoning to selectively “think” on...

#### OpenAI: GPT-5.2-Codex

- **ID**: `openai/gpt-5.2-codex`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $1.75/1M · 出力 $14.00/1M · キャッシュ読 $0.175/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-01-15
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.2-Codex is an upgraded version of GPT-5.1-Codex optimized for software engineering and coding workflows. It is designed for both interactive development sessions and long, independent execution of complex engineering tasks....

#### OpenAI: GPT-5.2 Pro

- **ID**: `openai/gpt-5.2-pro`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $21.00/1M · 出力 $168.00/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-12-11
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.2 Pro is OpenAI’s most advanced model, offering major improvements in agentic coding and long context performance over GPT-5 Pro. It is optimized for complex tasks that require step-by-step reasoning,...

#### OpenAI: GPT-5.3 Chat

- **ID**: `openai/gpt-5.3-chat`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $1.75/1M · 出力 $14.00/1M · キャッシュ読 $0.175/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2026-03-04
- **対応パラメータ**: max_completion_tokens, max_tokens, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.3 Chat is an update to ChatGPT's most-used model that makes everyday conversations smoother, more useful, and more directly helpful. It delivers more accurate answers with better contextualization and significantly...

#### OpenAI: GPT-5.3-Codex

- **ID**: `openai/gpt-5.3-codex`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $1.75/1M · 出力 $14.00/1M · キャッシュ読 $0.175/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-02-25
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.3-Codex is OpenAI’s most advanced agentic coding model, combining the frontier software engineering performance of GPT-5.2-Codex with the broader reasoning and professional knowledge capabilities of GPT-5.2. It achieves state-of-the-art results...

#### OpenAI: GPT-5.4

- **ID**: `openai/gpt-5.4`
- **Provider**: openai
- **Context**: 1.05M (1,050,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $2.50/1M · 出力 $15.00/1M · キャッシュ読 $0.25/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-03-06
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.4 is OpenAI’s latest frontier model, unifying the Codex and GPT lines into a single system. It features a 1M+ token context window (922K input, 128K output) with support for...

#### OpenAI: GPT-5.4 Image 2

- **ID**: `openai/gpt-5.4-image-2`
- **Provider**: openai
- **Context**: 272K (272,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text+image  (in: image,text,file → out: image,text)
- **Pricing**: 入力 $8.00/1M · 出力 $15.00/1M · キャッシュ読 $2.00/1M · Web検索 $0.01
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-04-22
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, top_logprobs

[GPT-5.4](https://openrouter.ai/openai/gpt-5.4) Image 2 combines OpenAI's GPT-5.4 model with state-of-the-art image generation capabilities from GPT Image 2. It enables rich multimodal workflows, allowing users to seamlessly move between reasoning, coding, and...

#### OpenAI: GPT-5.4 Mini

- **ID**: `openai/gpt-5.4-mini`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: file,image,text → out: text)
- **Pricing**: 入力 $0.75/1M · 出力 $4.50/1M · キャッシュ読 $0.075/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-08-31
- **登録日**: 2026-03-17
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.4 mini brings the core capabilities of GPT-5.4 to a faster, more efficient model optimized for high-throughput workloads. It supports text and image inputs with strong performance across reasoning, coding,...

#### OpenAI: GPT-5.4 Nano

- **ID**: `openai/gpt-5.4-nano`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: file,image,text → out: text)
- **Pricing**: 入力 $0.2/1M · 出力 $1.25/1M · キャッシュ読 $0.02/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-08-31
- **登録日**: 2026-03-17
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.4 nano is the most lightweight and cost-efficient variant of the GPT-5.4 family, optimized for speed-critical and high-volume tasks. It supports text and image inputs and is designed for low-latency...

#### OpenAI: GPT-5.4 Pro

- **ID**: `openai/gpt-5.4-pro`
- **Provider**: openai
- **Context**: 1.05M (1,050,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $30.00/1M · 出力 $180.00/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-03-06
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.4 Pro is OpenAI's most advanced model, building on GPT-5.4's unified architecture with enhanced reasoning capabilities for complex, high-stakes tasks. It features a 1M+ token context window (922K input, 128K...

#### OpenAI: GPT-5.5

- **ID**: `openai/gpt-5.5`
- **Provider**: openai
- **Context**: 1.05M (1,050,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: file,image,text → out: text)
- **Pricing**: 入力 $5.00/1M · 出力 $30.00/1M · キャッシュ読 $0.5/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-12-01
- **登録日**: 2026-04-25
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.5 is OpenAI’s frontier model designed for complex professional workloads, building on GPT-5.4 with stronger reasoning, higher reliability, and improved token efficiency on hard tasks. It features a 1M+ token...

#### OpenAI: GPT-5.5 Pro

- **ID**: `openai/gpt-5.5-pro`
- **Provider**: openai
- **Context**: 1.05M (1,050,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: file,image,text → out: text)
- **Pricing**: 入力 $30.00/1M · 出力 $180.00/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-12-01
- **登録日**: 2026-04-25
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

GPT-5.5 Pro is OpenAI’s high-capability model optimized for deep reasoning and accuracy on complex, high-stakes workloads. It features a 1M+ token context window (922K input, 128K output) with support for...

#### OpenAI: GPT Audio

- **ID**: `openai/gpt-audio`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text+audio->text+audio  (in: text,audio → out: text,audio)
- **Pricing**: 入力 $2.50/1M · 出力 $10.00/1M · 音声 $32.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **登録日**: 2026-01-20
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

The gpt-audio model is OpenAI's first generally available audio model. The new snapshot features an upgraded decoder for more natural sounding voices and maintains better voice consistency. Audio is priced...

#### OpenAI: GPT Audio Mini

- **ID**: `openai/gpt-audio-mini`
- **Provider**: openai
- **Context**: 128K (128,000) tok / max出力 16,384 tok
- **Modality**: text+audio->text+audio  (in: text,audio → out: text,audio)
- **Pricing**: 入力 $0.6/1M · 出力 $2.40/1M · 音声 $0.6/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **登録日**: 2026-01-20
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

A cost-efficient version of GPT Audio. The new snapshot features an upgraded decoder for more natural sounding voices and maintains better voice consistency. Input is priced at $0.60 per million...

#### OpenAI: GPT Chat Latest

- **ID**: `openai/gpt-chat-latest`
- **Provider**: openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $5.00/1M · 出力 $30.00/1M · キャッシュ読 $0.5/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **登録日**: 2026-05-06
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, tool_choice, tools, top_logprobs

GPT Chat Latest points to OpenAI's stable API alias `chat-latest` that always resolves to the latest Instant chat model used in ChatGPT. As OpenAI rolls out new Instant model updates...

#### OpenAI: gpt-oss-120b

- **ID**: `openai/gpt-oss-120b`
- **Provider**: openai
- **Context**: 131K (131,072) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.039/1M · 出力 $0.18/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-08-06
- **HF**: `openai/gpt-oss-120b`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

gpt-oss-120b is an open-weight, 117B-parameter Mixture-of-Experts (MoE) language model from OpenAI designed for high-reasoning, agentic, and general-purpose production use cases. It activates 5.1B parameters per forward pass and is optimized...

#### OpenAI: gpt-oss-120b (free)

- **ID**: `openai/gpt-oss-120b:free`
- **Provider**: openai
- **Context**: 131K (131,072) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-08-06
- **HF**: `openai/gpt-oss-120b`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, seed, stop, temperature, tool_choice, tools

gpt-oss-120b is an open-weight, 117B-parameter Mixture-of-Experts (MoE) language model from OpenAI designed for high-reasoning, agentic, and general-purpose production use cases. It activates 5.1B parameters per forward pass and is optimized...

#### OpenAI: gpt-oss-20b

- **ID**: `openai/gpt-oss-20b`
- **Provider**: openai
- **Context**: 131K (131,072) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.029/1M · 出力 $0.14/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-08-06
- **HF**: `openai/gpt-oss-20b`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

gpt-oss-20b is an open-weight 21B parameter model released by OpenAI under the Apache 2.0 license. It uses a Mixture-of-Experts (MoE) architecture with 3.6B active parameters per forward pass, optimized for...

#### OpenAI: gpt-oss-20b (free)

- **ID**: `openai/gpt-oss-20b:free`
- **Provider**: openai
- **Context**: 131K (131,072) tok / max出力 8,192 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-08-06
- **HF**: `openai/gpt-oss-20b`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, seed, stop, temperature, tool_choice, tools

gpt-oss-20b is an open-weight 21B parameter model released by OpenAI under the Apache 2.0 license. It uses a Mixture-of-Experts (MoE) architecture with 3.6B active parameters per forward pass, optimized for...

#### OpenAI: gpt-oss-safeguard-20b

- **ID**: `openai/gpt-oss-safeguard-20b`
- **Provider**: openai
- **Context**: 131K (131,072) tok / max出力 65,536 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.075/1M · 出力 $0.3/1M · キャッシュ読 $0.037/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-10-30
- **HF**: `openai/gpt-oss-safeguard-20b`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, temperature, tool_choice, tools, top_p

gpt-oss-safeguard-20b is a safety reasoning model from OpenAI built upon gpt-oss-20b. This open-weight, 21B-parameter Mixture-of-Experts (MoE) model offers lower latency for safety tasks like content classification, LLM filtering, and trust...

#### OpenAI: o1

- **ID**: `openai/o1`
- **Provider**: openai
- **Context**: 200K (200,000) tok / max出力 100,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $15.00/1M · 出力 $60.00/1M · キャッシュ読 $7.50/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2024-12-18
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

The latest and strongest model family from OpenAI, o1 is designed to spend more time thinking before responding. The o1 model series is trained with large-scale reinforcement learning to reason...

#### OpenAI: o1-pro

- **ID**: `openai/o1-pro`
- **Provider**: openai
- **Context**: 200K (200,000) tok / max出力 100,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $150.00/1M · 出力 $600.00/1M · Web検索 $0.01
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2025-03-20
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs

The o1 series of models are trained with reinforcement learning to think before they answer and perform complex reasoning. The o1-pro model uses more compute to think harder and provide...

#### OpenAI: o3

- **ID**: `openai/o3`
- **Provider**: openai
- **Context**: 200K (200,000) tok / max出力 100,000 tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $8.00/1M · キャッシュ読 $0.5/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-04-17
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

o3 is a well-rounded and powerful model across domains. It sets a new standard for math, science, coding, and visual reasoning tasks. It also excels at technical writing and instruction-following....

#### OpenAI: o3 Deep Research

- **ID**: `openai/o3-deep-research`
- **Provider**: openai
- **Context**: 200K (200,000) tok / max出力 100,000 tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $10.00/1M · 出力 $40.00/1M · キャッシュ読 $2.50/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2025-10-11
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

o3-deep-research is OpenAI's advanced model for deep research, designed to tackle complex, multi-step research tasks.

Note: This model always uses the 'web_search' tool which adds additional cost.

#### OpenAI: o3 Mini

- **ID**: `openai/o3-mini`
- **Provider**: openai
- **Context**: 200K (200,000) tok / max出力 100,000 tok
- **Modality**: text+file->text  (in: text,file → out: text)
- **Pricing**: 入力 $1.10/1M · 出力 $4.40/1M · キャッシュ読 $0.55/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2025-02-01
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

OpenAI o3-mini is a cost-efficient language model optimized for STEM reasoning tasks, particularly excelling in science, mathematics, and coding. This model supports the `reasoning_effort` parameter, which can be set to...

#### OpenAI: o3 Mini High

- **ID**: `openai/o3-mini-high`
- **Provider**: openai
- **Context**: 200K (200,000) tok / max出力 100,000 tok
- **Modality**: text+file->text  (in: text,file → out: text)
- **Pricing**: 入力 $1.10/1M · 出力 $4.40/1M · キャッシュ読 $0.55/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2023-10-31
- **登録日**: 2025-02-13
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

OpenAI o3-mini-high is the same model as [o3-mini](/openai/o3-mini) with reasoning_effort set to high. o3-mini is a cost-efficient language model optimized for STEM reasoning tasks, particularly excelling in science, mathematics, and...

#### OpenAI: o3 Pro

- **ID**: `openai/o3-pro`
- **Provider**: openai
- **Context**: 200K (200,000) tok / max出力 100,000 tok
- **Modality**: text+image+file->text  (in: text,file,image → out: text)
- **Pricing**: 入力 $20.00/1M · 出力 $80.00/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-06-11
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

The o-series of models are trained with reinforcement learning to think before they answer and perform complex reasoning. The o3-pro model uses more compute to think harder and provide consistently...

#### OpenAI: o4 Mini

- **ID**: `openai/o4-mini`
- **Provider**: openai
- **Context**: 200K (200,000) tok / max出力 100,000 tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $1.10/1M · 出力 $4.40/1M · キャッシュ読 $0.275/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-04-17
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

OpenAI o4-mini is a compact reasoning model in the o-series, optimized for fast, cost-efficient performance while retaining strong multimodal and agentic capabilities. It supports tool use and demonstrates competitive reasoning...

#### OpenAI: o4 Mini Deep Research

- **ID**: `openai/o4-mini-deep-research`
- **Provider**: openai
- **Context**: 200K (200,000) tok / max出力 100,000 tok
- **Modality**: text+image+file->text  (in: file,image,text → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $8.00/1M · キャッシュ読 $0.5/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2025-10-11
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

o4-mini-deep-research is OpenAI's faster, more affordable deep research model—ideal for tackling complex, multi-step research tasks.

Note: This model always uses the 'web_search' tool which adds additional cost.

#### OpenAI: o4 Mini High

- **ID**: `openai/o4-mini-high`
- **Provider**: openai
- **Context**: 200K (200,000) tok / max出力 100,000 tok
- **Modality**: text+image+file->text  (in: image,text,file → out: text)
- **Pricing**: 入力 $1.10/1M · 出力 $4.40/1M · キャッシュ読 $0.275/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-04-17
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

OpenAI o4-mini-high is the same model as [o4-mini](/openai/o4-mini) with reasoning_effort set to high. OpenAI o4-mini is a compact reasoning model in the o-series, optimized for fast, cost-efficient performance while retaining...

### ▎openrouter（6）

#### Auto Router

- **ID**: `openrouter/auto`
- **Provider**: openrouter
- **Context**: 2M (2,000,000) tok
- **Modality**: text+image+file+audio+video->text+image  (in: text,image,audio,file,video → out: text,image)
- **Pricing**: 入力 変動(動的)/1M · 出力 変動(動的)/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Web検索, logprobs, Seed固定
- **登録日**: 2023-11-08
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_completion_tokens, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p, web_search_options

Your prompt will be processed by a meta-model and routed to one of dozens of models (see below), optimizing for the best possible output. To see which model was used,...

#### Body Builder (beta)

- **ID**: `openrouter/bodybuilder`
- **Provider**: openrouter
- **Context**: 128K (128,000) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 変動(動的)/1M · 出力 変動(動的)/1M
- **登録日**: 2025-12-05

Transform your natural language requests into structured OpenRouter API request objects. Describe what you want to accomplish with AI models, and Body Builder will construct the appropriate API calls. Example:...

#### Free Models Router

- **ID**: `openrouter/free`
- **Provider**: openrouter
- **Context**: 200K (200,000) tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-02-01
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

The simplest way to get free inference. openrouter/free is a router that selects free models at random from the models available on OpenRouter. The router smartly filters for models that...

#### OpenRouter: Fusion

- **ID**: `openrouter/fusion`
- **Provider**: openrouter
- **Context**: 128K (128,000) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 変動(動的)/1M · 出力 変動(動的)/1M
- **登録日**: 2026-05-13

Fusion turns your prompt into a small multi-model deliberation. A panel of expert models (see below) analyzes your prompt in parallel with web search and web fetch enabled, then a...

#### Owl Alpha

- **ID**: `openrouter/owl-alpha`
- **Provider**: openrouter
- **Context**: 1.04876M (1,048,756) tok / max出力 262,144 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2026-04-29
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tools, top_k, top_p

Owl Alpha is a high-performance foundation model designed for agentic workloads. Natively supports tool use, and long-context tasks, with strong performance in code generation, automated workflows, and complex instruction execution....

#### Pareto Code Router

- **ID**: `openrouter/pareto-code`
- **Provider**: openrouter
- **Context**: 2M (2,000,000) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 変動(動的)/1M · 出力 変動(動的)/1M
- **登録日**: 2026-04-21

The Pareto Router maintains a tiered shortlist of strong coding models, ranked by [Artificial Analysis](https://artificialanalysis.ai/) coding percentiles. Set min_coding_score between 0 and 1 on the [pareto-router plugin](https://openrouter.ai/docs/guides/routing/routers/pareto-router#the-min_coding_score-parameter) to control how...

### ▎perceptron（1）

#### Perceptron: Perceptron Mk1

- **ID**: `perceptron/perceptron-mk1`
- **Provider**: perceptron
- **Context**: 32K (32,768) tok / max出力 8,192 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.15/1M · 出力 $1.50/1M
- **Capabilities**: Structured outputs(JSONスキーマ), Reasoning(思考), Reasoning出力
- **登録日**: 2026-05-12
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, structured_outputs, temperature, top_k, top_p

Perceptron Mk1 (Mark One) is Perceptron's highest-quality vision-language model for video and embodied reasoning.** It accepts image and video inputs paired with natural language queries, and produces detailed visual understanding...

### ▎perplexity（5）

#### Perplexity: Sonar

- **ID**: `perplexity/sonar`
- **Provider**: perplexity
- **Context**: 127K (127,072) tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $1.00/1M · 出力 $1.00/1M · Web検索 $0.005
- **Capabilities**: Web検索
- **登録日**: 2025-01-28
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, temperature, top_k, top_p, web_search_options

Sonar is lightweight, affordable, fast, and simple to use — now featuring citations and the ability to customize sources. It is designed for companies seeking to integrate lightweight question-and-answer features...

#### Perplexity: Sonar Deep Research

- **ID**: `perplexity/sonar-deep-research`
- **Provider**: perplexity
- **Context**: 128K (128,000) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $8.00/1M · 推論 $3.00/1M · Web検索 $0.005
- **Capabilities**: Reasoning(思考), Reasoning出力, Web検索
- **登録日**: 2025-03-07
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, temperature, top_k, top_p, web_search_options

Sonar Deep Research is a research-focused model designed for multi-step retrieval, synthesis, and reasoning across complex topics. It autonomously searches, reads, and evaluates sources, refining its approach as it gathers...

#### Perplexity: Sonar Pro

- **ID**: `perplexity/sonar-pro`
- **Provider**: perplexity
- **Context**: 200K (200,000) tok / max出力 8,000 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $3.00/1M · 出力 $15.00/1M · Web検索 $0.005
- **Capabilities**: Web検索
- **登録日**: 2025-03-07
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, temperature, top_k, top_p, web_search_options

Note: Sonar Pro pricing includes Perplexity search pricing. See [details here](https://docs.perplexity.ai/guides/pricing#detailed-pricing-breakdown-for-sonar-reasoning-pro-and-sonar-pro) For enterprises seeking more advanced capabilities, the Sonar Pro API can handle in-depth, multi-step queries with added extensibility, like...

#### Perplexity: Sonar Pro Search

- **ID**: `perplexity/sonar-pro-search`
- **Provider**: perplexity
- **Context**: 200K (200,000) tok / max出力 8,000 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $3.00/1M · 出力 $15.00/1M · Web検索 $0.018
- **Capabilities**: Structured outputs(JSONスキーマ), Reasoning(思考), Reasoning出力, Web検索
- **登録日**: 2025-10-31
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, structured_outputs, temperature, top_k, top_p, web_search_options

Exclusively available on the OpenRouter API, Sonar Pro's new Pro Search mode is Perplexity's most advanced agentic search system. It is designed for deeper reasoning and analysis. Pricing is based...

#### Perplexity: Sonar Reasoning Pro

- **ID**: `perplexity/sonar-reasoning-pro`
- **Provider**: perplexity
- **Context**: 128K (128,000) tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $8.00/1M · Web検索 $0.005
- **Capabilities**: Reasoning(思考), Reasoning出力, Web検索
- **登録日**: 2025-03-07
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, temperature, top_k, top_p, web_search_options

Note: Sonar Pro pricing includes Perplexity search pricing. See [details here](https://docs.perplexity.ai/guides/pricing#detailed-pricing-breakdown-for-sonar-reasoning-pro-and-sonar-pro) Sonar Reasoning Pro is a premier reasoning model powered by DeepSeek R1 with Chain of Thought (CoT). Designed for...

### ▎poolside（2）

#### Poolside: Laguna M.1 (free)

- **ID**: `poolside/laguna-m.1:free`
- **Provider**: poolside
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力
- **登録日**: 2026-04-29
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, temperature, tool_choice, tools

Laguna M.1 is the flagship coding agent model from [Poolside](https://poolside.ai), optimized for complex software engineering tasks. Designed for agentic coding workflows, it supports tool calling and reasoning, with a 128K...

#### Poolside: Laguna XS.2 (free)

- **ID**: `poolside/laguna-xs.2:free`
- **Provider**: poolside
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力
- **登録日**: 2026-04-29
- **HF**: `poolside/Laguna-XS.2`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, temperature, tool_choice, tools

Laguna XS.2 is the second-generation model in the XS size class from [Poolside](https://poolside.ai), their efficient coding agent series. It combines tool calling and reasoning capabilities with a compact footprint, offering...

### ▎prime-intellect（1）

#### Prime Intellect: INTELLECT-3

- **ID**: `prime-intellect/intellect-3`
- **Provider**: prime-intellect
- **Context**: 131K (131,072) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.2/1M · 出力 $1.10/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2025-11-27
- **HF**: `PrimeIntellect/INTELLECT-3-FP8`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, structured_outputs, temperature, tool_choice, tools, top_k, top_p

INTELLECT-3 is a 106B-parameter Mixture-of-Experts model (12B active) post-trained from GLM-4.5-Air-Base using supervised fine-tuning (SFT) followed by large-scale reinforcement learning (RL). It offers state-of-the-art performance for its size across math,...

### ▎qwen（49）

#### Qwen2.5 72B Instruct

- **ID**: `qwen/qwen-2.5-72b-instruct`
- **Provider**: qwen
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.36/1M · 出力 $0.4/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2024-09-19
- **HF**: `Qwen/Qwen2.5-72B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen2.5 72B is the latest series of Qwen large language models. Qwen2.5 brings the following improvements upon Qwen2: - Significantly more knowledge and has greatly improved capabilities in coding and...

#### Qwen: Qwen2.5 7B Instruct

- **ID**: `qwen/qwen-2.5-7b-instruct`
- **Provider**: qwen
- **Context**: 131K (131,072) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.04/1M · 出力 $0.1/1M
- **Capabilities**: Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2024-10-16
- **HF**: `Qwen/Qwen2.5-7B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p

Qwen2.5 7B is the latest series of Qwen large language models. Qwen2.5 brings the following improvements upon Qwen2: - Significantly more knowledge and has greatly improved capabilities in coding and...

#### Qwen2.5 Coder 32B Instruct

- **ID**: `qwen/qwen-2.5-coder-32b-instruct`
- **Provider**: qwen
- **Context**: 128K (128,000) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.66/1M · 出力 $1.00/1M
- **Capabilities**: Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2024-11-12
- **HF**: `Qwen/Qwen2.5-Coder-32B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p

Qwen2.5-Coder is the latest series of Code-Specific Qwen large language models (formerly known as CodeQwen). Qwen2.5-Coder brings the following improvements upon CodeQwen1.5: - Significantly improvements in **code generation**, **code reasoning**...

#### Qwen: Qwen-Plus

- **ID**: `qwen/qwen-plus`
- **Provider**: qwen
- **Context**: 1M (1,000,000) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.26/1M · 出力 $0.78/1M · キャッシュ読 $0.052/1M · キャッシュ書 $0.325/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-02-01
- **対応パラメータ**: max_tokens, presence_penalty, response_format, seed, temperature, tool_choice, tools, top_p

Qwen-Plus, based on the Qwen2.5 foundation model, is a 131K context model with a balanced performance, speed, and cost combination.

#### Qwen: Qwen Plus 0728

- **ID**: `qwen/qwen-plus-2025-07-28`
- **Provider**: qwen
- **Context**: 1M (1,000,000) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.26/1M · 出力 $0.78/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-09-09
- **対応パラメータ**: max_tokens, presence_penalty, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

Qwen Plus 0728, based on the Qwen3 foundation model, is a 1 million context hybrid reasoning model with a balanced performance, speed, and cost combination.

#### Qwen: Qwen Plus 0728 (thinking)

- **ID**: `qwen/qwen-plus-2025-07-28:thinking`
- **Provider**: qwen
- **Context**: 1M (1,000,000) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.26/1M · 出力 $0.78/1M · キャッシュ書 $0.325/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-09-09
- **対応パラメータ**: include_reasoning, max_tokens, presence_penalty, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

Qwen Plus 0728, based on the Qwen3 foundation model, is a 1 million context hybrid reasoning model with a balanced performance, speed, and cost combination.

#### Qwen: Qwen2.5 VL 72B Instruct

- **ID**: `qwen/qwen2.5-vl-72b-instruct`
- **Provider**: qwen
- **Context**: 131K (131,072) tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.25/1M · 出力 $0.75/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-02-01
- **HF**: `Qwen/Qwen2.5-VL-72B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_p

Qwen2.5-VL is proficient in recognizing common objects such as flowers, birds, fish, and insects. It is also highly capable of analyzing texts, charts, icons, graphics, and layouts within images.

#### Qwen: Qwen3 14B

- **ID**: `qwen/qwen3-14b`
- **Provider**: qwen
- **Context**: 131K (131,702) tok / max出力 40,960 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.24/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-04-29
- **HF**: `Qwen/Qwen3-14B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

Qwen3-14B is a dense 14.8B parameter causal language model from the Qwen3 series, designed for both complex reasoning and efficient dialogue. It supports seamless switching between a "thinking" mode for...

#### Qwen: Qwen3 235B A22B

- **ID**: `qwen/qwen3-235b-a22b`
- **Provider**: qwen
- **Context**: 131K (131,072) tok / max出力 8,192 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.455/1M · 出力 $1.82/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-04-29
- **HF**: `Qwen/Qwen3-235B-A22B`
- **対応パラメータ**: include_reasoning, max_tokens, presence_penalty, reasoning, response_format, seed, temperature, tool_choice, tools, top_p

Qwen3-235B-A22B is a 235B parameter mixture-of-experts (MoE) model developed by Qwen, activating 22B parameters per forward pass. It supports seamless switching between a "thinking" mode for complex reasoning, math, and...

#### Qwen: Qwen3 235B A22B Instruct 2507

- **ID**: `qwen/qwen3-235b-a22b-2507`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.071/1M · 出力 $0.1/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-06-30
- **登録日**: 2025-07-22
- **HF**: `Qwen/Qwen3-235B-A22B-Instruct-2507`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-235B-A22B-Instruct-2507 is a multilingual, instruction-tuned mixture-of-experts language model based on the Qwen3-235B architecture, with 22B active parameters per forward pass. It is optimized for general-purpose text generation, including instruction following,...

#### Qwen: Qwen3 235B A22B Thinking 2507

- **ID**: `qwen/qwen3-235b-a22b-thinking-2507`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 262,144 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.1/1M · キャッシュ読 $0.1/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-06-30
- **登録日**: 2025-07-25
- **HF**: `Qwen/Qwen3-235B-A22B-Thinking-2507`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-235B-A22B-Thinking-2507 is a high-performance, open-weight Mixture-of-Experts (MoE) language model optimized for complex reasoning tasks. It activates 22B of its 235B parameters per forward pass and natively supports up to 262,144...

#### Qwen: Qwen3 30B A3B

- **ID**: `qwen/qwen3-30b-a3b`
- **Provider**: qwen
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.09/1M · 出力 $0.45/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-04-29
- **HF**: `Qwen/Qwen3-30B-A3B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

Qwen3, the latest generation in the Qwen large language model series, features both dense and mixture-of-experts (MoE) architectures to excel in reasoning, multilingual support, and advanced agent tasks. Its unique...

#### Qwen: Qwen3 30B A3B Instruct 2507

- **ID**: `qwen/qwen3-30b-a3b-instruct-2507`
- **Provider**: qwen
- **Context**: 131K (131,072) tok / max出力 32,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.0481/1M · 出力 $0.193/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-06-30
- **登録日**: 2025-07-30
- **HF**: `Qwen/Qwen3-30B-A3B-Instruct-2507`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-30B-A3B-Instruct-2507 is a 30.5B-parameter mixture-of-experts language model from Qwen, with 3.3B active parameters per inference. It operates in non-thinking mode and is designed for high-quality instruction following, multilingual understanding, and...

#### Qwen: Qwen3 30B A3B Thinking 2507

- **ID**: `qwen/qwen3-30b-a3b-thinking-2507`
- **Provider**: qwen
- **Context**: 131K (131,072) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.08/1M · 出力 $0.4/1M · キャッシュ読 $0.08/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-06-30
- **登録日**: 2025-08-29
- **HF**: `Qwen/Qwen3-30B-A3B-Thinking-2507`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-30B-A3B-Thinking-2507 is a 30B parameter Mixture-of-Experts reasoning model optimized for complex tasks requiring extended multi-step thinking. The model is designed specifically for “thinking mode,” where internal reasoning traces are separated...

#### Qwen: Qwen3 32B

- **ID**: `qwen/qwen3-32b`
- **Provider**: qwen
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.08/1M · 出力 $0.28/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-04-29
- **HF**: `Qwen/Qwen3-32B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-32B is a dense 32.8B parameter causal language model from the Qwen3 series, optimized for both complex reasoning and efficient dialogue. It supports seamless switching between a "thinking" mode for...

#### Qwen: Qwen3 8B

- **ID**: `qwen/qwen3-8b`
- **Provider**: qwen
- **Context**: 131K (131,072) tok / max出力 8,192 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.05/1M · 出力 $0.4/1M · キャッシュ読 $0.05/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-04-29
- **HF**: `Qwen/Qwen3-8B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-8B is a dense 8.2B parameter causal language model from the Qwen3 series, designed for both reasoning-heavy tasks and efficient dialogue. It supports seamless switching between "thinking" mode for math,...

#### Qwen: Qwen3 Coder 480B A35B

- **ID**: `qwen/qwen3-coder`
- **Provider**: qwen
- **Context**: 1.04858M (1,048,576) tok / max出力 65,536 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.22/1M · 出力 $1.80/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-06-30
- **登録日**: 2025-07-23
- **HF**: `Qwen/Qwen3-Coder-480B-A35B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-Coder-480B-A35B-Instruct is a Mixture-of-Experts (MoE) code generation model developed by the Qwen team. It is optimized for agentic coding tasks such as function calling, tool use, and long-context reasoning over...

#### Qwen: Qwen3 Coder 30B A3B Instruct

- **ID**: `qwen/qwen3-coder-30b-a3b-instruct`
- **Provider**: qwen
- **Context**: 160K (160,000) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.07/1M · 出力 $0.27/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-06-30
- **登録日**: 2025-07-31
- **HF**: `Qwen/Qwen3-Coder-30B-A3B-Instruct`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-Coder-30B-A3B-Instruct is a 30.5B parameter Mixture-of-Experts (MoE) model with 128 experts (8 active per forward pass), designed for advanced code generation, repository-scale understanding, and agentic tool use. Built on the...

#### Qwen: Qwen3 Coder Flash

- **ID**: `qwen/qwen3-coder-flash`
- **Provider**: qwen
- **Context**: 1M (1,000,000) tok / max出力 65,536 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.195/1M · 出力 $0.975/1M · キャッシュ読 $0.039/1M · キャッシュ書 $0.2437/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Seed固定
- **Knowledge cutoff**: 2025-06-30
- **登録日**: 2025-09-17
- **対応パラメータ**: max_tokens, presence_penalty, response_format, seed, temperature, tool_choice, tools, top_p

Qwen3 Coder Flash is Alibaba's fast and cost efficient version of their proprietary Qwen3 Coder Plus. It is a powerful coding agent model specializing in autonomous programming via tool calling...

#### Qwen: Qwen3 Coder Next

- **ID**: `qwen/qwen3-coder-next`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 262,144 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.11/1M · 出力 $0.8/1M · キャッシュ読 $0.07/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2026-02-04
- **HF**: `Qwen/Qwen3-Coder-Next`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-Coder-Next is an open-weight causal language model optimized for coding agents and local development workflows. It uses a sparse MoE design with 80B total parameters and only 3B activated per...

#### Qwen: Qwen3 Coder Plus

- **ID**: `qwen/qwen3-coder-plus`
- **Provider**: qwen
- **Context**: 1M (1,000,000) tok / max出力 65,536 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.65/1M · 出力 $3.25/1M · キャッシュ読 $0.13/1M · キャッシュ書 $0.8125/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-06-30
- **登録日**: 2025-09-24
- **対応パラメータ**: max_tokens, presence_penalty, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

Qwen3 Coder Plus is Alibaba's proprietary version of the Open Source Qwen3 Coder 480B A35B. It is a powerful coding agent model specializing in autonomous programming via tool calling and...

#### Qwen: Qwen3 Coder 480B A35B (free)

- **ID**: `qwen/qwen3-coder:free`
- **Provider**: qwen
- **Context**: 1.04858M (1,048,576) tok / max出力 262,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice
- **Knowledge cutoff**: 2025-06-30
- **登録日**: 2025-07-23
- **HF**: `Qwen/Qwen3-Coder-480B-A35B-Instruct`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, stop, temperature, tool_choice, tools, top_k, top_p

Qwen3-Coder-480B-A35B-Instruct is a Mixture-of-Experts (MoE) code generation model developed by the Qwen team. It is optimized for agentic coding tasks such as function calling, tool use, and long-context reasoning over...

#### Qwen: Qwen3 Max

- **ID**: `qwen/qwen3-max`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.78/1M · 出力 $3.90/1M · キャッシュ読 $0.156/1M · キャッシュ書 $0.975/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Seed固定
- **Knowledge cutoff**: 2025-06-30
- **登録日**: 2025-09-24
- **対応パラメータ**: max_tokens, presence_penalty, response_format, seed, temperature, tool_choice, tools, top_p

Qwen3-Max is an updated release built on the Qwen3 series, offering major improvements in reasoning, instruction following, multilingual support, and long-tail knowledge coverage compared to the January 2025 version. It...

#### Qwen: Qwen3 Max Thinking

- **ID**: `qwen/qwen3-max-thinking`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.78/1M · 出力 $3.90/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-02-10
- **対応パラメータ**: include_reasoning, max_tokens, presence_penalty, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

Qwen3-Max-Thinking is the flagship reasoning model in the Qwen3 series, designed for high-stakes cognitive tasks that require deep, multi-step reasoning. By significantly scaling model capacity and reinforcement learning compute, it...

#### Qwen: Qwen3 Next 80B A3B Instruct

- **ID**: `qwen/qwen3-next-80b-a3b-instruct`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.09/1M · 出力 $1.10/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-09-30
- **登録日**: 2025-09-12
- **HF**: `Qwen/Qwen3-Next-80B-A3B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-Next-80B-A3B-Instruct is an instruction-tuned chat model in the Qwen3-Next series optimized for fast, stable responses without “thinking” traces. It targets complex tasks across reasoning, code generation, knowledge QA, and multilingual...

#### Qwen: Qwen3 Next 80B A3B Instruct (free)

- **ID**: `qwen/qwen3-next-80b-a3b-instruct:free`
- **Provider**: qwen
- **Context**: 262K (262,144) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode
- **Knowledge cutoff**: 2025-09-30
- **登録日**: 2025-09-12
- **HF**: `Qwen/Qwen3-Next-80B-A3B-Instruct`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-Next-80B-A3B-Instruct is an instruction-tuned chat model in the Qwen3-Next series optimized for fast, stable responses without “thinking” traces. It targets complex tasks across reasoning, code generation, knowledge QA, and multilingual...

#### Qwen: Qwen3 Next 80B A3B Thinking

- **ID**: `qwen/qwen3-next-80b-a3b-thinking`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.0975/1M · 出力 $0.78/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-09-30
- **登録日**: 2025-09-12
- **HF**: `Qwen/Qwen3-Next-80B-A3B-Thinking`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-Next-80B-A3B-Thinking is a reasoning-first chat model in the Qwen3-Next line that outputs structured “thinking” traces by default. It’s designed for hard multi-step problems; math proofs, code synthesis/debugging, logic, and agentic...

#### Qwen: Qwen3 VL 235B A22B Instruct

- **ID**: `qwen/qwen3-vl-235b-a22b-instruct`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 16,384 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.2/1M · 出力 $0.88/1M · キャッシュ読 $0.11/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-09-24
- **HF**: `Qwen/Qwen3-VL-235B-A22B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-VL-235B-A22B Instruct is an open-weight multimodal model that unifies strong text generation with visual understanding across images and video. The Instruct model targets general vision-language use (VQA, document parsing, chart/table...

#### Qwen: Qwen3 VL 235B A22B Thinking

- **ID**: `qwen/qwen3-vl-235b-a22b-thinking`
- **Provider**: qwen
- **Context**: 131K (131,072) tok / max出力 32,768 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.26/1M · 出力 $2.60/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-09-24
- **HF**: `Qwen/Qwen3-VL-235B-A22B-Thinking`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p

Qwen3-VL-235B-A22B Thinking is a multimodal model that unifies strong text generation with visual understanding across images and video. The Thinking model is optimized for multimodal reasoning in STEM and math....

#### Qwen: Qwen3 VL 30B A3B Instruct

- **ID**: `qwen/qwen3-vl-30b-a3b-instruct`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.13/1M · 出力 $0.52/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-10-07
- **HF**: `Qwen/Qwen3-VL-30B-A3B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-VL-30B-A3B-Instruct is a multimodal model that unifies strong text generation with visual understanding for images and videos. Its Instruct variant optimizes instruction-following for general multimodal tasks. It excels in perception...

#### Qwen: Qwen3 VL 30B A3B Thinking

- **ID**: `qwen/qwen3-vl-30b-a3b-thinking`
- **Provider**: qwen
- **Context**: 131K (131,072) tok / max出力 32,768 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.13/1M · 出力 $1.56/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-10-07
- **HF**: `Qwen/Qwen3-VL-30B-A3B-Thinking`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-VL-30B-A3B-Thinking is a multimodal model that unifies strong text generation with visual understanding for images and videos. Its Thinking variant enhances reasoning in STEM, math, and complex tasks. It excels...

#### Qwen: Qwen3 VL 32B Instruct

- **ID**: `qwen/qwen3-vl-32b-instruct`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 32,768 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.104/1M · 出力 $0.416/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Seed固定
- **登録日**: 2025-10-23
- **HF**: `Qwen/Qwen3-VL-32B-Instruct`
- **対応パラメータ**: max_tokens, presence_penalty, response_format, seed, temperature, tool_choice, tools, top_p

Qwen3-VL-32B-Instruct is a large-scale multimodal vision-language model designed for high-precision understanding and reasoning across text, images, and video. With 32 billion parameters, it combines deep visual perception with advanced text...

#### Qwen: Qwen3 VL 8B Instruct

- **ID**: `qwen/qwen3-vl-8b-instruct`
- **Provider**: qwen
- **Context**: 256K (256,000) tok / max出力 32,768 tok
- **Modality**: text+image->text  (in: image,text → out: text)
- **Pricing**: 入力 $0.08/1M · 出力 $0.5/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **登録日**: 2025-10-15
- **HF**: `Qwen/Qwen3-VL-8B-Instruct`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Qwen3-VL-8B-Instruct is a multimodal vision-language model from the Qwen3-VL series, built for high-fidelity understanding and reasoning across text, images, and video. It features improved multimodal fusion with Interleaved-MRoPE for long-horizon...

#### Qwen: Qwen3 VL 8B Thinking

- **ID**: `qwen/qwen3-vl-8b-thinking`
- **Provider**: qwen
- **Context**: 256K (256,000) tok / max出力 32,768 tok
- **Modality**: text+image->text  (in: image,text → out: text)
- **Pricing**: 入力 $0.117/1M · 出力 $1.36/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-10-15
- **HF**: `Qwen/Qwen3-VL-8B-Thinking`
- **対応パラメータ**: include_reasoning, max_tokens, presence_penalty, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

Qwen3-VL-8B-Thinking is the reasoning-optimized variant of the Qwen3-VL-8B multimodal model, designed for advanced visual and textual reasoning across complex scenes, documents, and temporal sequences. It integrates enhanced multimodal alignment and...

#### Qwen: Qwen3.5-122B-A10B

- **ID**: `qwen/qwen3.5-122b-a10b`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 262,144 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.26/1M · 出力 $2.08/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-02-26
- **HF**: `Qwen/Qwen3.5-122B-A10B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

The Qwen3.5 122B-A10B native vision-language model is built on a hybrid architecture that integrates a linear attention mechanism with a sparse mixture-of-experts model, achieving higher inference efficiency. In terms of...

#### Qwen: Qwen3.5-27B

- **ID**: `qwen/qwen3.5-27b`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 65,536 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.195/1M · 出力 $1.56/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-02-26
- **HF**: `Qwen/Qwen3.5-27B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

The Qwen3.5 27B native vision-language Dense model incorporates a linear attention mechanism, delivering fast response times while balancing inference speed and performance. Its overall capabilities are comparable to those of...

#### Qwen: Qwen3.5-35B-A3B

- **ID**: `qwen/qwen3.5-35b-a3b`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 262,144 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.14/1M · 出力 $1.00/1M · キャッシュ読 $0.05/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-02-26
- **HF**: `Qwen/Qwen3.5-35B-A3B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

The Qwen3.5 Series 35B-A3B is a native vision-language model designed with a hybrid architecture that integrates linear attention mechanisms and a sparse mixture-of-experts model, achieving higher inference efficiency. Its overall...

#### Qwen: Qwen3.5 397B A17B

- **ID**: `qwen/qwen3.5-397b-a17b`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 65,536 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.39/1M · 出力 $2.34/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-02-16
- **HF**: `Qwen/Qwen3.5-397B-A17B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

The Qwen3.5 series 397B-A17B native vision-language model is built on a hybrid architecture that integrates a linear attention mechanism with a sparse mixture-of-experts model, achieving higher inference efficiency. It delivers...

#### Qwen: Qwen3.5-9B

- **ID**: `qwen/qwen3.5-9b`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 81,920 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.04/1M · 出力 $0.15/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-03-10
- **HF**: `Qwen/Qwen3.5-9B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

Qwen3.5-9B is a multimodal foundation model from the Qwen3.5 family, designed to deliver strong reasoning, coding, and visual understanding in an efficient 9B-parameter architecture. It uses a unified vision-language design...

#### Qwen: Qwen3.5-Flash

- **ID**: `qwen/qwen3.5-flash-02-23`
- **Provider**: qwen
- **Context**: 1M (1,000,000) tok / max出力 65,536 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.065/1M · 出力 $0.26/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-02-26
- **対応パラメータ**: include_reasoning, max_tokens, presence_penalty, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

The Qwen3.5 native vision-language Flash models are built on a hybrid architecture that integrates a linear attention mechanism with a sparse mixture-of-experts model, achieving higher inference efficiency. Compared to the...

#### Qwen: Qwen3.5 Plus 2026-02-15

- **ID**: `qwen/qwen3.5-plus-02-15`
- **Provider**: qwen
- **Context**: 1M (1,000,000) tok / max出力 65,536 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.26/1M · 出力 $1.56/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-02-16
- **対応パラメータ**: include_reasoning, max_tokens, presence_penalty, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

The Qwen3.5 native vision-language series Plus models are built on a hybrid architecture that integrates linear attention mechanisms with sparse mixture-of-experts models, achieving higher inference efficiency. In a variety of...

#### Qwen: Qwen3.5 Plus 2026-04-20

- **ID**: `qwen/qwen3.5-plus-20260420`
- **Provider**: qwen
- **Context**: 1M (1,000,000) tok / max出力 65,536 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.3/1M · 出力 $1.80/1M · キャッシュ書 $0.375/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-04-27
- **対応パラメータ**: include_reasoning, max_tokens, presence_penalty, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

Qwen3.5 Plus (April 2026) is a large-scale multimodal language model from Alibaba. It accepts text, image, and video input and produces text output, with a 1M token context window. This...

#### Qwen: Qwen3.6 27B

- **ID**: `qwen/qwen3.6-27b`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 262,140 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.29/1M · 出力 $3.20/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-04-27
- **HF**: `Qwen/Qwen3.6-27B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

Qwen3.6 27B is a dense 27-billion-parameter language model from the Qwen Team at Alibaba, released in April 2026. It features hybrid multimodal capabilities — accepting text, image, and video inputs...

#### Qwen: Qwen3.6 35B A3B

- **ID**: `qwen/qwen3.6-35b-a3b`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 262,140 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.14/1M · 出力 $1.00/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-04-27
- **HF**: `Qwen/Qwen3.6-35B-A3B`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

Qwen3.6-35B-A3B is an open-weight multimodal model from Alibaba Cloud with 35 billion total parameters and 3 billion active parameters per token. It uses a hybrid sparse mixture-of-experts architecture combining Gated...

#### Qwen: Qwen3.6 Flash

- **ID**: `qwen/qwen3.6-flash`
- **Provider**: qwen
- **Context**: 1M (1,000,000) tok / max出力 65,536 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.1875/1M · 出力 $1.12/1M · キャッシュ書 $0.2344/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-04-27
- **対応パラメータ**: include_reasoning, max_tokens, presence_penalty, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

Qwen3.6 Flash is a fast, efficient language model from Alibaba's Qwen 3.6 series. It supports text, image, and video input with a 1M token context window. Tiered pricing kicks in...

#### Qwen: Qwen3.6 Max Preview

- **ID**: `qwen/qwen3.6-max-preview`
- **Provider**: qwen
- **Context**: 262K (262,144) tok / max出力 65,536 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $1.04/1M · 出力 $6.24/1M · キャッシュ書 $1.30/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-04-27
- **対応パラメータ**: include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

Qwen3.6-Max-Preview is a proprietary frontier model from Alibaba Cloud built on a sparse mixture-of-experts architecture with approximately 1 trillion total parameters. It is optimized for agentic coding, tool use, and...

#### Qwen: Qwen3.6 Plus

- **ID**: `qwen/qwen3.6-plus`
- **Provider**: qwen
- **Context**: 1M (1,000,000) tok / max出力 65,536 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.325/1M · 出力 $1.95/1M · キャッシュ書 $0.4062/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-04-02
- **対応パラメータ**: include_reasoning, max_tokens, presence_penalty, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p

Qwen 3.6 Plus builds on a hybrid architecture that combines efficient linear attention with sparse mixture-of-experts routing, enabling strong scalability and high-performance inference. Compared to the 3.5 series, it delivers...

#### Qwen: Qwen3.7 Max

- **ID**: `qwen/qwen3.7-max`
- **Provider**: qwen
- **Context**: 1M (1,000,000) tok / max出力 65,536 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $3.75/1M · キャッシュ読 $0.25/1M · キャッシュ書 $1.56/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-05-22
- **対応パラメータ**: include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

Qwen3.7-Max is the flagship model in Alibaba's Qwen3.7 series. It supports text input and output and is designed for agent-centric workloads, with particular strengths in coding, office and productivity tasks,...

#### Qwen: Qwen3.7 Plus

- **ID**: `qwen/qwen3.7-plus`
- **Provider**: qwen
- **Context**: 1M (1,000,000) tok / max出力 65,536 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.4/1M · 出力 $1.60/1M · キャッシュ読 $0.08/1M · キャッシュ書 $0.5/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-06-03
- **対応パラメータ**: include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

Qwen3.7-Plus is a cost-effective model in Alibaba's Qwen3.7 series. It supports text and image input with text output, building on the series' text capabilities with a comprehensive upgrade to its...

### ▎rekaai（2）

#### Reka Edge

- **ID**: `rekaai/reka-edge`
- **Provider**: rekaai
- **Context**: 16K (16,384) tok / max出力 16,384 tok
- **Modality**: text+image+video->text  (in: image,text,video → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.1/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), Seed固定
- **登録日**: 2026-03-21
- **HF**: `RekaAI/reka-edge-2603`
- **対応パラメータ**: frequency_penalty, max_tokens, presence_penalty, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Reka Edge is an extremely efficient 7B multimodal vision-language model that accepts image/video+text inputs and generates text outputs. This model is optimized specifically to deliver industry-leading performance in image understanding,...

#### Reka Flash 3

- **ID**: `rekaai/reka-flash-3`
- **Provider**: rekaai
- **Context**: 65K (65,536) tok / max出力 65,536 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.2/1M
- **Capabilities**: Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-01-31
- **登録日**: 2025-03-13
- **HF**: `RekaAI/reka-flash-3`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, seed, stop, temperature, top_k, top_p

Reka Flash 3 is a general-purpose, instruction-tuned large language model with 21 billion parameters, developed by Reka. It excels at general chat, coding tasks, instruction-following, and function calling. Featuring a...

### ▎relace（2）

#### Relace: Relace Apply 3

- **ID**: `relace/relace-apply-3`
- **Provider**: relace
- **Context**: 256K (256,000) tok / max出力 128,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.85/1M · 出力 $1.25/1M
- **Capabilities**: Seed固定
- **登録日**: 2025-09-26
- **対応パラメータ**: max_tokens, seed, stop

Relace Apply 3 is a specialized code-patching LLM that merges AI-suggested edits straight into your source files. It can apply updates from GPT-4o, Claude, and others into your files at...

#### Relace: Relace Search

- **ID**: `relace/relace-search`
- **Provider**: relace
- **Context**: 256K (256,000) tok / max出力 128,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $1.00/1M · 出力 $3.00/1M
- **Capabilities**: Function calling, Tool choice, Seed固定
- **登録日**: 2025-12-09
- **対応パラメータ**: max_tokens, seed, stop, temperature, tool_choice, tools, top_p

The relace-search model uses 4-12 `view_file` and `grep` tools in parallel to explore a codebase and return relevant files to the user request. In contrast to RAG, relace-search performs agentic...

### ▎sao10k（4）

#### Sao10K: Llama 3 8B Lunaris

- **ID**: `sao10k/l3-lunaris-8b`
- **Provider**: sao10k
- **Context**: 8K (8,192) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.04/1M · 出力 $0.05/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-08-13
- **HF**: `Sao10K/L3-8B-Lunaris-v1`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_p

Lunaris 8B is a versatile generalist and roleplaying model based on Llama 3. It's a strategic merge of multiple models, designed to balance creativity with improved logic and general knowledge....

#### Sao10K: Llama 3.1 70B Hanami x1

- **ID**: `sao10k/l3.1-70b-hanami-x1`
- **Provider**: sao10k
- **Context**: 16K (16,000) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $3.00/1M · 出力 $3.00/1M
- **Capabilities**: Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2025-01-08
- **HF**: `Sao10K/L3.1-70B-Hanami-x1`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p

This is [Sao10K](/sao10k)'s experiment over [Euryale v2.2](/sao10k/l3.1-euryale-70b).

#### Sao10K: Llama 3.1 Euryale 70B v2.2

- **ID**: `sao10k/l3.1-euryale-70b`
- **Provider**: sao10k
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.85/1M · 出力 $0.85/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-08-28
- **HF**: `Sao10K/L3.1-70B-Euryale-v2.2`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Euryale L3.1 70B v2.2 is a model focused on creative roleplay from [Sao10k](https://ko-fi.com/sao10k). It is the successor of [Euryale L3 70B v2.1](/models/sao10k/l3-euryale-70b).

#### Sao10K: Llama 3.3 Euryale 70B

- **ID**: `sao10k/l3.3-euryale-70b`
- **Provider**: sao10k
- **Context**: 131K (131,072) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.65/1M · 出力 $0.75/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2023-12-31
- **登録日**: 2024-12-19
- **HF**: `Sao10K/L3.3-70B-Euryale-v2.3`
- **対応パラメータ**: frequency_penalty, logprobs, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_logprobs, top_p

Euryale L3.3 70B is a model focused on creative roleplay from [Sao10k](https://ko-fi.com/sao10k). It is the successor of [Euryale L3 70B v2.2](/models/sao10k/l3-euryale-70b).

### ▎stepfun（2）

#### StepFun: Step 3.5 Flash

- **ID**: `stepfun/step-3.5-flash`
- **Provider**: stepfun
- **Context**: 262K (262,144) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.09/1M · 出力 $0.3/1M · キャッシュ読 $0.02/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-01-30
- **HF**: `stepfun-ai/Step-3.5-Flash`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p

Step 3.5 Flash is StepFun's most capable open-source foundation model. Built on a sparse Mixture of Experts (MoE) architecture, it selectively activates only 11B of its 196B parameters per token....

#### StepFun: Step 3.7 Flash

- **ID**: `stepfun/step-3.7-flash`
- **Provider**: stepfun
- **Context**: 256K (256,000) tok / max出力 256,000 tok
- **Modality**: text+image+video->text  (in: text,image,video → out: text)
- **Pricing**: 入力 $0.2/1M · 出力 $1.15/1M · キャッシュ読 $0.04/1M
- **Capabilities**: Function calling, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs
- **登録日**: 2026-05-29
- **対応パラメータ**: frequency_penalty, include_reasoning, logprobs, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tools, top_logprobs, top_p

Step 3.7 Flash is StepFun's latest high-efficiency multimodal Mixture-of-Experts model. It pairs a 196B-parameter language backbone with a vision encoder for native image and video understanding, activating roughly 11B parameters...

### ▎switchpoint（1）

#### Switchpoint Router

- **ID**: `switchpoint/router`
- **Provider**: switchpoint
- **Context**: 131K (131,072) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.85/1M · 出力 $3.40/1M
- **Capabilities**: Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-07-12
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, seed, stop, temperature, top_k, top_p

Switchpoint AI's router instantly analyzes your request and directs it to the optimal AI from an ever-evolving library. As the world of LLMs advances, our router gets smarter, ensuring you...

### ▎tencent（2）

#### Tencent: Hunyuan A13B Instruct

- **ID**: `tencent/hunyuan-a13b-instruct`
- **Provider**: tencent
- **Context**: 131K (131,072) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.14/1M · 出力 $0.57/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-07-09
- **HF**: `tencent/Hunyuan-A13B-Instruct`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, reasoning, response_format, structured_outputs, temperature, top_k, top_p

Hunyuan-A13B is a 13B active parameter Mixture-of-Experts (MoE) language model developed by Tencent, with a total parameter count of 80B and support for reasoning via Chain-of-Thought. It offers competitive benchmark...

#### Tencent: Hy3 preview

- **ID**: `tencent/hy3-preview`
- **Provider**: tencent
- **Context**: 262K (262,144) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.063/1M · 出力 $0.21/1M · キャッシュ読 $0.021/1M
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-04-23
- **HF**: `tencent/Hy3-preview`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, seed, stop, temperature, tool_choice, tools, top_k, top_p

Hy3 preview is a high-efficiency Mixture-of-Experts model from Tencent designed for agentic workflows and production use. It supports configurable reasoning levels across disabled, low, and high modes, allowing it to...

### ▎thedrummer（4）

#### TheDrummer: Cydonia 24B V4.1

- **ID**: `thedrummer/cydonia-24b-v4.1`
- **Provider**: thedrummer
- **Context**: 131K (131,072) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.3/1M · 出力 $0.5/1M · キャッシュ読 $0.15/1M
- **Capabilities**: Seed固定
- **Knowledge cutoff**: 2024-04-30
- **登録日**: 2025-09-27
- **HF**: `thedrummer/cydonia-24b-v4.1`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p

Uncensored and creative writing model based on Mistral Small 3.2 24B with good recall, prompt adherence, and intelligence.

#### TheDrummer: Rocinante 12B

- **ID**: `thedrummer/rocinante-12b`
- **Provider**: thedrummer
- **Context**: 32K (32,768) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.17/1M · 出力 $0.43/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2024-04-30
- **登録日**: 2024-09-30
- **HF**: `TheDrummer/Rocinante-12B-v1.1`
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

Rocinante 12B is designed for engaging storytelling and rich prose. Early testers have reported: - Expanded vocabulary with unique and expressive word choices - Enhanced creativity for vivid narratives -...

#### TheDrummer: Skyfall 36B V2

- **ID**: `thedrummer/skyfall-36b-v2`
- **Provider**: thedrummer
- **Context**: 32K (32,768) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.55/1M · 出力 $0.8/1M · キャッシュ読 $0.25/1M
- **Capabilities**: Seed固定
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-03-11
- **HF**: `TheDrummer/Skyfall-36B-v2`
- **対応パラメータ**: frequency_penalty, logit_bias, max_tokens, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p

Skyfall 36B v2 is an enhanced iteration of Mistral Small 2501, specifically fine-tuned for improved creativity, nuanced writing, role-playing, and coherent storytelling.

#### TheDrummer: UnslopNemo 12B

- **ID**: `thedrummer/unslopnemo-12b`
- **Provider**: thedrummer
- **Context**: 32K (32,768) tok / max出力 32,768 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.4/1M · 出力 $0.4/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2024-04-30
- **登録日**: 2024-11-09
- **HF**: `TheDrummer/UnslopNemo-12B-v4.1`
- **対応パラメータ**: frequency_penalty, logprobs, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

UnslopNemo v4.1 is the latest addition from the creator of Rocinante, designed for adventure writing and role-play scenarios.

### ▎undi95（1）

#### ReMM SLERP 13B

- **ID**: `undi95/remm-slerp-l2-13b`
- **Provider**: undi95
- **Context**: 6K (6,144) tok / max出力 4,096 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.45/1M · 出力 $0.65/1M
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, logprobs, Seed固定
- **Knowledge cutoff**: 2023-06-30
- **登録日**: 2023-07-22
- **HF**: `Undi95/ReMM-SLERP-L2-13B`
- **対応パラメータ**: frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_a, top_k, top_logprobs, top_p

A recreation trial of the original MythoMax-L2-B13 but with updated models. #merge

### ▎upstage（1）

#### Upstage: Solar Pro 3

- **ID**: `upstage/solar-pro-3`
- **Provider**: upstage
- **Context**: 128K (128,000) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.15/1M · 出力 $0.6/1M · キャッシュ読 $0.015/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-01-27
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, structured_outputs, temperature, tool_choice, tools

Solar Pro 3 is Upstage's powerful Mixture-of-Experts (MoE) language model. With 102B total parameters and 12B active parameters per forward pass, it delivers exceptional performance while maintaining computational efficiency. Optimized...

### ▎writer（1）

#### Writer: Palmyra X5

- **ID**: `writer/palmyra-x5`
- **Provider**: writer
- **Context**: 1.04M (1,040,000) tok / max出力 8,192 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.6/1M · 出力 $6.00/1M
- **登録日**: 2026-01-21
- **対応パラメータ**: max_tokens, stop, temperature, top_k, top_p

Palmyra X5 is Writer's most advanced model, purpose-built for building and scaling AI agents across the enterprise. It delivers industry-leading speed and efficiency on context windows up to 1 million...

### ▎x-ai（4）

#### xAI: Grok 4.20

- **ID**: `x-ai/grok-4.20`
- **Provider**: x-ai
- **Context**: 2M (2,000,000) tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $2.50/1M · キャッシュ読 $0.2/1M · Web検索 $0.005
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **Knowledge cutoff**: 2025-09-01
- **登録日**: 2026-04-01
- **対応パラメータ**: include_reasoning, logprobs, max_tokens, reasoning, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

Grok 4.20 is a reasoning model from xAI with industry-leading speed and agentic tool calling capabilities. It combines the lowest hallucination rate on the market with strict prompt adherance, delivering...

#### xAI: Grok 4.20 Multi-Agent

- **ID**: `x-ai/grok-4.20-multi-agent`
- **Provider**: x-ai
- **Context**: 2M (2,000,000) tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $6.00/1M · キャッシュ読 $0.2/1M · Web検索 $0.005
- **Capabilities**: Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **Knowledge cutoff**: 2025-09-01
- **登録日**: 2026-04-01
- **対応パラメータ**: include_reasoning, logprobs, max_tokens, reasoning, response_format, seed, structured_outputs, temperature, top_logprobs, top_p

Grok 4.20 Multi-Agent is a variant of xAI’s Grok 4.20 designed for collaborative, agent-based workflows. Multiple agents operate in parallel to conduct deep research, coordinate tool use, and synthesize information...

#### xAI: Grok 4.3

- **ID**: `x-ai/grok-4.3`
- **Provider**: x-ai
- **Context**: 1M (1,000,000) tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $1.25/1M · 出力 $2.50/1M · キャッシュ読 $0.2/1M · Web検索 $0.005
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-05-01
- **対応パラメータ**: frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

Grok 4.3 is a reasoning model from xAI. It accepts text and image inputs with text output, and is suited for agentic workflows, instruction-following tasks, and applications requiring high factual...

#### xAI: Grok Build 0.1

- **ID**: `x-ai/grok-build-0.1`
- **Provider**: x-ai
- **Context**: 256K (256,000) tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $1.00/1M · 出力 $2.00/1M · キャッシュ読 $0.2/1M · Web検索 $0.005
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-05-21
- **対応パラメータ**: frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p

Grok Build 0.1 is xAI’s fast coding model trained specifically for agentic software engineering workflows. It supports text and image inputs with text output, and is optimized for interactive coding...

### ▎xiaomi（3）

#### Xiaomi: MiMo-V2-Flash

- **ID**: `xiaomi/mimo-v2-flash`
- **Provider**: xiaomi
- **Context**: 262K (262,144) tok / max出力 65,536 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.3/1M · キャッシュ読 $0.01/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2025-12-15
- **HF**: `XiaomiMiMo/MiMo-V2-Flash`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, response_format, stop, temperature, tool_choice, tools, top_p

MiMo-V2-Flash is an open-source foundation language model developed by Xiaomi. It is a Mixture-of-Experts model with 309B total parameters and 15B active parameters, adopting hybrid attention architecture. MiMo-V2-Flash supports a...

#### Xiaomi: MiMo-V2.5

- **ID**: `xiaomi/mimo-v2.5`
- **Provider**: xiaomi
- **Context**: 1.04858M (1,048,576) tok / max出力 131,072 tok
- **Modality**: text+image+audio+video->text  (in: text,audio,image,video → out: text)
- **Pricing**: 入力 $0.14/1M · 出力 $0.28/1M · キャッシュ読 $0.0028/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-04-23
- **HF**: `XiaomiMiMo/MiMo-V2.5`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, response_format, stop, temperature, tool_choice, tools, top_p

MiMo-V2.5 is a native omnimodal model by Xiaomi. It delivers Pro-level agentic performance at roughly half the inference cost, while surpassing MiMo-V2-Omni in multimodal perception across image and video understanding...

#### Xiaomi: MiMo-V2.5-Pro

- **ID**: `xiaomi/mimo-v2.5-pro`
- **Provider**: xiaomi
- **Context**: 1.04858M (1,048,576) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.435/1M · 出力 $0.87/1M · キャッシュ読 $0.0036/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-04-23
- **HF**: `XiaomiMiMo/MiMo-V2.5-Pro`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

MiMo-V2.5-Pro is Xiaomi’s flagship model, delivering strong performance in general agentic capabilities, complex software engineering, and long-horizon tasks, with top rankings on benchmarks such as ClawEval, GDPVal, and SWE-bench Pro....

### ▎z-ai（13）

#### Z.ai: GLM 4 32B 

- **ID**: `z-ai/glm-4-32b`
- **Provider**: z-ai
- **Context**: 128K (128,000) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.1/1M · 出力 $0.1/1M
- **Capabilities**: Function calling, Tool choice
- **Knowledge cutoff**: 2024-06-30
- **登録日**: 2025-07-25
- **対応パラメータ**: max_tokens, temperature, tool_choice, tools, top_p

GLM 4 32B is a cost-effective foundation language model. It can efficiently perform complex tasks and has significantly enhanced capabilities in tool use, online search, and code-related intelligent tasks. It...

#### Z.ai: GLM 4.5

- **ID**: `z-ai/glm-4.5`
- **Provider**: z-ai
- **Context**: 131K (131,072) tok / max出力 98,304 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.6/1M · 出力 $2.20/1M · キャッシュ読 $0.11/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-12-31
- **登録日**: 2025-07-26
- **HF**: `zai-org/GLM-4.5`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p

GLM-4.5 is our latest flagship foundation model, purpose-built for agent-based applications. It leverages a Mixture-of-Experts (MoE) architecture and supports a context length of up to 128k tokens. GLM-4.5 delivers significantly...

#### Z.ai: GLM 4.5 Air

- **ID**: `z-ai/glm-4.5-air`
- **Provider**: z-ai
- **Context**: 131K (131,072) tok / max出力 131,070 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.125/1M · 出力 $0.85/1M · キャッシュ読 $0.06/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-12-31
- **登録日**: 2025-07-26
- **HF**: `zai-org/GLM-4.5-Air`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p

GLM-4.5-Air is the lightweight variant of our latest flagship model family, also purpose-built for agent-centric applications. Like GLM-4.5, it adopts the Mixture-of-Experts (MoE) architecture but with a more compact parameter...

#### Z.ai: GLM 4.5 Air (free)

- **ID**: `z-ai/glm-4.5-air:free`
- **Provider**: z-ai
- **Context**: 131K (131,072) tok / max出力 96,000 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 無料/1M · 出力 無料/1M  🆓
- **Capabilities**: Function calling, Tool choice, Reasoning(思考), Reasoning出力
- **Knowledge cutoff**: 2024-12-31
- **登録日**: 2025-07-26
- **HF**: `zai-org/GLM-4.5-Air`
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, temperature, tool_choice, tools, top_p

GLM-4.5-Air is the lightweight variant of our latest flagship model family, also purpose-built for agent-centric applications. Like GLM-4.5, it adopts the Mixture-of-Experts (MoE) architecture but with a more compact parameter...

#### Z.ai: GLM 4.5V

- **ID**: `z-ai/glm-4.5v`
- **Provider**: z-ai
- **Context**: 65K (65,536) tok / max出力 16,384 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.6/1M · 出力 $1.80/1M · キャッシュ読 $0.11/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2024-12-31
- **登録日**: 2025-08-11
- **HF**: `zai-org/GLM-4.5V`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p

GLM-4.5V is a vision-language foundation model for multimodal agent applications. Built on a Mixture-of-Experts (MoE) architecture with 106B parameters and 12B activated parameters, it achieves state-of-the-art results in video understanding,...

#### Z.ai: GLM 4.6

- **ID**: `z-ai/glm-4.6`
- **Provider**: z-ai
- **Context**: 202K (202,752) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.43/1M · 出力 $1.74/1M · キャッシュ読 $0.08/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-03-31
- **登録日**: 2025-09-30
- **HF**: `zai-org/GLM-4.6`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

Compared with GLM-4.5, this generation brings several key improvements: Longer context window: The context window has been expanded from 128K to 200K tokens, enabling the model to handle more complex...

#### Z.ai: GLM 4.6V

- **ID**: `z-ai/glm-4.6v`
- **Provider**: z-ai
- **Context**: 131K (131,072) tok / max出力 24,000 tok
- **Modality**: text+image+video->text  (in: image,text,video → out: text)
- **Pricing**: 入力 $0.3/1M · 出力 $0.9/1M · キャッシュ読 $0.05/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2025-12-09
- **HF**: `zai-org/GLM-4.6V`
- **対応パラメータ**: frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p

GLM-4.6V is a large multimodal model designed for high-fidelity visual understanding and long-context reasoning across images, documents, and mixed media. It supports up to 128K tokens, processes complex page layouts...

#### Z.ai: GLM 4.7

- **ID**: `z-ai/glm-4.7`
- **Provider**: z-ai
- **Context**: 202K (202,752) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.4/1M · 出力 $1.75/1M · キャッシュ読 $0.08/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2025-12-22
- **HF**: `zai-org/GLM-4.7`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

GLM-4.7 is Z.ai’s latest flagship model, featuring upgrades in two key areas: enhanced programming capabilities and more stable multi-step reasoning/execution. It demonstrates significant improvements in executing complex agent tasks while...

#### Z.ai: GLM 4.7 Flash

- **ID**: `z-ai/glm-4.7-flash`
- **Provider**: z-ai
- **Context**: 202K (202,752) tok / max出力 16,384 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.06/1M · 出力 $0.4/1M · キャッシュ読 $0.01/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-01-19
- **HF**: `zai-org/GLM-4.7-Flash`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

As a 30B-class SOTA model, GLM-4.7-Flash offers a new option that balances performance and efficiency. It is further optimized for agentic coding use cases, strengthening coding capabilities, long-horizon task planning,...

#### Z.ai: GLM 5

- **ID**: `z-ai/glm-5`
- **Provider**: z-ai
- **Context**: 202K (202,752) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.6/1M · 出力 $1.92/1M · キャッシュ読 $0.12/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-02-12
- **HF**: `zai-org/GLM-5`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

GLM-5 is Z.ai’s flagship open-source foundation model engineered for complex systems design and long-horizon agent workflows. Built for expert developers, it delivers production-grade performance on large-scale programming tasks, rivaling leading...

#### Z.ai: GLM 5 Turbo

- **ID**: `z-ai/glm-5-turbo`
- **Provider**: z-ai
- **Context**: 202K (202,752) tok / max出力 131,072 tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $1.20/1M · 出力 $4.00/1M · キャッシュ読 $0.24/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-03-15
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p

GLM-5 Turbo is a new model from Z.ai designed for fast inference and strong performance in agent-driven environments such as OpenClaw scenarios. It is deeply optimized for real-world agent workflows...

#### Z.ai: GLM 5.1

- **ID**: `z-ai/glm-5.1`
- **Provider**: z-ai
- **Context**: 202K (202,752) tok
- **Modality**: text->text  (in: text → out: text)
- **Pricing**: 入力 $0.98/1M · 出力 $3.08/1M · キャッシュ読 $0.182/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-04-08
- **HF**: `zai-org/GLM-5.1`
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, parallel_tool_calls, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

GLM-5.1 delivers a major leap in coding capability, with particularly significant gains in handling long-horizon tasks. Unlike previous models built around minute-level interactions, GLM-5.1 can work independently and continuously on...

#### Z.ai: GLM 5V Turbo

- **ID**: `z-ai/glm-5v-turbo`
- **Provider**: z-ai
- **Context**: 202K (202,752) tok / max出力 131,072 tok
- **Modality**: text+image+video->text  (in: image,text,video → out: text)
- **Pricing**: 入力 $1.20/1M · 出力 $4.00/1M · キャッシュ読 $0.24/1M
- **Capabilities**: Function calling, Tool choice, JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-04-02
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, temperature, tool_choice, tools, top_p

GLM-5V-Turbo is Z.ai’s first native multimodal agent foundation model, built for vision-based coding and agent-driven tasks. It natively handles image, video, and text inputs, excels at long-horizon planning, complex coding,...

### ▎~anthropic（3）

#### Anthropic Claude Haiku Latest

- **ID**: `~anthropic/claude-haiku-latest`
- **Provider**: ~anthropic
- **Context**: 200K (200,000) tok / max出力 64,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $1.00/1M · 出力 $5.00/1M · キャッシュ読 $0.1/1M · キャッシュ書 $1.25/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-04-28
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p

This model always redirects to the latest model in the Anthropic Claude Haiku family.

#### Anthropic: Claude Opus Latest

- **ID**: `~anthropic/claude-opus-latest`
- **Provider**: ~anthropic
- **Context**: 1M (1,000,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $5.00/1M · 出力 $25.00/1M · キャッシュ読 $0.5/1M · キャッシュ書 $6.25/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-04-22
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, tool_choice, tools, verbosity

This model always redirects to the latest model in the Claude Opus family.

#### Anthropic Claude Sonnet Latest

- **ID**: `~anthropic/claude-sonnet-latest`
- **Provider**: ~anthropic
- **Context**: 1M (1,000,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: text,image,file → out: text)
- **Pricing**: 入力 $3.00/1M · 出力 $15.00/1M · キャッシュ読 $0.3/1M · キャッシュ書 $3.75/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力
- **登録日**: 2026-04-28
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p, verbosity

This model always redirects to the latest model in the Anthropic Claude Sonnet family.

### ▎~google（2）

#### Google Gemini Flash Latest

- **ID**: `~google/gemini-flash-latest`
- **Provider**: ~google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,536 tok
- **Modality**: text+image+file+audio+video->text  (in: text,image,video,file,audio → out: text)
- **Pricing**: 入力 $1.50/1M · 出力 $9.00/1M · キャッシュ読 $0.15/1M · キャッシュ書 $0.0833/1M · 推論 $9.00/1M · 画像 $1.5e-06/枚 · 音声 $3.00/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-01-01
- **登録日**: 2026-04-28
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

This model always redirects to the latest model in the Google Gemini Flash family.

#### Google Gemini Pro Latest

- **ID**: `~google/gemini-pro-latest`
- **Provider**: ~google
- **Context**: 1.04858M (1,048,576) tok / max出力 65,536 tok
- **Modality**: text+image+file+audio+video->text  (in: audio,file,image,text,video → out: text)
- **Pricing**: 入力 $2.00/1M · 出力 $12.00/1M · キャッシュ読 $0.2/1M · キャッシュ書 $0.375/1M · 推論 $12.00/1M · 画像 $2e-06/枚 · 音声 $2.00/1M · Web検索 $0.014
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **登録日**: 2026-04-28
- **対応パラメータ**: include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p

This model always redirects to the latest model in the Google Gemini Pro family.

### ▎~moonshotai（1）

#### MoonshotAI Kimi Latest

- **ID**: `~moonshotai/kimi-latest`
- **Provider**: ~moonshotai
- **Context**: 262K (262,144) tok / max出力 262,144 tok
- **Modality**: text+image->text  (in: text,image → out: text)
- **Pricing**: 入力 $0.684/1M · 出力 $3.42/1M · キャッシュ読 $0.144/1M
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, logprobs, Seed固定
- **登録日**: 2026-04-28
- **対応パラメータ**: frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, parallel_tool_calls, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p

This model always redirects to the latest model in the MoonshotAI Kimi family.

### ▎~openai（2）

#### OpenAI GPT Latest

- **ID**: `~openai/gpt-latest`
- **Provider**: ~openai
- **Context**: 1.05M (1,050,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: file,image,text → out: text)
- **Pricing**: 入力 $5.00/1M · 出力 $30.00/1M · キャッシュ読 $0.5/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-12-01
- **登録日**: 2026-04-28
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

This model always redirects to the latest model in the OpenAI GPT family.

#### OpenAI GPT Mini Latest

- **ID**: `~openai/gpt-mini-latest`
- **Provider**: ~openai
- **Context**: 400K (400,000) tok / max出力 128,000 tok
- **Modality**: text+image+file->text  (in: file,image,text → out: text)
- **Pricing**: 入力 $0.75/1M · 出力 $4.50/1M · キャッシュ読 $0.075/1M · Web検索 $0.01
- **Capabilities**: Function calling, Tool choice, Structured outputs(JSONスキーマ), JSON mode, Reasoning(思考), Reasoning出力, Seed固定
- **Knowledge cutoff**: 2025-08-31
- **登録日**: 2026-04-28
- **対応パラメータ**: include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools

This model always redirects to the latest model in the OpenAI GPT Mini family.
