import numpy as np 

def function(x):

	r5 = x
	b8 = 0
	paths = []
	try:
		if x < 3:
			r5 = 6*x
			paths.append(1)
		else:
			r5 = 6/r5
			b8 = x-r5
			b8 = b8/b8
			paths.append(2)
		if r5 >= 4:
			r5 = x+r5
			x = x/r5
			paths.append(3)
		else:
			b8 = r5-x
			b8 = x*2
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))