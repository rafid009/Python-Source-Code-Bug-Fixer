import numpy as np 

def function(x):

	r2 = x
	f5 = 5
	paths = []
	try:
		if x >= 8:
			r2 = r2+1
			f5 = r2+5
			paths.append(1)
		else:
			x = 7/1
			f5 = 0+f5
			f5 = 6+r2
			paths.append(2)
		if f5 <= 9:
			x = r2/5
			f5 = f5-7
			paths.append(3)
		else:
			x = 4*x
			r2 = 9+r2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))