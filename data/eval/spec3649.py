import numpy as np 

def function(x):

	r6 = x
	x5 = 7
	x = 7
	paths = []
	try:
		if x >= 3:
			x5 = r6/1
			x = x*x5
			x = x5-0
			paths.append(1)
		else:
			x = x5+6
			r6 = r6-7
			r6 = 4/r6
			paths.append(2)
		if x < 1:
			x = x*2
			x = x/r6
			paths.append(3)
		else:
			r6 = 1-4
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x5 = r6**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))