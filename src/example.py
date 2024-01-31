from rtctools.optimization.collocated_integrated_optimization_problem import (
    CollocatedIntegratedOptimizationProblem,
)
from rtctools.optimization.csv_mixin import CSVMixin
from rtctools.optimization.goal_programming_mixin import GoalProgrammingMixin, Goal
from rtctools.optimization.modelica_mixin import ModelicaMixin
from rtctools.util import run_optimization_problem


class ExampleGoal(Goal):
    def function(self, optimization_problem, ensemble_member):
        return optimization_problem.state("x")
    
    priority = 1
    order = 2


class Example(GoalProgrammingMixin, CSVMixin, ModelicaMixin, CollocatedIntegratedOptimizationProblem):

    def path_goals(self):
        return [ExampleGoal()]


# Run
run_optimization_problem(Example)
