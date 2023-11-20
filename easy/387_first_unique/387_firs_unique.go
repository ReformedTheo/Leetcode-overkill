package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Printf("Enter string: ")
	var str string
	fmt.Scanln(&str)
	strLow := strings.ToLower(str)

	// Create a map to count occurrences of each character
	charCount := make(map[rune]int)

	// Populate the map with character counts
	for _, char := range strLow {
		charCount[char]++
	}

	// Check for characters that appeared more than once
	for char, count := range charCount {
		if count > 1 {
			fmt.Printf("Char %c repeated in string \n", char)
		}
	}
}
