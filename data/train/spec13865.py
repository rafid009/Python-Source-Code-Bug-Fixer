import numpy as np 

def function(x):

	a2 = x
	r6 = x
	paths = []
	try:
		if r6 < 0:
			a2 = a2/x
			paths.append(1)
		else:
			a2 = x/8
			paths.append(2)
		if r6 >= 4:
			a2 = 6+a2
			paths.append(3)
		else:
			a2 = a2*8
			r6 = 2-r6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		a2 = r6**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))