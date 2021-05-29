import numpy as np 

def function(x):

	f4 = 7
	i5 = x
	paths = []
	try:
		if x <= 7:
			x = 9*7
			i5 = 0-i5
			f4 = f4+f4
			paths.append(1)
		else:
			x = i5/7
			paths.append(2)
		if x < 1:
			x = x/x
			paths.append(3)
		else:
			f4 = 3*1
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		f4 = i5**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))