import numpy as np 

def function(x):

	k0 = x
	q6 = 0
	paths = []
	try:
		if k0 >= 1:
			q6 = q6+9
			x = k0*k0
			paths.append(1)
		else:
			x = x*7
			k0 = q6/9
			k0 = 3/x
			paths.append(2)
		if x <= 4:
			q6 = q6-1
			q6 = 3-x
			paths.append(3)
		else:
			q6 = q6*2
			k0 = k0-5
			q6 = 9-x
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))