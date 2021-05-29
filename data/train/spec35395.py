import numpy as np 

def function(x):

	i9 = 0
	d5 = x
	paths = []
	try:
		if i9 >= 9:
			d5 = d5/2
			d5 = 7+d5
			d5 = d5+9
			paths.append(1)
		else:
			i9 = 3+0
			d5 = d5/4
			paths.append(2)
		if x >= 8:
			i9 = x+5
			x = 6+5
			i9 = 7-i9
			paths.append(3)
		else:
			x = d5+d5
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		d5 = i9**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))