import numpy as np 

def function(x):

	b8 = 2
	u3 = 3
	paths = []
	try:
		if b8 <= 0:
			b8 = 9-3
			paths.append(1)
		else:
			u3 = u3*3
			paths.append(2)
		if u3 >= 0:
			x = 1-x
			u3 = u3-1
			u3 = 0-u3
			paths.append(3)
		else:
			b8 = 9+x
			u3 = u3*3
			b8 = x/b8
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