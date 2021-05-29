import numpy as np 

def function(x):

	u3 = x
	paths = []
	try:
		if u3 < 0:
			u3 = 2/4
			u3 = u3*8
			u3 = u3-1
			paths.append(1)
		else:
			u3 = u3+5
			paths.append(2)
		if u3 < 3:
			u3 = 0/u3
			paths.append(3)
		else:
			x = x/8
			u3 = 9-u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))