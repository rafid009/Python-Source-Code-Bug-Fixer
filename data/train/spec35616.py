import numpy as np 

def function(x):

	u3 = x
	i4 = x
	x = 2
	paths = []
	try:
		if i4 <= 9:
			u3 = u3/5
			paths.append(1)
		else:
			x = x/6
			i4 = u3/i4
			x = 1*x
			paths.append(2)
		if i4 <= 0:
			u3 = u3-9
			paths.append(3)
		else:
			u3 = i4-u3
			x = x-0
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