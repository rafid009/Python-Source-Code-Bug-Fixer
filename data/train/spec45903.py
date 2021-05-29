import numpy as np 

def function(x):

	f8 = x
	j6 = x
	paths = []
	try:
		if f8 > 7:
			j6 = 7*f8
			j6 = j6/5
			paths.append(1)
		else:
			x = 6*3
			x = 7+f8
			paths.append(2)
		if f8 >= 8:
			x = 8/x
			x = x*x
			f8 = f8-2
			paths.append(3)
		else:
			j6 = 7*3
			j6 = f8+j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		f8 = j6**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))