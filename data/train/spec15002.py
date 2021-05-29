import numpy as np 

def function(x):

	v2 = x
	q2 = x
	paths = []
	try:
		if x >= 9:
			x = x-2
			v2 = 3-v2
			x = 5+x
			paths.append(1)
		else:
			v2 = v2-x
			paths.append(2)
		if x >= 9:
			q2 = 3*x
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		v2 = q2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))