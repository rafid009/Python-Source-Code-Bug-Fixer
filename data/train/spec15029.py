import numpy as np 

def function(x):

	r7 = x
	x2 = x
	paths = []
	try:
		if x2 < 9:
			x2 = x2/4
			x2 = 5/x
			x2 = 3-7
			paths.append(1)
		else:
			x2 = x2*x2
			r7 = 7/r7
			x2 = 6/1
			paths.append(2)
		if r7 > 4:
			x2 = 5*x2
			r7 = r7*2
			paths.append(3)
		else:
			x = x/x2
			x = 5*7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x2 = r7**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))