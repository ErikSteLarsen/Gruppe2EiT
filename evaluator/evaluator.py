from evaluator.truckRequirements import truckRequirements

class Evaluator:

    def assert_requirements(truck, measurement):
        """
        Run all tests and print the result

        TODO: Bedre håndtering av resultat, unngå printing i indre funksjoner
        """
        for req in truckRequirements:
            result = req.testRequirement(truck, measurement)
            print(result)
            return result
