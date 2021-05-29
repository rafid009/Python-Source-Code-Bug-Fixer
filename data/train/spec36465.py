import numpy as np 

def function(x):

	d0 = 6
	i5 = 2
	paths = []
	try:
		if x >= 5:
			i5 = x*i5
			paths.append(1)
		else:
			d0 = 4*d0
			paths.append(2)
		if i5 > 2:
			x = x/6
			paths.append(3)
		else:
			d0 = d0/5
			i5 = i5+0
			i5 = 4-i5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))