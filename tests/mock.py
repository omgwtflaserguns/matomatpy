
class MicroMock(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @staticmethod
    def get_log_mock():
        return MicroMock(fatal=lambda msg: (),
                         error=lambda msg: (),
                         info=lambda msg: (),
                         debug=lambda msg: (),
                         warn=lambda msg: (),
                         warning=lambda msg: ())
