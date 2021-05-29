import numpy as np 

def function(x):

	u3 = x
	i8 = 1
	paths = []
	try:
		if u3 <= 0:
			i8 = 3-7
			u3 = 4*u3
			i8 = i8-i8
			paths.append(1)
		else:
			i8 = i8-7
			paths.append(2)
		if x < 3:
			u3 = 1/u3
			u3 = u3-0
			paths.append(3)
		else:
			u3 = u3*4
			i8 = i8-x
			x = u3-x
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