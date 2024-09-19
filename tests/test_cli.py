import subprocess
import pytest

def test_create_user():
    result = subprocess.run(
        ['python', 'fittrack/cli.py', '--create-user', '--name', 'John Doe', '--age', '30', '--height', '180', '--weight', '75', '--fitness-level', 'Intermediate'],
        capture_output=True, text=True
    )
    assert 'User \'John Doe\' created successfully.' in result.stdout
