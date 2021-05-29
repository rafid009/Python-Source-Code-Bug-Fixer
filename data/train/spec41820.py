import numpy as np 

def function(x):

	t7 = 2
	h3 = x
	paths = []
	try:
		if t7 > 8:
			h3 = h3-h3
			paths.append(1)
		else:
			h3 = h3-5
			t7 = x/5
			paths.append(2)
		if h3 < 6:
			t7 = 3*2
			t7 = t7/t7
			paths.append(3)
		else:
			h3 = 3/h3
			x = 0+9
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		t7 = h3**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))