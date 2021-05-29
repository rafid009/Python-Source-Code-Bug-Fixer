import numpy as np 

def function(x):

	r2 = x
	j1 = 2
	paths = []
	try:
		if r2 >= 5:
			j1 = x/j1
			paths.append(1)
		else:
			x = 8/r2
			x = x-6
			j1 = j1+7
			paths.append(2)
		if r2 <= 4:
			r2 = r2*0
			x = x+3
			paths.append(3)
		else:
			j1 = 6/2
			j1 = 8+3
			j1 = j1-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))