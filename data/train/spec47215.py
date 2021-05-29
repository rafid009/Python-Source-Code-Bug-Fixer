import numpy as np 

def function(x):

	u7 = x
	j0 = x
	paths = []
	try:
		if j0 < 2:
			u7 = x+x
			j0 = j0-j0
			paths.append(1)
		else:
			x = x*x
			x = x/u7
			paths.append(2)
		if j0 < 8:
			j0 = j0*2
			j0 = 0*j0
			paths.append(3)
		else:
			j0 = j0/1
			u7 = u7*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))