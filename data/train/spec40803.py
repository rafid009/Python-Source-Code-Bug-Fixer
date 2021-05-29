import numpy as np 

def function(x):

	x6 = 4
	f3 = x
	paths = []
	try:
		if x6 <= 5:
			x6 = 4/x
			x = x-1
			x6 = f3+x6
			paths.append(1)
		else:
			x6 = x6/f3
			x = x+x
			paths.append(2)
		if f3 < 9:
			x = 1-x
			x6 = 7*x6
			paths.append(3)
		else:
			x6 = x6+x6
			x = 0+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f3 = x**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))