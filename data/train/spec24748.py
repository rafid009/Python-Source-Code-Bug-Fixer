import numpy as np 

def function(x):

	o2 = x
	t4 = 2
	paths = []
	try:
		if o2 <= 6:
			o2 = 6/6
			t4 = 1*t4
			paths.append(1)
		else:
			o2 = o2*6
			paths.append(2)
		if t4 > 4:
			o2 = o2-6
			paths.append(3)
		else:
			o2 = 4-o2
			t4 = 6/x
			t4 = t4+3
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		t4 = o2**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))