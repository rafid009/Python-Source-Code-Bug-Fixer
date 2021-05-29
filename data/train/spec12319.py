import numpy as np 

def function(x):

	a2 = x
	i2 = x
	paths = []
	try:
		if x <= 4:
			i2 = x-5
			paths.append(1)
		else:
			x = x+1
			i2 = i2+1
			paths.append(2)
		if a2 > 2:
			i2 = 0/i2
			x = x/6
			paths.append(3)
		else:
			a2 = a2-7
			i2 = 1-i2
			i2 = i2*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))