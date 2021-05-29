import numpy as np 

def function(x):

	r5 = 6
	e7 = x
	paths = []
	try:
		if r5 >= 5:
			r5 = 1*x
			x = e7/9
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if e7 <= 6:
			r5 = 5+r5
			r5 = 7-r5
			r5 = r5*8
			paths.append(3)
		else:
			e7 = e7+4
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		x = r5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))