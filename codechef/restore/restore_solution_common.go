package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type FastReader struct {
	index  int
	tokens []string
	*bufio.Reader
}

func (r *FastReader) UpdatesTokenIfRequired() {
	if len(r.tokens) == r.index {
		line, _ := r.ReadString('\n')
		r.tokens = strings.Fields(line)
		r.index = 0
	}
}

func (r *FastReader) NextToken() string {
	r.UpdatesTokenIfRequired()
	token := (r.tokens)[r.index]
	r.index++
	return token
}

func (r *FastReader) ReadInt() int {
	val, _ := strconv.Atoi(r.NextToken())
	return val
}
func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

var max = 4 * 1000000

func next() int {
	max--
	return max
}

func main() {
	reader := FastReader{Reader: bufio.NewReader(os.Stdin)}
	tests := reader.ReadInt()

	for i := 0; i < tests; i++ {
		max = 4 * 1000000

		N := reader.ReadInt()
		dict := map[int]int{}

		for i := 0; i < N; i++ {
			temp := reader.ReadInt()

			if _, ok := dict[temp]; !ok {
				dict[temp] = next()
			}

			fmt.Printf("%d ", dict[temp])
		}

		fmt.Println()
	}
}
