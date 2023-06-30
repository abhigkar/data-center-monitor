import board
import busio
import winbond
import digitalio
import storage

clock = board.GP18
MOSI = board.GP19
MISO = board.GP16
CS = digitalio.DigitalInOut(board.GP15)

spi = busio.SPI(clock, MOSI, MISO)

flash = winbond.W25QFlash(spi, CS)
#vfs = storage.VfsFat(flash)
#storage.mount(vfs, "/flash")