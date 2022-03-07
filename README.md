# LATIHAN4DPBO2022

> Saya Rizal Teddyansyah (2000107) mengerjakan Latihan 4 dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk kkeberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin...

Repository ini dibuat untuk memenuhi Tugas Latihan 4 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek (DPBO).

## Desain
![Desain.png](https://github.com/rzltdysh17/LATIHAN4DPBO2022/blob/main/Desain.png)

- Kelas Vehicle merupakan parent dari kelas Airplane dan Ship. Karena Airplane dan Ship sendiri merupakan jenis dari kendaraan (vehicle). Oleh karena itu, hubungan antar kelas menggunakan Hierarchical Inheritance.
- Kelas Person dan Job merupakan parent dari kelas Driver. Karena Driver merupakan manusia (person) dan jenis pekerjaan (job). Oleh karena itu, hubungan antar kelas menggunakan Multiple Inheritance.
- Yang membedakan antara kelas Airplane dan Ship adalah adanya atribut tambahan yang berbeda yaitu wingsLength dengan tipe data Float untuk kelas Airplane dan countryOfManufacture dengan tipe data String untuk kelas Ship. 
- Pada kelas Vehicle terdapat metode move menggunakan atribut isMove dengan tipe data Boolean. Dimana True "is moving" dan False "isn't moving".
- Pada kelas Person terdapat metode sleep menggunakan atribut isSleep dengan tipe data Boolean. Dimana True "is sleeping" dan False "isn't sleeping".

## Screenshoot dari Program setelah dijalankan:
- Airplane

  ![airplane.png](https://github.com/rzltdysh17/LATIHAN4DPBO2022/blob/main/SS/airplane.png)

- Vehicle from Airplane

  ![vehicle_airplane](https://github.com/rzltdysh17/LATIHAN4DPBO2022/blob/main/SS/vehicle_airplane.png)

- Ship
  
  ![ship.png](https://github.com/rzltdysh17/LATIHAN4DPBO2022/blob/main/SS/ship.png)
  
- Vehicle from Ship
  
  ![vehicle_ship.png](https://github.com/rzltdysh17/LATIHAN4DPBO2022/blob/main/SS/vehicle_ship.png)
  
- Driver

  ![driver1.png](https://github.com/rzltdysh17/LATIHAN4DPBO2022/blob/main/SS/driver1.png)
  ![driver2.png](https://github.com/rzltdysh17/LATIHAN4DPBO2022/blob/main/SS/driver2.png)
  
 - Person from Driver
   
   ![person.png](https://github.com/rzltdysh17/LATIHAN4DPBO2022/blob/main/SS/person.png)

 - Job from Driver
   
   ![job.png](https://github.com/rzltdysh17/LATIHAN4DPBO2022/blob/main/SS/job.png)
