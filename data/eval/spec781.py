import numpy as np 

def function(x):

	f6 = 1
	f9 = x
	paths = []
	try:
		if f9 <= 5:
			x = 0+x
			f9 = f9-3
			paths.append(1)
		else:
			f6 = 7-f6
			paths.append(2)
		if f6 <= 7:
			x = x-3
			x = x/f9
			paths.append(3)
		else:
			x = f9-f9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f6 = f9**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))