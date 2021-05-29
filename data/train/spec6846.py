import numpy as np 

def function(x):

	j7 = x
	d8 = x
	x = 1
	paths = []
	try:
		if x < 7:
			j7 = x*x
			paths.append(1)
		else:
			d8 = 3-j7
			paths.append(2)
		if x >= 1:
			j7 = j7+2
			paths.append(3)
		else:
			j7 = d8+j7
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		j7 = d8**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))