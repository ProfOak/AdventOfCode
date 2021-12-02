package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var (
		file    *os.File
		scanner *bufio.Scanner
		numbers []int
	)

	file, _ = os.Open("day1.input")
	defer file.Close()

	scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		i, _ := strconv.Atoi(scanner.Text())
		numbers = append(numbers, i)
	}

	fmt.Println(partOne(numbers))
	fmt.Println(partTwo(numbers))
}

func partOne(numbers []int) int {
	var (
		total int
		prev  int
	)
	prev = numbers[0]
	for _, next := range numbers[1:] {
		if next > prev {
			total++
		}
		prev = next
	}
	return total
}

func partTwo(numbers []int) int {
	var (
		prev  int = numbers[0] + numbers[1] + numbers[2]
		total int
	)
	for i, next := range numbers[1:] {
		if i+3 > len(numbers) {
			break
		}

		next = numbers[i] + numbers[i+1] + numbers[i+2]
		if next > prev {
			total++
		}
		prev = next
	}
	return total
}
