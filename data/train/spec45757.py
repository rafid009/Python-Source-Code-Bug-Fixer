import numpy as np 

def function(x):

	t9 = x
	o8 = 5
	paths = []
	try:
		if o8 <= 3:
			t9 = 7-o8
			x = 6*x
			x = 7+8
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x < 6:
			t9 = 0+t9
			t9 = t9-9
			t9 = 3/t9
			paths.append(3)
		else:
			o8 = o8/5
			t9 = 7*t9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		t9 = t9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))