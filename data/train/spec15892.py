import numpy as np 

def function(x):

	d9 = x
	a2 = x
	paths = []
	try:
		if x > 5:
			d9 = d9/8
			a2 = a2*a2
			paths.append(1)
		else:
			a2 = x+a2
			x = x-3
			d9 = x+x
			paths.append(2)
		if x <= 5:
			x = x-a2
			paths.append(3)
		else:
			a2 = 0-6
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		a2 = d9**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))