import numpy as np 

def function(x):

	r1 = x
	r6 = 9
	x = x
	paths = []
	try:
		if r6 <= 5:
			r6 = r1+r1
			paths.append(1)
		else:
			r1 = 0-1
			paths.append(2)
		if r6 > 1:
			r1 = 3-7
			r1 = 9*r1
			paths.append(3)
		else:
			x = x-r1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))