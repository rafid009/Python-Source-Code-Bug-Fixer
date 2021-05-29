import numpy as np 

def function(x):

	f4 = 8
	t2 = 4
	paths = []
	try:
		if f4 < 0:
			f4 = 8/f4
			f4 = f4+1
			t2 = t2*9
			paths.append(1)
		else:
			t2 = 7*t2
			f4 = f4-4
			x = x+9
			paths.append(2)
		if t2 >= 5:
			f4 = 5*f4
			paths.append(3)
		else:
			f4 = x/f4
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