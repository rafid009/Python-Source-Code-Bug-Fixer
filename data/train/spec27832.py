import numpy as np 

def function(x):

	k4 = x
	e2 = x
	paths = []
	try:
		if k4 > 4:
			k4 = k4-k4
			paths.append(1)
		else:
			e2 = k4+e2
			k4 = e2/k4
			paths.append(2)
		if e2 <= 8:
			x = 8/5
			k4 = k4+9
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		k4 = e2**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))