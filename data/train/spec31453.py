import numpy as np 

def function(x):

	j1 = x
	r3 = 7
	paths = []
	try:
		if r3 > 6:
			j1 = 5+j1
			j1 = r3+j1
			r3 = r3*x
			paths.append(1)
		else:
			j1 = 8/j1
			x = 0+x
			paths.append(2)
		if j1 > 9:
			j1 = 7/7
			paths.append(3)
		else:
			x = x/1
			x = x/7
			x = x*4
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))