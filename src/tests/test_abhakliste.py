from pytest import CaptureFixture, fixture, raises

from abhakliste import Abhakliste


@fixture
def abhaker() -> Abhakliste:
    """Initialize the Abhakliste object.

    Returns:
        The Abhakliste object.
    """
    return Abhakliste()


def test_error_capturing(abhaker: Abhakliste) -> None:
    """Test that the error is captured and can be retrieved."""
    with abhaker.run_context(desc="Test"):
        raise ValueError("Error")


def test_run_context(abhaker: Abhakliste) -> None:
    """Test that the run_context works as expected."""
    variable = "old"
    with abhaker.run_context(desc="Test"):
        variable = "new"
    assert variable == "new", "The context manager did not run the code inside it."


def test_output(abhaker: Abhakliste, capsys: CaptureFixture) -> None:
    """Test that the output is as expected."""
    description = "Test Description"
    normal_msg = "Test Output"
    error_msg = "Test Error Output"

    with abhaker.run_context(desc=description):
        print(normal_msg)

    with abhaker.run_context(desc=description):
        print(error_msg)
        raise ValueError("Error")

    output = capsys.readouterr()
    assert description in output.out
    assert normal_msg not in output.out
    assert error_msg in output.out


def test_error_count(abhaker: Abhakliste) -> None:
    """Test that failed tasks are counted."""
    with abhaker.run_context(desc="Test"):
        raise ValueError("Error")

    assert abhaker.error_runs == 1
    assert abhaker.total_runs == 1

    with raises(RuntimeError):
        abhaker.raise_on_fail()
