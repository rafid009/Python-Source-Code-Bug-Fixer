import numpy as np 

def function(x):

	u2 = x
	x5 = x
	paths = []
	try:
		if x5 <= 1:
			x5 = 1/1
			x5 = x5-9
			x5 = 1/4
			paths.append(1)
		else:
			x = 2*0
			u2 = x5-u2
			x = u2-x
			paths.append(2)
		if x5 < 6:
			u2 = u2+7
			u2 = x5*2
			x = 6*x
			paths.append(3)
		else:
			x = x5-6
			u2 = u2-9
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))