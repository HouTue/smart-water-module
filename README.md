Bước 1: Đăng ký 
 https://www.hivemq.com/mqtt-cloud-broker/
 Sau đó tạo một cluster và lấy những thông tin sau
Host: x
Port: x
Username: x
Password: x

Bước 2: Install thư viện chạy thử file py
- pip install -r requirements.txt
        Chạy thử file water_sensor_sim.py
- py water_sensor_sim.py

Bước 3: Cài đặt node.js, red-node
https://nodejs.org tải những phiên bản LTS (rcm v24.3.0)
Kiểm tra xem đã cài đặt, có node.js chưa sau đó tới bước cài đặt red-node
- npm install -g --unsafe-perm node-red
Sau khi cài đặt xong chạy: node-red và vào http://localhost:1880

Bước 4: Setup Manage palette
- Vào Manage palette chọn install
- Tại thanh tìm kiếm: node-red-contrib-mqtt-broker -> Install
- Tương tự node-red-dashboard -> Install 

Bước 5: Copy flow.json và vào import trên mqtt sau đó ấn deloy (ở bước này cần chỉnh lại một tí kết nối nếu bị lỗi mqtt in/out không connect được)

Bước 6: Ấn deloy và qua file main py chạy

Bước 7: Vào dashboard http://localhost:1880/ui