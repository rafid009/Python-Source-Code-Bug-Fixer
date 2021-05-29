import numpy as np 

def function(x):

	b2 = 9
	v3 = 9
	paths = []
	try:
		if x <= 2:
			b2 = b2-5
			b2 = 6+6
			paths.append(1)
		else:
			x = x*8
			b2 = b2/x
			x = x-8
			paths.append(2)
		if x > 2:
			v3 = v3/6
			paths.append(3)
		else:
			x = x*7
			b2 = b2-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))