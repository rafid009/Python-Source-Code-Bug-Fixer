import numpy as np 

def function(x):

	r3 = 6
	v5 = 0
	paths = []
	try:
		if r3 <= 6:
			v5 = v5-0
			paths.append(1)
		else:
			v5 = r3-v5
			v5 = 8-r3
			paths.append(2)
		if v5 > 2:
			r3 = r3*7
			r3 = 8+r3
			paths.append(3)
		else:
			r3 = x-r3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))