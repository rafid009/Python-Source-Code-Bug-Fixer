import numpy as np 

def function(x):

	x3 = x
	u3 = 5
	paths = []
	try:
		if x >= 0:
			x = 8-6
			paths.append(1)
		else:
			x = x+x
			u3 = 7*9
			x3 = 2+x3
			paths.append(2)
		if u3 >= 7:
			x = 0*x
			x3 = x3+8
			u3 = x*5
			paths.append(3)
		else:
			x3 = x3*x3
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		u3 = x3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))