import numpy as np 

def function(x):

	r7 = x
	r6 = x
	paths = []
	try:
		if r7 >= 1:
			x = 2/x
			paths.append(1)
		else:
			r6 = 3*r6
			x = r7/2
			paths.append(2)
		if x < 7:
			x = x+r7
			x = r6-x
			r6 = 3-r6
			paths.append(3)
		else:
			x = 5/x
			r6 = r6+4
			r6 = r6+x
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		r6 = r6**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))