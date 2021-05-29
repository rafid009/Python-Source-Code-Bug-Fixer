import numpy as np 

def function(x):

	a7 = 9
	a1 = x
	paths = []
	try:
		if a7 <= 7:
			a1 = a1/7
			a1 = a1/2
			a7 = 4/2
			paths.append(1)
		else:
			x = 3+8
			paths.append(2)
		if a7 <= 4:
			x = x*8
			paths.append(3)
		else:
			a1 = a1*a7
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))