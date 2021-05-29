import numpy as np 

def function(x):

	t8 = 6
	h1 = x
	paths = []
	try:
		if t8 > 1:
			x = x+1
			paths.append(1)
		else:
			x = 1/9
			t8 = 6-t8
			paths.append(2)
		if x <= 4:
			h1 = 6*h1
			t8 = 9*h1
			t8 = t8+5
			paths.append(3)
		else:
			x = 8-6
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		t8 = t8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))