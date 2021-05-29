import numpy as np 

def function(x):

	r5 = x
	g5 = 1
	paths = []
	try:
		if r5 >= 5:
			x = r5-8
			x = 1-7
			paths.append(1)
		else:
			r5 = r5/5
			x = g5/3
			x = r5-x
			paths.append(2)
		if r5 >= 9:
			r5 = 2-r5
			r5 = 7/9
			paths.append(3)
		else:
			x = x/g5
			r5 = 2+r5
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