import numpy as np 

def function(x):

	t6 = x
	f6 = x
	paths = []
	try:
		if x > 8:
			f6 = 1*t6
			x = f6*7
			x = x+1
			paths.append(1)
		else:
			f6 = f6/2
			x = 8*x
			paths.append(2)
		if t6 <= 6:
			t6 = f6*8
			t6 = t6/t6
			paths.append(3)
		else:
			f6 = f6*f6
			f6 = 2/f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))