import numpy as np 

def function(x):

	k6 = x
	e2 = 1
	paths = []
	try:
		if k6 <= 2:
			e2 = e2-k6
			paths.append(1)
		else:
			x = x-k6
			k6 = e2+5
			paths.append(2)
		if e2 < 2:
			k6 = k6/7
			e2 = e2+7
			e2 = 8+e2
			paths.append(3)
		else:
			x = k6+7
			e2 = 9/x
			e2 = 8*3
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		e2 = k6**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))