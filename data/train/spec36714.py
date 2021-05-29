import numpy as np 

def function(x):

	o4 = x
	t9 = x
	paths = []
	try:
		if t9 <= 4:
			t9 = t9/o4
			t9 = t9/o4
			paths.append(1)
		else:
			t9 = t9*2
			o4 = 2-o4
			o4 = o4*1
			paths.append(2)
		if t9 >= 8:
			t9 = x+4
			o4 = o4*2
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		o4 = t9**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))