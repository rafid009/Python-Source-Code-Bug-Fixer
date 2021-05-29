import numpy as np 

def function(x):

	f8 = x
	u3 = x
	x = 9
	paths = []
	try:
		if u3 >= 2:
			x = 0-2
			f8 = f8*f8
			paths.append(1)
		else:
			u3 = u3/7
			u3 = x*9
			x = x+x
			paths.append(2)
		if x < 2:
			u3 = 5-9
			paths.append(3)
		else:
			x = 8+x
			u3 = u3+x
			x = f8+f8
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