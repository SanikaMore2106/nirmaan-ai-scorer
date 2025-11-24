def keyword_score(text, keywords):
    text_low = text.lower()
    found = [k for k in keywords if k.lower() in text_low]
    score = (len(found) / max(len(keywords), 1)) * 100
    return score, found

def length_score(count, min_w, max_w):
    if min_w and max_w and min_w <= count <= max_w:
        return 100
    if min_w and count < min_w:
        return (count / min_w) * 100
    if max_w and count > max_w:
        return (max_w / count) * 100
    return 100

def score_transcript(transcript, rubric):
    words = transcript.split()
    wc = len(words)

    total_weight = sum(r["weight"] for r in rubric)
    weighted_sum = 0
    output = []

    for r in rubric:
        # RULE-BASED ONLY
        kw_s, found_kw = keyword_score(transcript, r["keywords"])
        len_s = length_score(wc, r["min_words"], r["max_words"])
        R = 0.6 * kw_s + 0.4 * len_s

        # NO SEMANTIC MODEL → FIXED SCORE
        S = 50  

        # Combined Score
        score = (0.7 * R) + (0.3 * S)

        weighted_sum += score * r["weight"]

        output.append({
            "criterion_id": r["criterion_id"],
            "score": round(score, 2),
            "keywords_found": found_kw,
            "keyword_score": round(kw_s, 2),
            "semantic_score": None,  # removed
            "length_score": round(len_s, 2),
            "weight": r["weight"]
        })

    overall = weighted_sum / total_weight

    return {
        "overall_score": round(overall, 2),
        "word_count": wc,
        "criteria": output
    }
