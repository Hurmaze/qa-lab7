import parser


class TestSuite():
    def test_iperf3_client_connection(self, client):
        output, error = client
        assert not error
        results = parser.parse(output)
        for line in results:
            assert float(line['Transfer']) > 1.5 and float(line['Bandwidth']) > 1
