import numpy as np 

def function(x):

	k2 = 2
	t2 = x
	paths = []
	try:
		if k2 >= 4:
			t2 = t2+6
			k2 = t2*8
			t2 = 0+0
			paths.append(1)
		else:
			x = 5-t2
			k2 = 9+k2
			k2 = k2/9
			paths.append(2)
		if k2 <= 8:
			t2 = 7/t2
			k2 = 5*t2
			paths.append(3)
		else:
			k2 = k2*6
			t2 = k2-1
			k2 = t2*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))