import random
from datetime import datetime

def calculate_risk(risk_type, probability):
    """
    Calculates the risk level based on a probabilistic event,
    handling the edge cases of 0 and 1 probability.
    """
    # Handle deterministic cases for probability 0 or 1
    if probability == 0:
        return 0.1  # Deterministic low risk
    if probability == 1:
        return 3.5 + random.uniform(0, 1) # Deterministic high risk

    # Handle probabilistic case for 0 < probability < 1
    if random.random() <= probability:
        # --- Risk Event OCCURS ---
        # Calculate a high-risk level, with some minor random variation
        base_high_risk = 3.0
        risk_level = base_high_risk + random.uniform(0, 1.5)
    else:
        # --- Risk Event DOES NOT OCCUR ---
        # Return a low, background risk level, with minor random variation
        risk_level = random.uniform(0.1, 0.5)

    return min(risk_level, 5.0)  # Cap the risk level at a max of 5.0

def get_random_location():
    """Returns a random location from a predefined list."""
    locations = ['武汉']
    return random.choice(locations)

def get_current_time():
    """Returns the current time formatted as a string."""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
