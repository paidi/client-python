import requests
import json
import config

def report_result(**kwargs):
    """Report result to the RiseML API.

    You can provide experiment_id as part of kwargs explcitly.
    Otherwise it will be inferred from the environment.

    Args:
        **kwargs: Arbitrary arguments with result: value pairs.

    Returns:
        None
    
    Example:
        report_result(accuracy=.3, loss=.1)

    """
    if not config.experiment_id:
        experiment_id = kwargs.pop('experiment_id', None)
    if experiment_id:
        try:
            r = requests.post('%s/experiments/%s/result' % (config.api_host,
                                                            experiment_id),
                              data = {'result': json.dumps(kwargs)})
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print('Results not reported: %s' % e)
    else:
        print('Results not reported. Can only report inside running job environment.')