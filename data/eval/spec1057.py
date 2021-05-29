import numpy as np 

def function(x):

	a0 = x
	a1 = x
	paths = []
	try:
		if x <= 3:
			a0 = 3+a0
			paths.append(1)
		else:
			x = 5+x
			paths.append(2)
		if a0 <= 5:
			a0 = a0+1
			a1 = 2-a1
			x = 8+0
			paths.append(3)
		else:
			a0 = a1+9
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