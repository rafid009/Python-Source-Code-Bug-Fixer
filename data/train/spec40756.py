import numpy as np 

def function(x):

	a1 = x
	s5 = 2
	paths = []
	try:
		if x < 9:
			x = x/x
			a1 = a1/x
			s5 = 5/a1
			paths.append(1)
		else:
			a1 = 6/a1
			paths.append(2)
		if x <= 1:
			x = 9+x
			paths.append(3)
		else:
			a1 = 9/a1
			x = x/3
			a1 = a1-6
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