import numpy as np 

def function(x):

	j1 = 1
	r3 = x
	paths = []
	try:
		if x <= 5:
			j1 = j1/5
			r3 = 8*2
			j1 = 9+j1
			paths.append(1)
		else:
			j1 = 8/x
			x = j1+6
			x = j1*5
			paths.append(2)
		if x < 5:
			x = 9-x
			r3 = 3/r3
			j1 = j1*r3
			paths.append(3)
		else:
			r3 = 5-8
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