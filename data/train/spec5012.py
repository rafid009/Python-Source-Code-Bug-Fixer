import numpy as np 

def function(x):

	k9 = x
	q4 = 3
	paths = []
	try:
		if q4 > 5:
			q4 = 8+q4
			paths.append(1)
		else:
			k9 = 3+6
			x = 8-x
			x = 7/x
			paths.append(2)
		if q4 < 9:
			q4 = q4+4
			paths.append(3)
		else:
			x = 2-0
			k9 = x*k9
			k9 = q4/k9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))