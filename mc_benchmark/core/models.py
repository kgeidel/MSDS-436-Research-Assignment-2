from django.db import models


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