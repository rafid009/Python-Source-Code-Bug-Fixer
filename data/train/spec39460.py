import numpy as np 

def function(x):

	r6 = x
	l8 = x
	paths = []
	try:
		if l8 > 2:
			r6 = 8-4
			paths.append(1)
		else:
			l8 = l8+6
			l8 = l8*3
			x = 4+x
			paths.append(2)
		if x >= 6:
			r6 = 9+8
			l8 = l8*0
			l8 = 8*3
			paths.append(3)
		else:
			l8 = 1/1
			l8 = 3+l8
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		r6 = r6**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))