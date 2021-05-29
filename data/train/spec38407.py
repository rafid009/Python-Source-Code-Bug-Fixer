import numpy as np 

def function(x):

	x6 = 7
	i5 = 3
	paths = []
	try:
		if i5 <= 2:
			x = x6-x
			x = x*x
			x = 7-x
			paths.append(1)
		else:
			x6 = 5/i5
			i5 = 3*i5
			x6 = 6+i5
			paths.append(2)
		if i5 >= 4:
			x = x-6
			paths.append(3)
		else:
			x = x6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))