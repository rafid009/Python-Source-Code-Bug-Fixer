import numpy as np 

def function(x):

	f6 = x
	g3 = 0
	paths = []
	try:
		if g3 >= 4:
			g3 = g3-4
			f6 = f6/6
			paths.append(1)
		else:
			x = x*8
			x = x*7
			paths.append(2)
		if g3 <= 6:
			f6 = x*0
			g3 = g3/9
			f6 = g3*f6
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))