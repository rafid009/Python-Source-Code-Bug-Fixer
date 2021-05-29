import numpy as np 

def function(x):

	j9 = x
	f6 = x
	x = 2
	paths = []
	try:
		if x > 6:
			x = f6-x
			f6 = 6*f6
			f6 = x-7
			paths.append(1)
		else:
			x = f6/f6
			f6 = f6*8
			paths.append(2)
		if x < 9:
			j9 = j9-f6
			paths.append(3)
		else:
			x = 6/x
			f6 = 4-6
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		f6 = j9**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))