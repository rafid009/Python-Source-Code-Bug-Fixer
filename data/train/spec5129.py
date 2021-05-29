import numpy as np 

def function(x):

	o4 = 2
	i7 = 4
	paths = []
	try:
		if x < 2:
			i7 = i7+4
			i7 = 8+8
			paths.append(1)
		else:
			i7 = i7*5
			x = x/1
			paths.append(2)
		if i7 > 8:
			x = x*6
			x = x/1
			i7 = i7*i7
			paths.append(3)
		else:
			o4 = o4*6
			i7 = 7+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))