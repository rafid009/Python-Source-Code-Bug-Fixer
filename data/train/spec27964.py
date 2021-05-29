import numpy as np 

def function(x):

	k6 = x
	a7 = x
	paths = []
	try:
		if x <= 4:
			x = k6+6
			x = 7/x
			paths.append(1)
		else:
			x = a7-2
			a7 = a7/k6
			k6 = 9+k6
			paths.append(2)
		if k6 <= 3:
			k6 = 8*6
			paths.append(3)
		else:
			k6 = 5+3
			k6 = x*k6
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))