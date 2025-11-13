// 최대 2번의 연산 - TypeScript 풀이

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim();
let a: number = parseInt(input, 10);

// 1번 과정: a가 짝수라면 2로 나눈다
if (a % 2 === 0) {
  a = a / 2;
}

// 2번 과정: (1번 과정을 거친 뒤) a가 홀수라면 1을 더한 뒤 2로 나눈다
if (a % 2 !== 0) {
  a = (a + 1) / 2;
}

console.log(a.toString());
