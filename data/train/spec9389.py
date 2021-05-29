import numpy as np 

def function(x):

	r9 = x
	i3 = 0
	paths = []
	try:
		if i3 <= 0:
			x = x+4
			x = 9*4
			paths.append(1)
		else:
			r9 = r9*8
			paths.append(2)
		if x <= 2:
			r9 = 8/6
			r9 = r9-i3
			x = r9+6
			paths.append(3)
		else:
			x = i3-x
			x = 3*x
			r9 = 4*r9
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))