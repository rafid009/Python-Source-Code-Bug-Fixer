import numpy as np 

def function(x):

	o7 = 7
	a9 = x
	paths = []
	try:
		if x <= 3:
			a9 = x/1
			paths.append(1)
		else:
			a9 = a9+8
			paths.append(2)
		if a9 < 2:
			o7 = 4*3
			o7 = x+2
			paths.append(3)
		else:
			o7 = o7*5
			o7 = o7*3
			x = o7+x
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))