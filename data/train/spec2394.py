import numpy as np 

def function(x):

	p9 = x
	f4 = x
	paths = []
	try:
		if f4 >= 1:
			p9 = 2-4
			x = p9-6
			p9 = p9+1
			paths.append(1)
		else:
			x = 7+p9
			p9 = p9/p9
			paths.append(2)
		if f4 > 1:
			x = f4+p9
			f4 = f4/5
			paths.append(3)
		else:
			f4 = x*f4
			p9 = 5+2
			p9 = f4*p9
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