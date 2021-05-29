import numpy as np 

def function(x):

	u3 = x
	v0 = 6
	paths = []
	try:
		if u3 < 0:
			u3 = 9/7
			v0 = v0+v0
			paths.append(1)
		else:
			v0 = v0+x
			paths.append(2)
		if u3 <= 9:
			u3 = u3*x
			paths.append(3)
		else:
			v0 = v0/2
			x = u3*x
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