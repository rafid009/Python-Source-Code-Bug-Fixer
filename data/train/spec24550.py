import numpy as np 

def function(x):

	q5 = x
	k2 = 0
	paths = []
	try:
		if q5 > 0:
			q5 = q5*7
			paths.append(1)
		else:
			k2 = k2-k2
			paths.append(2)
		if k2 > 3:
			q5 = 5+q5
			k2 = 6+4
			paths.append(3)
		else:
			k2 = k2/4
			q5 = q5+2
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))