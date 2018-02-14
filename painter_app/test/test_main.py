from unittest import TestLoader, TextTestRunner, TestSuite
from painter_app.test.test_modules import TestModules
from painter_app.test.test_painter_main import TestPainterMain

if __name__ == "__main__":
    loader = TestLoader()
    start_dir = ''
    suite = loader.discover(start_dir)

    runner = TextTestRunner(verbosity = 2)
    runner.run(suite)

