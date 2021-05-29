import numpy as np 

def function(x):

	r5 = 6
	v1 = 5
	paths = []
	try:
		if x < 1:
			v1 = v1*4
			paths.append(1)
		else:
			r5 = 9+r5
			r5 = v1*2
			paths.append(2)
		if v1 > 4:
			v1 = v1-9
			v1 = v1+3
			x = r5*x
			paths.append(3)
		else:
			r5 = 5/6
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