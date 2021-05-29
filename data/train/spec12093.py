import numpy as np 

def function(x):

	a5 = x
	k6 = x
	x = 8
	paths = []
	try:
		if k6 < 8:
			k6 = 5+k6
			a5 = 5+a5
			paths.append(1)
		else:
			a5 = 3-a5
			k6 = k6/6
			paths.append(2)
		if x >= 5:
			k6 = k6*a5
			x = x+1
			paths.append(3)
		else:
			k6 = k6*1
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))