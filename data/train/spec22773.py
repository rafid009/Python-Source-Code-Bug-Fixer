import numpy as np 

def function(x):

	v8 = 8
	p7 = 4
	paths = []
	try:
		if p7 < 2:
			p7 = p7*p7
			paths.append(1)
		else:
			x = 2/x
			paths.append(2)
		if x <= 1:
			p7 = v8/6
			v8 = 5*v8
			x = x/3
			paths.append(3)
		else:
			x = v8-9
			x = v8-9
			v8 = 3/v8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))