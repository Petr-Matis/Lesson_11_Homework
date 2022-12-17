from flask import Flask, render_template
from utils import get_all, get_candidate_by_pk, get_candidates_by_skills, get_candidates_by_name

app = Flask(__name__)


@app.route("/")
def index():
    candidates = get_all()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:id>")
def get_candidate(id):
    candidate = get_candidate_by_pk(id)
    return render_template('card.html', candidate=candidate)

@app.route("/search/<candidate_name>")
def get_candidates_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))




@app.route("/skills/<skill>")
def get_candidates_by_skills(skill):
    candidates = get_candidate_by_skill(skill)

    return render_template('skill.html', candidates=candidates, count_candidates=len(candidates))



app.run(debug=True)
