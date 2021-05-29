import numpy as np 

def function(x):

	r8 = 0
	t2 = x
	x = 3
	paths = []
	try:
		if t2 >= 6:
			x = 7*x
			x = x+4
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if t2 < 5:
			x = x*x
			r8 = 7-1
			r8 = 0+r8
			paths.append(3)
		else:
			t2 = t2+x
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