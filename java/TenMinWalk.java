public class TenMinWalk {
  public static boolean isValid(char[] walk) {
    // Jika panjang array bukan 10, kembalikan false
    if (walk.length != 10) {
      return false;
    }
    
    int north = 0, south = 0, east = 0, west = 0;
    
    // Iterasi melalui array walk dan hitung masing-masing arah
    for (char direction : walk) {
      switch (direction) {
        case 'n': north++; break;
        case 's': south++; break;
        case 'e': east++; break;
        case 'w': west++; break;
      }
    }
    
    // Periksa apakah langkah ke utara sama dengan langkah ke selatan
    // dan langkah ke timur sama dengan langkah ke barat
    return north == south && east == west;
  }
  
  public static void main(String[] args) {
    // Contoh kasus uji
    System.out.println(isValid(new char[] {'n','s','n','s','n','s','n','s','n','s'})); // true
    System.out.println(isValid(new char[] {'w','e','w','e','w','e','w','e','w','e','w','e'})); // false
    System.out.println(isValid(new char[] {'w'})); // false
    System.out.println(isValid(new char[] {'n','n','n','s','n','s','n','s','n','s'})); // false
  }
}
