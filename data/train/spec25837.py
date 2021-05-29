import numpy as np 

def function(x):

	t8 = 4
	j0 = x
	paths = []
	try:
		if t8 < 5:
			x = j0-x
			t8 = j0+6
			x = x/2
			paths.append(1)
		else:
			x = x*8
			x = x-1
			paths.append(2)
		if t8 > 4:
			x = x*5
			paths.append(3)
		else:
			x = t8+x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		t8 = j0**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))