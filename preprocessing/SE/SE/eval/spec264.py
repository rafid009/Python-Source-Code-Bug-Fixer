import numpy as np 

def function(x):

	f9 = x
	u3 = 1
	paths = []
	try:
		if u3 >= 2:
			x = 9+x
			paths.append(1)
		else:
			f9 = 1-f9
			u3 = u3+x
			x = x/u3
			paths.append(2)
		if u3 < 1:
			f9 = f9*f9
			f9 = 0+f9
			paths.append(3)
		else:
			f9 = f9-u3
			x = 1/u3
			x = x/1
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