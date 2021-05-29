import numpy as np 

def function(x):

	j5 = 7
	t9 = 4
	paths = []
	try:
		if t9 < 7:
			j5 = j5/4
			j5 = j5+2
			x = j5+x
			paths.append(1)
		else:
			j5 = j5-9
			t9 = 1/9
			paths.append(2)
		if x < 8:
			t9 = x/t9
			t9 = t9+3
			paths.append(3)
		else:
			j5 = j5+9
			j5 = j5*7
			j5 = 5-8
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