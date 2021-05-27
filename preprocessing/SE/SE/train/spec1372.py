import numpy as np 

def function(x):

	d6 = 6
	i9 = 9
	paths = []
	try:
		if d6 < 5:
			x = 5-i9
			x = x-8
			d6 = d6-3
			paths.append(1)
		else:
			i9 = 1-x
			x = x+9
			paths.append(2)
		if d6 > 2:
			d6 = 7*d6
			paths.append(3)
		else:
			i9 = d6*0
			x = 6/2
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		d6 = i9**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))