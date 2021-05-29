import numpy as np 

def function(x):

	u3 = x
	n2 = 6
	paths = []
	try:
		if x >= 8:
			x = x/x
			paths.append(1)
		else:
			x = 6/x
			n2 = n2*2
			u3 = u3/x
			paths.append(2)
		if x <= 2:
			u3 = u3+u3
			u3 = u3-u3
			u3 = 4*6
			paths.append(3)
		else:
			n2 = n2-5
			x = x*n2
			u3 = u3/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))