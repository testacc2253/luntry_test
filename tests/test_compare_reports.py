from utils import check_lists_similarity, load_json_file


def test_compare_reports(base_client):
    application_name = 'registry.luntry.com/luntry/charon'
    reference_report_name = 'reference_report.json'

    cluster_id = base_client.get_cluster_id()
    digest = base_client.get_image_digest(cluster_id, application_name)
    image_id = base_client.get_image_id(digest)
    report = base_client.get_report(image_id)

    reference_report = load_json_file(reference_report_name)
    result = check_lists_similarity(report, reference_report)

    assert result is True, "The reports do not match."
