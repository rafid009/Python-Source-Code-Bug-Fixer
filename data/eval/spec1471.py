import numpy as np 

def function(x):

	i2 = 7
	a0 = 9
	paths = []
	try:
		if a0 > 4:
			a0 = 8-a0
			paths.append(1)
		else:
			i2 = 6*x
			paths.append(2)
		if i2 > 6:
			i2 = a0*x
			x = x/6
			a0 = i2-4
			paths.append(3)
		else:
			a0 = a0/3
			a0 = i2-a0
			a0 = 6+2
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		i2 = a0**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))