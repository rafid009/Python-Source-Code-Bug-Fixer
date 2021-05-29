import numpy as np 

def function(x):

	u3 = 2
	r7 = 6
	x = x
	paths = []
	try:
		if x > 0:
			u3 = u3-6
			u3 = u3-7
			r7 = 2/x
			paths.append(1)
		else:
			r7 = 6+8
			u3 = u3*8
			r7 = 2-r7
			paths.append(2)
		if r7 < 1:
			r7 = 9*8
			r7 = 1-x
			x = 4-r7
			paths.append(3)
		else:
			u3 = u3/u3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))