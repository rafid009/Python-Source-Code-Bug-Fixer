import numpy as np 

def function(x):

	j1 = x
	t9 = x
	paths = []
	try:
		if x <= 5:
			t9 = t9*6
			j1 = j1*1
			paths.append(1)
		else:
			t9 = 9+2
			x = x*8
			x = x/t9
			paths.append(2)
		if t9 < 9:
			x = x+x
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))