# main.py

def calculate_task_cost(model_name, cost_per_token, efficiency_factor, base_tokens_for_task):
    """
    Calculates the total cost for a specific task based on model efficiency.
    A less efficient model will have a higher efficiency_factor (>1), requiring more tokens.
    A more efficient model will have a lower efficiency_factor (<1), requiring fewer tokens.
    """
    tokens_used = int(base_tokens_for_task * efficiency_factor)
    total_cost = tokens_used * cost_per_token
    return tokens_used, total_cost

# --- Model Definitions ---
# These values are hypothetical to demonstrate the paradox discussed in the article.

# Model A: Lower cost per token, but less efficient (requires more tokens for the same task)
MODEL_A_NAME = "BasicLLM"
MODEL_A_COST_PER_TOKEN = 0.00001  # e.g., $0.01 per 1000 tokens
MODEL_A_EFFICIENCY_FACTOR = 1.5   # Requires 1.5x the base tokens for a task

# Model B (e.g., Gemini 4 Neon): Higher cost per token, but more efficient (requires fewer tokens)
MODEL_B_NAME = "Gemini4Neon"
MODEL_B_COST_PER_TOKEN = 0.00002  # e.g., $0.02 per 1000 tokens (2x Model A's per-token cost)
MODEL_B_EFFICIENCY_FACTOR = 0.7   # Requires only 0.7x the base tokens for the same task

# --- Task Definition ---
# A hypothetical number of tokens a task would ideally take if perfectly efficient.
BASE_TOKENS_FOR_TASK = 1000

# --- Simulation ---
print("--- AI Model Cost Simulation for a Single Task ---")
print(f"Hypothetical Base Tokens for Task: {BASE_TOKENS_FOR_TASK}\n")

# Calculate cost for Model A
tokens_a, cost_a = calculate_task_cost(
    MODEL_A_NAME, MODEL_A_COST_PER_TOKEN, MODEL_A_EFFICIENCY_FACTOR, BASE_TOKENS_FOR_TASK
)
print(f"Model: {MODEL_A_NAME}")
print(f"  Cost per token: ${MODEL_A_COST_PER_TOKEN:.6f}")
print(f"  Efficiency Factor: {MODEL_A_EFFICIENCY_FACTOR} (uses {tokens_a} tokens)")
print(f"  Total Task Cost: ${cost_a:.6f}\n")

# Calculate cost for Model B
tokens_b, cost_b = calculate_task_cost(
    MODEL_B_NAME, MODEL_B_COST_PER_TOKEN, MODEL_B_EFFICIENCY_FACTOR, BASE_TOKENS_FOR_TASK
)
print(f"Model: {MODEL_B_NAME}")
print(f"  Cost per token: ${MODEL_B_COST_PER_TOKEN:.6f}")
print(f"  Efficiency Factor: {MODEL_B_EFFICIENCY_FACTOR} (uses {tokens_b} tokens)")
print(f"  Total Task Cost: ${cost_b:.6f}\n")

# --- Conclusion and Paradox Demonstration ---
print("--- Conclusion ---")
# This block illustrates the 'High Cost Per Token, Low Cost Per Task' paradox.
# Model B, despite its higher per-token cost, achieves a lower total task cost due to superior efficiency.
if cost_a > cost_b:
    print(f"Despite {MODEL_B_NAME} having a higher cost per token (${MODEL_B_COST_PER_TOKEN:.6f} vs ${MODEL_A_COST_PER_TOKEN:.6f}),")
    print(f"its higher efficiency leads to a lower total cost per task (${cost_b:.6f} vs ${cost_a:.6f}).")
    print("This demonstrates the 'High Cost Per Token, Low Cost Per Task' paradox.")
else:
    print("In this simulation, the cheaper per-token model also resulted in a cheaper total task cost.")
    print("Adjust model parameters (cost_per_token, efficiency_factor) to observe the paradox.")
