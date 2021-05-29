import numpy as np 

def function(x):

	r6 = 6
	r1 = x
	x = 0
	paths = []
	try:
		if x < 6:
			x = x+1
			paths.append(1)
		else:
			r6 = 6*r6
			r1 = 1+r1
			r1 = 2/r1
			paths.append(2)
		if x <= 4:
			r6 = r6*9
			x = 8/r1
			x = x/r1
			paths.append(3)
		else:
			x = x/6
			x = x/x
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