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
