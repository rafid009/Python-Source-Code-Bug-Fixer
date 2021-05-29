import numpy as np 

def function(x):

	a1 = x
	j5 = 9
	paths = []
	try:
		if x >= 7:
			x = x/x
			a1 = x-0
			paths.append(1)
		else:
			j5 = j5*9
			paths.append(2)
		if x < 5:
			a1 = a1-2
			a1 = a1*3
			paths.append(3)
		else:
			a1 = 7/a1
			a1 = j5/a1
			x = x*8
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))