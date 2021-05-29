import numpy as np 

def function(x):

	e1 = x
	t5 = 3
	paths = []
	try:
		if t5 > 0:
			e1 = 3+7
			e1 = 3-6
			paths.append(1)
		else:
			t5 = t5/3
			x = t5+5
			x = 4/7
			paths.append(2)
		if e1 < 1:
			t5 = 1+4
			t5 = x*9
			t5 = 8-1
			paths.append(3)
		else:
			x = 8/x
			e1 = 7-e1
			e1 = e1*4
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