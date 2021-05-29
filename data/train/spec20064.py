import numpy as np 

def function(x):

	u3 = x
	u1 = 8
	paths = []
	try:
		if x >= 1:
			x = x+1
			u3 = x-u3
			u3 = u3-5
			paths.append(1)
		else:
			x = u3*7
			u3 = u3/u3
			paths.append(2)
		if u1 >= 6:
			u1 = u1*5
			paths.append(3)
		else:
			u1 = 4+u3
			u3 = u3/u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))