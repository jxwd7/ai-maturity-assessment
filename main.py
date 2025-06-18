from assessment_data import PILLARS_DATA
from scoring import (
    calculate_pillar_score,
    calculate_overall_maturity_score,
    map_score_to_level
)

# 3. Define a sample set of answers for all 6 pillars.
# Ensure scores are between 1 and 5, and each pillar has 5 scores.
SAMPLE_USER_ANSWERS = {
    "Business": [3, 4, 3, 5, 4],      # Example scores
    "People": [2, 3, 3, 4, 2],        # Example scores
    "Governance": [4, 4, 3, 3, 2],    # Example scores
    "Platform": [5, 4, 5, 4, 5],      # Example scores
    "Security": [3, 3, 4, 2, 3],      # Example scores
    "Operations": [4, 3, 3, 4, 4]     # Example scores
}

def main():
    # 4. Initialize an empty dictionary to store calculated pillar scores.
    pillar_scores_calculated = {}

    print("--- Pillar Scores ---")
    # 5. Loop through each pillar in PILLARS_DATA:
    for pillar_data in PILLARS_DATA:
        pillar_name = pillar_data["name"]

        # b. Retrieve the sample answer scores for this pillar.
        # Ensure the pillar_name from PILLARS_DATA matches keys in SAMPLE_USER_ANSWERS
        if pillar_name not in SAMPLE_USER_ANSWERS:
            print(f"Warning: No sample answers found for pillar: {pillar_name}. Skipping.")
            continue

        user_scores_for_pillar = SAMPLE_USER_ANSWERS[pillar_name]

        # c. Calculate the pillar score.
        calculated_score = calculate_pillar_score(user_scores_for_pillar)

        # d. Store the calculated score.
        pillar_scores_calculated[pillar_name] = calculated_score

        # e. Map the pillar score to its maturity level.
        maturity_level = map_score_to_level(calculated_score)

        # f. Print the pillar's name, its raw score, and its maturity level.
        print(f"{pillar_name}: Score = {calculated_score:.2f}, Level = {maturity_level}")

    # 6. Calculate the overall maturity score.
    # Ensure scores are passed in the correct order as defined in calculate_overall_maturity_score.
    # (business, people, governance, platform, security, operations)

    # Retrieve scores safely, providing a default (e.g., 0.0 or an error) if a pillar score wasn't calculated
    # For this script, we assume all pillars in PILLARS_DATA are in SAMPLE_USER_ANSWERS due to the setup.
    # If a pillar was skipped above, this might error or use a potentially missing key.
    # However, our SAMPLE_USER_ANSWERS is comprehensive for PILLARS_DATA.

    overall_raw_score, overall_percentage_score = calculate_overall_maturity_score(
        business_score=pillar_scores_calculated.get("Business", 0.0),
        people_score=pillar_scores_calculated.get("People", 0.0),
        governance_score=pillar_scores_calculated.get("Governance", 0.0),
        platform_score=pillar_scores_calculated.get("Platform", 0.0),
        security_score=pillar_scores_calculated.get("Security", 0.0),
        operations_score=pillar_scores_calculated.get("Operations", 0.0)
    )

    # 7. Map the returned raw overall score to its maturity level.
    overall_maturity_level = map_score_to_level(overall_raw_score)

    # 8. Print the overall results.
    print("\n--- Overall Maturity ---")
    print(f"Overall Raw Score (1-5): {overall_raw_score:.2f}")
    print(f"Overall Percentage Score (0-100%): {overall_percentage_score:.2f}%")
    print(f"Overall Maturity Level: {overall_maturity_level}")

if __name__ == "__main__":
    main()
