from evaluator.truckRequirements import truckRequirements

def assert_requirements(truck, measurement):
    """
    Run all tests and return the result
    """
    results = []
    for req in truckRequirements:
        results.append(req.testRequirement(truck, measurement))
    return results
