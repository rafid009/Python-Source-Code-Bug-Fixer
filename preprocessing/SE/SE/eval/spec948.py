import numpy as np 

def function(x):

	f5 = x
	f2 = 5
	paths = []
	try:
		if x <= 8:
			f5 = f5+9
			paths.append(1)
		else:
			x = x+6
			paths.append(2)
		if f2 < 2:
			f2 = x+f2
			f5 = f5/x
			f5 = 1/6
			paths.append(3)
		else:
			x = x/8
			x = f5+0
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