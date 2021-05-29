import numpy as np 

def function(x):

	t5 = 2
	o8 = 8
	paths = []
	try:
		if t5 > 1:
			x = x-o8
			t5 = t5/8
			t5 = x-t5
			paths.append(1)
		else:
			o8 = 4*o8
			t5 = t5-5
			paths.append(2)
		if o8 < 1:
			t5 = o8-t5
			o8 = 9+o8
			paths.append(3)
		else:
			o8 = 8+o8
			x = o8*t5
			o8 = o8/7
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		t5 = t5**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))