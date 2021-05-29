import numpy as np 

def function(x):

	n7 = 5
	u3 = 5
	paths = []
	try:
		if u3 >= 8:
			n7 = 2+n7
			u3 = u3/5
			paths.append(1)
		else:
			u3 = 2/u3
			paths.append(2)
		if x >= 2:
			n7 = n7/u3
			u3 = x/1
			paths.append(3)
		else:
			n7 = n7*n7
			n7 = 5*n7
			x = 0-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))