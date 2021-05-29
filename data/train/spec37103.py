import numpy as np 

def function(x):

	n6 = x
	r5 = x
	paths = []
	try:
		if x > 0:
			n6 = n6-0
			n6 = n6+1
			x = 4/1
			paths.append(1)
		else:
			r5 = 3+r5
			paths.append(2)
		if r5 <= 5:
			n6 = 6/r5
			r5 = 9*n6
			n6 = 4+8
			paths.append(3)
		else:
			n6 = n6/8
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