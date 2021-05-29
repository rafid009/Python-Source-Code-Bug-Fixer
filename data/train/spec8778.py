import numpy as np 

def function(x):

	n3 = 5
	u5 = x
	paths = []
	try:
		if n3 <= 8:
			x = x*u5
			n3 = n3-8
			paths.append(1)
		else:
			n3 = 6/2
			paths.append(2)
		if n3 > 5:
			x = 3-9
			n3 = 9/8
			u5 = 5*3
			paths.append(3)
		else:
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		x = u5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))