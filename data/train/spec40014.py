import numpy as np 

def function(x):

	r7 = x
	o1 = 3
	paths = []
	try:
		if r7 > 8:
			r7 = o1-r7
			paths.append(1)
		else:
			o1 = r7-1
			o1 = 7/o1
			paths.append(2)
		if r7 < 2:
			o1 = o1*r7
			paths.append(3)
		else:
			x = x*3
			r7 = 2/r7
			o1 = o1*2
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