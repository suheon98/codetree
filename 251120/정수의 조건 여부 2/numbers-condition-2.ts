import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim();
const a = Number(input);

if (a === 5) {
    console.log("A");
}
if (a % 2 === 0) {
    console.log("B");
}
