# Dự Án Thu Thập Dữ Liệu Tin Tức

## Giới Thiệu

Dự án này sử dụng Apache Airflow để tự động thu thập dữ liệu tin tức từ các trang web và lưu trữ dữ liệu vào cơ sở dữ liệu PostgreSQL. 
Sử dụng Flask được sử dụng để hiển thị các tin tức đã thu thập được và cung cấp một giao diện người dùng để xem tin tức.

## Các Thành Phần

- **Airflow**: Quản lý và tự động hóa các tác vụ thu thập dữ liệu.
- **Flask**: Xây dựng giao diện người dùng để hiển thị tin tức.
- **PostgreSQL**: Lưu trữ dữ liệu tin tức.
- **Docker**: Container hóa ứng dụng và cơ sở dữ liệu.
