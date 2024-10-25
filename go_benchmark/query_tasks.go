package main

import (
	"fmt"
	"math"
)

func execute_query_task_1() []EndState {
	records := get_endstates()
	// Prepare to catch the matching EndStates
	var matches []EndState
	// iterate through the records and check for the matching condition
	for i := 0; i < len(records); i++ {
		r := records[i]
		if r.top_left.String == "X" && r.middle_middle.String == "X" && r.bottom_right.String == "X" {
			// X won on the main diagonal
			matches = append(matches, r)
		} else if r.bottom_left.String == "X" && r.middle_middle.String == "X" && r.top_right.String == "X" {
			// X won on the anti diagonal
			matches = append(matches, r)
		} else if r.top_left.String == "O" && r.middle_middle.String == "O" && r.bottom_right.String == "O" {
			// O won on the main diagonal
			matches = append(matches, r)
		} else if r.bottom_left.String == "O" && r.middle_middle.String == "O" && r.top_right.String == "O" {
			// O won on the anti diagonal
			matches = append(matches, r)
		}
	}
	return matches
}

func execute_query_task_2() string {
	records := get_endstates()
	var win_count int
	for i := 0; i < len(records); i++ {
		if records[i].x_wins_flag {
			win_count += 1
		}
	}
	result := float64(win_count) / float64(len(records)) * 100
	result = math.Round(result*100) / 100
	return fmt.Sprintf("%.2f%%", result)
}

type Score struct {
	X int
	O int
}

func execute_query_task_3() Score {
	records := get_endstates()
	var score Score
	for i := 0; i < len(records); i++ {
		r := records[i]
		if r.top_left.String == "X" {
			score.X += 1
		} else if r.top_left.String == "O" {
			score.O += 1
		}
		if r.top_middle.String == "X" {
			score.X += 2
		} else if r.top_middle.String == "O" {
			score.O += 2
		}
		if r.top_right.String == "X" {
			score.X += 3
		} else if r.top_right.String == "O" {
			score.O += 3
		}
		if r.middle_left.String == "X" {
			score.X += 4
		} else if r.middle_left.String == "O" {
			score.O += 4
		}
		if r.middle_middle.String == "X" {
			score.X += 5
		} else if r.middle_middle.String == "O" {
			score.O += 5
		}
		if r.middle_right.String == "X" {
			score.X += 6
		} else if r.middle_right.String == "O" {
			score.O += 6
		}
		if r.bottom_left.String == "X" {
			score.X += 7
		} else if r.bottom_left.String == "O" {
			score.O += 7
		}
		if r.bottom_middle.String == "X" {
			score.X += 8
		} else if r.bottom_middle.String == "O" {
			score.O += 8
		}
		if r.bottom_right.String == "X" {
			score.X += 9
		} else if r.bottom_right.String == "O" {
			score.O += 9
		}
	}
	return score
}
