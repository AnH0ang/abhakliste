import subprocess
import sys

from abhakliste._capture import Capturing


def test_simple_capture() -> None:
    """Test that the Capturing class caputures a writes to `stdout`."""
    with Capturing() as c:
        print("Hello")
        sys.stdout.write("World!")
        sys.stderr.write("Error!")

    assert c.stdout == "Hello\nWorld!"
    assert c.stderr == "Error!"


def test_subprocess_capture() -> None:
    """Test that the Capturing class caputures a writes in subprocess."""
    with Capturing() as c:
        subprocess.Popen(["echo", "Hello"], stdout=sys.stdout, stderr=sys.stderr).wait()

    assert c.stdout == "Hello\n"
    assert c.stderr == ""


def test_reassignment() -> None:
    """Test that the Capturing class correctly reassigns `stdout` and `stderr`."""
    orginial_stdout = sys.stdout
    orginial_stderr = sys.stderr

    with Capturing() as _:
        assert sys.stdout is not orginial_stdout
        assert sys.stderr is not orginial_stderr

    assert sys.stdout is orginial_stdout
    assert sys.stderr is orginial_stderr
