import unittest
from unittest.mock import patch, MagicMock
import reader

class TestReader(unittest.TestCase):

    @patch('reader.socket.socket')
    def test_receive_time(self, mock_socket):
        mock_sock_instance = MagicMock()
        mock_socket.return_value = mock_sock_instance
        mock_sock_instance.recvfrom.return_value = (b'current_time', ('localhost', 12345))

        reader_instance = reader.Reader(('localhost', 12345))
        received_time = reader_instance.receive_time()

        mock_sock_instance.recvfrom.assert_called_once()
        self.assertEqual(received_time, 'current_time')

    @patch('reader.socket.socket')
    def test_close(self, mock_socket):
        mock_sock_instance = MagicMock()
        mock_socket.return_value = mock_sock_instance

        reader_instance = reader.Reader(('localhost', 12345))
        reader_instance.close()

        mock_sock_instance.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
