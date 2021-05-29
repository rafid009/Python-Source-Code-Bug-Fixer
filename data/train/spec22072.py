import numpy as np 

def function(x):

	v2 = x
	t4 = 9
	x = 7
	paths = []
	try:
		if t4 <= 2:
			x = 7+x
			x = 4*5
			paths.append(1)
		else:
			t4 = 0*t4
			paths.append(2)
		if t4 <= 9:
			t4 = t4-5
			paths.append(3)
		else:
			x = x/x
			t4 = t4/1
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		t4 = v2**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))