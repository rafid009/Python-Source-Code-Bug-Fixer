import numpy as np 

def function(x):

	p7 = x
	i0 = 9
	paths = []
	try:
		if i0 >= 2:
			i0 = i0+0
			paths.append(1)
		else:
			i0 = 6-i0
			x = 0*i0
			paths.append(2)
		if i0 <= 1:
			x = 1/1
			i0 = 4-i0
			paths.append(3)
		else:
			p7 = p7/i0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))