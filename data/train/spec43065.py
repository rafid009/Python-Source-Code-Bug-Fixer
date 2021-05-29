import numpy as np 

def function(x):

	j0 = 6
	r5 = x
	paths = []
	try:
		if r5 >= 1:
			r5 = r5+5
			x = x*6
			paths.append(1)
		else:
			j0 = 8-0
			j0 = r5+8
			paths.append(2)
		if j0 <= 4:
			x = 9/j0
			paths.append(3)
		else:
			x = x*7
			x = r5/4
			j0 = x+x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))