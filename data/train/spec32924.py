import numpy as np 

def function(x):

	r4 = 8
	t7 = x
	x = x
	paths = []
	try:
		if t7 > 3:
			t7 = x-0
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if r4 >= 6:
			x = x+6
			t7 = x/t7
			x = t7+x
			paths.append(3)
		else:
			r4 = x*8
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		t7 = t7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))