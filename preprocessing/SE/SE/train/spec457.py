import numpy as np 

def function(x):

	l3 = 2
	i2 = 9
	paths = []
	try:
		if l3 >= 3:
			x = x*l3
			paths.append(1)
		else:
			x = x*4
			l3 = 9-l3
			l3 = 5/l3
			paths.append(2)
		if i2 >= 0:
			x = 6-x
			paths.append(3)
		else:
			i2 = i2*i2
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))