from cmath import phase
from machine import Pin, I2C, SPI
from modules.configuration import Configuration

def init_i2c(cfg:Configuration):
    i2c_if = cfg.get("i2c")
    scl_pin = Pin(cfg.get("scl"))
    sda_pin = Pin(cfg.get("sda"))
    freq = cfg.get("freq")
    return I2C(i2c_if, scl=scl_pin, sda=sda_pin, freq=freq)

def init_spi(cfg:Configuration):
    spi_if = cfg.get("spi")
    miso_pin = Pin(cfg.get("miso"))
    sck_pin = Pin(cfg.get("sck"))
    mosi_pin = Pin(cfg.get("mosi"))
    baudrate = cfg.get("baudrate") or 1000000
    polarity = cfg.get("polarity") or 1
    phase = cfg.get("phase") or 1
    return SPI(spi_if,
            miso=miso_pin, 
            sck=sck_pin, 
            mosi=mosi_pin,
            bits=8,
            firstbit=SPI.MSB,
            baudrate=baudrate,
            polarity=polarity,
            phase=phase)