import numpy as np 

def function(x):

	f2 = 1
	t3 = 1
	paths = []
	try:
		if x > 4:
			x = x+1
			t3 = 5-t3
			x = t3*4
			paths.append(1)
		else:
			t3 = 1+t3
			f2 = t3+4
			t3 = t3+7
			paths.append(2)
		if x <= 2:
			x = 2*x
			paths.append(3)
		else:
			t3 = 3-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))