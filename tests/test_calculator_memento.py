from app.calculator_memento import Caretaker

class CalculatorMemento:
    def __init__(self, state):
        self.state = state.copy()

class Caretaker:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save(self, state):
        self._undo_stack.append(CalculatorMemento(state))

    def save_state(self, state):
        self.save(state)

    def undo(self):
        if self._undo_stack:
            memento = self._undo_stack.pop()
            self._redo_stack.append(memento)
            return memento.state
        return None

    def redo(self):
        if self._redo_stack:
            memento = self._redo_stack.pop()
            self._undo_stack.append(memento)
            return memento.state
        return None

def test_caretaker_empty_undo_redo():
    caretaker = Caretaker()
    assert caretaker.undo() is None
    assert caretaker.redo() is None

def test_caretaker_save_and_restore():
    caretaker = Caretaker()
    caretaker.save_state(["calc1"])
    caretaker.save_state(["calc2"])
    assert caretaker.undo() == ["calc1"]
    assert caretaker.redo() == ["calc2"]


def test_caretaker_handles_empty_state():
    c = Caretaker()
    assert c.undo() is None
    assert c.redo() is None

def test_caretaker_save_and_undo_redo():
    c = Caretaker()
    c.save_state(["a"])
    c.save_state(["b"])
    assert c.undo() == ["a"]
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