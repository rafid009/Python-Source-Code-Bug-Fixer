import numpy as np 

def function(x):

	g9 = 8
	f6 = x
	paths = []
	try:
		if g9 >= 2:
			x = 8/x
			g9 = 0+0
			paths.append(1)
		else:
			f6 = f6+5
			g9 = 1/g9
			paths.append(2)
		if x <= 7:
			x = 1+f6
			paths.append(3)
		else:
			x = 7-6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f6 = f6**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))