import numpy as np 

def function(x):

	r2 = x
	f5 = 2
	paths = []
	try:
		if r2 > 1:
			x = r2/6
			f5 = f5*8
			paths.append(1)
		else:
			r2 = 4+1
			x = x-8
			paths.append(2)
		if r2 <= 8:
			r2 = r2*3
			paths.append(3)
		else:
			f5 = 3/f5
			f5 = f5-7
			f5 = f5-x
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