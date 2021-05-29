import numpy as np 

def function(x):

	e6 = 3
	j4 = x
	x = 4
	paths = []
	try:
		if j4 <= 0:
			x = e6*1
			paths.append(1)
		else:
			x = e6-x
			paths.append(2)
		if x <= 6:
			j4 = j4*7
			e6 = e6-7
			e6 = j4/e6
			paths.append(3)
		else:
			x = x/7
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