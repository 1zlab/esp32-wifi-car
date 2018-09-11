import micropython
from machine import Timer
from car_config import car_property
from car import Car
import utime
# 设定紧急意外缓冲区的大小为100
micropython.alloc_emergency_exception_buf(100)

# 创建一个小车
car = Car(is_debug=True)

# # 创建定时器 这里用的是定时器4
# timer = Timer(4)
# # 设置定时器回调 100ms执行一次
# ctl_period = int(car_property['PID_CTL_PERIOD']*1000) # 控制周期，转换为ms
# timer.init(period=ctl_period, mode=Timer.PERIODIC, callback=lambda t: car.callback(t))

car.left_motor.pwm(500)
car.right_motor.pwm(500)

# 前进5s
utime.sleep_ms(5000)

# 停下
car.stop()