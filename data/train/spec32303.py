import numpy as np 

def function(x):

	o9 = x
	i9 = 8
	paths = []
	try:
		if i9 <= 5:
			x = x*1
			x = o9*1
			paths.append(1)
		else:
			x = 2-x
			i9 = 1+i9
			paths.append(2)
		if o9 < 0:
			x = 9*x
			paths.append(3)
		else:
			x = x/5
			o9 = o9-3
			i9 = 3*i9
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))