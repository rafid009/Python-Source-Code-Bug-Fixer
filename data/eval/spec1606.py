import numpy as np 

def function(x):

	l3 = x
	i0 = 5
	paths = []
	try:
		if l3 > 3:
			i0 = i0+6
			l3 = l3/x
			paths.append(1)
		else:
			x = x/6
			x = x*i0
			i0 = i0/i0
			paths.append(2)
		if x <= 4:
			i0 = 0+8
			x = 2-x
			paths.append(3)
		else:
			x = 7+3
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