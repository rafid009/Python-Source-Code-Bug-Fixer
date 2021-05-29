import numpy as np 

def function(x):

	r6 = x
	n2 = x
	paths = []
	try:
		if x >= 4:
			r6 = 8-6
			n2 = n2-n2
			paths.append(1)
		else:
			r6 = r6+8
			x = 1-x
			paths.append(2)
		if r6 <= 0:
			x = x/8
			x = 4-3
			paths.append(3)
		else:
			x = x-r6
			r6 = r6/5
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