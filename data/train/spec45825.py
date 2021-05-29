import numpy as np 

def function(x):

	a2 = 0
	f5 = x
	paths = []
	try:
		if a2 > 5:
			a2 = 5*a2
			a2 = f5/x
			paths.append(1)
		else:
			a2 = a2-a2
			a2 = a2/9
			f5 = f5+8
			paths.append(2)
		if x >= 3:
			a2 = 3-f5
			paths.append(3)
		else:
			f5 = 8*f5
			a2 = a2/x
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))