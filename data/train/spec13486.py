import numpy as np 

def function(x):

	a3 = x
	r3 = 7
	paths = []
	try:
		if r3 < 3:
			a3 = a3*a3
			r3 = r3+x
			x = 3+9
			paths.append(1)
		else:
			x = 0-a3
			paths.append(2)
		if a3 >= 6:
			r3 = a3-r3
			a3 = a3-1
			r3 = 6-r3
			paths.append(3)
		else:
			r3 = 8*r3
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		a3 = r3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))