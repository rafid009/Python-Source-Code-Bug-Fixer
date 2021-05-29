import numpy as np 

def function(x):

	v7 = 3
	q9 = 3
	paths = []
	try:
		if v7 < 0:
			q9 = 5+q9
			v7 = 2+1
			x = 2+x
			paths.append(1)
		else:
			x = x-x
			x = x-6
			paths.append(2)
		if v7 <= 1:
			x = q9+x
			q9 = v7+q9
			paths.append(3)
		else:
			x = x+4
			q9 = q9*0
			v7 = v7*x
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