import numpy as np 

def function(x):

	j5 = 3
	d7 = 7
	paths = []
	try:
		if j5 < 5:
			x = x/6
			d7 = d7-5
			paths.append(1)
		else:
			x = 6/x
			j5 = 4+j5
			paths.append(2)
		if j5 >= 5:
			d7 = d7+6
			paths.append(3)
		else:
			j5 = j5-4
			x = x*j5
			d7 = d7*j5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		d7 = j5**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))