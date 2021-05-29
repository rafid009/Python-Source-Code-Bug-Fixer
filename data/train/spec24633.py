import numpy as np 

def function(x):

	l3 = 1
	i7 = x
	paths = []
	try:
		if i7 <= 8:
			x = x-0
			paths.append(1)
		else:
			x = x+i7
			l3 = l3/8
			i7 = 1/i7
			paths.append(2)
		if i7 > 6:
			i7 = 5/i7
			x = x/l3
			l3 = l3/9
			paths.append(3)
		else:
			l3 = l3*1
			l3 = l3*6
			x = 8/x
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