import numpy as np 

def function(x):

	l5 = x
	i4 = x
	x = 1
	paths = []
	try:
		if i4 <= 3:
			x = i4*x
			l5 = 7-l5
			i4 = 8+i4
			paths.append(1)
		else:
			x = 4+1
			paths.append(2)
		if i4 < 3:
			x = x*i4
			x = x*x
			paths.append(3)
		else:
			i4 = i4/i4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))