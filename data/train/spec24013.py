import numpy as np 

def function(x):

	j0 = 5
	u3 = x
	paths = []
	try:
		if x < 5:
			j0 = j0-5
			paths.append(1)
		else:
			x = x+6
			paths.append(2)
		if u3 > 2:
			u3 = u3+4
			x = u3*x
			paths.append(3)
		else:
			x = 0/9
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