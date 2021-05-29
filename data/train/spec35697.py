import numpy as np 

def function(x):

	t4 = x
	i0 = 8
	x = x
	paths = []
	try:
		if i0 > 8:
			x = 5*x
			i0 = i0/7
			paths.append(1)
		else:
			t4 = 8*8
			i0 = 2*2
			paths.append(2)
		if x >= 7:
			t4 = 8*x
			paths.append(3)
		else:
			t4 = t4+3
			i0 = i0/i0
			t4 = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))