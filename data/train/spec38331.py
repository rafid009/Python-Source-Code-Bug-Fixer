import numpy as np 

def function(x):

	d5 = 8
	i9 = x
	paths = []
	try:
		if d5 < 0:
			d5 = 3*d5
			i9 = 4/i9
			paths.append(1)
		else:
			d5 = d5/7
			d5 = 3*0
			paths.append(2)
		if d5 <= 1:
			d5 = d5+d5
			paths.append(3)
		else:
			x = x/8
			i9 = i9/d5
			x = x-i9
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))