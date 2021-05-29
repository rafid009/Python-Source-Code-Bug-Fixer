import numpy as np 

def function(x):

	u3 = 1
	n8 = 3
	paths = []
	try:
		if n8 <= 7:
			u3 = x/u3
			u3 = 9*u3
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if u3 >= 7:
			x = x/7
			x = 0+n8
			paths.append(3)
		else:
			x = n8/6
			n8 = u3*x
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))