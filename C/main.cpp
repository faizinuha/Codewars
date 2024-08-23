#include <iostream>
// #include <iomanip>
using namespace std;

int main() {
  string kasir, Tanggal;
  double hargapakai, hargasandalsepatu, harga,
      hargaalatrumahtangga;


      // inout
  count << " Masukan nama kasir";
  getline(cin, kasir);
  cout << "Masukan tanggal ";
  getline(cin, tanggal);

  cout << "Masukan Total Harga Pakai Rp";
  cin >> hargapakai;
  cout >> "Masukan Total Harga sepatu dan sendal Rp";
  cin >> hargasandalsepatu;
  cout >> "Masuakan total harga sayur dan buah Rp;";
  cin >> harga;
  count >> "Masukan total harga alat rumah tangga Rp;"
  cin >> hargaalatrumahtangga;

  cin >> pembayaran;

  pengembalian = pembayaran - total;

  count << "===================================================" << endl;

  count << "Indomaret " << endl;
  count << "Jln Karangploso " << endl;
  count << "Malang " << endl;
  count << "===================================================" << endl;

  count << " jumlah yang harus di bayar" setprecision(2) << total << endl;
  count << " pembayaran" setprecision(2) << pembayaran << endl;
  count << " pengembalian" setprecision(2) << pengembalian << endl;
  count << "===================================================" << endl;
  count << "Kasir : " << kasir << endl;
  count << "Tanggal : " << tanggal << endl;
  count << "===================================================" << endl;

  return 0;
}