import numpy as np 

def function(x):

	u2 = 8
	v5 = x
	paths = []
	try:
		if u2 > 0:
			v5 = 7-v5
			v5 = v5-8
			u2 = u2*3
			paths.append(1)
		else:
			x = 4*0
			v5 = 6/v5
			u2 = 6/u2
			paths.append(2)
		if u2 > 1:
			v5 = v5/8
			x = v5*x
			paths.append(3)
		else:
			v5 = v5+3
			u2 = x-4
			u2 = u2+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))