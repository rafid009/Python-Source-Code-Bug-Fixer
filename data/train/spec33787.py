import numpy as np 

def function(x):

	f7 = x
	f5 = x
	paths = []
	try:
		if f5 >= 7:
			f5 = f5+5
			paths.append(1)
		else:
			x = 3/7
			paths.append(2)
		if x > 1:
			f5 = 6+f5
			f5 = f5+9
			paths.append(3)
		else:
			f5 = f5/5
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f5 = f7**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))