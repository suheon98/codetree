import * as fs from "fs";

// 입력 전체를 읽어서 공백 기준으로 나눔
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const a = input[0];
const b = input[1];

function parity(n: number): string {
  return n % 2 === 0 ? "even" : "odd";
}

// 각 수에 대한 짝/홀 정보 출력
console.log(parity(a));
console.log(parity(b));
