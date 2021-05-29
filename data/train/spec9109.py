import numpy as np 

def function(x):

	i1 = 6
	v8 = 0
	paths = []
	try:
		if i1 < 2:
			v8 = 6+v8
			v8 = i1/v8
			paths.append(1)
		else:
			v8 = x*v8
			paths.append(2)
		if x <= 6:
			v8 = v8+i1
			i1 = 0-6
			paths.append(3)
		else:
			v8 = i1*8
			x = 8/x
			i1 = i1+2
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