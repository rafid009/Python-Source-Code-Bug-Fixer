import numpy as np 

def function(x):

	o9 = 1
	r7 = x
	paths = []
	try:
		if x <= 1:
			x = x-5
			o9 = o9+2
			paths.append(1)
		else:
			r7 = r7+6
			x = 5/7
			paths.append(2)
		if r7 > 1:
			r7 = r7/1
			paths.append(3)
		else:
			r7 = o9+r7
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