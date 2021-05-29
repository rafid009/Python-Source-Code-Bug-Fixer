import numpy as np 

def function(x):

	e6 = x
	j4 = x
	paths = []
	try:
		if j4 <= 6:
			j4 = j4*x
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if j4 < 5:
			x = 8-2
			paths.append(3)
		else:
			x = 1/x
			e6 = e6*2
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))