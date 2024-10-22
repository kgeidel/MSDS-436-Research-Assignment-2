# Python imports
import itertools

# Django imports
from django.db import models
from django.db.models import Q
from django.utils import timezone

# Third-party imports
import pandas as pd


class EndState(models.Model):
    ''' An instance of this class is a potential end-of-game state in a tic-tac-toe game '''

    top_left = models.CharField(max_length=1, blank=True, null=True)
    top_middle = models.CharField(max_length=1, blank=True, null=True)
    top_right = models.CharField(max_length=1, blank=True, null=True)
    middle_left = models.CharField(max_length=1, blank=True, null=True)
    middle_middle = models.CharField(max_length=1, blank=True, null=True)
    middle_right = models.CharField(max_length=1, blank=True, null=True)
    bottom_left = models.CharField(max_length=1, blank=True, null=True)
    bottom_middle = models.CharField(max_length=1, blank=True, null=True)
    bottom_right = models.CharField(max_length=1, blank=True, null=True)
    x_wins_flag = models.BooleanField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = [
                    'top_left', 'top_middle', 'top_right',
                    'middle_left', 'middle_middle', 'middle_right',
                    'bottom_left', 'bottom_middle', 'bottom_right',
                ],
                name = 'unique_endstate',
            )
        ]

class BenchmarkTrial:
    ''' Instances of this vanilla (non-django) Python class represent a single trial of the Monte Carlo Performance benchmark '''

    def execute_query_task_1(self):
        # args for which X wins on the main diagonal
        x_main = Q(top_left='X', middle_middle='X', bottom_right='X')
        # args for which X wins on the anti diagonal
        x_anti = Q(bottom_right='X', middle_middle='X', top_right='X')
        # args for which O wins on the main diagonal
        o_main = Q(top_left='O', middle_middle='O', bottom_right='O')
        # args for which O wins on the anti diagonal
        o_anti = Q(bottom_right='O', middle_middle='O', top_right='O')    
        return EndState.objects.filter(
            x_main | x_anti | o_main | o_anti
        )

    def execute_query_task_2(self):
        return f'{100*EndState.objects.filter(x_wins_flag=True).count()/EndState.objects.all().count():0.2f}%'
    
    def execute_query_task_3(self):
        SCORE_MAP = {
            'top_left': 1,
            'top_middle': 2,
            'top_right': 3,
            'middle_left': 4,
            'middle_middle': 5,
            'middle_right': 6,
            'bottom_left': 7, 
            'bottom_middle': 8, 
            'bottom_right': 9,
        }
        # Keep track of the score
        scores = {'X': 0, 'O': 0}
        # using itertools to loop over every attr/square (top_left, top_middle, etc) of every record
        for game, attr in itertools.product(EndState.objects.all(), SCORE_MAP.keys()):
            # find which team owns this square
            owner = getattr(game, attr, None)
            if owner is not None:
                # increment that team's score by the square's value
                scores[owner] += SCORE_MAP[attr]
        return scores

    def run_trial(self):
        # Run each query task, time how long it takes
        t_0 = timezone.now()
        t1_results = self.execute_query_task_1()
        t_1 = timezone.now()
        t2_results = self.execute_query_task_2()
        t_2 = timezone.now()
        t3_results = self.execute_query_task_3()
        t_3 = timezone.now()
        # assemble & return the results in the form of a tuple
        # (
        #   task_1_duration, task_1_results, task_2_duration, task_2_results, task_3_duration, task_3_results
        # )
        return (
            t_1 - t_0, t1_results,
            t_2 - t_1, t2_results,
            t_3 - t_2, t3_results,
        )

class BenchmarkExperiment:
    ''' Objects of this class represent a collection of trials of the MC benchmark experiment '''
    RESULT_DF_COLUMNS = [
        'task_1_duration', 'task_1_results',
        'task_2_duration', 'task_2_results',
        'task_3_duration', 'task_3_results',
    ]

    def __init__(self, n=100):
        self.n = n
        self.results = pd.DataFrame(
            columns = self.RESULT_DF_COLUMNS
        )

    def run_benchmark(self):
        results = []
        for i in range(self.n):
            results.append(BenchmarkTrial().run_trial())
        self.results = pd.DataFrame(results, columns=self.RESULT_DF_COLUMNS)
        self.clean_results()

    def clean_results(self):
        ''' Neaten up how the results are displayed in the pandas dataframe '''
        
        # Have trial nums start at 1
        self.results.index += 1

        # These results are in microseconds, no need for days:hrs:mins: etc
        timedelta_cols = ['task_1_duration', 'task_2_duration', 'task_3_duration']
        for col in timedelta_cols:
            self.results[col] = self.results[col].apply(lambda x: x.microseconds)
        
        # The specific queryset of endstates isn't important.
        # We can just take a hash value of the queryset to show they are essentially the same
        self.results['task_1_results'] = self.results['task_1_results'].apply(
            lambda x: hash(x)
        )

        # Add a column with the total time for all tasks
        self.results['total_microseconds'] = self.results['task_1_duration'] + self.results['task_2_duration'] + self.results['task_3_duration']