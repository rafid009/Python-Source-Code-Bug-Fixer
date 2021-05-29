import numpy as np 

def function(x):

	a3 = 1
	r7 = x
	x = 4
	paths = []
	try:
		if x < 0:
			x = x/a3
			x = x/7
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if x <= 3:
			x = a3-x
			r7 = 0/8
			paths.append(3)
		else:
			a3 = 9-7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		r7 = r7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))