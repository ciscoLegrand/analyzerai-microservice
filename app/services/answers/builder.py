from app.models.answer import Answer

def create_answer(answer_data):
    """Crea un objeto Answer a partir de los datos proporcionados."""
    return Answer(answer_data)

def process_answers(response_data,):
    """Procesa los datos de respuesta y devuelve una lista de objetos Answer."""
    return [create_answer(answer_data) for answer_data in response_data['answers']]
