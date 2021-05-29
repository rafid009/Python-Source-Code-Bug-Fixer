import numpy as np 

def function(x):

	i3 = x
	a0 = x
	paths = []
	try:
		if x > 6:
			i3 = x-i3
			x = x-6
			paths.append(1)
		else:
			x = x-5
			a0 = 5*a0
			paths.append(2)
		if a0 >= 3:
			x = x*2
			a0 = a0+a0
			paths.append(3)
		else:
			a0 = 1+a0
			i3 = 6/4
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))