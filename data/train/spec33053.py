import numpy as np 

def function(x):

	e5 = x
	v3 = 7
	paths = []
	try:
		if x < 7:
			e5 = e5/9
			paths.append(1)
		else:
			x = 5*e5
			paths.append(2)
		if v3 > 9:
			e5 = 9/e5
			e5 = 2/v3
			x = x-1
			paths.append(3)
		else:
			e5 = e5*v3
			e5 = x*8
			v3 = v3/1
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))