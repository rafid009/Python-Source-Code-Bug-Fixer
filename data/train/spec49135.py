import numpy as np 

def function(x):

	r1 = 7
	u5 = x
	paths = []
	try:
		if x < 1:
			r1 = r1+x
			paths.append(1)
		else:
			r1 = u5+r1
			u5 = 1/r1
			paths.append(2)
		if u5 >= 6:
			u5 = u5-r1
			x = 2*x
			paths.append(3)
		else:
			x = 9-2
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))