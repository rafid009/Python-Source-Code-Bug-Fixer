import numpy as np 

def function(x):

	w5 = x
	i7 = x
	paths = []
	try:
		if w5 > 4:
			x = 2+x
			x = x-9
			paths.append(1)
		else:
			i7 = 2/i7
			paths.append(2)
		if x >= 2:
			i7 = 0/i7
			x = x+i7
			paths.append(3)
		else:
			x = x*6
			x = w5/7
			w5 = 7/w5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))