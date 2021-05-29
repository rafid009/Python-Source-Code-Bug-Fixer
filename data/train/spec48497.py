import numpy as np 

def function(x):

	j1 = x
	o8 = 5
	paths = []
	try:
		if j1 <= 7:
			x = x+o8
			o8 = 7*x
			paths.append(1)
		else:
			j1 = j1/2
			o8 = 4-3
			paths.append(2)
		if o8 > 6:
			x = x-x
			o8 = o8/9
			paths.append(3)
		else:
			x = x-2
			o8 = o8*7
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))