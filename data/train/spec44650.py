import numpy as np 

def function(x):

	f4 = 1
	t1 = 6
	paths = []
	try:
		if f4 <= 5:
			x = x-t1
			t1 = 0*9
			f4 = 1*f4
			paths.append(1)
		else:
			x = x*5
			x = x-9
			paths.append(2)
		if t1 >= 4:
			f4 = f4*7
			x = 9+8
			x = x+2
			paths.append(3)
		else:
			t1 = f4*8
			t1 = t1-t1
			f4 = 2/7
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