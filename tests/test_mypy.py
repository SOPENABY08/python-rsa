import pathlib
import unittest

import mypy.api

test_modules = ['rsa', 'tests']


class MypyRunnerTest(unittest.TestCase):
    def test_run_mypy(self):
        proj_root = pathlib.Path(__file__).parent.parent
        args = ['--incremental', '--ignore-missing-imports'] + [str(proj_root / dirname) for dirname
                                                                in test_modules]

        result = mypy.api.run(args)

        stdout, stderr, status = result

        messages = []
        if stderr:
            messages.append(stderr)
        if stdout:
            messages.append(stdout)
        if status:
            messages.append('Mypy failed with status %d' % status)
        if messages:
            self.fail('\n'.join(['Mypy errors:'] + messages))
