import numpy as np 

def function(x):

	n9 = x
	r7 = x
	x = 8
	paths = []
	try:
		if x > 2:
			r7 = 9+r7
			paths.append(1)
		else:
			n9 = n9+5
			paths.append(2)
		if r7 > 4:
			x = 1+x
			n9 = n9-x
			r7 = n9-r7
			paths.append(3)
		else:
			x = 4*9
			r7 = 5+2
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