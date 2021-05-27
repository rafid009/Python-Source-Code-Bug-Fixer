import numpy as np 

def function(x):

	u8 = x
	r6 = x
	paths = []
	try:
		if r6 > 3:
			r6 = r6-9
			r6 = r6*1
			r6 = r6*r6
			paths.append(1)
		else:
			r6 = r6-r6
			paths.append(2)
		if r6 >= 2:
			x = 7*x
			paths.append(3)
		else:
			r6 = r6*u8
			u8 = 4*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))