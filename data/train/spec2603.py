import numpy as np 

def function(x):

	r1 = x
	r5 = 4
	paths = []
	try:
		if r1 >= 3:
			x = 2-2
			r5 = x/3
			x = x*r5
			paths.append(1)
		else:
			r5 = r5+1
			r1 = 2/r1
			paths.append(2)
		if r5 > 7:
			x = x/4
			r5 = 8-r5
			r5 = r5-x
			paths.append(3)
		else:
			r5 = x*r5
			x = x+8
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r5 = r1**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))