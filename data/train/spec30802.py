import numpy as np 

def function(x):

	r3 = x
	r1 = x
	paths = []
	try:
		if r1 >= 2:
			x = x/7
			paths.append(1)
		else:
			x = x*x
			x = x/6
			paths.append(2)
		if r3 >= 2:
			r1 = 8-6
			paths.append(3)
		else:
			r3 = x+5
			x = x/r3
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))