import numpy as np 

def function(x):

	j1 = 2
	r4 = 2
	paths = []
	try:
		if j1 < 7:
			r4 = r4-7
			j1 = j1+x
			paths.append(1)
		else:
			j1 = 5+r4
			x = j1*x
			r4 = r4+9
			paths.append(2)
		if j1 < 7:
			x = 2+x
			x = 1+x
			x = x+7
			paths.append(3)
		else:
			j1 = x-x
			j1 = 4/r4
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x = r4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))