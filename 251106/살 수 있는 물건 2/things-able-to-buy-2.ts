import * as fs from "fs";
const input = fs.readFileSync(0, "utf-8").trim();
const N = parseInt(input);

const items: { [key: string]: number } = {
  book: 3000,
  mask: 1000,
  pen: 500,
};

let maxPrice = 0;
let result = "no";

for (const [name, price] of Object.entries(items)) {
  if (price <= N && price > maxPrice) {
    maxPrice = price;
    result = name;
  }
}

console.log(result);
