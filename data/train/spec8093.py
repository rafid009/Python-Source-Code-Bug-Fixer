import numpy as np 

def function(x):

	f6 = 5
	r2 = 5
	paths = []
	try:
		if f6 <= 1:
			x = x*4
			f6 = f6/1
			f6 = f6*6
			paths.append(1)
		else:
			x = f6*x
			r2 = r2/5
			r2 = r2+r2
			paths.append(2)
		if r2 > 1:
			f6 = r2-f6
			paths.append(3)
		else:
			x = x*8
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