import numpy as np 

def function(x):

	i7 = 5
	d9 = x
	paths = []
	try:
		if i7 <= 8:
			x = x-1
			paths.append(1)
		else:
			i7 = 5/i7
			d9 = 7*d9
			paths.append(2)
		if x <= 3:
			x = x/1
			x = 6+x
			i7 = d9+3
			paths.append(3)
		else:
			i7 = 0+d9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))