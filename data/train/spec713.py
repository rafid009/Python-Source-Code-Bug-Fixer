import numpy as np 

def function(x):

	f4 = 7
	t1 = 1
	paths = []
	try:
		if t1 <= 7:
			t1 = t1/2
			t1 = x+8
			f4 = 1/f4
			paths.append(1)
		else:
			t1 = 8/t1
			paths.append(2)
		if x < 6:
			f4 = f4*7
			f4 = 3+f4
			paths.append(3)
		else:
			f4 = 3+7
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