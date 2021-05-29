import numpy as np 

def function(x):

	u3 = 5
	r7 = x
	paths = []
	try:
		if x > 0:
			u3 = u3*6
			paths.append(1)
		else:
			u3 = r7-u3
			r7 = r7/u3
			r7 = r7/3
			paths.append(2)
		if u3 <= 2:
			x = 9/x
			paths.append(3)
		else:
			x = x/x
			r7 = 3/x
			u3 = 7-u3
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