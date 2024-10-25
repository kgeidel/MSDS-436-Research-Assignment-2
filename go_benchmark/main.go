package main

import (
	"database/sql"
	"fmt"
	"io/fs"
	"log"
	"os"
	"time"

	_ "github.com/mattn/go-sqlite3"
)

type EndState struct {
	id            int
	top_left      sql.NullString
	top_middle    sql.NullString
	top_right     sql.NullString
	middle_left   sql.NullString
	middle_middle sql.NullString
	middle_right  sql.NullString
	bottom_left   sql.NullString
	bottom_middle sql.NullString
	bottom_right  sql.NullString
	x_wins_flag   bool
}

func main() {
	n := 100
	fmt.Printf("RUNNING %d TRIALS...", n)
	run_experiment(n)
	fmt.Print("DONE\n\n")
}

func get_endstates() []EndState {
	// Connect to db
	db, err := sql.Open("sqlite3", "../mc_benchmark/db.sqlite3")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// query db
	rows, err := db.Query("SELECT * FROM core_endstate;")
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	// make EndState structs and append to a slice
	var records []EndState

	for rows.Next() {
		// Init an endstate record
		var record EndState
		err = rows.Scan(
			&record.id,
			&record.top_left,
			&record.top_middle,
			&record.top_right,
			&record.middle_left,
			&record.middle_middle,
			&record.middle_right,
			&record.bottom_left,
			&record.bottom_middle,
			&record.bottom_right,
			&record.x_wins_flag,
		)
		if err != nil {
			log.Fatal(err)
		}
		// add it to records
		records = append(records, record)
	}
	return records
}

func run_experiment(n int) {
	// Prepare a file to record results
	results_filepath := "results.csv"
	mode := os.O_APPEND | os.O_WRONLY
	perm := fs.FileMode(0664)
	file, err := os.OpenFile(results_filepath, mode, perm)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Iterate over n trials
	for i := 0; i < n; i++ {
		t1, t2, t3, t_total := run_trial()
		results_entry := fmt.Sprintf("%d, %d, %d, %d\n", t1, t2, t3, t_total)
		_, err := file.WriteString(results_entry)
		if err != nil {
			log.Fatal(err)
		}
	}
	file.Sync()
}

func run_trial() (int64, int64, int64, int64) {
	t_0 := time.Now()
	execute_query_task_1()
	t_1 := time.Now()
	execute_query_task_2()
	t_2 := time.Now()
	execute_query_task_3()
	t_3 := time.Now()
	// calculate task durations
	d_1 := t_1.Sub(t_0)
	d_1us := d_1.Microseconds()
	d_2 := t_2.Sub(t_1)
	d_2us := d_2.Microseconds()
	d_3 := t_3.Sub(t_2)
	d_3us := d_3.Microseconds()
	d_total := d_1us + d_2us + d_3us
	return d_1us, d_2us, d_3us, d_total
}
