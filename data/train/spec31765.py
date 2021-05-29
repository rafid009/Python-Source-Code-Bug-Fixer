import numpy as np 

def function(x):

	f4 = x
	j9 = 5
	paths = []
	try:
		if f4 >= 1:
			f4 = x+f4
			j9 = f4+f4
			paths.append(1)
		else:
			j9 = 3+j9
			paths.append(2)
		if x > 9:
			x = x-x
			x = x/1
			paths.append(3)
		else:
			x = 6+x
			x = x+f4
			f4 = 4/j9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))