import numpy as np 

def function(x):

	i0 = 4
	t5 = x
	paths = []
	try:
		if i0 < 3:
			i0 = 3-i0
			i0 = i0-3
			i0 = 1-i0
			paths.append(1)
		else:
			t5 = t5+3
			i0 = t5-i0
			paths.append(2)
		if x <= 4:
			i0 = t5-7
			paths.append(3)
		else:
			t5 = x+i0
			x = 2*7
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		t5 = i0**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))