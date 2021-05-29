import numpy as np 

def function(x):

	r4 = 3
	f2 = 6
	paths = []
	try:
		if x <= 7:
			r4 = r4+7
			paths.append(1)
		else:
			x = r4-3
			f2 = f2+x
			f2 = f2-3
			paths.append(2)
		if x < 6:
			r4 = x+r4
			r4 = x+f2
			paths.append(3)
		else:
			r4 = f2-r4
			x = x+r4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))