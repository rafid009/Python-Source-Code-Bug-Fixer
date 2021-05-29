import numpy as np 

def function(x):

	v1 = 7
	a1 = 7
	paths = []
	try:
		if x <= 3:
			x = x-v1
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if x < 4:
			a1 = a1*8
			v1 = v1*x
			a1 = a1-4
			paths.append(3)
		else:
			x = 7-2
			a1 = a1/a1
			a1 = a1/a1
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		a1 = v1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))