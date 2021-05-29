import numpy as np 

def function(x):

	a2 = x
	i2 = x
	paths = []
	try:
		if a2 >= 6:
			a2 = x/i2
			a2 = 0/a2
			x = a2-5
			paths.append(1)
		else:
			i2 = x/i2
			paths.append(2)
		if a2 >= 7:
			a2 = 3*0
			i2 = 6-6
			paths.append(3)
		else:
			i2 = 0*0
			i2 = i2-x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))