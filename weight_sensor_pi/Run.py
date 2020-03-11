import time
import spidev

spi_ch = 0

"""
" Interface for reading ADC-value of mcp3008
" Remenber install spidev with pip install spidev
" [Used interface for mcp3002 with two channel input]pip install spidev
"""


# Enable SPI
spi = spidev.SpiDev(0, spi_ch)
spi.max_speed_hz = 1200000

def read_adc(adc_ch, vref = 5):
    # Make sure ADC channel is 0 or 1
    if adc_ch >= 8:
        adc_ch = 0
    
    # Construct SPI message
    #  First bit (Start): Logic high (1)
    #  Second bit (SGL/DIFF): 1 to select single mode
    #  Third bit (ODD/SIGN): Select channel
    #  Fourth bit (MSFB): 0 for LSB first
    #  Next 12 bits: 0 (don't care)

    msg = 0b10000000 | ( ((adc_ch & 7) << 4))
    msg = [0b00000001, msg, 0b00000000]
    reply = spi.xfer2(msg)

    # Construct single integer out of the reply (2 bytes)
    adc_readout = []
    adc = 0
    for n in reply:
        adc_readout.append(n)
        #adc = (adc << 8) + n

    # Last bit (0) is not part of ADC value, shift to remove it
    adc = adc >> 1
    value = (adc_readout[1]<<8) & 0b1100000000
    value = value | (adc_readout[2] & 0xff)
    adc = value

    # Calculate voltage form ADC value
    voltage = (vref * adc) / 1024

    return voltage

# Report the channel 0 and channel 1 voltages to the terminal
try:
    while True:
        before = time.time()
        adc_0 = read_adc(0)
        after = time.time()
        total_time = after - before
        print("time: %.20f\n" % total_time)
        print("Ch 0:", round(adc_0, 2), "V")
        time.sleep(1)

finally:
    GPIO.cleanup()
