function add(a, b) {
  let carry = 0;
  let result = "";
  
  let i = a.length - 1;
  let j = b.length - 1;
  
  while (i >= 0 || j >= 0 || carry > 0) {
    const digit1 = i >= 0 ? +a[i] : 0;
    const digit2 = j >= 0 ? +b[j] : 0;
    const sum = digit1 + digit2 + carry;
    
    result = (sum % 10) + result;
    carry = Math.floor(sum / 10);
    
    i--;
    j--;
  }
  
  return result;
}

// Contoh penggunaan
console.log(add("123", "321")); // "444"
console.log(add("11", "99"));   //
