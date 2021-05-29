import numpy as np 

def function(x):

	r2 = x
	f7 = 2
	paths = []
	try:
		if f7 <= 1:
			f7 = 5+f7
			r2 = r2-6
			x = 2+x
			paths.append(1)
		else:
			x = x+5
			x = 8-x
			paths.append(2)
		if x > 5:
			r2 = x+x
			r2 = r2/x
			x = x/8
			paths.append(3)
		else:
			r2 = r2/9
			f7 = x-x
			x = x/4
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))