import numpy as np 

def function(x):

	u3 = x
	x8 = x
	paths = []
	try:
		if x > 5:
			u3 = 6/u3
			x = x+x8
			u3 = 6/u3
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if u3 <= 8:
			u3 = 6-u3
			u3 = u3+u3
			paths.append(3)
		else:
			x = 2*9
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