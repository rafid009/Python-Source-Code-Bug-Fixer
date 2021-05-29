import numpy as np 

def function(x):

	z5 = 5
	f3 = x
	paths = []
	try:
		if x >= 4:
			x = 9/x
			x = 0+x
			paths.append(1)
		else:
			z5 = 7*5
			x = f3/x
			paths.append(2)
		if x < 3:
			x = x+7
			paths.append(3)
		else:
			x = 6*5
			f3 = f3/8
			f3 = z5+f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))