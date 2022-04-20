Usage

-- 创建网络命名空间 CreateNetns.sh --
sh CreateNetns.sh NETNS_NAME

-- 创建网桥 CreateBr.sh --
sh CreateBr.sh BRIDGE_NAME

-- 创建veth对 CreateVethPair.sh --
sh CreateVethPair.sh VETH_1 VETH_p

-- 启动设备 Setup.sh --
sh Setup.sh DEVICE_NAME 
或
sh Setup.sh DEVICE_NAME NETNS_NAME //设备在网络命名空间时

-- 添加IP AddIP.sh --
sh AddIP.sh DEVICE_NAME DEVICE_IP NETNS_NAME //设备在网络命名空间内时
或
sh AddIP.sh DEVICE_NAME DEVICE_IP

-- 将veth连在网络命名空间 VethToNetns.sh --
sh VethToNetns.sh VETH_NAME NETNS_NAME

-- 将设备连在网桥上 MasterBr.sh --
sh MasterBr.sh DEVICE_NAME BRIDGE_NAME

-- 删除 # bysj
# bysj
