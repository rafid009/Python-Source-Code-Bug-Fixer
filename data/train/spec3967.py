import numpy as np 

def function(x):

	m1 = x
	f8 = 8
	paths = []
	try:
		if m1 < 2:
			x = x+1
			f8 = f8/f8
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if m1 >= 8:
			m1 = 0*0
			x = x*m1
			f8 = f8+f8
			paths.append(3)
		else:
			f8 = f8*9
			f8 = 1-f8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))