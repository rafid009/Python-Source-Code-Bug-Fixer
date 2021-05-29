import numpy as np 

def function(x):

	t5 = 3
	h1 = x
	x = 1
	paths = []
	try:
		if t5 > 5:
			t5 = 2*x
			x = x+3
			paths.append(1)
		else:
			x = t5+x
			paths.append(2)
		if t5 <= 1:
			t5 = h1*x
			paths.append(3)
		else:
			x = h1*5
			h1 = 1+3
			h1 = t5+h1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))