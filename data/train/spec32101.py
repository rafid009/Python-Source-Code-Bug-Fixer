import numpy as np 

def function(x):

	t2 = x
	t8 = x
	x = x
	paths = []
	try:
		if t2 <= 5:
			x = x+3
			paths.append(1)
		else:
			x = x*7
			t2 = t2-4
			paths.append(2)
		if t2 >= 0:
			t8 = x*8
			t2 = t2-6
			paths.append(3)
		else:
			t8 = t2/9
			t2 = 5*t2
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