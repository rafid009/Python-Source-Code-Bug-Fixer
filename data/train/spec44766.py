import numpy as np 

def function(x):

	b3 = 7
	u3 = x
	paths = []
	try:
		if u3 >= 0:
			x = 4+x
			paths.append(1)
		else:
			u3 = 1-9
			b3 = b3+u3
			paths.append(2)
		if u3 >= 2:
			b3 = x+0
			paths.append(3)
		else:
			x = 8+x
			u3 = x/u3
			u3 = 6-7
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))