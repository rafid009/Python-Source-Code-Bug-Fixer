import numpy as np 

def function(x):

	g9 = 1
	f2 = x
	paths = []
	try:
		if x < 8:
			g9 = 7+x
			paths.append(1)
		else:
			f2 = g9-f2
			x = 0-7
			x = x*4
			paths.append(2)
		if x <= 4:
			f2 = f2-3
			x = x*f2
			paths.append(3)
		else:
			f2 = f2+g9
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		f2 = f2**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))