def generate_shark_feedback(transcript, delivery_score, content_score):

    feedback = f"""
    🦈 Visionary Shark: Loves the ambition, wants scalability!
    🦈 Finance Shark: Needs stronger revenue numbers.
    🦈 Customer Advocate: Clarity is good but needs deeper problem insights.
    """

    avg = (delivery_score + content_score) / 2

    if avg > 70:
        verdict = "Invest 🚀"
    elif avg > 50:
        verdict = "Need More Info 🤔"
    else:
        verdict = "Not Invest ❌"

    return feedback, verdict
