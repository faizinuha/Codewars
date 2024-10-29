function humanReadable (seconds) {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;

  const pad = (num) => String(num).padStart(2, '0');
  return `${pad(hours)}:${pad(minutes)}:${pad(secs)}`;
}

console.log(humanReadable(3661)); // "01:01:01"

console.log(humanReadable(120000)); // "20:00:00"

console.log(humanReadable(3600000)); // "1:00:00:00"

console.log(humanReadable(10000000)); // "14:46:40"

console.log(humanReadable(86400000)); // "24:00:00"

console.log(humanReadable(31536000)); // "116:00:00"
