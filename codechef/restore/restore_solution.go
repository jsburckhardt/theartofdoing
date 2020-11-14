package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer func() { _ = writer.Flush() }()

	T := int(ReadNum(reader))
	for i := 0; i < T; i++ {
		n := int(ReadNum(reader))
		b := ReadNums(reader, n)
		a := make([]int, n)
		st := 1
		for j := n - 1; j >= 0; j-- {
			if b[j]-1 == int64(j) {
				a[j] = st
				st++
			} else {
				a[j] = a[b[j]-1]
			}
		}
		for j := 0; j < n; j++ {
			_, _ = fmt.Fprint(writer, a[j], " ")
		}
		_, _ = fmt.Fprintln(writer)
	}
}

func ReadInt64(bs []byte, from int, val *int64) int {
	negative := false
	if from < len(bs) && bs[from] == '-' {
		negative = true
		from++
	}
	for from < len(bs) && bs[from] >= '0' && bs[from] <= '9' {
		*val = (*val)*10 + int64(bs[from]-'0')
		from++
	}
	if negative {
		*val *= -1
	}
	return from
}

func ReadNum(reader *bufio.Reader) (val int64) {
	bs, _ := reader.ReadBytes('\n')
	ReadInt64(bs, 0, &val)
	return
}

func ReadNums(reader *bufio.Reader, n int) []int64 {
	ret := make([]int64, n)
	bs, _ := reader.ReadBytes('\n')
	from := 0
	for i := 0; i < n; i++ {
		for from < len(bs) && (bs[from] < '0' || bs[from] > '9') && bs[from] != '-' {
			from++
		}
		from = ReadInt64(bs, from, &ret[i])
	}
	return ret
}

func ReadTwoNums(reader *bufio.Reader) (val0, val1 int64) {
	ret := ReadNums(reader, 2)
	val0, val1 = ret[0], ret[1]
	return
}

func ReadThreeNums(reader *bufio.Reader) (val0, val1, val2 int64) {
	ret := ReadNums(reader, 3)
	val0, val1, val2 = ret[0], ret[1], ret[2]
	return
}

func ReadFourNums(reader *bufio.Reader) (val0, val1, val2, val3 int64) {
	ret := ReadNums(reader, 4)
	val0, val1, val2, val3 = ret[0], ret[1], ret[2], ret[3]
	return
}
