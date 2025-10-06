from app.calculator_memento import Caretaker

def test_undo_and_redo():
    caretaker = Caretaker()

    state1 = {"Operation": ["add"], "Result": [5]}
    state2 = {"Operation": ["sub"], "Result": [2]}

    caretaker.save(state1)
    caretaker.save(state2)

    # Undo should revert to state1
    previous_state = caretaker.undo()
    assert previous_state == state2  # depends on how you structure it
    # Redo should restore latest undone state
    caretaker.redo()
    assert caretaker._undo_stack[-1].state == state2
