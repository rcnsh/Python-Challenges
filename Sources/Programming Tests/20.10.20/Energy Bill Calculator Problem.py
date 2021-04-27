def RawEnergyOutput(PreviousMeterReading, CurrentMeterReading, CalorificValue):
    UnitsUsed = CurrentMeterReading - PreviousMeterReading
    kWh = UnitsUsed * 1.022 * CalorificValue / 3.6
    Energy = 0.0284 * kWh
    return Energy

TotalCost = RawEnergyOutput(50, 40, 39.3)