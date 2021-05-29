import numpy as np 

def function(x):

	t6 = 6
	a0 = 6
	x = 4
	paths = []
	try:
		if a0 < 1:
			x = a0-4
			a0 = a0/6
			paths.append(1)
		else:
			a0 = x+1
			x = 0*x
			t6 = a0-t6
			paths.append(2)
		if a0 <= 1:
			x = 1*7
			x = a0+x
			paths.append(3)
		else:
			a0 = 4-a0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))