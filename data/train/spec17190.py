import numpy as np 

def function(x):

	f1 = x
	f9 = 1
	paths = []
	try:
		if f1 > 1:
			f1 = 8-f1
			f9 = f9/x
			x = x-x
			paths.append(1)
		else:
			x = 4*x
			f9 = f1+f1
			paths.append(2)
		if x >= 3:
			f9 = 7+x
			f9 = 5+f9
			x = f1*x
			paths.append(3)
		else:
			f9 = f9+9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))