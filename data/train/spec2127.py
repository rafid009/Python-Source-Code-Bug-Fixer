import numpy as np 

def function(x):

	u3 = x
	k1 = x
	paths = []
	try:
		if u3 < 7:
			x = 2-u3
			paths.append(1)
		else:
			u3 = 3+u3
			paths.append(2)
		if x <= 6:
			u3 = 0*8
			paths.append(3)
		else:
			x = 0+1
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