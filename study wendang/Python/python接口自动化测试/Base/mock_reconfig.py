import mock


def mock_reconfig(response_data, mock_method, url, requests_data, method):
    mock_data = mock.Mock(return_value=response_data)
    mock_method = mock_data
    res = mock_method(url, method, requests_data)
    return res
