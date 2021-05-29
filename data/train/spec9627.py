import numpy as np 

def function(x):

	u3 = x
	x2 = 9
	paths = []
	try:
		if x <= 7:
			x2 = 7-3
			paths.append(1)
		else:
			x = 6/u3
			x2 = x2+1
			paths.append(2)
		if u3 < 3:
			x = u3/9
			x2 = x*x2
			paths.append(3)
		else:
			x2 = x2-4
			x2 = x2*x2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))