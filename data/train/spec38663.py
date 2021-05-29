import numpy as np 

def function(x):

	j3 = x
	d5 = x
	paths = []
	try:
		if j3 < 5:
			x = x*6
			paths.append(1)
		else:
			x = x/4
			x = x*4
			j3 = j3/j3
			paths.append(2)
		if d5 > 3:
			d5 = x+j3
			j3 = x/7
			d5 = 9-d5
			paths.append(3)
		else:
			j3 = j3-2
			d5 = x/x
			d5 = d5+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))