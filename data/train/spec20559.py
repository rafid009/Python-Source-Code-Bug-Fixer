import numpy as np 

def function(x):

	a3 = 0
	l9 = x
	x = x
	paths = []
	try:
		if a3 <= 5:
			l9 = a3*l9
			l9 = 2/4
			l9 = l9*l9
			paths.append(1)
		else:
			a3 = a3/7
			a3 = a3*4
			paths.append(2)
		if x > 4:
			a3 = a3-7
			a3 = a3+0
			x = x-a3
			paths.append(3)
		else:
			l9 = l9+9
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))