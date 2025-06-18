from typing import List

def calculate_pillar_score(answer_scores: List[int]) -> float:
    """
    Calculates the average score for a single pillar based on user's answers.

    Args:
        answer_scores: A list of scores (integers) for the answers selected
                       by the user for a single pillar.

    Returns:
        The average score for the pillar as a float. Returns 0.0 if the
        input list is empty.
    """
    if not answer_scores:
        return 0.0
    return sum(answer_scores) / len(answer_scores)

# Example usage for calculate_pillar_score (can be removed or commented out later):
# if __name__ == '__main__':
#     scores1 = [1, 3, 4, 2, 5]
#     print(f"Pillar score for {scores1}: {calculate_pillar_score(scores1)}")

#     scores_empty = []
#     print(f"Pillar score for {scores_empty}: {calculate_pillar_score(scores_empty)}")


PILLAR_WEIGHTS = {
    "Business": 0.25,
    "Platform": 0.25,
    "People": 0.15,
    "Operations": 0.15,
    "Governance": 0.10,
    "Security": 0.10,
}

def calculate_overall_maturity_score(
    business_score: float,
    people_score: float,
    governance_score: float,
    platform_score: float,
    security_score: float,
    operations_score: float
) -> tuple[float, float]:
    """
    Calculates the overall maturity score based on individual pillar scores and their weights.

    Args:
        business_score: Score for the Business pillar.
        people_score: Score for the People pillar.
        governance_score: Score for the Governance pillar.
        platform_score: Score for the Platform pillar.
        security_score: Score for the Security pillar.
        operations_score: Score for the Operations pillar.

    Returns:
        A tuple containing the raw overall score (1-5 scale) and the
        percentage score (0-100%), both rounded to two decimal places.
    """
    overall_score = (
        business_score * PILLAR_WEIGHTS["Business"] +
        platform_score * PILLAR_WEIGHTS["Platform"] +
        people_score * PILLAR_WEIGHTS["People"] +
        operations_score * PILLAR_WEIGHTS["Operations"] +
        governance_score * PILLAR_WEIGHTS["Governance"] +
        security_score * PILLAR_WEIGHTS["Security"]
    )
    percentage_score = (overall_score - 1) * 25
    return round(overall_score, 2), round(percentage_score, 2)

# Example usage for calculate_overall_maturity_score (can be removed or commented out later):
# if __name__ == '__main__':
#     # Calculate pillar scores first (example values)
#     business = calculate_pillar_score([4,4,5,3,4]) # Example: 4.0
#     people = calculate_pillar_score([3,3,2,4,3])   # Example: 3.0
#     governance = calculate_pillar_score([2,2,3,2,3])# Example: 2.4
#     platform = calculate_pillar_score([5,4,5,4,5])  # Example: 4.6
#     security = calculate_pillar_score([4,3,4,3,4])  # Example: 3.6
#     operations = calculate_pillar_score([3,4,3,4,3])# Example: 3.4

#     raw_score, perc_score = calculate_overall_maturity_score(
#         business_score=business,
#         people_score=people,
#         governance_score=governance,
#         platform_score=platform,
#         security_score=security,
#         operations_score=operations
#     )
#     print(f"Overall Raw Score: {raw_score}, Percentage Score: {perc_score}%")
#     # Expected for above example scores:
#     # Business: 4.0 * 0.25 = 1.0
#     # Platform: 4.6 * 0.25 = 1.15
#     # People:   3.0 * 0.15 = 0.45
#     # Ops:      3.4 * 0.15 = 0.51
#     # Gov:      2.4 * 0.10 = 0.24
#     # Sec:      3.6 * 0.10 = 0.36
#     # Sum (Overall Raw): 1.0 + 1.15 + 0.45 + 0.51 + 0.24 + 0.36 = 3.71
#     # Percentage: (3.71 - 1) * 25 = 2.71 * 25 = 67.75%

MATURITY_LEVELS = {
    "Level 1": "Level 1: Initial / Ad-Hoc",
    "Level 2": "Level 2: Managed / Opportunistic",
    "Level 3": "Level 3: Defined / Strategic",
    "Level 4": "Level 4: Embedded", # Consistent with table in PRD
    "Level 5": "Level 5: Optimizing / Transformational",
}

def map_score_to_level(score: float) -> str:
    """
    Maps a given score (1-5 scale) to its corresponding maturity level description.

    Args:
        score: The score to map, typically an average pillar score or the
               overall maturity score.

    Returns:
        A string describing the maturity level, or an error message if the
        score is outside the valid range.
    """
    # Round the score to two decimal places to handle potential floating point inaccuracies
    # For example, a calculated score of 1.8000000000000003 should map to Level 1
    # And a score of 1.809 should map to Level 2.
    # This is a common issue with float comparisons.
    # However, direct comparison should be fine given the problem's score boundaries.
    # Let's stick to direct comparison as per example, but keep this in mind if issues arise.

    if not (1.0 <= score <= 5.0):
        return "Invalid score: Score must be between 1.0 and 5.0" # Handles scores slightly outside due to float math too if not rounded

    # It's slightly safer to check from highest to lowest or lowest to highest to avoid complex range conditions.
    # Given the structure, direct mapping to ranges is also clear.
    if score <= 1.80: # Catches 1.00 to 1.80
        return MATURITY_LEVELS["Level 1"]
    elif score <= 2.60: # Catches 1.81 to 2.60 (since >1.80 is implicit from previous branches)
        return MATURITY_LEVELS["Level 2"]
    elif score <= 3.40: # Catches 2.61 to 3.40
        return MATURITY_LEVELS["Level 3"]
    elif score <= 4.20: # Catches 3.41 to 4.20
        return MATURITY_LEVELS["Level 4"]
    elif score <= 5.00: # Catches 4.21 to 5.00
        return MATURITY_LEVELS["Level 5"]
    else:
        # This case should theoretically not be reached if the initial check 1.0 <= score <= 5.0 is robust.
        # However, it's a safeguard.
        return "Invalid score: Score out of expected 1.0-5.0 range after checks."

# Example usage for map_score_to_level (can be removed or commented out later):
# if __name__ == '__main__':
#     print(f"Score 1.0: {map_score_to_level(1.0)}")
#     print(f"Score 1.80: {map_score_to_level(1.80)}")
#     print(f"Score 1.81: {map_score_to_level(1.81)}")
#     print(f"Score 2.60: {map_score_to_level(2.60)}")
#     print(f"Score 2.61: {map_score_to_level(2.61)}")
#     print(f"Score 3.40: {map_score_to_level(3.40)}")
#     print(f"Score 3.41: {map_score_to_level(3.41)}")
#     print(f"Score 4.20: {map_score_to_level(4.20)}")
#     print(f"Score 4.21: {map_score_to_level(4.21)}")
#     print(f"Score 5.0: {map_score_to_level(5.0)}")
#     print(f"Score 0.5: {map_score_to_level(0.5)}")
#     print(f"Score 5.5: {map_score_to_level(5.5)}")
#     print(f"Score 3.0 (Calculated): {map_score_to_level(3.0)}") # Expected: Level 3
#     print(f"Score 4.1 (Calculated): {map_score_to_level(4.1)}") # Expected: Level 4
