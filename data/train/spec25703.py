import numpy as np 

def function(x):

	u3 = x
	e5 = 3
	paths = []
	try:
		if u3 > 9:
			x = 2+x
			paths.append(1)
		else:
			u3 = 3/6
			u3 = u3-u3
			e5 = e5-6
			paths.append(2)
		if e5 < 1:
			x = u3*7
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))