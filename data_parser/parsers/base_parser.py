from abc import ABCMeta, abstractmethod

from data_parser.exceptions import InvalidFormatError


class BaseParser(metaclass=ABCMeta):
    _enabled_outputs = []
    _output_mapper = dict()
    _internal_data = None

    def __init__(self, raw_data):
        self._raw_data = raw_data

    def process_data(self, output_format=None):
        self._validate_output_format(output_format)
        mapped_output = self._output_mapper[output_format]
        if not self._internal_data:
            self._internal_data = self._data_to_internal_format()
        return self._get_output(mapped_output)

    @abstractmethod
    def _data_to_internal_format(self):
        pass

    @abstractmethod
    def _get_output(self, mapped_output):
        pass

    def _validate_output_format(self, output_format):
        if not output_format:
            raise InvalidFormatError("Output format can't be None")
        if output_format not in self._enabled_outputs:
            raise InvalidFormatError("Output format not in "
                                     ", ".join(self._enabled_outputs))