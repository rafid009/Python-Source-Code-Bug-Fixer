import numpy as np 

def function(x):

	a4 = x
	k5 = x
	paths = []
	try:
		if k5 > 1:
			a4 = a4+a4
			x = x*6
			k5 = k5-x
			paths.append(1)
		else:
			a4 = 9*0
			k5 = 0+k5
			paths.append(2)
		if a4 > 3:
			k5 = 2+k5
			paths.append(3)
		else:
			k5 = 3-k5
			k5 = 2*k5
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		a4 = k5**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))