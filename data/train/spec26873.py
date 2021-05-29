import numpy as np 

def function(x):

	r0 = x
	f4 = 2
	x = 7
	paths = []
	try:
		if f4 < 7:
			x = 2/x
			x = x-f4
			x = 7*x
			paths.append(1)
		else:
			r0 = r0/5
			x = f4+r0
			paths.append(2)
		if r0 <= 8:
			f4 = x+x
			paths.append(3)
		else:
			x = 3-x
			r0 = r0*1
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