import numpy as np 

def function(x):

	f5 = 3
	u3 = x
	paths = []
	try:
		if u3 >= 6:
			x = x+6
			paths.append(1)
		else:
			u3 = x+5
			x = f5/x
			x = x/2
			paths.append(2)
		if u3 < 4:
			u3 = 9+u3
			u3 = u3*x
			paths.append(3)
		else:
			f5 = f5/6
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