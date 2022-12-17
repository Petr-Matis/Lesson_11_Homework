import json


def load_candidates():
    """загружает список кандидатов из файла"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    """возвращает список кандидатов """
    return load_candidates()


def get_candidate_by_pk(id):
    """возвращаеткандидата по 'id' """

    for candidate in get_all():
        if candidate['id'] == id:
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает список кандидатов по 'name' """
    result = []
    for candidate in get_all():
        if candidate_name.lower() in candidate['name'].lower():
            result.append(candidate)
    return result


def get_candidates_by_skills(skill):
    """возвращает список кандидатов по 'skill' """
    candidates = []
    for candidate in get_all():
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates
