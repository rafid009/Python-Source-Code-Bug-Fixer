import numpy as np 

def function(x):

	l6 = 7
	k1 = x
	paths = []
	try:
		if x > 9:
			x = 7+9
			paths.append(1)
		else:
			x = l6-7
			paths.append(2)
		if k1 >= 7:
			k1 = k1/5
			paths.append(3)
		else:
			k1 = 7/k1
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		l6 = k1**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))