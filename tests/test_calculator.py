from app.calculator import calculator

def run_calculator_with_inputs(inputs, monkeypatch, capsys):
    input_generator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
    calculator()
    return capsys.readouterr().out

def test_calculator_addition(monkeypatch, capsys):
    inputs = ["add 2 3", "exit"]
    captured = run_calculator_with_inputs(inputs, monkeypatch, capsys)
    assert "Result: 5.0" in captured

def test_calculator_division_by_zero(monkeypatch, capsys):
    inputs = ["divide 1 0", "exit"]
    captured = run_calculator_with_inputs(inputs, monkeypatch, capsys)
    assert "Divide by zero is not allowed." in captured