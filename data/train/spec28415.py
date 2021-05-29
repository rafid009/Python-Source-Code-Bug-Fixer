import numpy as np 

def function(x):

	i2 = x
	r7 = 8
	paths = []
	try:
		if x > 1:
			x = r7+x
			x = x-8
			paths.append(1)
		else:
			x = i2/r7
			paths.append(2)
		if i2 >= 5:
			r7 = 5+x
			r7 = 1-i2
			paths.append(3)
		else:
			r7 = r7/2
			r7 = 9+r7
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