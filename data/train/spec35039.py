import numpy as np 

def function(x):

	a9 = 2
	f1 = x
	paths = []
	try:
		if x < 4:
			x = f1/x
			a9 = a9/6
			a9 = 9*a9
			paths.append(1)
		else:
			a9 = a9/9
			paths.append(2)
		if a9 <= 1:
			f1 = 9*a9
			a9 = a9-a9
			x = x+x
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))