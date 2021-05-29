import numpy as np 

def function(x):

	a2 = 0
	t7 = x
	paths = []
	try:
		if x >= 1:
			x = x-7
			paths.append(1)
		else:
			x = t7+x
			a2 = 3+3
			x = 4-x
			paths.append(2)
		if t7 >= 4:
			a2 = a2/9
			a2 = 8-a2
			paths.append(3)
		else:
			x = 4/x
			a2 = 1*t7
			a2 = a2-a2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))