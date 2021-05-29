import numpy as np 

def function(x):

	a2 = x
	d5 = x
	paths = []
	try:
		if a2 < 2:
			a2 = 1*0
			x = 0/x
			x = 3+x
			paths.append(1)
		else:
			d5 = d5/1
			x = x-7
			paths.append(2)
		if d5 < 9:
			a2 = a2-4
			paths.append(3)
		else:
			d5 = d5-a2
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		a2 = d5**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))