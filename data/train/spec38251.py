import numpy as np 

def function(x):

	t4 = 2
	o6 = x
	paths = []
	try:
		if t4 <= 0:
			t4 = 2+3
			o6 = 6+o6
			t4 = 0+9
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if o6 > 8:
			x = 2+x
			t4 = t4+5
			o6 = o6*5
			paths.append(3)
		else:
			o6 = o6-5
			o6 = 2+o6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))