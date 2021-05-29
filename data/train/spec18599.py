import numpy as np 

def function(x):

	j9 = x
	d9 = x
	paths = []
	try:
		if d9 >= 5:
			x = 1/3
			j9 = 9-j9
			x = x/8
			paths.append(1)
		else:
			x = 0-x
			d9 = x-d9
			paths.append(2)
		if d9 <= 3:
			x = 8+d9
			j9 = 4*j9
			x = x*5
			paths.append(3)
		else:
			x = 9*7
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))