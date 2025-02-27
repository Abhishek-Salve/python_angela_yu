# pseudo code
# apis ?

# testcases
# register write
# sw

# wdt

# clock 1 Mhz
# wdt counter = 5 seconds
# WDTCNT 64bits --> hex value
# prescaler 1

# 1/1mhz * wdt_count = 5 seconds
# wdt_count = 5 * 1Mhz
# wdt_count = 5 s/ 0.0000001 s

# WDT ISR enable
# GPREG = 0x5a5a5a5a
# j.write_reg(WDTCNT, wdt_count)
# j.write_reg(WDT_START)
# time.sleep(5)
# check GPREG pass register
# check WDT status

# prescaler 2
#

