import numpy as np 

def function(x):

	t3 = 2
	f0 = x
	paths = []
	try:
		if t3 >= 1:
			t3 = 4+8
			x = x+9
			paths.append(1)
		else:
			f0 = 7/f0
			x = 0*3
			t3 = 0+7
			paths.append(2)
		if f0 < 5:
			f0 = 1/1
			t3 = 0+x
			paths.append(3)
		else:
			f0 = f0/f0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))