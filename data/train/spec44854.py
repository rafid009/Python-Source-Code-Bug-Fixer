import numpy as np 

def function(x):

	j7 = x
	i2 = 6
	paths = []
	try:
		if x > 5:
			x = x*4
			paths.append(1)
		else:
			i2 = i2-7
			x = 8*x
			paths.append(2)
		if x <= 4:
			i2 = j7/i2
			x = i2/x
			paths.append(3)
		else:
			x = x/j7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))