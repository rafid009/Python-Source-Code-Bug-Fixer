import numpy as np 

def function(x):

	v5 = 5
	q4 = 9
	paths = []
	try:
		if q4 >= 2:
			v5 = 9*2
			x = 3*x
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if x <= 4:
			q4 = 8-x
			q4 = q4+4
			paths.append(3)
		else:
			x = x+0
			v5 = q4+v5
			q4 = v5+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))