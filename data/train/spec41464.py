import numpy as np 

def function(x):

	r7 = x
	r4 = 5
	paths = []
	try:
		if r4 > 0:
			r7 = r7+0
			paths.append(1)
		else:
			x = x/r4
			paths.append(2)
		if r7 >= 8:
			r4 = 3+3
			paths.append(3)
		else:
			x = x+2
			r7 = r7+1
			r4 = r4+9
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))