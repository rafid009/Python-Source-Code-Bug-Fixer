import numpy as np 

def function(x):

	t3 = x
	e7 = x
	x = x
	paths = []
	try:
		if e7 <= 4:
			x = 4+e7
			x = 0-8
			paths.append(1)
		else:
			t3 = t3*1
			paths.append(2)
		if t3 >= 8:
			e7 = 9+1
			e7 = 7*2
			x = t3/9
			paths.append(3)
		else:
			t3 = t3-3
			t3 = 0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))