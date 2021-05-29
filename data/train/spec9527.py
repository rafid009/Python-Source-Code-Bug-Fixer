import numpy as np 

def function(x):

	e5 = 2
	r6 = x
	paths = []
	try:
		if r6 < 9:
			r6 = 1*r6
			e5 = x+3
			x = 3*e5
			paths.append(1)
		else:
			x = e5*x
			r6 = r6*5
			r6 = x-5
			paths.append(2)
		if e5 < 1:
			r6 = 8*9
			paths.append(3)
		else:
			r6 = 7+9
			e5 = e5+9
			r6 = x/2
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))