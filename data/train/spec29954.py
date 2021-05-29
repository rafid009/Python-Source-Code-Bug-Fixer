import numpy as np 

def function(x):

	r3 = 8
	q7 = 1
	paths = []
	try:
		if x > 3:
			q7 = q7+1
			paths.append(1)
		else:
			x = x/q7
			paths.append(2)
		if r3 >= 5:
			x = x/r3
			q7 = 5+3
			q7 = r3/4
			paths.append(3)
		else:
			x = x+r3
			x = 9+x
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))