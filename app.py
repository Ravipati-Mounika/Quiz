@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(
        session["user_id"]
    )

    results = Result.query.filter_by(
        username=session["username"]
    ).order_by(
        Result.id.desc()
    ).all()

    categories = db.session.query(
        Question.category
    ).distinct().all()

    categories = [
        category[0]
        for category in categories
    ]

    total_quizzes = len(results)

    if total_quizzes > 0:

        total_percentage = sum(
            (r.score / r.total) * 100
            for r in results
        )

        average_score = round(
            total_percentage / total_quizzes
        )

        best_score = max(
            round((r.score / r.total) * 100)
            for r in results
        )

    else:

        average_score = 0
        best_score = 0

    recent_results = results[:5]

    return render_template(
        "dashboard.html",
        user=user,
        categories=categories,
        total_quizzes=total_quizzes,
        average_score=average_score,
        best_score=best_score,
        recent_results=recent_results
    )