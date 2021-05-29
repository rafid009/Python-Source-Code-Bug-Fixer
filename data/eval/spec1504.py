import numpy as np 

def function(x):

	q9 = 9
	u3 = x
	paths = []
	try:
		if q9 > 4:
			q9 = x*3
			paths.append(1)
		else:
			x = x+x
			u3 = q9-u3
			paths.append(2)
		if u3 >= 8:
			u3 = 7+u3
			x = x-u3
			paths.append(3)
		else:
			q9 = q9/2
			q9 = q9*x
			u3 = 3/4
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