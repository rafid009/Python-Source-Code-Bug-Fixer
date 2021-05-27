import numpy as np 

def function(x):

	t8 = x
	f1 = x
	paths = []
	try:
		if x >= 4:
			x = x*4
			f1 = 3*t8
			t8 = t8/f1
			paths.append(1)
		else:
			f1 = 4/5
			x = x*t8
			f1 = f1*3
			paths.append(2)
		if f1 >= 7:
			t8 = 2*8
			t8 = 7-6
			x = 5+5
			paths.append(3)
		else:
			t8 = t8*3
			f1 = 3/f1
			x = x*t8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))