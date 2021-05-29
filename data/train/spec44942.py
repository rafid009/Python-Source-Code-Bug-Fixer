import numpy as np 

def function(x):

	e6 = x
	u3 = x
	paths = []
	try:
		if u3 < 9:
			x = x/8
			x = x*1
			e6 = x/e6
			paths.append(1)
		else:
			u3 = 3+u3
			paths.append(2)
		if u3 >= 9:
			x = 4*x
			u3 = 7+x
			u3 = u3+e6
			paths.append(3)
		else:
			e6 = e6-u3
			x = x*e6
			x = u3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))