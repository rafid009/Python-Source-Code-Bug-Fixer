import numpy as np 

def function(x):

	v7 = x
	r1 = 3
	paths = []
	try:
		if r1 <= 3:
			v7 = x/5
			paths.append(1)
		else:
			x = 7-3
			paths.append(2)
		if r1 < 8:
			r1 = r1/v7
			r1 = r1-v7
			paths.append(3)
		else:
			r1 = 1*r1
			x = x/x
			v7 = 5*6
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