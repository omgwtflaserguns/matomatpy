
import abc


class FormBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def show(self, screen):
        return
