import numpy as np 

def function(x):

	a9 = x
	i2 = x
	paths = []
	try:
		if a9 >= 8:
			i2 = i2*a9
			a9 = a9-a9
			paths.append(1)
		else:
			a9 = x-i2
			a9 = x-a9
			paths.append(2)
		if i2 > 7:
			i2 = 4+i2
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		a9 = i2**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))