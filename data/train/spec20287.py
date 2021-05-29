import numpy as np 

def function(x):

	q2 = x
	k7 = 4
	paths = []
	try:
		if q2 < 7:
			q2 = q2*k7
			paths.append(1)
		else:
			k7 = k7+q2
			paths.append(2)
		if x < 9:
			k7 = k7+3
			k7 = 9*8
			paths.append(3)
		else:
			x = x/5
			x = x/k7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))