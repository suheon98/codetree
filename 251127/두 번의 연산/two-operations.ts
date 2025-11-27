// 두 번의 연산 - TypeScript

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim();
let A = Number(input);

// 1단계: 홀수면 3 더하기
if (A % 2 !== 0) {
  A += 3;
}

// 2단계: 3의 배수면 3으로 나누기
if (A % 3 === 0) {
  A = A / 3;
}

// 결과 출력
console.log(A);
