import numpy as np 

def function(x):

	a3 = 1
	k6 = 9
	paths = []
	try:
		if x <= 0:
			k6 = k6-5
			a3 = a3*a3
			paths.append(1)
		else:
			x = 7-x
			a3 = 8*a3
			paths.append(2)
		if x >= 2:
			a3 = 2-8
			a3 = a3*1
			k6 = k6-k6
			paths.append(3)
		else:
			x = x*3
			x = x/a3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		k6 = a3**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))