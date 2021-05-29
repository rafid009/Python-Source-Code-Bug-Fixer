import numpy as np 

def function(x):

	d4 = x
	t5 = 7
	x = x
	paths = []
	try:
		if d4 <= 7:
			x = x/x
			t5 = d4*5
			d4 = t5*4
			paths.append(1)
		else:
			x = d4-8
			paths.append(2)
		if x > 7:
			t5 = 2-t5
			d4 = d4/6
			t5 = t5/d4
			paths.append(3)
		else:
			x = x/x
			t5 = d4+8
			t5 = t5*0
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		d4 = d4**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))