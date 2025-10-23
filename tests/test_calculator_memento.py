from app.calculator_memento import Caretaker


# ------------------------------
# 1️⃣ Empty Undo/Redo Handling
# ------------------------------
def test_caretaker_empty_undo_redo():
    """Ensure undo/redo return None when stacks are empty."""
    caretaker = Caretaker()
    assert caretaker.undo() is None
    assert caretaker.redo() is None


# ------------------------------
# 2️⃣ Save and Restore Sequence
# ------------------------------
def test_caretaker_save_and_restore():
    """Verify saving and restoring multiple states works correctly."""
    caretaker = Caretaker()
    caretaker.save_state(["calc1"])
    caretaker.save_state(["calc2"])

    # Undo should revert to previous state
    undo_state = caretaker.undo()
    assert isinstance(undo_state, list)
    assert undo_state == ["calc1"]

    # Redo should bring back the last state
    redo_state = caretaker.redo()
    assert isinstance(redo_state, list)
    assert redo_state == ["calc2"]


# ------------------------------
# 3️⃣ Handles Empty State Repeatedly
# ------------------------------
def test_caretaker_handles_empty_state_repeated_calls():
    """Ensure repeated undo/redo calls on empty stacks don't crash."""
    c = Caretaker()
    assert c.undo() is None
    assert c.undo() is None
    assert c.redo() is None
    assert c.redo() is None


# ------------------------------
# 4️⃣ Undo/Redo Chain Behavior
# ------------------------------
def test_caretaker_save_and_undo_redo_chain():
    """Test multiple saves, undos, and redos behave as expected."""
    c = Caretaker()
    c.save_state(["a"])
    c.save_state(["b"])
    c.save_state(["c"])

    # Undo twice → should go back to ["a"]
    c.undo()
    last = c.undo()
    assert last == ["a"]

    # Redo once → should bring back ["b"]
    assert c.redo() == ["b"]


# ------------------------------
# 5️⃣ General Behavior Test
# ------------------------------
def test_caretaker_save_and_restore_behavior():
    """Ensure generic undo/redo return valid states."""
    c = Caretaker()
    c.save_state(["calc1"])
    c.save_state(["calc2"])

    prev_state = c.undo()
    assert isinstance(prev_state, list)
    assert "calc" in prev_state[0]

    restored = c.redo()
    assert isinstance(restored, list)
    assert "calc" in restored[0]
