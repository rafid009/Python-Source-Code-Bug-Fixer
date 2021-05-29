import numpy as np 

def function(x):

	f0 = x
	t2 = x
	x = 5
	paths = []
	try:
		if x > 0:
			x = 1+f0
			t2 = t2-1
			paths.append(1)
		else:
			f0 = 8/1
			f0 = f0/f0
			paths.append(2)
		if t2 >= 4:
			t2 = 0/t2
			t2 = x*f0
			t2 = 9+t2
			paths.append(3)
		else:
			f0 = f0+f0
			x = 9*5
			x = f0-f0
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))