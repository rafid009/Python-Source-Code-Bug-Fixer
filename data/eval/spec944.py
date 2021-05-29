import numpy as np 

def function(x):

	t9 = 4
	i4 = x
	x = x
	paths = []
	try:
		if i4 >= 2:
			i4 = i4+7
			x = x+x
			t9 = x/t9
			paths.append(1)
		else:
			t9 = t9+1
			t9 = 8+2
			t9 = 1-t9
			paths.append(2)
		if i4 <= 2:
			t9 = 8-t9
			x = x-x
			i4 = i4+3
			paths.append(3)
		else:
			i4 = i4*2
			i4 = 0*i4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))