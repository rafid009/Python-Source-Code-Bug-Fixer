import numpy as np 

def function(x):

	u3 = x
	d5 = 6
	paths = []
	try:
		if x >= 3:
			x = x+u3
			u3 = u3*d5
			paths.append(1)
		else:
			x = x-7
			d5 = x-d5
			d5 = d5*9
			paths.append(2)
		if d5 < 4:
			x = u3/x
			paths.append(3)
		else:
			u3 = u3*8
			d5 = 7/u3
			u3 = x+x
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