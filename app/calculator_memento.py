import copy

class CalculatorMemento:
    def __init__(self, state):
        self._state = copy.deepcopy(state)

    def get_state(self):
        return copy.deepcopy(self._state)

class Caretaker:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save_state(self, state):
        self._undo_stack.append(CalculatorMemento(state))
        self._redo_stack.clear()

    def undo(self):
        if not self._undo_stack:
            print("⚠️ Nothing to undo.")
            return None

        memento = self._undo_stack.pop()
        self._redo_stack.append(memento)

        prev_state = self._undo_stack[-1].get_state() if self._undo_stack else []
        return prev_state

    def redo(self):
        if not self._redo_stack:
            print("⚠️ Nothing to redo.")
            return None

        memento = self._redo_stack.pop()
        self._undo_stack.append(memento)
        return memento.get_state()
