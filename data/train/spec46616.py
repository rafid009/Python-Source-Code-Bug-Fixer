import numpy as np 

def function(x):

	o0 = x
	t7 = 3
	paths = []
	try:
		if x > 1:
			t7 = t7+o0
			x = x+5
			o0 = t7-3
			paths.append(1)
		else:
			t7 = 0+7
			paths.append(2)
		if t7 <= 0:
			o0 = o0*9
			t7 = t7+1
			paths.append(3)
		else:
			o0 = 0+o0
			x = x-1
			t7 = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))