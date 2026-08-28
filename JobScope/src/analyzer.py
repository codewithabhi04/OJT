def extract_skills(df):
    skills_list = ["Python", "SQL", "Machine Learning", "Excel", "Deep Learning", "Java", "AWS"]

    def find_skills(text):
        text = str(text).lower()
        found = []

        for skill in skills_list:
            if skill.lower() in text:
                found.append(skill)

        return found  # no "Other"

    df["skills"] = df.apply(
        lambda row: find_skills(
            str(row["title"]) + " " +
            str(row["company"]) + " " +
            str(row["location"]) + " " +
            str(row.get("experience", ""))
        ),
        axis=1
    )

    return df