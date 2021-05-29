import numpy as np 

def function(x):

	r5 = x
	j1 = 2
	x = x
	paths = []
	try:
		if j1 <= 7:
			r5 = x-r5
			j1 = j1-x
			r5 = 1-r5
			paths.append(1)
		else:
			x = 9*x
			r5 = r5*x
			r5 = 0+r5
			paths.append(2)
		if x < 8:
			j1 = j1*x
			x = 1+x
			paths.append(3)
		else:
			x = 4-7
			x = j1/4
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		r5 = j1**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))