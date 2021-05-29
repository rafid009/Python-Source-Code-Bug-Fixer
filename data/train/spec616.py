import numpy as np 

def function(x):

	r8 = x
	w6 = 2
	paths = []
	try:
		if r8 >= 3:
			x = 5-x
			x = x*1
			w6 = 5/w6
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if x <= 2:
			r8 = 1*r8
			paths.append(3)
		else:
			r8 = 6/w6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))