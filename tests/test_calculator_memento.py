from app.calculator_memento import Caretaker

def test_caretaker_empty_undo_redo():
    caretaker = Caretaker()
    assert caretaker.undo() is None
    assert caretaker.redo() is None

def test_caretaker_save_and_restore():
    caretaker = Caretaker()
    caretaker.save_state(["calc1"])
    caretaker.save_state(["calc2"])

    undo_state = caretaker.undo()
    assert isinstance(undo_state, list)
    assert undo_state == ["calc1"]

    redo_state = caretaker.redo()
    assert isinstance(redo_state, list)
    assert redo_state == ["calc2"]

def test_caretaker_handles_empty_state_repeated_calls():
    c = Caretaker()
    assert c.undo() is None
    assert c.undo() is None
    assert c.redo() is None
    assert c.redo() is None

def test_caretaker_save_and_undo_redo_chain():
    c = Caretaker()
    c.save_state(["a"])
    c.save_state(["b"])
    c.save_state(["c"])

    c.undo()
    last = c.undo()
    assert last == ["a"]

    assert c.redo() == ["b"]


def test_caretaker_save_and_restore_behavior():
    c = Caretaker()
    c.save_state(["calc1"])
    c.save_state(["calc2"])

    prev_state = c.undo()
    assert isinstance(prev_state, list)
    assert "calc" in prev_state[0]

    restored = c.redo()
    assert isinstance(restored, list)
    assert "calc" in restored[0]
