import numpy as np 

def function(x):

	o4 = 8
	t9 = 7
	paths = []
	try:
		if t9 > 9:
			x = x*0
			x = x*3
			paths.append(1)
		else:
			t9 = x+0
			paths.append(2)
		if o4 < 5:
			x = x+4
			paths.append(3)
		else:
			o4 = x*9
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		t9 = o4**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))