# tests/test_my_app.py

from my_app.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, Poetry!\n"