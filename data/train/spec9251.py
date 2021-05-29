import numpy as np 

def function(x):

	f7 = 6
	t8 = x
	paths = []
	try:
		if t8 >= 1:
			t8 = x/t8
			t8 = t8*6
			x = x*x
			paths.append(1)
		else:
			t8 = f7/t8
			paths.append(2)
		if x < 4:
			f7 = f7-0
			paths.append(3)
		else:
			f7 = f7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))