import numpy as np 

def function(x):

	t9 = x
	u3 = 3
	x = 2
	paths = []
	try:
		if x >= 5:
			u3 = u3-1
			paths.append(1)
		else:
			x = x/u3
			paths.append(2)
		if x < 9:
			u3 = u3+6
			u3 = u3+1
			paths.append(3)
		else:
			u3 = x-u3
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		u3 = t9**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))