import numpy as np 

def function(x):

	j7 = x
	d3 = x
	paths = []
	try:
		if d3 <= 9:
			x = x+x
			x = x+9
			paths.append(1)
		else:
			j7 = 3+0
			j7 = d3+5
			x = 7/3
			paths.append(2)
		if j7 > 4:
			d3 = 9-x
			paths.append(3)
		else:
			x = 4-9
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))