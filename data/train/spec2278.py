import numpy as np 

def function(x):

	n2 = 9
	r0 = x
	paths = []
	try:
		if r0 >= 7:
			n2 = n2/n2
			paths.append(1)
		else:
			r0 = r0*4
			paths.append(2)
		if r0 <= 0:
			n2 = n2/4
			paths.append(3)
		else:
			n2 = 9+7
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))