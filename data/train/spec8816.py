import numpy as np 

def function(x):

	r1 = x
	r6 = x
	paths = []
	try:
		if r6 < 2:
			r6 = 6/r6
			x = x+4
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if x > 9:
			x = 9/6
			x = 4*r1
			paths.append(3)
		else:
			r6 = x/9
			r6 = r6/2
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))