import numpy as np 

def function(x):

	v8 = 6
	o0 = x
	paths = []
	try:
		if x <= 2:
			o0 = 8-v8
			x = x*6
			o0 = 5+x
			paths.append(1)
		else:
			v8 = v8+9
			o0 = o0*o0
			x = 0*7
			paths.append(2)
		if v8 > 0:
			v8 = 6+v8
			v8 = 0-v8
			x = x+x
			paths.append(3)
		else:
			v8 = 7*v8
			x = x-x
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