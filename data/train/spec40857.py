import numpy as np 

def function(x):

	e1 = 8
	r8 = x
	paths = []
	try:
		if x <= 7:
			e1 = 3-e1
			paths.append(1)
		else:
			x = 1/e1
			r8 = r8*0
			paths.append(2)
		if r8 > 1:
			x = 4-r8
			paths.append(3)
		else:
			e1 = 8*e1
			r8 = 8+5
			r8 = x*e1
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