rentalTruck = 29.95

milesCost = 0.99

dolly = 10.00

estimateMiles = 30

tax = 0.0825

fee = 1

print "Cost of Uhaul truck: ",  rentalTruck
print "Cost of dolly: ", dolly
print "Cost per mile: ", milesCost
print "Estimated mileage: ", estimateMiles

print "Mileage estimated cost :", milesCost * estimateMiles

estimatedTax = (rentalTruck + dolly + fee + (milesCost * estimateMiles)) * tax

print "Estimated tax = ", estimatedTax

print "Total = ", estimatedTax + (milesCost * estimateMiles) + rentalTruck + dolly + fee

