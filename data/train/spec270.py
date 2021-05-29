import numpy as np 

def function(x):

	r0 = 9
	i8 = x
	paths = []
	try:
		if x < 7:
			r0 = r0/4
			r0 = 9*2
			r0 = 2-r0
			paths.append(1)
		else:
			x = 7/3
			i8 = i8*2
			x = x*5
			paths.append(2)
		if r0 <= 8:
			x = 2/x
			paths.append(3)
		else:
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))